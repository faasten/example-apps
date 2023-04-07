from PIL import Image
from io import BytesIO
import face_recognition

def handle(request, syscall):
    img_path = request['object-path']
    img_name = img_path.split(':')[-1]
    ret_list = []
    with syscall.fs_openblob(img_path) as blob:
        # internally face_recognition use Image.open
        img = face_recognition.load_image_file(blob)
        face_locations = face_recognition.face_locations(img)
        img = Image.fromarray(img)
        syscall.endorse()
        for (i, box) in enumerate(face_locations):
            # change (top, right, bottom, left) to (left, upper, right, lower)
            box = (box[3], box[0], box[1], box[2])
            face_img = img.crop(box)
            buff = BytesIO()
            face_img.save(buff, format='JPEG')
            face_path = ':'.join(['home', '%', img_name + '.face' + str(i)])
            if syscall.fs_createfile(face_path):
                if syscall.fs_write(face_path, buff.getvalue()):
                    ret_list.append(face_path)
                else:
                    return {'error': 'failed to write {}'.format(face_path)}
            else:
                return {'error': 'failed to create {}'.format(face_path)}
    return {'face_paths': ret_list}
