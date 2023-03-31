import cv2
import pupil_capture

# Create a capture instance for the PS Eye camera
capture = pupil_capture.get_capture(device_idx=0)

# Set the camera resolution
capture.frame_shape = (640, 480)

# Create a window to display the video stream
cv2.namedWindow('PS Eye Preview')

# Loop through the video stream frames
while True:
    # Get a frame from the camera
    frame = capture.get_frame()

    # Display the frame in the window
    cv2.imshow('PS Eye Preview', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the window
capture.release()
cv2.destroyAllWindows()
