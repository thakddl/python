import cv2

# 이미지 읽기
img_source = cv2.imread('images/iu.jpg', 1)
height, width = img_source.shape[:2]
crop_img = img_source[450:750,220:480]
# dst = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
dst = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
height, width = dst.shape[:2]
matrix = cv2.getRotationMatrix2D((width/2, height/2), -25, .5)
dst = cv2.warpAffine(dst, matrix, (width, height))

cv2.imwrite('images/grayImage.png',dst)
# 이미지 화면에 표시
cv2.imwrite('images/sun.png',dst)
cv2.imshow('IU', dst)
cv2.waitKey(0)
# 이미지 윈도우 삭제
cv2.destroyAllWindows()

