# 视频录制部分
import cv2

cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# 第三个参数则是镜头快慢的，10为正常，小于10为慢镜头
video = cv2.VideoWriter("D:/test/result.avi", fourcc, 20, size)
# classifier = cv2.CascadeClassifier("D:/test/demo/result.xml")

count = 0
while count > -1:
    ret, img = cap.read()
    video.write(img)
    cv2.imshow('video', img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cap.release()
cv2.destroyAllWindows()
