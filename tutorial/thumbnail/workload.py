from PIL import Image

def handle(event, cloudcall):
    download_path = event['input']['download_key']
    output_dir = event['input']['output_dir']
    sizes = event['input']['sizes']
    blobs = {}
    with cloudcall.fs_openblob(download_path) as blob:
        img = Image.open(blob)
        for size in sizes:
            img.thumbnail(tuple(size))
            thumbnail_name = '-'.join(map(str, size)) + '.jpeg'
            upload_path = ':'.join([output_dir, thumbnail_name])
            with cloudcall.create_blob() as newblob:
                img.save(newblob, format='JPEG')
                bn = newblob.finalize(b'')
                blobs[thumbnail_name] = bn
                cloudcall.fs_linkblob(upload_path, bn)
    return {'thumb-blobs': blobs}
