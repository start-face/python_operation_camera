# 该部分是同时录制视频和同时拍照的功能
import cv2, time

cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# 这种格式的编码生成的视频比较小
four_encode = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# 第三个参数则是镜头快慢的，10为正常，小于10为慢镜头
video = cv2.VideoWriter("D:/test/result(%s).avi" % (time.strftime("%Y%m%d%H%M%S", time.localtime())), four_encode, 20, size)

k, var = 0, 0

while k != 27:  # esc
    ret, img = cap.read()
    cv2.imshow("video windows", img)
    k = cv2.waitKey(20) & 0xff
    video.write(img)
    cv2.imwrite("D:/test/demo/image %04d(%s).jpg" % (var, time.strftime("%Y%m%d%H%M%S", time.localtime())), img)
    var += 1

video.release()
cap.release()
cv2.destroyAllWindows()
