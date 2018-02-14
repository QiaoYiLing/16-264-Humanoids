# 16-264-Humanoids Facial Recognition Project

## Team Members
Tanushree Mediratta, Yiling (Jovi) Qiao, Lena Li, Krithika Veerappan

## Project Description

For the first part of our project, we wanted to do something with facial/emotion recognition. We brainstormed many humanoid ideas, and most of them needed some kind of a command to be activated. Many current humanoids use voice activation as face recognition can be slightly more challenging. From cybersecurity to household chores, visual recognition can be a very useful tool for humanoids to execute their tasks.

However, improper facial recognition could create many more dangers. If the humanoid identified an incorrect person as a criminal, it could lead people on the wrong path. While working on this assignment, we encountered some difficulties with proper facial recognition.

With our project, when someone looks at a webcam, a box will frame their face and the computer will state which face it recognizes. Then it will read that name aloud. If an unknown person looks at the camera, it will show unknown.

We started by finding a GitHub repository face_recognition; we made some changes to that code. We edited the code to allow us to add pictures to the specified folder and names were automatically updated in the “database” we had created for this project. The automated updating made it easier for us to use the code as it did not require us to constantly be changing our code. On a macro scale, having this form of adding pictures would make it a smooth process for having a robot that can recognize people from larger databases (such as photos of all members of Carnegie Mellon).

We imported pygame, google’s text to speech api, face_recognition (discussed above), and OpenCV. The main purpose of OpenCV is to detect faces in the image the camera sees. All other packages and the API are used for processing further information based on the faces OpenCV detects.

The face recognition is from a live feed from the user’s webcam. To make things run faster, as efficiency is an important component for humanoids to meet the high standards set for them by science fiction, we made it process each video frame at ¼ resolution but display at full resolution.

We started by getting a reference to the default webcam. The next important step was to load a sample picture and learn how to recognize it.

We initialized some variables for the code to start running when it sees a face in the frame. Our next step was to create a pygame object instance. We also made a scoring system to improve accuracy. It took a single frame, and it resized it for faster face recognition. OpenCV uses BGR color, so we had to change it to RGB color for face_recognition to correctly interpret the frame. Every other frame is processed to save time, and all faces and face encodings are found in the particular frame. It can recognize multiple faces at the same time.

The code then checks for a face match in the set of known faces, and increments score for each match. To display the results of the face recognition, we had to readjust the size of the frame. The next thing to code was to draw a label below the face with the name. Finally, the Google text to speech API says hi to the person it recognizes or says “I’m sorry, I don’t know you.” to ones id doesn’t.

One bug is that it only detects faces in every other frame of the video. However, our first model detected faces in every frame but was less accurate. We decided to go with this version because accuracy is more important, and the bug could be fixed later.

https://youtu.be/xsEYHln5Av0
