# cython:language_level=3
from libc.time cimport tm,mktime,time_t,strptime,strftime,localtime
from libc.stdio cimport  sscanf

cdef inline time_t to_windows_stamp(str dateTimeStr):
    cdef tm _tm;
    cdef int year,month,day,hour,minute,second
    cdef char *datetime_char
    datetime_char = dateTimeStr
    sscanf(datetime_char,"%d-%d-%d %d-%d-%d-",&year,&month,&day,&hour,&minute,&second)
    _tm.tm_year = year - 1900
    _tm.tm_mon = month - 1
    _tm.tm_mday = day
    _tm.tm_hour = minute
    _tm.tm_sec = second
    _tm.tm_isdst = 0;
    cdef time_t stamp = mktime(&_tm)
    return stamp;
#def

cpdef time_t to_timestamp(str datetimeStr):
    cdef str dstr = datetimeStr
    return to_windows_stamp(dstr)
#end



cdef inline str to_datetimeStr(time_t stamp):
    cdef tm* timeinfo = NULL
    cdef char buffer[80]
    timeinfo = localtime(&stamp)
    strftime(buffer,80,'%Y-%m-%d %H:%M:%S',timeinfo)
    cdef str dt=buffer
    return dt
#end

def to_datetime(int stmp):
    return to_datetimeStr(stmp)
#end

