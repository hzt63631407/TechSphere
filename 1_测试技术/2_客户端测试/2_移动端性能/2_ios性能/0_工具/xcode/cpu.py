
import subprocess

# 性能用instruments

def run_instruments(bundle_id):
    # 构建 Instruments 命令
    cmd = [
        'instruments',
        '-t', 'Activity Monitor',
        '-w', 'DEVICE_UDID',  # 将 DEVICE_UDID 替换为实际的设备 UDID
        '-l', '300',  # 运行时长，单位为秒
        bundle_id
    ]

    # 执行 Instruments 命令，并捕获输出
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = proc.communicate()

    # 打印输出到控制台
    print(output.decode('utf-8'))


# 示例使用
bundle_id = "com.wuba.bangjob"
run_instruments(bundle_id)

