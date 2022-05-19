import cv2

# 이미지 읽기
img = cv2.imread('images/iu.jpg', 1)
img180 = cv2.rotate(img, cv2.ROTATE_180)
print(img)
# 이미지 화면에 표시
cv2.imshow('IU', img180)
cv2.waitKey(0)
# 이미지 윈도우 삭제
cv2.destroyAllWindows()
