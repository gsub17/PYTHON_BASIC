inp = list(map(int, input().split()))

C = inp[0]      # no. of college
N = inp[1]      # no. of students

C_no_of_seats = list(map(int, input().split()))

N_student = []

for i in range(0 , N , 1):
        temp = input().split(",")
        N_student.append(temp)

N_student2 = []
def convert(N_student):
    temp = N_student
    id1 = temp[0]
    id1 = int(id1[2])

    per = float(temp[1])
    per = int(per*100)

    choice1 = temp[2]
    choice1 = int(choice1[2])

    choice2 = temp[3]
    choice2 = int(choice2[2])

    choice3 = temp[4]
    choice3 = int(choice3[2])
    
    N_student2.append([id1,per,choice1,choice2,choice3])
    return

for i in range(0 , N , 1):
    temp = N_student[i]
    convert(temp)
 
N_student = N_student2

# take second element for sort
def takeSecond(elem):
    return elem[1]

# sort list with key
N_student.sort(key=takeSecond)
N_student.reverse()


def check(C_no_seats , detail):
    
    choice1 = detail[2]-1 # choice shows college no.
    choice2 = detail[3]-1
    choice3 = detail[4]-1
    
    if C_no_seats[choice1] > 0:
        C_no_seats[choice1] -= 1
        return detail[2]
    elif C_no_seats[choice2] > 0:
        C_no_seats[choice2] -= 1
        return detail[3]
    elif C_no_seats[choice3] > 0:
        C_no_seats[choice3] -= 1
        return detail[4]
    
    return 0



output = []

for i in range(0 , N , 1):
    temp = N_student[i]
    result = check(C_no_of_seats , temp)
    id = temp[0]
    
    if result != 0:
        x = "Student-"+str(id)+" C-"+str(result)
        output.append(x)


print(output)



