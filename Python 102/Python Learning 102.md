# Dates & Numbers

## abs(absolut):

Example:
```
number = -999
print(abs(number))
```
## round: 
Examples:
```
number = 3.754
print(round(number))
```
**Note**: here in example it will be 4
```
number = 3.754
print(round(number,2))
```
**Note**: but if specify it by 2 it will be 3.75 , and if i put 1 it will be 3.8 ..etc

## pow(power):
```
number = 3.754
print(pow(number,2))
```
## Max,Min,Sum:
```
number = 987,678,543,875,754
print(max(number))
print(min(number))
print(sum(number))
```
## square root: 
```
import math
number = 144
print(math.sqrt(number))
```
**Note**: you have to import math to find sqrt to use it

## remainder : 
```
import math
print(math.remainder(9,3))
```
## generate a random number between 1 -100
```
import random
print(random.randint(1,100))
```
## Create a date
```
import datetime
date = datetime.date(2024,5,5)
print(date)
print(date.year)
print(date.month)
print(date.day)
```
## Create time
```
import datetime
time = datetime.time(12,45,46)
print(time)
print(time.hour)
print(time.minute)
print(time.second)
```
## Create CURRENT time
```
import datetime
current_time = datetime.datetime.today()
print(current_time)
```
## Convert a date to text
```
import datetime
date= datetime.date(2024,5,5)
time = datetime.time(12,43,34)

print(date)
print(time)

print(date.strftime("%a %b %Y"))
print(time.strftime('%I %M %S'))
```
# Advanced Sequence

## Indexing: 
Example:
```
alpabet = 'abcdefghijklmnopqrstuvwxyz'
print(alpabet[13])
**Note** : you can use index by postive number(right) or negative start from (left), in list or tuple
text = "Ahmad"
print(text[-3])
```
## Slicing

### Close range:
```
text = 'this is python 102'
print(text[8:14])
```
**Note** :which specify the range to take the word start before word and on the end letter of word

### Open range:
```
text = 'this is python 102'
print(text[8:]) ####this take from range to the end
print(text[:7]) #### this take from begin to the range
print(text[:])  #### this take whole text
```
**Note**: you can use either postive number(right) or negative(left)

### jump:
```
text = 'this is python 102'
print(text[0:18:2]) ####outcame will be (ti spto 0)
```
**Note**: number 2 in ex represent the jump

## slice function:
```
text = 'this is python 102'
s = slice(8,14)
print(text[s])
```

## index:
```
text = 'this is python 102'
print(text.index('python'))
```
**Note**: index consider a case senstive

## len: 
```
text = 'this is python 102'
print(len(text)) #### to know how many items in the value
```
**Note**: it works with str & int

## Count: 
```
text = 'this is python 102'
the_list= [1,2,2,4,4,5,6,6,6,7,8]
the_tuple = (1,2,3,3,3,4,4,6,7,5)
print(text.count('s'))
print(the_list.count(6))
print(the_tuple.count(3))
```
**Note**: count consider a case senstive

## in: 
```
text = 'this is python 102'
print('python' in text) ####outcame either Ture/False
```
**Note**: if we want to make sure the text not in this varible (Not)
```
text = 'this is python 102'
print('python' not in text) ####outcame either Ture/False
```
**Note**: in consider a case senstive

## Merge and repeat:
### Merge:
```
first_name = 'Khaled'
Last_name = 'alharbi'
print(first_name + ' ' + Last_name)
```
### Repeat:
```
first_name = 'Khaled'
Last_name = 'alharbi'
print(first_name*3 )
```

# Advanced Strings

## Find:
```
text = 'this is python 102'
print(text.find('is')) ####it show the early index
```
**Note**: you can specifiy the find
```
text = 'this is python 102'
print(text.find('is',4,9))
```
## rfind:
```
text = 'this is python 102'
print(text.rfind('is')) #### it show last index  in varible
print(text.rfind('xx')) ####outcame will be -1 that mean does not find it in the varible
```
## split:
```
letters = 'A, B, C'
word = 'this is a python course 102'
split_letters = letters.split()
print(split_letters)
```
**Note**: the splint happend due to the space before the letter b and c
```
letters = 'A, B, C'
split_letters = letters.split(',')
print(split_letters)
```
**Note**: you can split by the characterstic such as "," in example above
```
word = 'this is a python course 102'
split_word = word.split('t',1)
print(split_word) ####oucome will be ['', 'his is a python course 102']
```
**Note**: you can split according to early detction such as in example above

## join:
```
letters = 'A, B, C'
split_letters = letters.split()
list_to_string = '#'.join(split_letters)
print(list_to_string)
```
**Note**: join not only covert the list to string.It also, convert tuple and dictonary

## Text verification:
```
values = 'Khaled102'
number = '01010110101'
print(values.isalnum())
print(number.isdigit())
```
## Replace function:
```
valuess = '1\n2\n3\n4\n5'
print(valuess.replace('\n','-'))
```
## strip function
```
sentence = '      python course 102       '
print(sentence.strip()) ####outcame it remove all the space in text
```
### lstrip : used to remove the spaces in front of text
```
sentence = '      python course 102       '
print(sentence.lstrip())
```
### rstrip : to remove the spaces after the text
```
sentence = '      python course 102       '
print(sentence.rstrip())
```
## Manipulating the text (lower,upper,swapcase,title) functions:
```
str = 'Hello everyone in python course 102'
print(str.lower())
print(str.upper())
print(str.swapcase())
print(str.title())
```
## Raw String
**Note**: '\t' : give tap squence while '\n' give new line
```
back_n = '\n hello dear family '
back_t ='\t hello dear family '
print(back_n)
print(back_t)
```
### using r
```
back_using_r = r'C:\ymyfinder\subfolder\subile\dex.txt'
print(back_using_r)
```
## format function:
```
f_name = 'Khaled'
La_name = 'almutri'
age = 23

print('Welcome dear {} {} . yor age is {}'.format(f_name,La_name,age))
```
**Note**: you can use index in {} according to format

# Advanced Lists

## 2D Lists:
```
value = [[1,2,3],True,'python']
print(value[0][1])
```
## filter function :
```
ages = [19,23,34,32,25,27,29,37,17,18,14]
adults = []

def fillter_age(ages):
    for age in ages:
        if age >= 18:
            adults.append(age)

    return adults
print(fillter_age(ages))
print(adults)
```

#### other way using fillter function
```
ages = [19,23,34,32,25,27,29,37,17,18,14]
adults = []
def fillter_other(age):
    return age  >= 18
print(list(filter(fillter_other,ages)))
```
## map function :
```
numbers = [5,10,15,20,25]
sq_numbers = []
def square (numbers):
    for num in numbers:
        sq_numbers.append(num**2)

    return sq_numbers
print(square(numbers))
```
#### other way using map function
```
numbers = [5,10,15,20,25]
sq_numbers = []
def square(num):
    return num ** 2
print(list(map(square, numbers)))
```
## sort Function:
```
list_one = [9,5,3,7]
list_two = ['Ahmad','khaled','mohammed']

list_one.sort(reverse= True)
list_two.sort(reverse= True)
print(list_one)
print(list_two)
```
**Note**: sort will sort the list ascending by deafulat , but using 'reverse' will sort backward the list

## reverse Function:
```
names = ['eman','fahad','maha','mustifa']
names.reverse()
print(names)
```
## List Comprehension:
```
ls = [1,2,3,4]
multiplied_list = []

for num in ls:
    multiplied_list.append(num*2)

print(multiplied_list)
```
#### list Comprehension way:
```
multiplied_list = [num*2 for num in ls]
print(multiplied_list)
### to add if condition to list Comprehension:
multiplied_list = [num*2for num in ls if num > 3]
print(multiplied_list)
```

# Advanced Functions
## Positional Arguments:
```
def information(name, age):
    print('My name is', name, 'and I am', age, 'years old')


information('Reem', 19)  ####positional arguments because the value will go to the paramenter in function order is matter
```

## Keyword Arguments:
```
def information_1(name, age):
    print('My name is ', name, 'and I am', age, 'years old')


information_1(name='ahmad',age=19)  ####keyword arguments because the value writtien with the paramenter order does not matter
```
## Default Parameter:
```
def information_2(name='fahad', age=18, courses='python102'):
    print('my name is ' + name + ' I am', age, 'years old and I am taking ' + courses + ' courses')


information_2()
information_2('Mohammed', 30, 'math')
```

## Argument Packing:
```
def avg(*args_packing):
    total = sum(args_packing)
    leng = len(args_packing)

    average = total / leng
    print(average)


avg(2, 6)

```
**Note**: it recives unlimitied numbers in shape of tuple  , but the important *

## Argument Unpacking:
```
def personal_information(name1, name2, name3):
    print('First student name: ', name1)
    print('Second student name: ', name2)
    print('third student name: ', name3)


names = 'Ahmad', 'Fahad', 'sara'

personal_information(names[0], names[1], names[2])  ####you can use * instead of indexing each number ex below
personal_information(*names)

```
## Packing & Unpacking:
```
def myfunc(*items):
    print(items)

items = ['Khaled', 'Mohammed', 'Hussian']
myfunc(*items)
```
## Dictionary Packing:
- it recive a keyword arugement in the parameter in shape of dictonrary
- to apply Argument Dictionary Packing use (**)
```
def dic_info(**kwargs):
    print(kwargs)
    print(type(kwargs))
dic_info(name = 'Khaled',age = 19 , city = 'Riyadh')
```
**Note**: it does not recive a positional argumenet due to use ** as Dictionary Packing

## Dictionary Unpacking:
```
def p_information(name,age):
    print('my name is ',name,' and I am ',age,'years old ')

d_information = {'name': 'Khaled','age':19}

p_information(**d_information)
```


