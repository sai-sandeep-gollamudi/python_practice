'''
students = {'Tony': 97,'John': 91,'Doe': 73,'Jane':93,'Peter': 87}

students_grade = {}

for k,v in students.items():
    g=''
    if(v>90):
        g='A'
    elif(v>80):
        g='B'
    elif(v>70):
        g='C'
    else:
        g='D'
    students_grade[k] = g

print(students_grade)

######################################################

travel_log = [{'Country':'France','Places_visited':['Paris','Dijon','Lille'],'Times_visited':'2'}]

country_name = input("Enter the country name: ")
places_visited=[]
while(True):
    name=input(f"Enter a place you visited in {country_name}: ")
    places_visited.append(name)
    ch = input("Type yes to enter any other places, no to exist: ")
    if(ch == 'n' or ch =='no' or ch =='No' or ch == 'NO'):
        break
times_visited = int(input(f"Enter the number of times you visited {country_name}: "))
travel_log.append({'Country':country_name,'Places_visited':places_visited,'Times_visited':times_visited})

print(travel_log)

'''

# avg temperature, and days which record temperature more than average
days = int(input("Enter the number of days: "))
c=1
s=0
l=[]
while(c<=days):
    temp = (int(input(f"Enter the temp of day {c}:  ")))
    s+=temp
    l.append(temp)
    c+=1

avg = round((s/days),2)
print(f"The average temperature is: {avg}")
print("The days where temperature is above average: ")
for i in range(len(l)):
    if(l[i]>avg):
        print(f"day {i+1}")


#max product of two integers in array
def max_prod(arr):
    arr = arr.sort(reverse=True)
    return arr[0]* arr[1]

#middle function which returns list without first and last elements
def middle(lst):
    # TODO
    out = []
    for i in range(1,len(lst)-1):
        out.append(lst[i])
    return out
    #return lst[1:-1]

#diagonal sum
def diagonal_sum(matrix):
    # TODO
    l = len(matrix)
    c=0
    s=0
    while(c<l):
        s=s+matrix[c][c]
        c+=1
    return s

#first and second best scores from list include duplicates
def first_second(my_list):
    # TODO
    my_list.sort(reverse=True)
    return my_list[0],my_list[1]


#remove duplicates from list
def remove_duplicates(arr):
    # TODO
    out = []
    for i in range(len(arr)):
        if arr[i] not in out:
            out.append(arr[i])
    return out

#Write a function to find all pairs of an integer array whose sum is equal to a given number.
#Do not consider commutative pairs.
def pair_sum(myList, sum):
    # TODO
    out=[]
    for i in range(len(myList)):
        for j in range(i,len(myList)):
            if(myList[i]+myList[j]==sum):
                out.append(f"{myList[i]}+{myList[j]}")
    return out

#check if the list has duplicates

def contains_duplicate(nums):
    # TODO
    seen = set()
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        seen.add(nums[i])
    return False
