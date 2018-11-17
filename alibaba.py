# -*- coding: utf-8 -*-
import re
raw_dict = input().split(';')
usercommand = input()

info_dict = {}
for info in raw_dict:
    if not info:
        continue
    info = info.split('_')
    kind = info[0]
    names = info[1]
    for name in names.split('|'):
        if name in info_dict.keys():
            info_dict[name].append(kind)
        else:
            info_dict[name] = [kind]

keys = [i for i in info_dict.keys()]
keys.sort(reverse=True)
isKey = []
for key in keys:
    index = usercommand.find(key)
    if index == -1:
        continue
    usercommand = list(usercommand)
    usercommand[index:index+len(key)] = str(index)*len(key)
    usercommand = ''.join(usercommand)
    temp = info_dict[key]
    temp.sort()
    isKey.append((key+'/'+','.join(temp),index))

res = re.split('\d+',usercommand)
isKey.sort(key=lambda x:x[1])
len1 = len(isKey)
len2 = len(res)
minlen = min(len1,len2)
result = []
for i in range(minlen):
    result.append(res[i])
    result.append(isKey[i][0])
if len2 > minlen:
    result.extend(res[minlen:])

if len1 > minlen:
    for i in isKey[minlen:]:
        result.append(i[0])
print(isKey)
print(usercommand)
print(res)
print(result)
print(' '.join(result).strip())

