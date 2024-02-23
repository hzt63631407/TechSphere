
# -*- coding:utf-8 -*-
import subprocess
import time


def get_output(cmd):
    code, data = subprocess.getstatusoutput(cmd)
    return data

start_time = time.time()

get_output("tidevice launch  com.wuba.bangjob")
# get_output("tidevice launch  com.xinanSDK.iphone")


end_time = time.time()

launch_time = end_time - start_time

print("应用启动时间：", launch_time)


# for i in range(10):
#     get_output("tidevice launch  com.wuba.bangjob")
#
#     time.sleep(10)
#
#     get_output("tidevice kill com.wuba.bangjob ")


# 记录启动时间

# 执行操作，例如点击按钮或者进行一些应用内的操作
# ...

# 计算启动时间


# 打印启动时间
