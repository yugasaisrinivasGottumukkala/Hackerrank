#Day 6 of Hackerrank 30 days of code

t=int(input()) #Number of test cases
for i in range(0,t):
    s=input() # read strings
    ec='' #Even charecters string
    odc=' ' #odd charecter string (already containg space(" "). 
    for i in range(0,len(s)):
        if i%2==0: # condition for even index checking
            ec+=s[i] # appending even index charecters to ec string
        else:
            odc+=s[i] # appending odd index charecters to odc string
    print(ec+odc) #printing concatenated ec and odc strings 
    
