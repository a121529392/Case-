import csv
from ctypes import *
from datetime import datetime as dt
from struct import *
class inputdata:
    def __init__(self): #the datatype of input
        self.datetime = 0 #datetime Y/M/D H:M:S
        self.item = 0 #the number of item
        self.name=0
        self.out=0 #if it is a arrive item out=0,if it is a shipped item out=1
class caserack:
    def __init__(self): #the datatype of input
        self.space = [] #datetime Y/M/D H:M:S
        self.name=[]
        self.num=[]
        self.item_name=0
ArriveDate=[]#keep the ArriveDate data
ArriveItem=[]#keep the ArriveItem data
ArriveName=[]#keep the ArriveTime data
ShippedDate=[]#keep the ShippedDate data
ShippedItem=[]#keep the ShippedItem data
ShippedName=[]#keep the ShippedTime data
f=open('input2.csv','r',encoding='big5')
for row in csv.DictReader(f):
    ArriveDate.append(row['ArriveDate'])#read ArriveDate
    ArriveItem.append(row['ArriveItem'])#read ArriveItem
    ArriveName.append(row['Arrivelname'])#read ArriveTime
    ShippedDate.append(row['ShippedDate'])#read ShippedDate
    ShippedItem.append(row['ShippedItem'])#read ShippedItem
    ShippedName.append(row['Shippedname'])#read ShippedTime
f.close()
print(len(ArriveDate))
print(len(ArriveItem))
print(len(ArriveName))
print(len(ShippedDate))
print(len(ShippedItem))
print(len(ShippedName))
ADate=[] #The argument that we keep the value of converting str to Date type(ArriveDate was str when we read from the file)
AllData=[] #Keep all of the data
SDate=[] #The argument that we keep the value of converting str to Date type(ShippedDate was str when we read from the file)
for x in range(0,len(ArriveDate),1): #this for loop is doing about converting the str type into Datetime Type(ArriveDate)
    if ArriveDate[x].strip(): #check if there is Data int the arrary
        ADate.append(dt.strptime(ArriveDate[x], "%Y-%m-%d %H:%M:%S"))
        AllData.append(inputdata()) #append alldata
        AllData[x].datetime=ADate[x] #put arrivedate into alldata
        AllData[x].item=int(ArriveItem[x]) #put arrive item into alldata
        AllData[x].name=ArriveName[x]
        AllData[x].out=0 #know if the item is come or out
count=0
print(len(AllData))
for x in range(len(AllData),len(ShippedDate)+len(AllData),1): #this for loop is doing about converting the str type into Datetime Type(ShippedDate)
    if ShippedDate[count].strip():
        SDate.append(dt.strptime(ShippedDate[count], "%Y-%m-%d %H:%M:%S"))
        AllData.append(inputdata())
        AllData[x].datetime=SDate[count]
        AllData[x].item=int(ShippedItem[count])
        AllData[x].name=ShippedName[count]
        AllData[x].out=1
        count+=1        
print(len(AllData))
for x in range(0,len(AllData),1):
    print(AllData[x].datetime)
    print(AllData[x].out)
hold=inputdata() #the argument we need in sort cause we need to hold and change
for a in range(0,len(AllData),1): #this loop is doing sorting the data's type
    for x in range(a,len(AllData),1):
        if AllData[x].datetime<AllData[a].datetime:
            hold=AllData[x]
            AllData[x]=AllData[a]
            AllData[a]=hold

position = 0 #the first position
posvertical=0
assume=3 #assume a move a block of the is 3
assumevertical=5
rackspace=[]
for i in range(0,6,1):
    rackspace.append(caserack())
    for j in range(0,2,1):
        rackspace[i].space.append(0)
        rackspace[i].num.append(0)
        rackspace[i].name.append("F09"+str(0)+str(j+1)+"-"+str(i+1))
        
    
f = open("result2.csv","w",newline='')
w = csv.writer(f)
w.writerow(['Location','Time','Name','Item','Available','Operation','DateTime'])
for x in range(0,len(AllData),1):#this loop is doing putting the item on the rack
    for a in range(0,2,1): #two space
        for b in range(0,len(rackspace),1): #6 level
            if rackspace[b].space[a]==0 and AllData[x].out==0 and AllData[x].item!=0:
                second=0#count the second
                if position!=a+1:
                    second+=(a+1-position)*assume*2 #go and back so *2
                if posvertical!=b:
                    second+=b*2*5 #level up and down's time
                rackspace[b].space[a]=1 #put the item in
                rackspace[b].item_name=AllData[x].name
                rackspace[b].num[a]=AllData[x].item
                AllData[x].item-=AllData[x].item
                w.writerow([rackspace[b].name[a],second,rackspace[b].item_name,rackspace[b].num[a],"not available","arrival",AllData[x].datetime])
            elif rackspace[b].item_name==AllData[x].name and AllData[x].out==1 and AllData[x].item!=0:
                second=0 
                if position!=a+1:
                    second+=(a+1-position)*assume*2 #go and back so *2
                if posvertical!=b:
                    second+=b*2*5 #level up and down's time
                rackspace[b].num[a]-=AllData[x].item
                if rackspace[b].num[a]==0:
                   rackspace[b].space[a]=0 
                AllData[x].item-=AllData[x].item
                if rackspace[b].num[a]==0:
                    w.writerow([rackspace[b].name[a],second,rackspace[b].item_name,rackspace[b].num[a],"available","shipped",AllData[x].datetime])
                else:
                    w.writerow([rackspace[b].name[a],second,rackspace[b].item_name,rackspace[b].num[a],"not available","shipped",AllData[x].datetime])
w.writerow(["F09 Rack"])
for x in range(0,2,1):
    for y in range(0,len(rackspace),1):
        if rackspace[y].num[x]==0:
            w.writerow([rackspace[y].name[x],"available"])
        else:
            w.writerow([rackspace[y].name[x],"not available"])

f.close()
        
