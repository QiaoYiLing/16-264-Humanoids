import face_recognition
import cv2
import os
from gtts import gTTS
import os
import pygame
from pygame import mixer

          
# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
 
known_face_encodings = []
known_face_names = []
picDir = "./pics/"
picAll = os.listdir(picDir)
for photoName in picAll:
    if photoName == '.DS_Store':
        continue
    temp_image = face_recognition.load_image_file(picDir+photoName)
    temp_encoding = face_recognition.face_encodings(temp_image)[0]
    known_face_encodings.append(temp_encoding)
    known_face_names.append(photoName.split('.')[0])



# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True



timer = 0

while True:
    timer += 1

    #create a pygame object instance
    pygame.init()
    pygame.mixer.init()
    
    #keep a score to improve accuracy
    score = [0]*len(known_face_names)
    
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            #increment score for each match
            while True in matches:
                match_index = matches.index(True)
                matches[match_index] = False

                #each time a match occurs, increase the score
                score[match_index] = match_index+1
                #name = known_face_names[match_index]
                
            #face_names.append(name)

    process_this_frame = not process_this_frame
    

    for (top, right, bottom, left) in face_locations:
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            # Draw a box around the face(s)
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            
    if timer%5 == 0:
        timer = 0
        sorted_score = sorted(score)
        highscore = sorted_score[-1]
        
        if highscore == 0:
            best_name = "unknown"
        else:
            highscore_index = score.index(highscore)            
            best_name = known_face_names[highscore_index]
            
        face_names.append(best_name)
 
           
        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4         

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        
        temp = face_names
        count = 0
        while "unknown" in temp:
            count += 1
            temp.remove("unknown")
        if count != 0:
            text_to_output = "Hi, " + ', '.join(temp) + "I'm sorry, I don't know " + str(count) + " of you."
        else:
            text_to_output = "Hi, " + ', '.join(temp)
        tts = gTTS(text=text_to_output, lang='en')
        tts.save("output.mp3")
        pygame.mixer.music.load('output.mp3')
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(30)
            
            
    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()



