#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.

## 走行体の設定
color_sensor= ColorSensor(Port.S3)          # カラーセンサー定義
ultra_sensor = UltrasonicSensor(Port.S1)    # 超音波センサー定義
left_motor = Motor(Port.B)                        # ２輪走行体用左モーター定義
right_motor = Motor(Port.C)                       # ２輪走行体用右モーター定義
robot = DriveBase(left_motor, right_motor, 55, 135)     # 長さの単位は mm
"""
DriveBase クラス
- 第１引数: 左モーター
- 第２引数: 右モーター
- 第３引数: タイヤの直径 [mm]
- 第４引数: 車幅 [mm] (車体の回転径)
"""

## 走行開始
ev3.speaker.beep()          # ビープ音を鳴らす

"""
# is_all_green()
## 左右モーターの現在の角度を取得して緑ライトを点灯していいかチェックする関数
## パラメータ
- l_angle: left rotate angle (int)
- r_angle: right rotate angle (int)
"""
def is_all_green(l_angle, r_angle):
    if 0 <= l_angle < 720 and 0 <= r_angle:
        return True
    else: 
        return False


while True:
    l_angle = left_motor.angle()
    r_angle = right_motor.angle()
    
    ev3.screen.draw_text(10, 10, "left")
    ev3.screen.draw_text(100, 10, "right")
    ev3.screen.draw_text(10, 50, f"{l_angle}")
    ev3.screen.draw_text(200, 50, f"{r_angle}")
    
    if is_all_green(l_angle, r_angle):
        ev3.light.on(Color.GREEN)       # 緑色のステータスライトを点灯させる
        wait(50)                        # 0.05 秒点灯継続
        ev3.light.off()                 # 点滅させるためにライト消灯
        wait(50)
    else:
        ev3.light.on(Color.RED)         # 赤色のステータスライトを点灯させる
        wait(50)                        # 0.05 秒点灯継続
        ev3.light.off()                 # 点滅させるためにライト消灯
        wait(50)