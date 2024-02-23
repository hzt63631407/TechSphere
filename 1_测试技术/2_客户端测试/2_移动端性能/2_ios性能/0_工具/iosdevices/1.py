
# from py_ios_device import py_ios_device as ios_device

from ios_device import py_ios_device


# 获取设备的udid
udid = ios_device.get_device_list()[0]['udid']

# 启动应用
ios_device.start_app(udid, 'com.apple.mobilesafari')

# 监控应用的状态
def callback(res):
    # 如果应用已经启动，打印启动时间
    if res['status'] == 'running':
        print(f'App launch time: {res["launch_time"]} ms')
    # 如果应用已经退出，停止监控
    elif res['status'] == 'exited':
        ios_device.stop_monitor_app(udid)

# 开始监控应用
ios_device.monitor_app(udid, callback)
