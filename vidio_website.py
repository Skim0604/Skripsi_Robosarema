from flask import Flask, render_template, Response, request
import cv2

app = Flask(__name__)

def gen_frames():  
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start')
def start():
    print("start")
    return 'start', 204

@app.route('/stop')
def stop():
    print("stop")
    return 'stop', 204

@app.route('/pick')
def pick():
    print("pick")
    return 'pick', 204

@app.route('/drop')
def drop():
    print("drop")
    return 'drop', 204

@app.route('/forward')
def forward():
    # Tambahkan kode untuk perintah maju
    print("forward")
    return 'Moved Forward', 200

@app.route('/backward')
def backward():
    # Tambahkan kode untuk perintah mundur
    print("backward")
    return 'Moved Backward', 200

@app.route('/left')
def left():
    # Tambahkan kode untuk perintah kiri
    print("left")
    return 'Moved Left', 200

@app.route('/right')
def right():
    # Tambahkan kode untuk perintah kanan
    print("right")
    return 'Moved Right', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
