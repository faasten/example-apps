from PIL import Image
from io import BytesIO
import face_recognition

def handle(event, syscall):
    download_path = event['input']['download_key']
    output_dir = event['input']['output_dir']
    blobs = {}
    # complete this function so that it uploads detected faces as blobs to
    # PyPI page of face_recognition: https://pypi.org/project/face-recognition/
    return {'face-blobs': blobs}
