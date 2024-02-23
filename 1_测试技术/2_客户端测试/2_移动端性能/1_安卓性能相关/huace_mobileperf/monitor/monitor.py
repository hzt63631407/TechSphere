import time
import adb, collect_memory, collect_cpu
# 测试持续时间 分钟
duration = 1
end_time = time.time() + duration * 60
print("当前时间：{0} , 预计结束时间： {1}".format(time.time(), end_time))
# 收集持续间隔 秒
t = 5
# 开始循环采集数据

start_activity = adb.get_current_activity()
package = adb.get_package()

while time.time() < end_time:
    try:
        collect_memory.collect(package)
        collect_cpu.collect(package)
    except:
        break
    time.sleep(t)

collect_memory.statistics()
collect_cpu.statistics()