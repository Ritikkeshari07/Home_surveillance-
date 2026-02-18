import cv2
import time
from datetime import datetime
import os

# Create images folder if it doesn't exist
if not os.path.exists("images"):
    os.makedirs("images")

# Load Haar cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Start webcam
video = cv2.VideoCapture(0)

# Save interval settings (seconds)
save_interval = 5
last_save_time = 0

while True:
    check, frame = video.read()

    if not check:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangle around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Save image only if face detected AND interval passed
    if len(faces) > 0:
        current_time = time.time()
        if current_time - last_save_time >= save_interval:
            exact_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = os.path.join("images", f"face_{exact_time}.jpg")
            cv2.imwrite(filename, frame)
            print(f"[INFO] Image saved: {filename}")
            last_save_time = current_time

    # Show window
    cv2.imshow("Home Surveillance", frame)

    # Press q to quit
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# Release resources
video.release()
cv2.destroyAllWindows()
