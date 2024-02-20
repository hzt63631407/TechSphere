# -*- coding: utf-8 -*-
import subprocess, pyecharts, adb, utils

# 报表数据
x_data = []
y_data = []


def collect(package):
    """
    收集CPU信息
    :return:
    """
    x_data.append(utils.utils.date_time())
    cmd1 = 'adb shell dumpsys cpuinfo | findstr ' + package
    print(cmd1)
    cpu = utils.adb.parse_cpu_info(subprocess.getstatusoutput(cmd1))
    y_data.append(float(cpu))
    print('CPU信息：', y_data)


def statistics():
    """
    统计分析结果
    :return:
    """
    # 3.生成图形报表
    pyecharts.charts.Line().add_xaxis(x_data).add_yaxis('CPU占用', y_data) \
        .set_series_opts(
            areastyle_opts=pyecharts.options.AreaStyleOpts(opacity=0.5),
            label_opts=pyecharts.options.LabelOpts(is_show=False),
        )\
        .set_global_opts(
            xaxis_opts=pyecharts.options.AxisOpts(name="采集时间"),
            yaxis_opts=pyecharts.options.AxisOpts(name="占用(百分比)"),
            title_opts=pyecharts.options.TitleOpts(title="CPU监控")) \
        .render(path=r'../report/CPU监控-{0}.html'.format(utils.date_time()))
