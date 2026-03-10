#fibonacci series 1
'''
n=int(input('enter no. of terms: '))
a=0
b=1
for i in range(n):
    print(a, end=' ')
    c=a+b
    a=b
    b=c
'''
#fibonacci series 2
'''
n=int(input())
a=0
b=1
if n <= 1:
    print(n)
for _ in range(2, n + 1):
        next_fib = a + b
        a = b
        b = next_fib
print(b)
'''
#fibonacci series 3
'''
number=int(input())
if number < 0:
    print(False)
a = 0
b = 1
if number == 0 or number == 1:
    print(True)
while b <= number:
    if b == number:
        print(True)
        break
    next_fib = a + b
    a = b
    b = next_fib
else:
    print(False)
'''
#armstrong 1
'''
n=int(input(' enter the no. :'))
t=n
sa=0
d=len(str(n))
while t>0:
    dig=t%10
    sa+=dig**d
    t//=10
if sa==n:
    print('yes')
else:
    print('no')
'''
#perfect 1
'''
n=int(input('enter'))
sum_perf=0
for i in range(1,n):
    if n%i==0:
        sum_perf+=i
if sum_perf==n:
    print('yes')
else:
    print('no')
'''
#perfect 2
'''
s=int(input('enter sarte range: '))
e=int(input('enter end range: '))
found=False
for num in range(s,e+1):
    d_sum=0
    for d in range(1,num):
        if num%d==0:
            d_sum+=d
    if d_sum==num:
        print(num, end= ' ')
        found=True
if not found:
    print('no')
'''
#prime 1
'''
n1=int(input('enter the start range: '))
n2=int(input('eter the end range: '))
if n1>1 and n2>1:
    for i in range(n1,n2+1):
        for j in range(2, i):
            if i%j==0:
                break
        else:
            print(i, end=' ')

print("--- Constrained Armstrong Number Finder ---")
start_range= int(input('Enter the starting number of the range: '))
end_range= int(input('Enter the ending number of the range: '))
found_any = False
for num in range(start_range, end_range + 1):
    no= num
    s= str(no)
    d= len(s)
    sum_arm = 0
    t=no
    while t> 0:
        digit = t % 10
        p = 1
        c = 0
        while c < d:
            p *= digit
            c += 1
                
            sum_arm += p
            t //= 10 
            if p == no:
                print(no, end=', ')
                found_any = True
if not found_any:
    print("No Armstrong numbers found in the specified range.")

emp = {101:'John', 102:'Alice', 103:'Bob'}
print(emp.get(104) == None)
print(emp[104])

scores = {'Sam':90, 'Eva':95, 'Jay':88}
print(sorted(scores.values()))
print(list(scores.values()))

s = "python is easy and python is powerful"
words = s.split()

d = {}
for w in words:
    d[w] = d.get(w, 0) + 1
print(d)

d = {'a':1,'b':2}
print(list(d.keys()))
print(list(d))
'''
#matrix 1
'''
lst=[]
r=int(input('enter the number of rows:'))
c=int(input('columns:'))
for i in range(r):
    row=[]
    for j in range(c):
        ele=int(input('element:'))
        row.append(ele)
    lst.append(row)
for i in range(r):
    for j in range(c):
        lst[i][j]=lst[i][j]*3
print(lst)
'''
#matrix 2
'''
lst=[]
r=int(input('rows'))
c=int(input('columns'))
for i in range(r):
    row=[]
    for j in range(c):
        ele=int(input('element'))
        row.append(ele)
    lst.append(row)
l=0
ri=0
for i in range(r):
    l+=lst[i][j]
    ri+=lst[i][r-1-i]
if r==c and r%2==1:
    tot=l+ri-lst[r//2][r//2]
else:
    tot=l+ri
print(tot)
'''
#matrix 3
'''
lst[]
r=int(input('rows'))
c=int(input('columns'))
for i in range(r):
    row=[]
    for j in range(c):
        ele=int(input('element'))
        row.append(ele)
    lst.append(row)
bor=0
for i in range(r):
    for j in range(c):
        if i==0 or i==r-1 and j==0 or j==c-1:
            bor+=lst[i][j]
print(bor)
        
'''
#predict the op
'''
birthday = {

'Newton':1642,

'Darwin': 1809,

'Turing': 1912

}

print ('keys:', birthday.keys())

print ('values:', birthday.values())

print ('items:', birthday.items())

print ('get:', birthday.get('Curie', 1867))

temp = {

'Curie': 1867,

'Hopper': 1906,

'Franklin': 1920
}
birthday.update(temp)

print ('after update:', birthday)

birthday.clear()

print ('after clear:', birthday)

'''
#annual paper
r=int(input('rowa:'))
c=int(input('col'))
lst=[]
for i in range(r):
    row=[]
    for j in range(c):
        ele=int(input('enter the element: '))
        row.append(ele)
    lst.append(row)
com=[]
for i in range(r):
    for j in range(c):
        num=lst[i][j]
        count=0
        for f in range(1,num+1):
            if num%f==0:
                count+=1
        if count>2:
            com.append(num)
print(com)
