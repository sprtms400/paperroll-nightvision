from picamera2 import Picamera2, Preview
import time

def main():
    # Picamera2 인스턴스 생성
    camera = Picamera2()

    # 프리뷰 구성 생성
    preview_config = camera.create_preview_configuration()

    # 카메라 구성
    camera.configure(preview_config)

    # 프리뷰 시작
    preview = Preview(camera)
    preview.start()

    # 카메라 시작
    camera.start()

    try:
        # 무한 루프를 돌면서 카메라 출력을 유지
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # 사용자가 Ctrl+C를 누르면 카메라 중지
        camera.stop()
        preview.stop()

if __name__ == "__main__":
    main()
