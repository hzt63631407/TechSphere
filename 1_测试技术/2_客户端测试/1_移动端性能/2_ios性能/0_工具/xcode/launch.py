
# xcode-select --install  是否安装
# xcode-select -p         查看路径
# open .bash_profile
# export PATH="/Applications/Xcode.app/Contents/Developer/usr/bin:$PATH"
# export PATH="/Applications/Xcode.app/Contents/Developer/usr/
# source ~/.bash_profile
# instruments -s devices

# instruments：
# https://testerhome.com/topics/16064

import subprocess

bundle_id = "com.xinanSDK.iphone"
template = "Time Profiler"
output_file = "launch_trace.trace"

command = [
    "xcrun",
    "instruments",
    "-w",
    bundle_id,
    "-t",
    template,
    "-l",
    "10",
    "-d",
    output_file
]

try:
    subprocess.run(command, check=True)
    print("应用启动时间已记录")
except subprocess.CalledProcessError as e:
    print("无法记录应用启动时间:", e)
