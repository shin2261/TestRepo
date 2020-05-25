# import my_module as mm

# courses = ['History', 'Math', 'Physics', 'CompSci']

# index = mm.find_index(courses, 'Math')
# print(index)

# ====================================================

# import sys
# # sys.path.append('/Users/shin/Destop....')#加入別的資料夾裡面的專案

# from my_module import find_index as fi, test
# courses = ['History', 'Math', 'Physics', 'CompSci']

# index = fi(courses, 'Math')
# # print(index)
# # print(test)
# # print(sys.path)查看你的path中有哪些引用

# #或者加在bash裡面
# #在terminal中 >nano ~/.bash_profile
# #        加入 >export PYTHONPATH="/Users/shin/Destop...."你的專案名

# ====================================================

import random
import math
import datetime
import calendar
import os

courses = ["History", "Math", "Physics", "CompSci"]
random_courses = random.choice(courses)
print(random_courses)
rads = math.radians(90)
print(rads)
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))
print(os.getcwd())
