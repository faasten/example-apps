from PIL import Image
import base64
from io import BytesIO

def handle(request, syscall):
    with syscall.open_blob(request['input-blob']) as blob:
        img_in_bytes = blob.read()
    img = Image.open(BytesIO(img_in_bytes))
    img.thumbnail(request['input']['size'])
    buff = BytesIO()
    img.save(buff, format='JPEG')
    buff = buff.getvalue()
    img_file_path = request['input']['path']
    if syscall.fs_createfile(img_file_path):
        if syscall.fs_write(img_file_path, buff):
            return {'thumbnail': img_file_path}
        return {'error': 'failed to write the thumbnail'}
    return {'error': 'failed to create the thumbnail'}
