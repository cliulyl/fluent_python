import sys
sys.path.append('..')
from common_modules.show import *

start_theme('元组作为数据记录：元组拆包（可用于任何可迭代对象）')

start_example('平行赋值')
city_info = ('Nanjing', 2023, 9000)
name, _, _ = city_info
print(f"city name: {name}")
end_example()

start_example('迭代中的平行赋值')
name_and_ages = [('Tom', 15), ('Ming', 16), ('Suse', 14)]
for name, age in name_and_ages:
    print(name)
end_example()

start_example('使用*来把可迭代对象拆开作为函数的参数 & 在print的%里使用单个元组对应格式字符串的空档')
t = (20, 7)
ret = divmod(*t)
# 以下两种写法都可以
# print('%r divs %r,' % t, 'quotient is %r with a remainder %r' % ret)
print('%r divs %r, quotient is %r with a remainder %r' % (*t, *ret))
end_example()

start_example('使用*处理剩下的元素')
a, b, *rest1 = range(5)
print(f'rest1 is {rest1}')
*rest2, a, b = range(6)[1:]
print(f'rest2 is {rest2}')
end_example()

start_example('嵌套元组拆包')
student_info = ('Ming', 19, ('Wang', 'Li'))
name, age, (father, mother) = student_info
print(f'father name is {father}')
end_example()


start_theme('具名元组')
from collections import namedtuple

start_example('构造及各字段显示')
ProgramInfo = namedtuple('ProgrameInfo', 'name language version date')
ProgramLanguage = namedtuple('ProgramLanguage', 'language_name version')
rmtt_code_data = ('rmtt', ProgramLanguage('python', '3.8'), '1.0', '2023-9-1')
rmtt_code_info = ProgramInfo(*rmtt_code_data)
print(f'ProgrameInfo fields: {ProgramInfo._fields}')
end_example()

start_example('友好打印')
for key, value in rmtt_code_info._asdict().items():
    print(key + ':', value)
end_example()

