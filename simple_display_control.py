import spidev
import time
import gc9a01

def main():
    # SPI 디스플레이 초기화
    disp = gc9a01.GC9A01(
        port=0,  # SPI 포트 (SPI0 또는 SPI1)
        cs=24,    # CS 핀 번호
        dc=22,   # DC 핀 번호
        rst=13,  # RST 핀 번호
        backlight=12,  # 백라이트 핀 번호 (필요한 경우)
        rotation=0,    # 화면 회전 (0, 90, 180, 270)
        spi_speed_hz=4000000   # SPI 속도 (Hz)
    )

    # 디스플레이 활성화
    disp.begin()

    # 화면 지우기
    disp.clear()

    # 텍스트 또는 그래픽 출력
    disp.display_text("Hello, World!", x=10, y=10, size=2, color=gc9a01.BLUE)
    
    # 5초 대기
    time.sleep(5)

if __name__ == '__main__':
    main()
