from picamera2 import Picamera2
import cv2
import numpy as np

def main():
    # Picamera2 인스턴스 생성
    camera = Picamera2()
    camera_config = camera.create_preview_configuration(main={"size": (640, 480)})
    camera.configure(camera_config)

    # 카메라 시작
    camera.start()

    while True:
        # 카메라로부터 프레임 캡처
        frame = camera.capture_array()

        # OpenCV를 사용하여 화면에 표시
        cv2.imshow("Frame", frame)

        # 'q' 키가 눌렸는지 확인
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 카메라 정지
    camera.stop()

    # 모든 창 닫기
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()