
# https://github.com/YueChen-C/py-ios-device/blob/main/doc/%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3.md
# https://github.com/YueChen-C/py-ios-device

from ios_device.py_ios_device import PyiOSDevice

from time import time

device = PyiOSDevice()

# if device.get_device() == True:
#     print(1)
# else:
#     print("请确认设备是否连接")

start_time = time()  # 记录开始时间

device.launch_app("com.wuba.bangjob")
# device.launch_app("com.xinanSDK.iphone")

end_time = time()  # 记录结束时间

launch_time = end_time - start_time

print("应用启动时间: {:.2f} 秒".format(launch_time))

# device.stop()





