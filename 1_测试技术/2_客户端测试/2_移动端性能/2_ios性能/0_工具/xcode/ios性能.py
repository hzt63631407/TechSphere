import subprocess
import re

# 获取iOS设备的CPU和内存使用情况
def get_device_perf(device_id):
    cpu_usage = None
    mem_usage = None

    # 使用xcrun命令行工具获取CPU和内存使用情况
    cmd = 'xcrun instruments -w {0} -t "Activity Monitor" -l 1 -v off -e ui false'.format(device_id)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = p.communicate()

    # 解析输出结果获取CPU和内存使用情况
    if not error:
        # 获取CPU使用情况
        cpu_pattern = re.compile('CPU usage: (\d+.\d+)%')
        cpu_match = cpu_pattern.search(output.decode())
        if cpu_match:
            cpu_usage = cpu_match.group(1)

        # 获取内存使用情况
        mem_pattern = re.compile('Physical memory: (\d+)MB \((\d+)MB wired, (\d+)MB active, (\d+)MB inactive, (\d+)MB free\)')
        mem_match = mem_pattern.search(output.decode())
        if mem_match:
            mem_usage = mem_match.group(1)

    return cpu_usage, mem_usage

# 获取设备列表
def get_device_list():
    device_list = []

    # 使用xcrun命令行工具获取设备列表
    cmd = 'xcrun instruments -s devices'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = p.communicate()

    # 解析输出结果获取设备列表
    if not error:
        device_pattern = re.compile('(.+) \((.+)\) \[(.+)\]')
        devices = device_pattern.findall(output.decode())
        for device in devices:
            device_id = device[2]
            if device_id.startswith('iphone') or device_id.startswith('ipad'):
                device_list.append(device_id)

    return device_list

if __name__ == '__main__':
    device_list = get_device_list()
    for device_id in device_list:
        cpu_usage, mem_usage = get_device_perf(device_id)
        print('{0}: CPU usage = {1}%, Memory usage = {2}MB'.format(device_id, cpu_usage, mem_usage))
