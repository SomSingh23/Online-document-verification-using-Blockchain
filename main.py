import hashlib
name = input("what is you name  : ")
age = input("what is you age    : ")
_ = name+age
print(_)
_ = _.encode()
print(_)
with open('test.pdf','rb') as obj:
    data = obj.read()
    data+=_
    print(data)
# print(data)
hash_value = hashlib.sha256(data).hexdigest()
print(hash_value)

with open('main.txt','a') as obj:
    obj.write(f"test.pdf unique hash =  {hash_value}")
    obj.write('\n')

