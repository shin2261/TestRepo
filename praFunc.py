# def hello_func():
#     print('Hello Function!')

# print(hello_func)
# hello_func()

# def hello_func():
#     return 'Hello Function!'
# print(hello_func())
# print(hello_func().upper()) # 把它當成return 的型別對待就好 return 是str 後面可以直接調用str的Func

# def hello_func(greeting, name = 'You'):
#     return '{}, {}  Function.'.format(greeting, name)
# print(hello_func('Hi'))
# print(hello_func('Hi', 'Hsin'))

# def student_info(*args, **kwargs):
#      print(args)
#      print(kwargs)
# student_info('Math', 'Art', name='John', age=22)
# course = ['Math', 'Art']
# info = {'name':'John', 'age': 22}
# student_info(course, info)
# student_info(*course, **info)
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years. """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""
    # Year 2017
    # month 2
    if not 1 <= month <= 12:
        return "Invalid Month"
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]


print(is_leap(2017))
print(days_in_month(2017, 2))
