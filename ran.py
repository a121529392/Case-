import random
import csv
from datetime import datetime, timedelta
class inputdata:
    def __init__(self):
        datetime=0
        name=0
        item=0
min_year=2017
max_year=datetime.now().year

start = datetime(min_year, 1, 1, 00, 00, 00)
years = max_year - min_year+1
end = start + timedelta(days=365 * years)
random_date = start + (end - start) * random.random()
a=str(random_date).split('.')
datetimedata=[]
ALLdate=[]
datetimedata.append(datetime.strptime(a[0],"%Y-%m-%d %H:%M:%S"))
day=a[0]
f = open("input2.csv","w",newline='')
w = csv.writer(f)
w.writerow(['ArriveDate','ArriveItem','Arrivelname','ShippedDate','ShippedItem','Shippedname'])
for i in range(0,3,1):#choice how may days
    new=datetime.strptime(day,"%Y-%m-%d %H:%M:%S") + timedelta(days=1)
    datetimedata.append(new)
    day=str(new)
for i in range(0,len(datetimedata),1):
    num=random.randint(1,10)#choice the range of data per day
    for j in range(0,num,1):
        day1=datetimedata[i]+timedelta(hours=random.randint(-24,24))
        day1=day1+timedelta(minutes=random.randint(-60,60))
        day1=day1+timedelta(seconds=random.randint(-60,60))
        if i==0 and j==0:
            ALLdate.append(day1)
        else:
            x=0
            while x<len(ALLdate):
                if day1==ALLdate[x]:
                    day1=datetimedata[i]+timedelta(hours=random.randint(-24,24))
                    day1=day1+timedelta(minutes=random.randint(-60,60))
                    day1=day1+timedelta(seconds=random.randint(-60,60))
                    x=0
                else:
                    x+=1                   
            ALLdate.append(day1)            

ArriveDate=[]
ShippedDate=[]
for a in range(0,len(ALLdate),1): #this loop is doing sorting the data's type
    for x in range(a,len(ALLdate),1):
        if ALLdate[x]<ALLdate[a]:
            hold=ALLdate[x]
            ALLdate[x]=ALLdate[a]
            ALLdate[a]=hold
count1=0
count2=0
for x in range(0,len(ALLdate),1):
    if random.randint(0,100)%2==1 and x!=0:
        ShippedDate.append(inputdata())
        ShippedDate[count1].datetime=ALLdate[x]
        count1+=1
    else:
        ArriveDate.append(inputdata())
        ArriveDate[count2].datetime=ALLdate[x]
        ArriveDate[count2].item=0
        count2+=1  
for i in range(0,len(ArriveDate),1):
    ArriveDate[i].name="c"+str(i)
    
for i in range(0,len(ShippedDate),1):
    countnum=1
    for j in range(0,len(ArriveDate),1):
        if ShippedDate[i].datetime>ArriveDate[j].datetime:
            if j==0:
                countnum=0
            countnum+=1
    num2=random.randint(0,len(ALLdate))%countnum
    ShippedDate[i].name=ArriveDate[num2].name
    ShippedDate[i].item=10*random.randint(1,20)
    ArriveDate[num2].item+=int(ShippedDate[i].item)
for x in range(0,len(ArriveDate),1):
    if ArriveDate[x].item==0:
        ArriveDate[x].item=10*random.randint(10,100)
print(len(ArriveDate))
print(len(ShippedDate))
if len(ArriveDate)>len(ShippedDate):
    for i in range(0,len(ShippedDate),1):
        w.writerow([ArriveDate[i].datetime,ArriveDate[i].item,ArriveDate[i].name,ShippedDate[i].datetime,ShippedDate[i].item,ShippedDate[i].name])
    for j in range(len(ShippedDate),len(ArriveDate),1):
        w.writerow([ArriveDate[j].datetime,ArriveDate[j].item,ArriveDate[j].name,'','',''])
else:
    for i in range(0,len(ArriveDate),1):
        w.writerow([ArriveDate[i].datetime,ArriveDate[i].item,ArriveDate[i].name,ShippedDate[i].datetime,ShippedDate[i].item,ShippedDate[i].name])
    for j in range(len(ArriveDate),len(ShippedDate),1):
        w.writerow(['','','',ShippedDate[j].datetime,ShippedDate[j].item,ShippedDate[j].name])    
f.close()
