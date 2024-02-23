

# https://github.com/alibaba/taobao-iphone-device

import time
import subprocess

def get_output(cmd):
    code, data = subprocess.getstatusoutput(cmd)
    return data


for i in range(5):

    start_time = time.time()   # 记录开始时间

    get_output("tidevice launch com.wuba.bangjob")

    end_time = time.time()     # 记录结束时间

    launch_time = end_time - start_time

    print("应用启动时间: {:.2f} 秒".format(launch_time))

    time.sleep(1)

    get_output("tidevice kill com.wuba.bangjob")