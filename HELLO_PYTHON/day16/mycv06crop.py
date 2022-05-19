import cv2

# 이미지 읽기
img = cv2.imread('images/iu.jpg', 1)
print(img)
crop_img = img[20:500,50:500]
# 이미지 화면에 표시
cv2.imshow('IU', crop_img)
cv2.waitKey(0)
# 이미지 윈도우 삭제
cv2.destroyAllWindows()
