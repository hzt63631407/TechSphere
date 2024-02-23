import pyecharts.options as opts
from pyecharts.charts import Line

x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]

c = (
    Line()
    .add_xaxis(x_data)
    .add_yaxis('启动时间',y_axis=y_data, is_step=True)
    .set_global_opts(title_opts=opts.TitleOpts(title="启动统计数据"))
    .render("line_base.html")
)