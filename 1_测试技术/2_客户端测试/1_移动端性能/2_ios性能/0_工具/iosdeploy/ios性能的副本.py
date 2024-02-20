import subprocess
import re
import time

# 使用subprocess库来运行ios-deploy命令并获取输出
def run_command(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode("utf-8")

# 获取连接的iOS设备列表
device_list = run_command("ios-deploy -c").strip().splitlines()

if not device_list:
    print("未检测到iOS设备连接")
    exit()

# 选择一个设备，并获取设备的UDID
device_udid = re.search(r"\[(.*?)\]", device_list[0]).group(1)

# 使用instruments命令来获取CPU使用情况、内存使用情况和FPS数据
command = f"instruments -w {device_udid} -t 'Activity Monitor' -l 10 -s instruments_script"
subprocess.Popen(command.split())

# 等待一段时间以获取一些CPU使用情况、内存使用情况和FPS数据
time.sleep(15)

# 从自定义脚本中提取CPU使用情况、内存使用情况和FPS数据
with open("instruments_script") as f:
    data = f.read()

cpu_data = re.findall(r"CPU usage: (\d+\.\d+)%", data)
memory_data = re.findall(r"Memory usage: (\d+\.\d+) MB", data)
fps_data = re.findall(r"FPS: (\d+\.\d+)", data)

# 打印结果
print("CPU usage:", cpu_data)
print("Memory usage:", memory_data)
print("FPS:", fps_data)
