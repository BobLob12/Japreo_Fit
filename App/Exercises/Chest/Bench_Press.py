import cv2
import mediapipe as mp
import numpy as np
import time
from AudioCoach.Messages.Message_Player import Congratulation_Message, Go_Up_Message 
from Rep_SoundEffects.Play_Rep_Sound import Rep_One, Rep_Two, Rep_Three, Rep_Four, Rep_Five, Rep_Six, Rep_Seven, Rep_Eight, Rep_Nine, Rep_Ten, Rep_Eleven, Rep_Twelve




mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


def BenchPress():




 cap = cv2.VideoCapture(0)




 # Curl counter variables
 counter = 0 
 stage = None

 ## Setup mediapipe instance
 with mp_pose.Pose(min_detection_confidence=0.8, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
      
        # Make detection
        results = pose.process(image)
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark
            
            # Get coordinates
            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            shoulder_1 = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            elbow_1 = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            wrist_1 = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

           
            


            def calculate_angle(a,b,c):
             a = np.array(a) # First
             b = np.array(b) # Mid
             c = np.array(c) # End
    
             radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
             angle = np.abs(radians*180.0/np.pi)
             round_angle = np.round(angle)
    
             if round_angle > 180.0:
              round_angle = 360-round_angle
        
             return round_angle 
            
            def calculate_angle2(a,b,c):
             a = np.array(a) # First
             b = np.array(b) # Mid
             c = np.array(c) # End
    
             radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
             angle2 = np.abs(radians*180.0/np.pi)
             round_angle2 = np.round(angle2)
    
             if round_angle2 > 180.0:
              round_angle2 = 360-round_angle2
        
             return round_angle2 
          

            # Calculate angle
            round_angle = calculate_angle(shoulder, elbow, wrist)
            round_angle2 = calculate_angle(shoulder_1,elbow_1,wrist_1)
            
            """
            # Visualize angle
            cv2.putText(image, str(round_angle), 
                           tuple(np.multiply(elbow, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4, cv2.LINE_AA
                                )
            
             # Visualize angle
            cv2.putText(image, str(round_angle2), 
                           tuple(np.multiply(elbow_1, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4, cv2.LINE_AA
                                )
            """
            
            # Curl counter logic
            if round_angle > 120:
                stage = "up"
            if round_angle < 98 and stage =='up':
                stage="down"
                counter +=1
                print(counter)

                if counter == 1:
               
                 Rep_One()
             

                if counter == 2:
               
                  Rep_Two()
 

                if counter == 3:
               
                   Rep_Three()
             

                if counter == 4:
               
                  Rep_Four()
              

                if counter == 5:
               
                  Rep_Five()


                if counter == 6:
               
                  Rep_Six()

                
                if counter == 7:
               
                 Rep_Seven()
             

                if counter == 8:
               
                  Rep_Eight()
 

                if counter == 9:
               
                   Rep_Nine()
             

                if counter == 10:
               
                  Rep_Ten()

                if counter == 11:
               
                  Rep_Eleven()

                if counter == 12:
               
                  Rep_Twelve()


                  cap.release()
                  cv2.destroyAllWindows()
                  time.sleep(2)
                  Congratulation_Message()
                       

            if round_angle2 > 160:
                stage = "up"
            if round_angle2 < 70 and stage =='up':
                stage="down"
                counter +=1
                print(counter)

                if counter == 1:
               
                 Rep_One()
             

                if counter == 2:
               
                  Rep_Two()
 

                if counter == 3:
               
                   Rep_Three()
             

                if counter == 4:
               
                  Rep_Four()
              

                if counter == 5:
               
                  Rep_Five()


                if counter == 6:
               
                  Rep_Six()

                
                if counter == 7:
               
                 Rep_Seven()
             

                if counter == 8:
               
                  Rep_Eight()
 

                if counter == 9:
               
                   Rep_Nine()
             

                if counter == 10:
               
                  Rep_Ten()

                if counter == 11:
               
                  Rep_Eleven()

                if counter == 12:
               
                  Rep_Twelve()


                  cap.release()
                  cv2.destroyAllWindows()
                  time.sleep(2)
                  Congratulation_Message()
        except:
            pass
        
        # Render curl counter
        # Setup status box

        """
        cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)
        
        # Rep data
        cv2.putText(image, 'REPS', (15,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, str(counter), 
                    (10,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
        cv2.putText(image, str('Pushups' ), 
                    (10,120), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 2, cv2.LINE_AA)
        
        # Stage data
        cv2.putText(image, 'STAGE', (65,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, stage, 
                    (60,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )               
        """
        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__BenchPress__':
   BenchPress()
