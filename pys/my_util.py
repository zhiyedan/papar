import time
from datetime import datetime
# 生成 string 时间
time_string = time.ctime()
# 生成 datetime
time_datetime = datetime.now()
time_datetime2 = datetime(2018, 4, 10, 17, 53, 59)
# 生成 timestamp
time_stamp = time.time()

# string to datetime
def str2dt(str_time):
    format_dt = "%Y-%m-%d %H:%M:%S"
    return datetime.strptime(str_time,format_dt)

# string to time
def str2time(str_time):
    format_dt = "%Y-%m-%d %H:%M:%S"
    return time.strptime(str_time,format_dt)

# string to timestamp
def str2ts(str_time):
    format_dt = "%Y-%m-%d %H:%M:%S"
    return time.mktime(time.strptime(str_time,format_dt))

# datetime to string
def dt2str(dt):
    format_dt = "%Y-%m-%d %H:%M:%S"
    return dt.strftime(format_dt)

# datetime to time
def dt2time(dt):
    return dt.timetuple()

# datetime to timestamp
def dt2ts(dt):
    time.mktime(dt.timetuple)

# time to string
def time2str(time_tuple):
    format_dt = "%Y-%m-%d %H:%M:%S"
    return time.strftime(format_dt,time_tuple)

# time to datetime
def time2dt(time_tuple):
    return datetime(*time_tuple[:6])

# time to timestamp
def time2ts(time_tuple):
    return time.mktime(time_tuple)

# timestamp to datetime
def ts2td(ts,local=True):
    if local:
#         本地时区
        return datetime.fromtimestamp(ts)
    else:
#         utc标准时区
        return datetime.utcfromtimestamp(ts)

# timestamp to time
def ts2time(ts):
    return time.localtime(ts)

# timestamp to string
def ts2str(ts):
    import pandas
    return str(pandas.to_datetime(ts,unit='s'))

# 获取30天前的日期
def get_pre_n_day(n_day):
    import datetime as dtime
    return datetime.now() - dtime.timedelta(days=n_day)
