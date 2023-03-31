import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize video capture device
cap = cv2.VideoCapture(0)

# Define the length of the lines extension
extension_length = 200

# Define font and position for status text overlay
font = cv2.FONT_HERSHEY_SIMPLEX
org = (10, 30)

# Define font size
font_size = 0.7

while True:
    # Capture video frame by frame
    ret, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    # Draw coordinate plane
    height, width = frame.shape[:2]
    center_x, center_y = int(width / 2), int(height / 2)
    cv2.line(frame, (0, center_y), (width, center_y), (0, 255, 0), 2)
    cv2.line(frame, (center_x, 0), (center_x, height), (0, 255, 0), 2)
    cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

    # Draw rectangle and dot on faces
    if len(faces) > 0:
        # Draw green "tracking" status text overlay
        cv2.putText(frame, 'Tracking', org, font, font_size, (0, 255, 0), 2, cv2.LINE_AA)

        for (x, y, w, h) in faces:
            # Draw rectangle
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Draw dot
            face_center_x, face_center_y = int(x + w / 2), int(y + h / 2)
            cv2.circle(frame, (face_center_x, face_center_y), 5, (0, 0, 255), -1)

            # Calculate distance from center of camera to face
            x_distance, y_distance = face_center_x - center_x, center_y - face_center_y
            print(f"X and Y coordinates: {x_distance:.0f},{y_distance:.0f}")

            # Print location based on coordinate plane
            if x_distance > 0 and y_distance > 0:
                print("Location: Top Right")
            elif x_distance < 0 and y_distance > 0:
                print("Location: Top Left")
            elif x_distance > 0 and y_distance < 0:
                print("Location: Bottom Right")
            elif x_distance < 0 and y_distance < 0:
                print("Location: Bottom Left")

    else:
        # Draw red "lost" status text overlay
        cv2.putText(frame, 'Lost', org, font, font_size, (0, 0, 255), 2, cv2.LINE_AA)

    # Show the frame
    cv2.imshow('Video', frame)

    # Exit if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()
