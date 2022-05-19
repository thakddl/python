import cv2

# 이미지 읽기
img_source = cv2.imread('images/iu.jpg', 1)
h,w = img_source.shape[:2]
# img_result = cv2.resize(img_source,dsize=(int(w*.5),int(h*.5)), interpolation = cv2.INTER_CUBIC)
img_result = cv2.resize(img_source, None, fx=.5, fy=.5, interpolation = cv2.INTER_CUBIC)
print(img_source)
# 이미지 화면에 표시
cv2.imshow('IU', img_result)
cv2.waitKey(0)
# 이미지 윈도우 삭제
cv2.destroyAllWindows()
