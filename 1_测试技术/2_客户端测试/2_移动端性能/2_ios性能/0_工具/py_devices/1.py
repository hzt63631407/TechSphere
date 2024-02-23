
# https://pypi.org/project/py-ios-device/

import time
import subprocess

def get_output(cmd):
    code, data = subprocess.getstatusoutput(cmd)
    return data

data = get_output("pyidevice instruments app_lifecycle  -b com.inhouse58.iphone")


# for i in range(5):
#
#     data = get_output("pyidevice instruments app_lifecycle  -b com.inhouse58.iphone")
#
#     print(data)
#
#     time.sleep(3)
#
#     get_output("tidevice kill com.wuba.bangjob")