import cv2
import mediapipe as mp
import numpy as np
import time
from playsound import playsound 
from Rep_SoundEffects.Play_Rep_Sound import Rep_One, Rep_Two, Rep_Three, Rep_Four, Rep_Five, Rep_Six, Rep_Seven, Rep_Twelve, Rep_Eleven, Rep_Eight, Rep_Nine, Rep_Ten
from AudioCoach.Messages.Message_Player import Congratulation_Message, Go_Up_Message 



mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


def HamstringCurls():
   

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
            Left_Hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            Left_Knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            Left_Ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

            Right_Hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            Right_Knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
            Right_Ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

           
            


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
            round_angle = calculate_angle(Left_Hip, Left_Knee, Left_Ankle)
            round_angle2 = calculate_angle(Right_Hip, Right_Knee, Right_Ankle)
            
            """
            # Visualize angle
            cv2.putText(image, str(round_angle), 
                           tuple(np.multiply(Left_Knee, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4, cv2.LINE_AA
                                )
            
             # Visualize angle
            cv2.putText(image, str(round_angle2), 
                           tuple(np.multiply(Right_Knee, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4, cv2.LINE_AA
                                )
            """
            # Curl counter logic
            if round_angle >= 140:
                stage = "up"
            if round_angle <= 80 and stage =='up':
                
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
                       

            if round_angle2 >= 140:
                stage = "up"
            if round_angle2 <= 80 and stage =='up':
                
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
        
        """
        # Render curl counter
        # Setup status box
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


if __name__ == '__HamstringCurls':
   HamstringCurls()