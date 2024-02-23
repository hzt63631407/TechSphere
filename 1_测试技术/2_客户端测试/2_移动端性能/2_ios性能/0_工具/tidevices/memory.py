

import time
import tidevice
from tidevice._perf import DataType


run_device = tidevice.Device()
perf = tidevice.Performance(run_device, [DataType.CPU, DataType.MEMORY, DataType.FPS])


def callback(_type: tidevice.DataType, value: dict):
    #可在此处存储性能数据
    print("R:", _type.value, value)

#传入APP Bundle ID
perf.start("com.wuba.bangjob", callback=callback)
# perf.start("com.xinanSDK.iphone", callback=callback)
time.sleep(10)
perf.stop()

