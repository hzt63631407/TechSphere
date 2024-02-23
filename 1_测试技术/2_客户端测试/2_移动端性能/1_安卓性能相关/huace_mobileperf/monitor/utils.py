import time


def date_time():
    return time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())