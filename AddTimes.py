from datetime import time
#function for adding two time objects
def add(time1, time2):
    h = time1.hour + time2.hour
    m = time1.minute + time2.minute
    total_m = (h * 60) + m
    hours = total_m // 60
    minutes = total_m % 60
    total_time = time((hours), (minutes))
    return total_time