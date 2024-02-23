
from ios_device import IOSDevice, USBMUXResponder
from time import time


with USBMUXResponder() as usbmux:
    with IOSDevice(usbmux) as ios_device:
        # 连接到设备
        ios_device.connect()

bundle_id = 'com.example.app'  # 替换为您要测试的应用的 Bundle ID

start_time = time()  # 记录开始时间
ios_device.launch_application(bundle_id)  # 启动应用
end_time = time()  # 记录结束时间

launch_time = end_time - start_time
print("应用启动时间: {:.2f} 秒".format(launch_time))