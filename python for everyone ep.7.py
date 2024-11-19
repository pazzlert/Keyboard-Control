Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = 'Somsak'
>>> age = 12
>>> age == 12
True
>>> age == 15
False
>>> if age == 12:
...     print('สามารถเรียนห้องป.6')
... 
...     
สามารถเรียนห้องป.6
>>> if age != 12:
...     print('ต้องไปเรียนห้องอื่น')
... 
...     
>>> age != 12
False
>>> age = 15
>>> if age != 12:
...     print('ต้องไปเรียนห้องอื่น')
... 
...     
ต้องไปเรียนห้องอื่น
>>> age = 18
>>> if age > 12:
...     print('คุณต้องไปถามครูว่าเรียนชั้นไหนได้บ้าง')
... 
...     
คุณต้องไปถามครูว่าเรียนชั้นไหนได้บ้าง
>>> if age > 12:
...     if age != 12:
...     print('ต้องไปเรียนห้องอื่น')
...     
SyntaxError: expected an indented block after 'if' statement on line 2
>>> if age >=12
SyntaxError: expected ':'
>>> if age > 12:
...     print('ห้องนี้รับอายุ 12 ขวบขึ้นไป คุณเข้าได้')
... 
...     
ห้องนี้รับอายุ 12 ขวบขึ้นไป คุณเข้าได้
>>> age = 7
>>> if age < 12:
...     print('ต้องเรียนป.4 ลงไปเท่านั้น')
... 
...     
ต้องเรียนป.4 ลงไปเท่านั้น
>>> age =12
>>> if age <= 12:
...     print('อายุ 12 ลงไปสามารถขึ้นรถไฟฟ้าฟรี')
... 
...     
อายุ 12 ลงไปสามารถขึ้นรถไฟฟ้าฟรี
>>> garage = ['toyota','isuzu','benz']
>>> car ='toyota''
SyntaxError: unterminated string literal (detected at line 1)
>>> car = 'toyota'
>>> 
>>> 
>>> car in garage
True
>>> car = 'honda'
>>> car in garage
False
