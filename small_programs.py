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