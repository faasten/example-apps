import face_recognition

def handle(request, syscall):
    image = face_recognition.load_image_file("your_file.jpg")
    face_locations = face_recognition.face_locations(image)
