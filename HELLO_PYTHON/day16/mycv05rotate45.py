import cv2

# 이미지 읽기
img = cv2.imread('images/iu.jpg', 1)
height, width, channel = img.shape
print(img.shape)
matrix = cv2.getRotationMatrix2D((width/2, height/2), -25, .5)
dst = cv2.warpAffine(img, matrix, (width, height))
# 이미지 화면에 표시
cv2.imshow('IU', dst)
cv2.waitKey(0)
# 이미지 윈도우 삭제
cv2.destroyAllWindows()
