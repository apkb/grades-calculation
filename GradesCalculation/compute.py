def sortById(elem):
    return int(elem[0])

def sortReportByLastName(elem):
    return elem[1]

def sortReportByGradeNumber(elem):
    return elem[8]

def showComponentDetails(component,studentList,a1total,a1stuList,a2total,a2stuList,projtotal,projstuList,test1total,test1stuList,test2total,test2stuList):
    if component=="a1":
        print("\nA1 grades ("+str(a1total)+")")
        showComponentRows(a1stuList,studentList)   
    elif component=="a2":
        print("\nA2 grades ("+str(a2total)+")")
        showComponentRows(a2stuList,studentList)
    elif component=="pr":
        print("\nProject grades ("+str(projtotal)+")")
        showComponentRows(projstuList,studentList)   
    elif component=="t1":
        print("\nTest1 grades ("+str(test1total)+")")
        showComponentRows(test1stuList,studentList)  
    elif component=="t2":
        print("\nTest2 grades ("+str(test2total)+")")
        showComponentRows(test2stuList,studentList)  

def showComponentRows(componentlist,studentList):
    for i in componentlist:
        id,fn,ln = [tup for tup in studentList if tup[0] == i[0]][0]
        print(i[0]+"\t"+ln+", "+fn+"\t"+i[1]) 
        
def showStandardReport(a1total,a1stuList,a2total,a2stuList,projtotal,projstuList,test1total,test1stuList,test2total,test2stuList,studentList,passpoint=50,sortcriteria="ID"):
    print("\n"+str.ljust("ID",5),str.ljust("LN",6),str.ljust("FN",6),str.ljust("A1",5),str.ljust("A2",5),str.ljust("PR",5),str.ljust("T1",5),str.ljust("T2",5),str.ljust("GR",5),str.ljust("FL",5))
    report=[]
    for i in studentList:
        a1marks=0
        a2marks=0
        projmarks=0
        test1marks=0
        test2marks=0
        gr=0
        fl=""
        if(len([tup for tup in a1stuList if tup[0] == i[0]])!=0):
            a1marks = [tup for tup in a1stuList if tup[0] == i[0]][0][1]
        if(len([tup for tup in a2stuList if tup[0] == i[0]])!=0):
            a2marks = [tup for tup in a2stuList if tup[0] == i[0]][0][1]
        if(len([tup for tup in projstuList if tup[0] == i[0]])!=0):
            projmarks = [tup for tup in projstuList if tup[0] == i[0]][0][1]
        if(len([tup for tup in test1stuList if tup[0] == i[0]])!=0):
            test1marks=[tup for tup in test1stuList if tup[0] == i[0]][0][1]
        if(len([tup for tup in test2stuList if tup[0] == i[0]])!=0):
            test2marks = [tup for tup in test2stuList if tup[0] == i[0]][0][1]
        gr = (7.5*int(a1marks)/int(a1total))+(7.5*int(a2marks)/int(a2total))+(25*int(projmarks)/int(projtotal))+(30*int(test1marks)/int(test1total))+(30*int(test2marks)/int(test2total))
        fl= computeFinalLetterGrade(round(gr), passpoint)
        report.append([i[0],i[2],i[1],a1marks,a2marks,projmarks,test1marks,test2marks,round(gr),fl])
    if(sortcriteria=="GR"):
        report.sort(key=sortReportByGradeNumber,reverse=True)
    elif(sortcriteria=="LN"):
        report.sort(key=sortReportByLastName)
    for r in report:
        id=str.ljust(r[0],5)
        ln=str.ljust(r[1],6)
        fn=str.ljust(r[2],6)
        a1=""
        if(r[3]!=0):
            a1=str(r[3])
        a1=str.ljust(a1,5)
        a2=""
        if(r[4]!=0):
            a2=str(r[4])
        a2=str.ljust(a2,5)
        pr=""
        if(r[5]!=0):
            pr=str(r[5])
        pr=str.ljust(pr,5)
        t1=""
        if(r[6]!=0):
            t1=str(r[6])
        t1=str.ljust(t1,5)
        t2=""
        if(r[7]!=0):
            t2=str(r[7])
        t2=str.ljust(t2,5)
        gr=""
        if(r[8]!=0):
            gr=str(r[8])
        gr=str.ljust(gr,5)
        fl=str.ljust(r[9],5)
        print(id,ln,fn,a1,a2,pr,t1,t2,gr, fl)
        
      
def computeFinalLetterGrade(gr,passpoint):
    fl=""
    delta=round((100-passpoint+1)/7)
    
    if(gr<passpoint):
        fl="F"
    elif(gr>=passpoint and gr<=passpoint+delta-1):
        fl="C"
    elif(gr>=passpoint+delta and gr<=passpoint+delta+delta-1):
        fl="B-"
    elif(gr>=passpoint+2*delta and gr<=passpoint+2*delta+delta-1):
        fl="B"
    elif(gr>=passpoint+3*delta and gr<=passpoint+3*delta+delta-1):
        fl="B+"
    elif(gr>=passpoint+4*delta and gr<=passpoint+4*delta+delta-1):
        fl="A-"
    elif(gr>=passpoint+5*delta and gr<=passpoint+5*delta+delta-1):
        fl="A"
    elif(gr>=passpoint+6*delta and gr<=100):
        fl="A+"
    return fl
          
def showComponentAverage(component,a1total,a1stuList,a2total,a2stuList,projtotal,projstuList,test1total,test1stuList,test2total,test2stuList):
    if component=="a1":
        calculateComponentAvg(component,a1stuList,a1total)   
    elif component=="a2":
        calculateComponentAvg(component,a2stuList,a2total)  
    elif component=="pr":
        calculateComponentAvg(component,projstuList,projtotal)  
    elif component=="t1":
        calculateComponentAvg(component,test1stuList,test1total)   
    elif component=="t2":
        calculateComponentAvg(component,test2stuList,test2total)    
        
def calculateComponentAvg(component,componentlist,maxmarks):
    size= len(componentlist)
    total=0
    for i in componentlist:
        total+=int(i[1])
    avg=round(total/size,2)
    title=""
    if(component=="a1"):
        title="A1 average: "  
    elif component=="a2":
        title="A2 average: " 
    elif component=="pr":
        title="Project average: "    
    elif component=="t1":
        title="Test1 average: " 
    elif component=="t2":
        title="Test2 average: " 
    print("\n"+title+str(avg)+"/"+str(maxmarks))