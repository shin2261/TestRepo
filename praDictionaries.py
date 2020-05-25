student = {'name': 'John', 'age': 25, 'coures': ['Math','CompSci']}

print(student)
print(student['coures'])
print(student.get('name'))
print(student.get('phone', 'Not Found'))

student['phone'] = '555-555'
student['name'] = 'Jane'
print(student)

student.update({'name': 'Mike', 'age': 26, 'phone': '6666-6666'})
print(student)

# del student['age']
# print(student)

age = student.pop('age')
print(student)
print(age)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

for key ,value in student.items():
    print(key, value)