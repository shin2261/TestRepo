# LIST
courses = ['History','Math', 'Physics', 'CompSci']
courses_2 = ['Art','Education']
# num
# print(courses)
# print(courses[3])
# print(courses[-1])
# print(courses[0:2])
# print(courses[:2])
# print(courses[2:])

#inset append pop remove reverse 
#courses.append('Art')
#print(courses)
#courses.insert(0, 'Art')

# courses.insert(0,courses_2)
# print(courses)
# print(courses[0])

# courses.extend(courses_2)
# print(courses)

# courses.remove('Math')
# print(courses)

# popped = courses.pop()
# print(popped)
# print(courses)  

# courses.reverse()
# print(courses)

# sort 
# nums = [1,5,2,4,3]
# courses.sort()
# nums.sort()
# print(nums)
# print(courses)
# courses.sort(reverse = True)
# nums.sort(reverse = True)
# print(nums)
# print(courses)
# sorted_course = sorted(courses)
# print(sorted_course)
# print(min(nums))
# print(max(nums))
# print(sum(nums)) 
# print(courses.index('CompSci'))
# print('Art' in courses)
# print('CompSci ' in courses)

# for loop
# for item in courses:
#     print(item)
# for index, courses in enumerate(courses, start=1):
#     print(index, courses)

#join split
# courses_str = '-'.join(courses)
# print(courses_str)
# new_list = courses_str.split('-')
# print(new_list)


#Tuple
    #Mutable
# list_1 = ['History','Math', 'Physics', 'CompSci']
# list_2 = list_1
# print(list_1)
# print(list_2)
# list_1[0] = 'Art'
# print(list_1)
# print(list_2)
    #Immutable
# tuple_1 = ('History','Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1
# print(tuple_1)
# print(tuple_2)
# tuple_1[0] = 'Art'(tuple 不能改變)
# print(tuple_1)
# print(tuple_2)

#Set
# cs_courese ={'History', 'Math', 'Physics', 'CompSci','Math'}
# print(cs_courese)
# print('Math' in cs_courese)
# art_courese ={'History', 'Math', 'Art', 'Design'}
# print(cs_courese.intersection(art_courese))
# print(cs_courese.difference(art_courese))
# print(cs_courese.union(art_courese))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_Tuple = ()
empty_Tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()

