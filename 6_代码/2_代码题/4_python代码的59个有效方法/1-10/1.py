# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 第一条 确认python的版本
# 1.确认自己的python版本
# python 查看自己的python版本

# 2.which python查看python的解释器  which behave查看解释器位置
# 在环境变量添加 export PATH="/Users/huangzetao/.pyenv/versions/3.6.5/bin:${PATH}"     #安装python3.6.5时选择的路径
# 增加路径下的解释器 可以使这个路径下所有解释器都生效 且优先级高于/usr/local/bin
# 因为有python和python3 所以都执行的是3.6.5的版本
# https://www.zhihu.com/question/30941329

# 3.如果看到的/usr/local/bin/behave 解释器在这里
# 可以修改文件 如behave：#!/Users/huangzetao/.pyenv/versions/3.6.5/bin/python   python不可修改？通过设置路径

# 4.设置python路径 添加.bash_profile
# alias python="/Users/huangzetao/.pyenv/versions/3.6.5/bin/python”  只是在控制执行python时执行的时3.6.5的版本 没有真正改变python系统版本
# 使用shell脚本时其他版本


# 5.解释器的位置有 /usr/bin/   /usr/local/bin/
# export PATH="/Users/huangzetao/.pyenv/versions/3.6.5/bin:${PATH}"


