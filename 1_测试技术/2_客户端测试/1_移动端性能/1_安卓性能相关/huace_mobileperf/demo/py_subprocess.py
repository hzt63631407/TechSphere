# 演示python执行 adb
import subprocess

results=subprocess.getstatusoutput('adb devices')

print(results[1].split("\n")[-2])