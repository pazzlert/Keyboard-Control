Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> cars = ['toyota','honda','benz']
>>> cars.append('byd')
>>> print(cars)
['toyota', 'honda', 'benz', 'byd']
>>> cars.remove('honda')
>>> print(cars)
['toyota', 'benz', 'byd']
>>> cars.insert(0,'tesla')
>>> print(cars)
['tesla', 'toyota', 'benz', 'byd']
>>> print(cars[0])
tesla
>>> print(cars[1])
toyota
>>> print(cars[0,1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(cars[0,1,2,3,4])
TypeError: list indices must be integers or slices, not tuple
>>> 
>>> for c in cars:
...     print(c)
... 
...     
tesla
toyota
benz
byd
>>> print(*cars)
tesla toyota benz byd
>>> for i,c in enumerate(cars):
...     print(i,c)
... 
...     
0 tesla
1 toyota
2 benz
3 byd
>>> for i,c in enumerate(cars, start=0):
...     print('ลำดับที่ {} {}'.format(i,c))
... 
...     
ลำดับที่ 0 tesla
ลำดับที่ 1 toyota
ลำดับที่ 2 benz
ลำดับที่ 3 byd
>>> for i,c in enumerate(cars, start=1):
...     print('ลำดับที่ {} {}'.format(i,c))
... 
...     
ลำดับที่ 1 tesla
ลำดับที่ 2 toyota
ลำดับที่ 3 benz
ลำดับที่ 4 byd
>>> enumerate คือฟังก์ชั่นที่เราจะได้เลขขึ้นมา
SyntaxError: invalid syntax
>>> ้hello(5)
SyntaxError: invalid character '้' (U+0E49)
