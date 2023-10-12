import serial

import time

import cv2


serialcomm = serial.Serial('COM4', 9600)

serialcomm.timeout = 1


# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the webcam
vid = cv2.VideoCapture(0)
i = "on"
j= "off"
while True:
    # Read a frame from the webcam
    ret, frame = vid.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Check if at least one face is detected
    if len(faces) > 0:
        time.sleep(2)  # Add a 2-second delay
        
        print("Face detected")

        serialcomm.write(i.encode())

        print(serialcomm.readline().decode('ascii'))


        time.sleep(0.5)



        

    else:
        time.sleep(2)  # Add a 2-second delay
        
        print("No face detected")

        serialcomm.write(j.encode())
        
        print(serialcomm.readline().decode('ascii'))

        time.sleep(0.5)

        

    # for (x, y, w, h) in faces:
    #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    
    cv2.imshow('Face Detection', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


        

    # Draw a green rectangle around each detected face
    

# Release the video capture object and close the OpenCV windows

serialcomm.close()

vid.release()
cv2.destroyAllWindows()
