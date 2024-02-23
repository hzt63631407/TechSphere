
# -*- coding:utf-8 -*-
import subprocess
import logging

def get_output(cmd):
    code, data = subprocess.getstatusoutput(cmd)
    # if code != 0:
    #     logger.error(f"Invalid cmd, errmsg: {data}")
    return data

# data = get_output("tidevice install /Users/a58/Downloads/basicpck-373419-ISDDeviceManagerKit_Example_v2.0.1.2.2_Debug.ipa")
data = get_output("tidevice install /Users/a58/Downloads/basicpck-373817-Inhouse-WBDEBUG-04-26_17.18\(12.12.0\).ipa")


print(data)