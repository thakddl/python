import cv2

# 이미지 읽기
img = cv2.imread('images/b.png', 1)
print(img)
# 이미지 화면에 표시
cv2.imshow('IU', img)
cv2.waitKey(0)
# 이미지 윈도우 삭제
cv2.destroyAllWindows()

# r.png
# [[[ 36  28 237]
#   [ 36  28 237]]
#
#  [[ 36  28 237]
#   [ 36  28 237]]
#
#  [[ 36  28 237]
#   [ 36  28 237]]]

# g.png
# [[[ 87 182  48]
#   [ 76 177  34]]
#
#  [[ 76 177  34]
#   [ 76 177  34]]
#
#  [[ 76 177  34]
#   [ 76 177  34]]]

# b.png
# [[[204  72  63]
#   [204  72  63]]
#
#  [[204  72  63]
#   [204  72  63]]
#
#  [[204  72  63]
#   [204  72  63]]]