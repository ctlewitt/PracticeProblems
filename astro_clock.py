# given a list of 3 numbers (seconds/minute, minutes/hour, hours/day)
# and 2 strings representing times (in HH:MM:SS format)
# calculate the number of seconds between the two times
# assume that the second time is after the first and always within 1 day
# e.g., [20,60,24], "01:05:15", "01:06:05" => 10


# 1:1:1
# 0:1:1
# =>
#
# 1:1:1
# 2:2:2
# => 1:1:1

HRS = 0
MINS = 1
SECS = 2

def astro_clock_diff(units_of_time, time1_str, time2_str):
    #format time and get conversion units in correct order
    time1 = [int(time_unit) for time_unit in time1_str.split(":")]
    time2 = [int(time_unit) for time_unit in time2_str.split(":")]
    units_of_time_correct_order = list(reversed(units_of_time))
    #convert times to seconds
    seconds_in_time1 = convert_to_seconds(units_of_time_correct_order, time1)
    seconds_in_time2 = convert_to_seconds(units_of_time_correct_order, time2)
    #get difference
    diff_secs = seconds_in_time2 - seconds_in_time1
    #return difference (if it's negative, it's tomorrow's time, so add a day)
    print(diff_secs)
    return diff_secs if diff_secs >= 0 else diff_secs + secs_per_day(units_of_time_correct_order)


def convert_to_seconds(units_of_time, time):
    return time[HRS] * secs_per_hr(units_of_time) + time[MINS] * secs_per_min(units_of_time) + time[SECS]

def secs_per_day(units_of_time):
    return units_of_time[HRS] * units_of_time[MINS] * units_of_time[SECS]

def secs_per_hr(units_of_time):
    return units_of_time[MINS] * units_of_time[SECS]

def secs_per_min(units_of_time):
    return units_of_time[SECS]




print(astro_clock_diff([20,60,24], "00:05:15", "00:05:14"))