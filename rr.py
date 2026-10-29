import cv2
import face_recognition

# Өөрийн нүүрний зураг
my_image = face_recognition.load_image_file("myface.jpg")
my_face = face_recognition.face_encodings(my_image)[0]

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    faces = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, faces)

    for encoding, location in zip(encodings, faces):

        match = face_recognition.compare_faces(
            [my_face],
            encoding
        )[0]

        top, right, bottom, left = location

        if match:
            text = "ACCESS GRANTED"
            color = (0, 255, 0)
        else:
            text = "ACCESS DENIED"
            color = (0, 0, 255)

        cv2.rectangle(
            frame,
            (left, top),
            (right, bottom),
            color,
            2
        )

        cv2.putText(
            frame,
            text,
            (left, bottom + 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2
        )

    cv2.imshow("Face Login", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()


