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

a=""" JSON and XML are the two competing standards
in web programming"""
print(a)

new_List=['foo', 'John', 'bar', 'zoo', 'loo', 'too']

import json
list2=["one",'two','three','four']
json_array = json.dumps(list2)


print(json_array)
print("\n\n")

json_data="""
    {
        "integer":1,
        "inner_object":{
            "nothing":null,
            "boolean":false,
            "string":"foo"
        },
        "list_of_strings":[
            "one",
            "two"
        ]
    }
"""
python_dict = json.loads(json_data)
print(python_dict)


print("\n")

def Join2arrays(arr1,arr2):
    L1=json.loads(arr1)
    L2=json.loads(arr2)
    joinedL=L1+L2
    return json.dumps(joinedL)
A1='["one","two"]'
A2='["4","three"]'
print(Join2arrays(A1,A2))
print("\n")

def JSONize(value):
    try:
        value=json.loads(value)
    except ValueError:
        print("Value Error:")
        pass
    except TypeError:
        print("Type Error:")
        pass
    return json.dumps(value)

print(JSONize("ONE"))
print(JSONize("'ONE'"))
print(JSONize(False))
print(JSONize("false"))
print(JSONize("1"))
print(JSONize(1))


import sqlite3

conn=sqlite3.connect("example.db")

cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys=ON")

##cursor.execute("""
##CREATE TABLE users2(
##    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
##    email TEXT NOT NULL,
##    name TEXT NOT NULL
##    )
##""")
##cursor.execute("""
##CREATE TABLE cars2(
##    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
##    brand TEXT NOT NULL,
##    model TEXT NOT NULL,
##    owner INTEGER NOT NULL,
##    FOREIGN KEY(owner) REFERENCES users2(id) ON DELETE CASCADE
##    )
##""")
cursor.execute('INSERT INTO users2 VALUES(NULL,'
               '"john.smith@pythonvisually.com","John Smith")')
cursor.execute('INSERT INTO cars2 VALUES(NULL, "Fiat","Polo",1)')
cursor.execute('INSERT INTO cars2 VALUES(NULL,"BMW","X6",1)')

cursor.execute('INSERT INTO users2 VALUES(NULL,'
               '"ron.heart@pythonvisually.com","Ron Heart")')
cursor.execute('INSERT INTO cars2 VALUES(NULL, "Fierro","GT",2)')
cursor.execute('INSERT INTO cars2 VALUES(NULL,"Jeep","Wrangler",2)')
cursor.execute('INSERT INTO cars2 VALUES(NULL,"Jeep","Cheroke",2)')

cursor.execute('INSERT INTO users2 VALUES(NULL,'
               '"fred.thompson@cox.net","Fred Thompson")')
cursor.execute('INSERT INTO cars2 VALUES(NULL, "Jaguire","XJS",3)')
# Does this fucking thing delete the table entries every time I run this.
# If I comment the above out the tables are always empty... the only way
# to have anything show up is to leave the above uncommented!
# Oh I KNOW what it is... in databases, you need to execute a 'save to table'
# command before the records are preminantly stored in the db.

rows=list(cursor.execute('SELECT * FROM users2'))
print(len(rows))
print(rows)
print('\n')

rows2=list(cursor.execute('SELECT * FROM cars2'))
print(len(rows2))
print(rows2)
print('\n')

# Flask website: http://flask.pocoo.org/

##from flask import Flask
##app=Flask(__name__)
##@app.route("/")
##def hello():
##    return "Hello World!"
##if __name__ == "__main__":
##    app.run(debug=True)
##

#    Instead of using set FLASK_APP = myApp.py, use setx FLASK_APP myApp.py
#    Restart the terminal, and FLASK_APP will have the new value
# See SETX /? - SETX FLASK_APP = "hello.py" - restart cmd window (or edit it
# in system variables area in Win 10

from PIL import Image
from urllib.request import urlopen
import io
#response = urlopen("http://a/b/c.jpg")
response = urlopen("http://www.playrific.com/images/media/a_1269363061813_45574.png")
im_file=io.BytesIO(response.read())
im=Image.open(im_file)
im=im.rotate(90)
im=im.resize((800,600))
im.save("Downloaded_image2.jpg","JPEG")

import os
for root,dirs,files in os.walk(".",topdown=True):
    for name in files:
        print(os.path.join(root,name))
    for name in dirs:
        print(os.path.join(root,name))

#slate isnt available anymore
"""
import slate
#f=open("timer555.pdf")
f=open("spicetoqucs.pdf")
doc=slate.PDF(f)
print(doc)
print(doc[1])
"""

# FLASK Install youtube video (https://www.youtube.com/watch?v=QjtW-wnXlUY)
"""
Virtual Environment
"-m venv env" at command prompt
"emv\Scripts\activate" type at command prompt (no need to cd)

then "pip install flask" install into vm
now "set FLASK_APP = hello.py" after creating file in vm 'env' folder
then "flask run"
it will spit out URL:5000 (127.0.0.1:5000)  - of course cant see it on other
computers...smh

ctrl c to stop server
then deactivate to leave vm

"""

size=128,128
filename="Downloaded_image2.jpg"
im=Image.open(filename)
im.thumbnail(size,Image.ANTIALIAS)
im.save(filename + ".thumbnail","JPEG")

    
#File remover (desabled it)
import os
import time
count=0
kept=0
deleted=0
for(root,dirs,files)in os.walk('.'):
    for filename in files:
        if filename.endswith('.txt'):
#            f=open(filename,'r')
            f=open(filename,'r')
            sdate=f.readline();
            f.close()
        



