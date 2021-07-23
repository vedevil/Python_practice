import array as arr
a=arr.array('i',[6,7,9,8])
print(a)
print(a.buffer_info())
print(a.typecode)
a.reverse()
print(a)
