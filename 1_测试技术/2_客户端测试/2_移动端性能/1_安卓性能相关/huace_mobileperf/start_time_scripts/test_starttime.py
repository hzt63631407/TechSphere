# # -*- coding: utf-8 -*-
# import subprocess, pyecharts, adb, utils
#
# # 1. 获取当前应用信息
# start_activity = utils.adb.get_current_activity()
# package = utils.adb.get_package()
#
# # 2. 生成折线图所需的数据
# x_data = []
# y_data = []
#
# # 3. 循环重启10次应用
# for runCount in range(1, 11):
#     x_data.append('第{0}次'.format(runCount))
#     cmd1 = 'adb shell am start -S -W ' + start_activity + ' | findstr TotalTime'
#     print(cmd1)
#     start_time = utils.adb.parse_start_time(subprocess.getstatusoutput(cmd1))
#     print(u'# 冷启动, 第%d次:' % runCount, start_time)
#     y_data.append(int(start_time))
#     utils.adb.stop_app(package, start_activity)
#
# # 4.生成图形报表
# pyecharts.charts.Line().add_xaxis(x_data).add_yaxis('启动时间', y_data)\
#     .set_global_opts(title_opts=pyecharts.options.TitleOpts(title= "启动耗时趋势图_平均时间{0}毫秒".format(sum(y_data) / len(y_data))))\
#     .render(path=r'../report/启动时间性能测试-{0}.html'.format(utils.utils.date_time()))