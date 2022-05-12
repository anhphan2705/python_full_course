import time

# epoch = a date and time from which a computer measures system time

# time.ctime(seconds_past_epoch) = Convert a time expressed in seconds since epoch to a readable string
print(time.ctime(0))

#time.time() = return current seconds since epoch
print(time.time())

# time.ctime(time.time()) = the current time
print(time.ctime(time.time()))

# time.localtime() = object containing the current local time
time_object = time.localtime()

# UTC or Coordinated Universal Time is the primary time standard by which the word regulates clocs and time. It is within about 1 second of mean solar time at 0 degree longtitude, and is not adjusted fr daylight saving time.
time_object_utc = time.gmtime()

# strftime(format, t) = a function that is used for formating a time object into string
# Different type of format = https://docs.python.org/3/library/time.html#time.strftime
local_time = time.strftime("%B %d %Y %H:%M:%S ", time_object)
print(local_time)

# strptime(string, format) = convert a string into a readable time object
time_string = "20 April, 2020"
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)

# time.asctime(t) = accept a tuple representative of time
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

#time.mktime(t) = accept a tuple representation of time or a time object and return the seconds from epic till time
time_string = time.mktime(time_tuple)
print(time_string)

#time.perf_counter() = return how long it takes for thread(s) to finish the task