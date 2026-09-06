a=5
print(a);
b=int(input("enter a number:"));
print("the number you entered is:",b);
c=a+b
print("the sum of a and b is :",c);
print(type(a));
print(type(b));
print(type(c));
d=str(c)
print(type(d));
e=int(input("enter another number:"));
if(e!=2):
    print("e is not equal to 2");
else:
    print("e is equal to 2");
f=int(input("enter a number for f:"));
g=int(input("enter another number for g:"));
h=int(input("enter another number for h:"));
if(f>g and f>h):
    print("f is the greatest number");
elif(g>f and g>h):
    print("g is the greatest number");
else:
    print("h is the greatest number");
marks=int(input("enter your marks:"));
if(marks>=90):
    print("Grade A");
elif(marks>=80):
    print("Grade B");
elif(marks>=70):
    print("Grade C");
elif(marks>=60):
    print("Grade D");
else:
    print("Grade F");
j=int(input("enter a number for j:"));
if(j%2==0):
    print("j is an even number");
else:
    print("j is an odd number");
i=int(input("enter a number for i:"));
for i in range(1,11,2):
    print(i);
for i in range(10,0,-1):
    print(i);
j=int(input("enter a number for j:"));
for k in range(1,j+1):
    print(k);
while(j>0):
    print(j);
    j=j-1;
students = ["Kaja", "Ram", "John"]
colors = ("Red", "Blue")
skills = {"Python", "SQL"}
student = {
    "name":"Kaja",
    "age":20
}
class Student:
    def __init__(self,name):
        self.name = name

s = Student("Kaja")
try:
    num = int(input())
except:
    print("Invalid Input")
    
def add(a, b):
    return a + b

result = add(10, 20)

print(result)