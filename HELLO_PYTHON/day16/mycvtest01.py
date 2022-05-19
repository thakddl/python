import cv2

# 이미지 읽기
img_source = cv2.imread('images/iu.jpg', 1)
h,w = img_source.shape[:2]
crop_img = img_source[450:750,220:480]
# 이미지 화면에 표시
cv2.imwrite('images/rose.png',crop_img)
cv2.imshow('IU', crop_img)
cv2.waitKey(0)
# 이미지 윈도우 삭제
cv2.destroyAllWindows()

