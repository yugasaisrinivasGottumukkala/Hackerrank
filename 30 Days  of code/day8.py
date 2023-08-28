#Day 8 of Hackerrank 30 days of code
#Dictionaries
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
contact={}
for i in range(n):
    key,value=input().split()
    contact[key]=value

for i in range(0,n):
        try:
            s=input().strip()
            if s in contact.keys():
                print("{}={}".format(s,contact[s]))
            else:
                print("Not found")
        except EOFError:
            break
