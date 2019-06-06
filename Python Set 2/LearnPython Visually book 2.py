
#File remover (desabled it)
import os
import time
count=0
kept=0
deleted=0


the_file = open("integers.txt")
lines = the_file.readlines()
for line in lines:
    print(line)
the_file.close



#File remover (desabled it)
import os
import time
count=0
kept=0
deleted=0
for(root,dirs,files)in os.walk('.'):
    for filename in files:
        if filename.endswith('.txt'):
            f=open(filename,'r')
            sdate=f.readline();
            f.close()
#            pdate=time.strptime(sdate,'%Y%-m%-d\n')
            pdate=time.strptime(sdate,'d/m%/%Y%\n')
            if pdate.tm_year>2002:
                kept+=1
                print(filename)
            else:
                print("os.remove(filename)")
                print(filename)
                print(pdate)
            deleted+=1
        count+=1
    print("Total files: " + str(count))
    print("Kept: "+str(kept))
    print("Deleted: "+str(deleted))
print("Total files: " + str(count))
print("Kept: "+str(kept))
print("Deleted: "+str(deleted))
    
