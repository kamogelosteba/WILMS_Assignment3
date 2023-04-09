#kamogleo steba
#218686206
#Assignment 2

s='fullstackslp'

print(s[0])
print(s[-1])
print(s[4:9])
print(s[9:])
print(s[7:10])

numb=int(len(s))

#writing a string in reverse
name=''
while  numb > 0:
     
    numb=numb-1
    name=name + s[int(numb)]

print(name)

#using indexing and keys 
d1={'simple_key':'Hello'}

#using keys
print(d1['simple_key'])

d2={'k1':{'k2':'Hello'}}
print(d2['k1']['k2'])

d3={'k1':[{'nest_key':['This is deep',['Hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

#sets question

mylist=[1,1,1,1,1,2,2,2,2,3,3,3,3]
new_list=set(mylist)

print(new_list)


#formatting part

age =45
name = "Kyle"
print("Hello my dog's name is {}and he looks {}".format(name,age))