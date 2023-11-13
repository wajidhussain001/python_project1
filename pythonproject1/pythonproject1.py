import cv2

#Open a connection to the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop if 'w' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

#Release the camera and close the window
cap.release()
cv2.destroyAllWindows()