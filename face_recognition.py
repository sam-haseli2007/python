import face_recognition as fr

img = fr.__loader__image_file("elon.jpg")
encoding = fr.get_encoding(img)[0]