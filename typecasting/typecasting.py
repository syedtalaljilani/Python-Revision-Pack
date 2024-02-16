# Type casting
data = '200'
# data = data+10 can only concatenate str (not "int") to str
print(data)
data = int(data)+10 # 200 string convert into int 200+10 = 210

print(data) # 210
string= 'True'
print(type(string)) #str
string=bool(string)
print(type(string))# bool