'''Task-
  In second year computer engineering class, group A student's play cricket, group B students play badminton and group C students play football.
Write a Python program using functions to compute following: - a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.
(Note- While realizing the group, duplicate entries should be avoided, Do not use SET built-in functions)
'''
def removeDuplicate(d):
    lst=[]
    for i in d:
        if i not in lst:
            lst.append(i)
    return lst

inter=[]
def intersection(l1,l2):
	for i in l1:
		if i in l2:
			inter.append(i)
	return inter
uni=[]
def union(l1,l2):
	for i in l2:
		if i not in uni:
			uni.append(i)
	return uni
diff=[]
def differnce(l1,l2):
	for i in l1:
		if i not in l2:
			diff.append(i)
	return diff
Cricket = []
n = int(input("\n\nEnter number of students who play cricket : "))
for i in range(0, n):
    m = int(input("Enter the roll numbers of students " + str(i+1) + " "  ))
    Cricket.append(m) 
print("Original list of students playing cricket is :" +str(Cricket))
Cricket=removeDuplicate(Cricket)
print("The list of students playing cricket after removing duplicates : " +str(Cricket))


Football = []
n = int(input("\n\nEnter number of students who play football : "))
for i in range(0, n):
    m = int(input("Enter the roll numbers of students " + str(i+1) + " "  ))
    Football.append(m)
print("Original list of students playing football :" +str(Football))
Football=removeDuplicate(Football)
print("The list of students playing football after removing duplicates : " +str(Football))




Badminton = []
n = int(input("\n\nEnter number of students who play badminton : "))
for i in range(0, n):
    m = int(input("Enter the roll numbers of students " + str(i+1) + " "  ))
    Badminton.append(m) 
print("Original list of students playing badminton :" +str(Badminton))
Badminton=removeDuplicate(Badminton)
print("The list of students playing badminton after removing duplicates : " +str(Badminton))





flag=1
while flag==1:
    print("\n\n--------------------MENU--------------------\n")
    print("1. List of students who play both cricket and badminton")
    print("2. List of students who play either cricket or badminton but not both")
    print("3. List of students who play neither cricket nor badminton")
    print("4. Number of students who play cricket and football but not badminton")
    print("5. Exit\n")
    ch=int(input("Enter your Choice (from 1 to 5) :"))

    if ch==1:
        print("Number of students who play both cricket and badminton : ", intersection(Cricket,Badminton))
        a = input("\n\nDo you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==2:
        union(Cricket, Badminton)
        intersection(Cricket,Badminton)
        print("Number of students who play either cricket or badminton but not both : ", differnce(uni,inter))
        a = input("\n\nDo you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==3:
        print("Number of students who play neither cricket nor badminton : ",)
        a = input("\n\nDo you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==4:
        print("Number of students who play cricket and football but not badminton : ", CBnF(Cricket,Football,Badminton))
        a = input("\n\nDo you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==5:
        flag=0
        print("Thanks for using this program!")

    else:
        print("!!Wrong Choice!! ")
        a=input("\n\nDo you want to continue (yes/no) :")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Thanks for using this program!")
            



			
