from picamera2 import Picamera2
import cv2
import numpy as np

def capture_and_display():
    camera = Picamera2()
    camera_config = camera.create_preview_configuration()
    camera.configure(camera_config)
    camera.start()

    while True:
        # 카메라에서 이미지 캡처
        frame = camera.capture_array()

        # 이미지 리사이징 (240x240으로 조정)
        resized_frame = cv2.resize(frame, (240, 240))

        # 이미지를 SPI 디스플레이의 프레임버퍼로 출력
        with open('/dev/fb1', 'wb') as fb:  # X는 실제 프레임버퍼 번호
            fb.write(resized_frame.tobytes())

if __name__ == "__main__":
    capture_and_display()