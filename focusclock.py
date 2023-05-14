import time
import winsound

# 设置工作时间和休息时间（单位：秒）
work_time = 25*60
rest_time = 5*60

while True:
    # 工作时间计时
    print("Work time started.")
    for i in range(work_time, 0, -1):
        time.sleep(1)
    # 提醒休息
    winsound.Beep(1000, 1000)
    print("Rest time started.")
    # 休息时间计时
    for i in range(rest_time, 0, -1):
        time.sleep(1)
    # 提醒工作
    winsound.Beep(1000, 1000)
