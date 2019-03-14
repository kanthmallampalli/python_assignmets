'''
a string is list of char,index of string starts from 0
 individuval characters from string can be retrived by using slicing function with the help of index
strings are immutable

isallnum() finds any special char
isalpha () finds contains only alpha or not
is digits() finds string contains oly digits or not
is lower() finds lowers case
is upper () finds upper case
is space() string contains only white space
loweer() string to lower case
upper () string to upper case
lstrip() remover spaces from left side
r strip() removers spaces from right side
strip() remover space from all sides
endswith ()
starts with()

'''

s='uday'

print(s[1:3])


t ="%%*T$"
y= t.isalpha()
print(y)


u="589"
x=u.isdigit()
print(x)
z="6987"
i=z.isnumeric()
print(i)


print(s.endswith('t'))


print(s.startswith('u'))

s="7676IIHg"

print(s.isalnum())

