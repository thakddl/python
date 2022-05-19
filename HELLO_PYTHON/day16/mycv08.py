import cv2
# print(cv2.__version__)

img_source = cv2.imread('images/iu.jpg',1)
crop_img = img_source[450:750,220:480]
cv2.imshow("dangdang", crop_img) # 불러온 이미지를 Lenna라는 이름으로 창 표시.
cv2.imwrite("images/rose.jpg", crop_img) # imgs 폴더에 Lenna_GrayScale.png 이미지 저장

cv2.waitKey() # 키보드 입력이 들어올 때까지 창을 유지
cv2.destroyAllWindows() # 모든 윈도우 창을 제거
