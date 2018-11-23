# 拍照部分
import cv2

cap = cv2.VideoCapture(0)
var = 0
k = 0
print("begin to record images…")

while k != 27:  # esc
    ret, img = cap.read(0)
    cv2.imshow("video windows", img)
    k = cv2.waitKey(20) & 0xff
    cv2.imwrite("D:/test/demo/imaged % 04d.jpg" % (var), img)
    var += 1

cap.release()
cv2.destroyAllWindows()
print("end to record images")
