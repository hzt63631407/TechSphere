import subprocess
import time


def get_current_activity():
    """
    获取当前 activity
    :return:
    """
    activitys = subprocess.getstatusoutput('adb shell dumpsys activity top | findstr ACTIVITY')[1].split("\n")
    start_activity = activitys[len(activitys) - 1].split()[1]
    return start_activity


def get_package():
    """
    获取当前 package
    :return:
    """
    start_activity = get_current_activity()
    package = start_activity.split("/")[0]
    return package


def stop_app(package, start_activity):
    """
    退出指定应用
    :param package:  当前package
    :param start_activity:  当前activity
    :return:
    """
    while True:
        subprocess.getstatusoutput('adb shell am force-stop ' + package)
        cur_activity = get_package()
        if cur_activity != start_activity:
            break
        time.sleep(1)

def parse_start_time(cmd_result):
    """
    解析重启命令返回的内容
    :return:
    """
    return cmd_result[1].split("\n")[0].split(':')[1]


def parse_memory_info(cmd_result):
    """
    解析 内存信息命令 返回的内容
    :return:
    """
    return cmd_result[1].split("\n")[0].split('K')[0].strip().replace(",", "")


def parse_cpu_info(cmd_result):
    """
    解析 CPU信息命令 返回的内容
    :return:
    """
    return cmd_result[1].split("\n")[0].strip().split(' ')[0].strip().replace("%", "")