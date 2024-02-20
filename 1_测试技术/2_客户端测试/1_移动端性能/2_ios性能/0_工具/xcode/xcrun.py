import subprocess
import plistlib

# 启动xctrace record命令并记录跟踪数据
record_command = 'xcrun xctrace record --device <device_UDID> --template "System Trace" --output trace_output.trace'
subprocess.run(record_command, shell=True)

# 停止记录跟踪数据
stop_command = 'killall xcrun'
subprocess.run(stop_command, shell=True)

# 分析跟踪数据并导出为plist文件
export_command = 'xcrun xctrace export --input trace_output.trace --output launch_time.plist'
subprocess.run(export_command, shell=True)

# 读取launch_time.plist文件
with open('launch_time.plist', 'rb') as f:
    plist_data = plistlib.load(f)

# 提取应用启动时间
launch_events = plist_data['traceEvents']
launch_time_event = next((event for event in launch_events if event.get('name') == 'launchApplication'), None)
launch_time = launch_time_event['time']

# 打印应用启动时间
print('应用启动时间：', launch_time)
