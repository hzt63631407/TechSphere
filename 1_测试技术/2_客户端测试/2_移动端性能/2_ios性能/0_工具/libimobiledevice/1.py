
import subprocess
import re

# brew install libimobiledevice
# brew install ios-deploy
# b343809365c830b3d0aed519389b1cf32c4671c4
# bundle_id = "com.wuba.bangjob"



cmd = ['idevicedebug', '--udid', 30a1e9e6b6b5d867729ef4a8a3c5d4458e25937e, 'run', "com.wuba.bangjob"]


def get_app_performance_data(bundle_id):
    # 使用ideviceinfo获取应用程序的进程ID
    command = 'ideviceinfo -k UniqueDeviceID'
    output = subprocess.check_output(command, shell=True).decode('utf-8')
    device_udid = output.strip()

    # 使用idevicesyslog过滤应用程序的日志
    command = f'idevicesyslog -u {device_udid} | grep "{bundle_id}"'
    print(command)
    syslog_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    print(syslog_process)

    # 从日志中解析性能数据
    cpu_usage = None
    memory_usage = None
    for line in iter(syslog_process.stdout.readline, b''):
        line = line.decode('utf-8').strip()
        if 'CPU usage:' in line:
            cpu_usage = re.search(r'CPU usage:\s+(\d+\.\d+)\s%', line)
        elif 'Memory usage:' in line:
            memory_usage = re.search(r'Memory usage:\s+(\d+)\sbytes', line)

        if cpu_usage and memory_usage:
            break
    print(cpu_usage,memory_usage)
    # 打印性能数据
    if cpu_usage:
        cpu_percent = float(cpu_usage.group(1))
        print(f"CPU使用率：{cpu_percent}%")
    else:
        print("无法获取CPU使用率。")

    if memory_usage:
        memory_bytes = int(memory_usage.group(1))
        memory_mb = memory_bytes / (1024 * 1024)
        print(f"内存使用：{memory_mb:.2f} MB")
    else:
        print("无法获取内存使用信息。")

# 调用函数以获取特定iOS应用的性能数据
bundle_id = "com.wuba.bangjob"
get_app_performance_data(bundle_id)
