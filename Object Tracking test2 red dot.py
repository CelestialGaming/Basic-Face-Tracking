import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw a rectangle and a dot for each detected face
    for (x, y, w, h) in faces:
        # Find the center of the face
        center_x = x + w // 2
        center_y = y + h // 2

        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Draw a dot at the center of the face
        cv2.circle(frame, (center_x, center_y), 2, (0, 0, 255), -1)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Check for user input to quit
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()
