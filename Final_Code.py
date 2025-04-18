import random
from engi1020.arduino.api import *
from time import sleep, time
import cv2
import HandTrackingModule as htm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt




scores = []


def playgame():
    while True:
        task = []
        color_index_dict = {}
        list_num = [1,2,3,4,5]
        name_inp = input('Enter your Name: ').upper()
        difficulty_list = [['easy'],['medium'],['hard']]
        task_list = ['RED','BLUE','GREEN','YELLOW','PURPLE']
        value_of_fingers = []
        colors_chosen = []
        diff_inp = input('Enter difficulty level: ').lower()
        if diff_inp == 'easy':
            task.append(random.sample(task_list,3))
            sleep_timer = 2
            duration = 20
        elif diff_inp == 'medium':
            task.append(random.sample(task_list,4))
            sleep_timer = 2
            duration = 30
        elif diff_inp == 'hard':
            task.append(random.sample(task_list,5))
            sleep_timer = 3
            duration = 36
        else:
            print('Invalid')
            continue
        
        break

    for q in task:
        for h in q:
            color_index_dict[h] = random.choice(list_num)
    for aaa,bbb in color_index_dict.items():
        value_of_fingers.append(bbb)
        colors_chosen.append(aaa)

    def get_color():
        while True:
            for i in task:
                for j in i:
                    if j == 'RED':
                        rgb_lcd_clear()
                        sleep(sleep_timer)
                        rgb_lcd_colour(255,0,0)
                    elif j == 'BLUE':
                        rgb_lcd_clear()
                        sleep(sleep_timer)
                        rgb_lcd_colour(0,0,255)
                    elif j == 'GREEN':
                        rgb_lcd_clear()
                        sleep(sleep_timer)
                        rgb_lcd_colour(0,255,0)
                    elif j == 'YELLOW':
                        rgb_lcd_clear()
                        sleep(sleep_timer)
                        rgb_lcd_colour(255,255,0)
                    elif j == 'PURPLE':
                        rgb_lcd_clear()
                        sleep(sleep_timer)
                        rgb_lcd_colour(125,0,255)  
                sleep(sleep_timer)
                rgb_lcd_colour(0,255,255)
            break


    rgb_lcd_clear()
    """ speaking.say("get ready for the game")
    speaking.runAndWait() """
    print("Get ready for the Game!")
    print('countdown: ',3)
    sleep(1)
    print('countdown: ',2)
    sleep(1)
    print('countdown: ',1)
    sleep(1)
    # get_color()
    get_color()
    sleep(2)
    rgb_lcd_print('Memorise the ',)
    rgb_lcd_print('Values very well',1)
    sleep(5)
    rgb_lcd_clear()

    for vvv,mmm in zip(value_of_fingers,colors_chosen):
        rgb_lcd_colour(0,255,255)
        rgb_lcd_print(f'Value for {mmm}')
        rgb_lcd_print(f'is {vvv}:',1,6)
        sleep(3)
        rgb_lcd_clear()


    cap = cv2.VideoCapture(0)
    cap.set(3,650)
    cap.set(4,500)


    points = 0
    start_time = time()
    detector = htm.handDetector(detectionCon=0.75) 
    tips_ids = [4,8,12,16,20]
    time1 = duration-6
    time2 = time1-6
    time3 = time2-6
    time4 = time3-6
    time5 = time4-6
    fingers_count1 = 0


    while True:
        if diff_inp == 'easy' :
            success, img = cap.read()
            img = detector.findHands(img)
            lmlist = detector.findPosition(img, draw=True)
            if len(lmlist) != 0:
                fingers = []
                if lmlist[tips_ids[0]][1] > lmlist[tips_ids[0]-1][1]:
                        fingers.append(1)
                else:
                    fingers.append(0)
                for id in range(1,5):
                    if lmlist[tips_ids[id]][2] < lmlist[tips_ids[id]-2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                fingers_count1 = sum(fingers)
            
            
            elapsed_time = time() - start_time
            remaining_time = duration - int(elapsed_time)

            cv2.putText(img, f'Timer: {remaining_time}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.rectangle(img, (20,425), (250, 825), (255,0,0), cv2.FILLED)
            cv2.putText(img, str(fingers_count1), (75,675), cv2.FONT_HERSHEY_PLAIN, 13, (0,255,0), 25 )


            if remaining_time == 0 or remaining_time <= 0:
                cap.release()
                cv2.destroyAllWindows()
                break
            elif remaining_time == time1+2:
                cv2.putText(img, 'Enter Color 1', (1250,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 3)
            elif remaining_time == time1:
                try:
                    x1 = fingers
                except: 
                    x1 = []
                
                color1 = sum(x1)
                if color1 != value_of_fingers[0]:
                    buzzer_note(5,400,4)
                    num_of_points = points
                elif color1 == value_of_fingers[0]:
                    num_of_points = points + 1
            elif remaining_time == time2+2:
                cv2.putText(img, 'Enter Color 2', (1250,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 3)
            elif remaining_time == time2:
                try:
                    x2 = fingers
                except:
                    x2 = []
                color2 = sum(x2)
                if color2 != value_of_fingers[1]:
                    buzzer_note(5,400,4)
                    num_of_points2 = num_of_points
                elif color2 == value_of_fingers[1]:
                    num_of_points2 = num_of_points + 1
            elif remaining_time == time3+2:
                cv2.putText(img, 'Enter Color 3', (1250,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 3)
            elif remaining_time == time3:
                try:
                    x3 = fingers
                except:
                    x3 = []
                color3 = sum(x3)
                if color3 != value_of_fingers[2]:
                    buzzer_note(5,400,4)
                    num_of_points3 = num_of_points2
                elif color3 == value_of_fingers[2]:
                    num_of_points3 = num_of_points2 + 1
            cv2.imshow('image', img)
            cv2.waitKey(1)

    # Medium Difficulty

        elif diff_inp == 'medium':
            success, img = cap.read()
            img = detector.findHands(img)
            lmlist = detector.findPosition(img, draw=True)
            if len(lmlist) != 0:
                fingers = []
                if lmlist[tips_ids[0]][1] > lmlist[tips_ids[0]-1][1]:
                        fingers.append(1)
                else:
                    fingers.append(0)
                for id in range(1,5):
                    if lmlist[tips_ids[id]][2] < lmlist[tips_ids[id]-2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                fingers_count1 = sum(fingers)
            
            elapsed_time = time() - start_time
            remaining_time = duration - int(elapsed_time)

            cv2.putText(img, f'Timer: {remaining_time}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.rectangle(img, (20,425), (250, 825), (255,0,0), cv2.FILLED)
            cv2.putText(img, str(fingers_count1), (75,675), cv2.FONT_HERSHEY_PLAIN, 13, (0,255,0), 25 )
            
            if remaining_time == 0 or remaining_time <= 0:
                cap.release()
                cv2.destroyAllWindows()
                break
            elif remaining_time == time1+2:
                cv2.putText(img, 'Enter Color 1', (1250,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 3)
            elif remaining_time == time1:
                try:
                    x1 = fingers
                except: 
                    x1 = []
                
                color1 = sum(x1)
                if color1 != value_of_fingers[0]:
                    buzzer_note(5,400,4)
                    num_of_points = points
                elif color1 == value_of_fingers[0]:
                    num_of_points = points + 1
            elif remaining_time == time2+2:
                cv2.putText(img, 'Enter Color 2', (1250,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 3)
            elif remaining_time == time2:
                x2 = fingers
                color2 = sum(x2)
                if color2 != value_of_fingers[1]:
                    buzzer_note(5,400,4)
                    num_of_points2 = num_of_points
                elif color2 == value_of_fingers[1]:
                    num_of_points2 = num_of_points + 1
            elif remaining_time == time3+2:
                cv2.putText(img, 'Enter Color 3', (1250,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 3)
            elif remaining_time == time3:
                x3 = fingers
                color3 = sum(x3)
                if color3 != value_of_fingers[2]:
                    buzzer_note(5,400,4)
                    num_of_points3 = num_of_points2
                elif color3 == value_of_fingers[2]:
                    num_of_points3 = num_of_points2 + 1
            elif remaining_time == time4+2:
                cv2.putText(img, 'Enter Color 4', (1250,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 3)
            elif remaining_time == time4:
                x4 = fingers
                color4 = sum(x4)
                if color4 != value_of_fingers[3]:
                    buzzer_note(5,400,4)
                elif color4 == value_of_fingers[3]:
                    num_of_points4 = num_of_points3 + 1
            cv2.imshow('image', img)
            cv2.waitKey(1)

    # hard difficulty

        elif diff_inp == 'hard':
            success, img = cap.read()
            img = detector.findHands(img)
            lmlist = detector.findPosition(img, draw=True)
            if len(lmlist) != 0:
                fingers = []
                if lmlist[tips_ids[0]][1] > lmlist[tips_ids[0]-1][1]:
                        fingers.append(1)
                else:
                    fingers.append(0)
                for id in range(1,5):
                    if lmlist[tips_ids[id]][2] < lmlist[tips_ids[id]-2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                fingers_count1 = sum(fingers)
            
            elapsed_time = time() - start_time
            remaining_time = duration - int(elapsed_time)

            cv2.putText(img, f'Timer: {remaining_time}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.rectangle(img, (20,425), (250, 825), (255,0,0), cv2.FILLED)
            cv2.putText(img, str(fingers_count1), (75,675), cv2.FONT_HERSHEY_PLAIN, 13, (0,255,0), 25 )
            
            
            if remaining_time == 0:
                cap.release()
                cv2.destroyAllWindows()
                break
            elif remaining_time == time1+2:
                cv2.putText(img, 'Enter Color 1', (1250,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 3)
            elif remaining_time == time1:
                try:
                    x1 = fingers
                except: 
                    x1 = []
                
                color1 = sum(x1)
                if color1 != value_of_fingers[0]:
                    buzzer_note(5,400,4)
                    num_of_points = points
                elif color1 == value_of_fingers[0]:
                    num_of_points = points + 1
            elif remaining_time == time2+2:
                cv2.putText(img, 'Enter Color 2', (1250,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 3)
            elif remaining_time == time2:
                x2 = fingers
                color2 = sum(x2)
                if color2 != value_of_fingers[1]:
                    buzzer_note(5,400,4)
                    num_of_points2 = num_of_points
                elif color2 == value_of_fingers[1]:
                    num_of_points2 = num_of_points + 1
            elif remaining_time == time3+2:
                cv2.putText(img, 'Enter Color 3', (1250,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 3)
            elif remaining_time == time3:
                x3 = fingers
                color3 = sum(x3)
                if color3 != value_of_fingers[2]:
                    buzzer_note(5,400,4)
                    num_of_points3 = num_of_points2
                elif color3 == value_of_fingers[2]:
                    num_of_points3 = num_of_points2 + 1
            elif remaining_time == time4+2:
                cv2.putText(img, 'Enter Color 4', (1250,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 3)
            elif remaining_time == time4:
                x4 = fingers
                color4 = sum(x4)
                if color4 != value_of_fingers[3]:
                    buzzer_note(5,400,4)
                    num_of_points4 = num_of_points3
                elif color4 == value_of_fingers[3]:
                    num_of_points4 = num_of_points3 + 1
            elif remaining_time == time5+2:
                cv2.putText(img, 'Enter Color 5', (1250,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 3)
            elif remaining_time == time5:
                x5 = fingers
                color5 = sum(x5)
                if color5 != value_of_fingers[4]:
                    buzzer_note(5,400,4)
                    num_of_points5 = num_of_points4
                elif color5 == value_of_fingers[4]:
                    num_of_points5 = num_of_points4 + 1
            cv2.imshow('image', img)
            cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()
    sleep(2)

# Displaying scores
    if diff_inp == 'easy':
        if num_of_points3 == 0:
            rgb_lcd_print("Fail",0,6)
            rgb_lcd_print('Try again :)',1,2)
            sleep(10)
            rgb_lcd_clear()
        else:
            rgb_lcd_print('Congrats',0,4)
            rgb_lcd_print(f'You got {num_of_points3} points',1)
            sleep(10)
            rgb_lcd_clear()
        final_points = num_of_points3

    elif diff_inp == 'medium':
        if num_of_points4 == 0:
            rgb_lcd_print("Fail",0,6)
            rgb_lcd_print('Try again :)',1,2)
            sleep(10)
            rgb_lcd_clear()
        else:
            rgb_lcd_print('Congrats',0,4)
            rgb_lcd_print(f'You got {num_of_points4} points',1)
            sleep(10)
            rgb_lcd_clear()
        final_points = num_of_points4
            
    elif diff_inp == 'hard':
        if num_of_points5 == 0:
            rgb_lcd_print("Fail",0,6)
            rgb_lcd_print('Try again :)',1,2)
            sleep(10)
            rgb_lcd_clear()
        else:
            rgb_lcd_print('Congrats',0,4)
            rgb_lcd_print(f'You got {num_of_points5} points',1)
            sleep(10)
            rgb_lcd_clear()
        final_points = num_of_points5
    
    scores.append((name_inp,final_points))
    play_again = input("Do you want to play again? ").lower()

    if play_again == 'yes':
        playgame()
    elif play_again == 'no':
        plt.xlabel('Players')
        plt.ylabel('Scores')
        plt.grid(True)
        names, scores1 = zip(*scores)
        plt.bar(names, scores1,color='skyblue')
        plt.savefig('scores.png')
        print('Check your score!')


playgame()

