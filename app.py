import sys
import cv2 
import imutils
from yoloDet import YoloTRT

# use path for library and engine file
model = YoloTRT(library="yolov5/buildModelYoloV5s/libmyplugins.so", engine="yolov5/buildModelYoloV5s/trainYoloV5s.engine", conf=0.8, yolo_ver="v5")

cap = cv2.VideoCapture(0) # KAMERA WEBCAM

while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=600)
    detections, t = model.Inference(frame)
    
    for obj in detections:
        print(obj['class'], obj['conf'], obj['box'])
        if obj['class'] == "KORBAN":
            x1, y1, x2, y2 = obj['box']
            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1) # Menampilkan titik tengah dengan lingkaran merah
    
    print("FPS: {} sec".format(1/t))
    
    cv2.imshow("Output", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
