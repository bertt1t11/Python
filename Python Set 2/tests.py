#dictionary
ages = {
    "John":34,
    "Matt":23,
    "Natasha":27,
    "Gabriella":33
    }

new_List=['foo', 'John', 'bar', 'zoo', 'loo', 'too']

laps = 0
while laps < 10:
    laps +=1
    print(laps)
    print("and")
print("Done")   #loop exited

a=5
b=11
c=a+b
print(c)

print(a is b)
print(id(a))
print(id(b))
print(id(c))
print (id(a)-id(b))

a=b
print(a is b)

a=b=c=d=e=f="Hello World"
print(a,' ', b, '\n', "f= ", f)

integer = 3
my_float = 3.14159
text = "String"
text2='String2'
print(my_float," ",text2)
x=b'byte string?'
print(x)
y=bytearray(b"Hello World!")

myList = [1,2,3,4,5]
myTuple = (a,b,c,d,e)   #tuples are like lists that you cant change
ass=set("Set")
bbb=frozenset(["Paris","NY","Milano"])

print(y)
print(myList)
print(myTuple)
print(ass, " ", bbb)

Long_text = """  Long text is done
like this, I am not sure how
significant this is, but
I guess experience will demonstrate
its usefulness in the bredth of
time"""
print(Long_text)

a = str(100)
b = int("235")
print(a," ",b)

a = 6
a**=3  #a=A^3
print(a)

name="My Name is Earl"
print(name[0])
print(name[1])
print(name[9])
print(name[-1])
print(name[-15])
print(name[7])
print(name[12])

print("m" in name)
print("x" in name)
print(len(name))

cat = new_List[3] + "Ass" + str(a) + " " + name + " " + str(my_float)
print(cat)

car = 0
def hi(bar, name2 = "Mr Fibbs"): #default value assignment
    print("Hello there " + name2 + ", you go now!")
    print("fobar")
    bar *=5
    car = bar+5
    print(bar)
    if bar > 25:
        print("bar is too high")
        car +=2
    elif bar > 4 and bar < 8:
        print("bar is just right")
    else:
        print("bar is too low")
        car*=15

    print("car = " + str(car))
    return bar+100

print(hi(15,"ass"))
print(hi(4))




class CarCar:
    def __init__(self,model,max_speed):
        self.model = model
        self.max_speed = max_speed
        self.speed = 0
    def accelerate(self,speed_difference):
        self.speed += abs(speed_difference)
        self.speed = min(self.speed,self.max_speed)
    def decelerate(self,speed_difference):
        self.speed -= abs(speed_difference)
        self.speed=max(slef.speed,-5)

bmw_x6 = CarCar(model="BMW X6",max_speed = 230)
bmw_x6.accelerate(30)

print(bmw_x6.model," ",bmw_x6.max_speed,"\n",bmw_x6.speed)
print("done")

laps = 0
while laps < 10:
    laps +=1
    print(laps)
    print("and")
    if laps==6:break
    if laps==3:continue
else:
    print("Shit, now WHAT?")

numbers = [1,2,5,6,7,8,9]
for number in numbers:
    print("looking at " + str(number))
    if number>6:
        print("TOO BIG: " + str(number) + "!!")
        break
    

print("Done")   #loop exited

for name in ages:
    print(name)

the_file = open("integers.txt","w")
integers = [1,2,3,4,5,6,22,21,55,2,1,86,3]
for integer in integers:
    the_file.write(str(integer)+'\n')
    the_file.close

the_file = open("integers.txt")
lines = the_file.readlines()
for line in lines:
    print(line)
the_file.close

try:
    1/0
except ZeroDivisionError as e:
    print(str(e)+". But it is totally fine.")

import getpass
print(getpass.getuser())

from getpass import getuser
print(getuser())

from os.path import abspath, curdir
print(curdir)
print(abspath(curdir))

#multiplatform file rename/remove

from os import remove, rename, rmdir
from os.path import join
"""
remove(join("foo","one.txt"))
rename(join("foo","two.txt"),join("foo","bar.txt"))
rmdir("foo")  # wont deletr directory with files in it
"""
from os import listdir
print(listdir(curdir))

MyTxt = "Fuck this shit, you know that Python is just a shit scripting language and that C++ is where the shit is at!"

print(MyTxt)

import re
#found = re.search("*hit",MyTxt)  # Error, BIG Error

found =  re.search("shit",MyTxt)
print(found)
print("""Trying: re.search("F*shit",MyTxt)
         re.search("*shit",MyTxt) produces
         a BIG error BTW""")
found = re.search("F*shit",MyTxt)
print(found)
print("\n" + "\n")
print(str(found) + " Assholes\n\n") #This wont work unless you convert the 'found' object to a string      

noMatch=re.search("found",MyTxt)
print(noMatch)
print(type(noMatch))

found2 = re.search("yo.*hon",MyTxt)
print(found2)

print(found2.start())
print(found2.end())
print(found2.group())
print(MyTxt[16:36])

TL = list(re.finditer("shit",MyTxt))
print(TL)
print("2nd list item: " + str(TL[1]))      

abc = """\nSearch wildcards"
A Cardinality is a set of something,
   . = arbitrary character
   * = Zero or more
   + = One or more
   ? = Zero or one
   [m] = Exact number of symbols
   {m,n] = At least m and n at most
   ^ = Beginning of line (or can mean NOT)
   $ = End of the line"""

print(abc)

ass = str(re.search("^hit",MyTxt))
print(ass + "- shit dont work")
#print("this language is pure SHIT")
print(re.search("^Beginning","Beginning of line"))
print(re.search("inning","Beginning of line"))
print(re.search('[^line]','Beginning of line')) # NOT line
print(re.search('end$','Find me at the end'))

print(re.search('th.*$','Find me at the end'))

txt="The quick brown fox jumps over the lazy dog quick"
print(re.findall("quick|dog",txt))              # | or
print(re.findall("quick+",txt))                 # + one or more
print(re.findall("quick*",txt))                 # * zero or more
print(re.findall("quick?",txt))                 # ? zero or one
print(re.findall("quick ([a-z]+)",txt))         # () group
print(re.findall("[Tt]he ([a-z]{4})",txt))      # {} exactly
print(re.findall("[Tt]he ([a-z]{4,5})",txt))    # {x,y} at least X and at most y
print(re.findall("jumps.+dog",txt))             # . any singel character

pme = """\n\nRegular Expressions
. = Any Character
\" Double quote character
\\ Backslash
\t tab
\n newline
[0-9] Any digit inclusively
[^0-9] Any character that is NOT a digit
[^a-z] Any character that is NOT a lower case letter
[a-zA-Z0-9_] Any digit, letter or an underscore

[0-9]+ means one or more digits
([1-9][1][0-9]+)? = An optional number that does not start with zero.
Parentheses let you combine multiple symbole into SYMBOL groups and apply
cardinalities to the whole group.  The above group could be rephrased as:
Zero or one number that begins with exactly one digit that is not zero
and multiple arbitrary digits afterwards.
[^_][a-z]* = A string that may contain any lowercase letter but cant be
preceded with an underscore.

"""
print(pme)

# To replace first occurence...
print(re.sub("qui.*wn","fubar",txt))
print(txt)
import math
print(math.sin(math.radians(30)))
print(math.cos(math.pi*.75))

print(math.e)
print(math.sqrt(17))

            
            
