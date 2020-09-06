# https://hogni.tistory.com/11
from datetime import date, time, datetime
    
f=open("C:\\mylab\\book\\scheduler\\hello.txt", "a+")    

now = datetime.now()

f.write("time : {now}\n".format(now=str(now)))
f.close()


