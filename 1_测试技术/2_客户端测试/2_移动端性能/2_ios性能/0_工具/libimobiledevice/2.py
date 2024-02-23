
import subprocess
import re
import time

def measure_app_startup_time(bundle_id):
    # 启动应用程序的调试会话
    subprocess.run(['idevicedebug', 'run', bundle_id])

    # 等待应用程序启动完成
    time.sleep(2)  # 可根据需要调整等待时间

    # 使用idevicedebug获取应用程序的启动时间
    command = 'idevicedebug -u booted log 2>&1 | grep -m 1 "running for"'
    output = subprocess.check_output(command, shell=True).decode('utf-8')

    # 解析输出以获取启动时间
    startup_time = re.search(r'running for ([0-9.]+)', output)
    if startup_time:
        time_seconds = float(startup_time.group(1))
        print(f"应用程序启动时间：{time_seconds:.2f} 秒")
    else:
        print("无法获取应用程序启动时间。")

    # 停止应用程序的调试会话
    subprocess.run(['idevicedebug', 'stop'])

# 调用函数以获取特定iOS应用的启动时间
bundle_id = "com.wuba.bangjob"
measure_app_startup_time(bundle_id)
