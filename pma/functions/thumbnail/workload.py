from PIL import Image
from io import BytesIO

def handle(request, syscall):
    # fs path to the original photo
    photo_path = request['object-path']
    # open the photo
    with syscall.fs_openblob(photo_path) as blob:
        img = Image.open(blob)
        # resize
        img.thumbnail(tuple(request['input']['size']))
        buff = BytesIO()
        img.save(buff, format='JPEG')

    # save thumbnail
    photo_filename = photo_path.split(':')[-1]
    thumbnail_filename = photo_filename + '.resized'
    syscall.endorse()
    thumbnail_path = ':'.join(['home', '%', thumbnail_filename])
    if syscall.fs_createfile(thumbnail_path):
        if syscall.fs_write(thumbnail_path, buff.getvalue()):
            return {'thumbnail': thumbnail_path}
        return {'error': 'failed to write the thumbnail'}
    return {'error': 'failed to create the thumbnail'}
