import subprocess

# 执行命令并返回输出
def run_command(cmd):
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = proc.communicate()
    return output.decode('utf-8').strip()

# 获取设备的 UDID
def get_device_udid():
    cmd = ['idevice_id', '-l']
    output = run_command(cmd)
    return output

# 获取应用的 PID
def get_app_pid(bundle_id):
    udid = get_device_udid()
    cmd = ['/opt/homebrew/bin/idevicedebug', '--udid', udid, 'run', bundle_id]
    print(cmd)
    output = run_command(cmd)
    pid = None
    if output.startswith("DEBUG: "):
        pid = output.split("DEBUG: ")[1]
    return pid

# 获取应用的 CPU 使用率
def get_cpu_usage(pid):
    cmd = ['/opt/homebrew/bin/idevicedebug', '--udid', udid, 'run', bundle_id]
    output = run_command(cmd)
    cpu_usage = None
    lines = output.strip().split('\n')
    for line in lines:
        if line.startswith(str(pid)):
            cpu_usage = line.split()[1]
            break
    return cpu_usage

# 获取应用的内存使用量
def get_memory_usage(bundle_id):
    udid = get_device_udid()
    cmd = ['idevicedebug', '--udid', udid, 'shell', 'ps', '-ax', '|', 'grep', bundle_id]
    output = run_command(cmd)
    memory_usage = None
    lines = output.strip().split('\n')
    for line in lines:
        if bundle_id in line:
            memory_usage = line.split()[5]
            break
    return memory_usage

# 示例用法
bundle_id = "com.wuba.bangjob"

pid = get_app_pid(bundle_id)
if pid:
    cpu_usage = get_cpu_usage(pid)
    memory_usage = get_memory_usage(bundle_id)
    print("应用的 CPU 使用率: {}%".format(cpu_usage))
    print("应用的内存使用量: {} KB".format(memory_usage))
else:
    print("应用未安装或未找到")
