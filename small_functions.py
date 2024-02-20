# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Vishwa Kumaravel
# Section: 579
# Assignment: 9.16
# Date: 10/20/2023
#
import math

def parta(r_sphere, r_cyl):
    V_sphere = (4/3) * (math.pi) * (r_sphere**3)
    h_cap = r_sphere - math.sqrt((r_sphere**2 - r_cyl**2))
    h_cyl = 2*r_sphere - 2*h_cap
    V_cyl = math.pi * (r_cyl**2) * (h_cyl)
    V_cap = (1/6)*math.pi*h_cap*(3*(r_cyl**2) + h_cap**2)
    V_bead = V_sphere - V_cyl - V_cap*2
    return (V_bead)
#print(parta(1, 0.25))

def partb(n):
    list1 = []
    i = 1
    while i < n:
        list1.append(i)
        i = i +2
        if sum(list1) == n:
            return list1
        while sum(list1) > n:
            list1.pop(0)
            if(sum(list1) == n):
                return list1
    return False
#print(partb(15))       

def partc(char, name, company, email):
    most_len = 0
    fin_str = ""
    lenn = ''
    if len(name) >= len(company) and len(name) >= len(email):
        most_len = len(name) + 4
    elif len(company) >= len(name) and len(company) > len(email):
        most_len = len(company) + 4
    else:
        most_len = len(email) + 4
    
    name_space = ((most_len-len(name))//2) * ' '
    print(len(name_space))
    company_space = ((most_len-len(company))//2) * ' '
    email_space = ((most_len-len(email))//2) * ' '
    first_fourth_row = char * (most_len + 2)

    if len(name_space)*2 + len(name) + 2 < len(first_fourth_row):
        lenn = ' '

    fin_str = f"{first_fourth_row}\n{char}{name_space}{name}{name_space}{lenn}{char}\n{char}{company_space}{company}{company_space}{char}\n{char}{email_space}{email}{email_space}{char}\n{first_fourth_row}"
    return fin_str
print(partc('*', 'Dr. Ritchey', 'Texas A&M University','snritchey@tamu.edu'))

def partd(list1):
    max_1 = max(list1)
    min_1 = min(list1)
    med_2 = 0
    med_3 = 0
    med_1 = 0

    sorted_list = list1.sort()
    if(len(list1) % 2 == 1):
        med_1 = list1[(len(list1)//2)]
    else:
        med_2 = list1[(len(list1)//2)]
        med_3 = list1[(len(list1)//2) - 1]
        med_1 = int((med_2 + med_3)//2)
    return min_1, med_1, max_1
#print(partd([-3.4, -7.5, -2.1, 2.1, 9.6, 4.6]))

def parte(time, distance):
    t_diff = 0
    d_diff = 0
    vel = []
    for i in range(1, len(time)):
        t_diff = time[i] - time[i-1]
        d_diff = distance[i] - distance[i-1]
        vel.append(d_diff/t_diff)
    
    return vel
#print(parte([0, 1, 2, 3], [0, 1, 4, 9]))

def partf(list1):
    for i in range(len(list1)):
        for j in range(len(list1)):
            if(list1[i] + list1[j] == 2027):
                return (list1[i]*list1[j])
    return False
#print(partf([1149, 5926, 1111, 2222, 3333, 916, 5555]))

def partg(x, tol):
    sum1 = 0
    term = 0
    n = 1
    while True:
        term = (2 / (2 * n - 1)) * (x ** (2 * n - 1))
        if abs(term) < tol:
            break
        sum1 += term
        n += 1
    return sum1
#print(partg(0.5, 1e-6))
        
            





