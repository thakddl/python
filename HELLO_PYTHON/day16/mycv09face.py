import cv2

# haarcascade 불러오기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# 이미지 불러오기
img = cv2.imread('images/iu.jpg', 1)
pang = cv2.imread('images/pang.png', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 얼굴 찾기
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    roi = img[y:y+h, x:x+w]#배경이미지의 변경할(다음 로고 넣을) 영역
    pang_re = cv2.resize(pang, dsize=(w,h), interpolation = cv2.INTER_CUBIC)#영역에 맞게 팽수 변환
    pang_h,pang_w = pang_re.shape[:2]
    
    mask = cv2.cvtColor(pang_re, cv2.COLOR_BGR2GRAY)#로고를 흑백처리
    #이미지 이진화 => 배경은 검정. 팽수는 흰색
    mask[mask[:]==255]=0
    mask[mask[:]>0]=255
    mask_inv = cv2.bitwise_not(mask)
    
    pang2 = cv2.bitwise_and(pang_re, pang_re, mask=mask)# 팽수만 추출
    back = cv2.bitwise_and(roi, roi, mask=mask_inv)
    dst = cv2.add(pang2, back)
    img[y:y+h, x:x+w] = dst

    # 눈 찾기
    # roi_color = img[y:y + h, x:x + w]
    # roi_gray = gray[y:y + h, x:x + w]
    # eyes = eye_cascade.detectMultiScale(roi_gray)
    # for (ex, ey, ew, eh) in eyes:
    #     cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

# 영상 출력
cv2.imshow('image', img)

key = cv2.waitKey(0)
cv2.destroyAllWindows()