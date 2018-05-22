import compute

f = open("class.txt","r") 
studentList = []
for line in f:
    stuinfo=[]
    info=line.split("|")
    for i in info:
        stuinfo.append(i.rstrip())
    studentList.append(stuinfo)
f.close();

studentList.sort(key=compute.sortById)

def readComponentFile(componentFileName):
    f = open(componentFileName,"r")
    lnum=0
    comp_total=0
    comp_stuList=[]
    for line in f:
        if(lnum==0):
           comp_total=line.rstrip()
        else:
           comp_info=[]
           info=line.split("|")
           for i in info:
               comp_info.append(i.rstrip())
           comp_stuList.append(comp_info)
        lnum+=1  
    f.close() 
    comp_stuList.sort(key=compute.sortById)
    return comp_total, comp_stuList

a1details=a1total,a1stuList = readComponentFile("a1.txt")
a2total,a2stuList = readComponentFile("a2.txt")
projtotal,projstuList = readComponentFile("project.txt")
test1total,test1stuList = readComponentFile("test1.txt")
test2total,test2stuList = readComponentFile("test2.txt")     

while True:
    print("\n1> Display individual component\n2> Display component average\n3> Display Standard Report\n4> Sort by alternate column\n5> Change Pass/Fail point\n6> Exit")
    choice = input(">>> ")
    if choice=="6":
        print("Good Bye")
        break
    elif choice=="5":
        passpoint=input("Choose P/F point: ")
        compute.showStandardReport(a1total,a1stuList,a2total,a2stuList,projtotal,projstuList,test1total,test1stuList,test2total,test2stuList,studentList,int(passpoint))
    elif choice=="4":
        sortcriteria=input("Choose sort criteria(LN/GR): ")
        compute.showStandardReport(a1total,a1stuList,a2total,a2stuList,projtotal,projstuList,test1total,test1stuList,test2total,test2stuList,studentList,50,sortcriteria)
    elif choice=="3":
        compute.showStandardReport(a1total,a1stuList,a2total,a2stuList,projtotal,projstuList,test1total,test1stuList,test2total,test2stuList,studentList)
    elif choice=="2":
        component=input("Choose component(A1/A2/PR/T1/T2): ").lower()
        while(component!="a1" and component!="a2" and component!="pr" and component!="t1" and component!="t2"):
            print("Invalid component, please enter again\n")
            component=input("Choose component(A1/A2/PR/T1/T2): ").lower()
        compute.showComponentAverage(component,a1total,a1stuList,a2total,a2stuList,projtotal,projstuList,test1total,test1stuList,test2total,test2stuList)
    elif choice=="1":
        component=input("Choose component(A1/A2/PR/T1/T2): ").lower()
        while(component!="a1" and component!="a2" and component!="pr" and component!="t1" and component!="t2"):
            print("Invalid component, please enter again\n")
            component=input("Choose component(A1/A2/PR/T1/T2): ").lower()
        compute.showComponentDetails(component,studentList,a1total,a1stuList,a2total,a2stuList,projtotal,projstuList,test1total,test1stuList,test2total,test2stuList)
    else:
        print("Invalid choice, please choose again\n")
