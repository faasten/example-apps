from PIL import Image

def handle(event, cloudcall):
    download_path = event['input']
    output_dir = event['output_dir']
    sizes = event['sizes']
    with cloudcall.fs_openblob(download_path) as blob:
        img = Image.open(blob)
        for size in sizes:
            img.thumbnail(tuple(size))
            thumnail_name = '-'.join(size) + '.jpeg'
            thumbnail_path = ':'.join([output_dir, thumbnail_name])
            with cloudcall.create_blob(thumbnail_path) as newblob:
                img.save(newblob, format='JPEG')
                newblob.finalize(b'')
