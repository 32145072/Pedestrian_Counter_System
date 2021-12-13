#  https://www.denshi.club/parts/2021/05/gpiozero13import-mcp3001mcp3002mcp3004mcp3008-2.html

#  gpiozero doc: https://gpiozero.readthedocs.io/en/stable/

#  つなぎ方: https://chasuke.com/motionsensor/

#  人感センサーについて: https://deviceplus.jp/hobby/pir-motion-sensors-with-raspberrypi-python/

from gpiozero import MotionSensor
import schedule
from time import sleep

pir = MotionSensor(9)
count_pedestrian = 0

def write_spread_sheet():
    # ここにスプレッドシートに書き込む処理
    pass

schedule.every().hour.do(write_spread_sheet)    # 1時間ごとに用意してあるスプレッドシートに変数:count_pedestrianの中身を送る処理

while True:
    
    try:
        pir.wait_for_motion()
        count_pedestrian += 1
        sleep(2)
        
        print(count_pedestrian) # test code
        
    except KeyboardInterrupt:
        print("終了")

