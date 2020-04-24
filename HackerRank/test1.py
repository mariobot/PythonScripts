#Original 

if __name__ == '__main__':
    #students = []
    #students = [['Harsh',20],['Beria',20],['Varun',19],['Kakunami',19],['Vikas',21]]
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]] 

    #for _ in range(int(input())):
    #    name = input()
    #    score = float(input())
    #    alumn = [name,score]
    #    list.append(alumn)
    
    def takeSecond(elem):
        return elem[1]

    students.sort(key=takeSecond)

    #for i in students:
    #    print(i)

    #students.remove(students[0])

    def remove_first(list_studens):
        m = list_studens[0][1]
        ltt = []
        for x in list_studens:
            if x[1] == m:
                list_studens.remove(x)
            else:
                ltt.append(x)
        return ltt

    students = remove_first(students)

    def goup_same(list_studens):
        min_val = list_studens[0][1] 
        __result = []
        for ss in list_studens:
            if ss[1] == min_val:
                __result.append(ss[0])
        return __result
    
    #for g in students:
    #    print(g)

    result = goup_same(students)

    result.sort()

    for it in result:
        print(it) 
    



    

