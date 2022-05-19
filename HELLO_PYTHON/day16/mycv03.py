import cv2

# 이미지 읽기
img = cv2.imread('images/r.png', 1)
# aa = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img)
print(dst)
# 이미지 화면에 표시
cv2.imshow('IU', dst)
cv2.waitKey(0)
# 이미지 윈도우 삭제
cv2.destroyAllWindows()
