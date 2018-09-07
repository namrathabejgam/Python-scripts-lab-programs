my_dict={1:'a',2:'b',3:'c'}
m_d={3:'d'}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict.get(1))
my_dict.update(m_d)
print(my_dict)
print(my_dict.setdefault(4,'e'))
my_dict.pop(4)
print(my_dict)
my_dict.popitem()
print(my_dict)
keys = {'a', 'e', 'i', 'o', 'u' }
value = 'vowel'
vowels = dict.fromkeys(keys, value)
print(vowels)
print(my_dict.copy())
my_dict.clear()
print(my_dict)
