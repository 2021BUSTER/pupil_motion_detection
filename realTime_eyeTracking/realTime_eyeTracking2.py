"""
Eye detection Using Dlib
pre-train (68 key point)  - shape68.dat에 미리 pre train되어 있음
dlib 라이브러리 - 실시간 prediction이 가능하게 함 
face keypoint detector - dlib 모듈의 직사각형 객체를 단순히 얼굴의 좌표인 입력으로 사용
		     - dlib의 내장 정면 얼굴 감지기를 사용
CNN을 사용하는 것이 정확도와 스피트면에서 좋음
"""

import cv2
import dlib
import numpy as np
from scipy.spatial import distance
import time
import threading

coord=np.ndarray([])
c_bad=0
c_good=0
cnt=0

start=0
bad_flag=0

def shape_to_np(shape, dtype="int"):
	# initialize the list of (x, y)-coordinates
	coords = np.zeros((68, 2), dtype=dtype)
	# loop over the 68 facial landmarks and convert them
	# to a 2-tuple of (x, y)-coordinates
	for i in range(0, 68):
		coords[i] = (shape.part(i).x, shape.part(i).y)
	# return the list of (x, y)-coordinates
	return coords

def eye_on_mask(mask, side):            
    points = [shape[i] for i in side]
    points = np.array(points, dtype=np.int32)
    mask = cv2.fillConvexPoly(mask, points, 255)    # 데이터 유형 np.int32 , 255= white로 채워진 영역이 있는 이미지로 반환
    return mask

def contouring(thresh, mid, img, right=False):
    global coord
    cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) 
    try:
        cnt = max(cnts, key = cv2.contourArea)
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

        if right:
            cx += mid
        cv2.circle(img, (cx, cy), 4, (0, 0, 255), 2)
        coord=np.array([cx,cy])
        
    except:
        #print("눈 감음")
        pass

def eyes_tracking(right=False):
    global coord
    global c_bad,c_good,bad_flag
    global start
    if right==False and coord.size == 2:
        l_top_y=(shape[37][1]+shape[38][1])/2
        l_bottom_y=(shape[41][1]+shape[40][1])/2
        l_left_x=(shape[38][0]+shape[40][0])/2  
        l_right_x=(shape[37][0]+shape[41][0])/2
        
        flag_eyes = 0

        if coord[0] > (l_left_x - 2) :
            # print("l 범위 = ", l_left_x-2, " ", coord[0])
            flag_eyes=1
        if coord[0] < (l_right_x + 2):
            #print("r 범위 = ", l_right_x+2, " ", coord[0])
            #print("오른쪽")
            flag_eyes=1
        if coord[1] < (l_top_y + 2) :
            #print("위",coord[1], " ",l_top_y)
            # print("t 범위 = ",l_top_y + 2, " ", coord[1] )  
            flag_eyes=1  
        # if coord[1] > l_bottom_y-2:
        #     print("아래",coord[1]," ",l_bottom_y)
        #     flag_eyes=1

        if flag_eyes == 1 :
            #print("집중해!")
            flag_eyes = 0
            if bad_flag==0:
                start=time.time()
                bad_flag=1

            else:
                check_T=time.time()-start
                if check_T>5:
                    c_bad+=1
                    bad_flag=0
                    print("집중하자",check_T)
                    check_T=0
                    start=0
                    bad_flag=0
            
        elif flag_eyes == 0:
            #print("잘했어 예지")
            bad_flag=0
           
        
        #if coord[1] > l_bottom_y:
        #    print("아래")
        #elif coord[1] > l_top_y and coord[0] > l_left_x and coord[0] < l_right_x:
        #    print("정면")
        #else:
        #    print("딴짓 baaaam")

        # if coord[0]>l_left_x and coord[0]<l_right_x: #and coord[1]>l_bottom_y and coord[1]<l_top_y:
        #     print("정면")
        # else:
        #     print("no 정면")


detector = dlib.get_frontal_face_detector()     # dlib에 내장된 얼굴 정면 탐지
predictor = dlib.shape_predictor('shape_68.dat')    # 미리 학습된 얼굴의 68개 좌표
#predictor = dlib.shape_predictor("/Users/JeongYerin/Desktop/Capstone Design/source_code/pupil_motion_detection/realTime_eyeTracking/shape_68.dat")    # 미리 학습된 얼굴의 68개 좌표
left = [36, 37, 38, 39, 40, 41] # shape_68의 left 눈의 좌표
right = [42, 43, 44, 45, 46, 47]    # shape_68의 right 눈의 좌표

cap = cv2.VideoCapture(0)
ret, img = cap.read()
thresh = img.copy()

cv2.namedWindow('image')
kernel = np.ones((9, 9), np.uint8)

def nothing(x):
    pass
cv2.createTrackbar('threshold', 'image', 0, 255, nothing)   # bar 생성

# count = 0
# def startTimer():
#     global count
#     timer = threading.Timer(10, startTimer)     # 10초 마다 타이머 실행
#     timer.start()
#     print(count)
#     count += 1
#     if count > 5:
#         count=0
#         timer.cancel()
while(True):

    #startTimer()
    
    ret, img = cap.read() # ret: 잘 읽어왔는지 true or false, img : 프레임값 읽어옴
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # gray scale로 바꾸기
    rects = detector(gray, 1)   # 모든 face detector를 포함하고 있음 (사각형(얼굴을 인식)) -> white 영역이 눈의 영역
  
    if  len(rects)==0:
        if bad_flag==0:
            start=0
            start=time.time()
            bad_flag=1

        else:
            check_T=time.time()-start
            if check_T>5:
                c_bad+=1
                print("집중하자",check_T)
                bad_flag=0
                check_T=0
                start=0
                bad_flag=0
    
    for rect in rects:
        

        shape = predictor(gray, rect)       
        shape = shape_to_np(shape)
        mask = np.zeros(img.shape[:2], dtype=np.uint8)  # 웹캡 프레임 사이즈로 0으로 채우기 = black mask만들기
       
        mask = eye_on_mask(mask, left)      # left,right 눈 좌표를 mask에 그리기위해
        mask = eye_on_mask(mask, right)

        mask = cv2.dilate(mask, kernel, 5) # morphological operation으로 black mask의 눈 영역을 조금 확장시킴
        eyes = cv2.bitwise_and(img, img, mask=mask)     # (0,0,0)인 부분을 모두 (255,255,255)로 바꾸어 안구만 부분만 유일하게 어두운 부분이 되도록 함
                                                        # 비트 And연산 , mask : 적용 지점
        mask = (eyes == [0, 0, 0]).all(axis=2) 
        eyes[mask] = [255, 255, 255]
        mid = (shape[42][0] + shape[39][0]) // 2
        eyes_gray = cv2.cvtColor(eyes, cv2.COLOR_BGR2GRAY)  # threshodld를 하기 위해 gray scale로 바꾸기

        threshold = cv2.getTrackbarPos('threshold', 'image')    # threshold는 binary mask를 만들어줌 (0,1) , 눈알부분의 최적의 threshold값을 찾는게 목표
                                                                # threshold값이 lighting condition에 따라 달라서 bar로 threshold값을 조절해야 함
        _, thresh = cv2.threshold(eyes_gray, threshold, 255, cv2.THRESH_BINARY)
        thresh = cv2.erode(thresh, None, iterations=2) #1       # 이미지 침식 , iterations = 반복횟수
        thresh = cv2.dilate(thresh, None, iterations=4) #2      # 이미지 팽창
        thresh = cv2.medianBlur(thresh, 3) #3                   # median filter
        thresh = cv2.bitwise_not(thresh)                        # cv.findCounters()가 오브젝트로 눈알을 인식하기 위해 오브젝트는 white, 배경은 black으로 바꿔줘야 함

        contouring(thresh[:, 0:mid], mid, img)
        eyes_tracking()
        contouring(thresh[:, mid:], mid, img, True)
        eyes_tracking(True)
        
        # if cnt==10:
        #     if (c_good + c_bad)/2 > 0:
        #         print("집중하고 있네!!")
        #     else:
        #         print("집중하자!!") 
        #     c_bad=0
        #     c_good=0
        #     cnt=0
        for (x, y) in shape[36:48]:
            cv2.circle(img, (x, y), 2, (255, 0, 0), -1)
    # show the image with the face detections + facial landmarks

    cv2.imshow('eyes', img)
    cv2.imshow("image", thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
