num=int(input("Number of records:"))
list1=[]
n=0
marks1=[]
highest_marks=0
highest_scorer=""
lowest_scorer=""
lowest_marks=0
average=0

while n != num:
    n+=1
    dict1={}
    roll_no=input("Enter Your Roll No:")
    name=input("Enter Your name:")
    age=int(input("Enter Your Age:"))
    marks=int(input("Enter Your Marks:"))
    dict1["Roll_no"]=roll_no
    dict1["Name"]=name
    dict1["Age"]=age
    dict1["Marks"]=marks
    list1.append(dict1)
print("Results:")
print("**roll_num** | **name** | **age** | **marks**(out of 100)")
for i in range(num):
    print(list1[i]["Roll_no"]+" | "+list1[i]["Name"]+" | "+str(list1[i]["Age"])+" | "+str(list1[i]["Marks"]))
    marks1.append(list1[i]["Marks"])
highest_marks=max(marks1)
lowest_marks=min(marks1)    
average=sum(marks1)/len(marks1)
for i in range(num):
    if (list1[i]["Marks"]) == highest_marks:
        
        highest_scorer=list1[i]["Name"]
    if (list1[i]["Marks"]) == lowest_marks:
        lowest_scorer=list1[i]["Name"]
        
print(f"Class Average is {average} \nHighest Scorer is {highest_scorer} \nLowest Scorer is {lowest_scorer}")