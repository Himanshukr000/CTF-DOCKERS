key1 = '885189600'
flag = 'RITSEC{woman_where_is_my_super_suit}'

res = ''

for i in range(0,len(flag)):
	res += '\\\\' + str(hex(ord(flag[i])^ord(key1[i%len(key1)])))[1:]
print res
