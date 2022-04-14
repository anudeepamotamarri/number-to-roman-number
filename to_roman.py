def convert_to_roman(num):
    multiple_of_one=["","I","II","III","IV","V","VI","VII","VIII","IX"]
    multiple_of_ten=["","X","XX","XXX","XL","L","LX","LXX","XXC","XC"]
    multiple_of_hundred=["","C","CC","CCC","CD","D","DC","DCC","CCM","CM"]
    multiple_of_thousand=["","M","MM","MMM","MMMM"]
    string=str(num)
    length=len(string)
    x=0
    ans=""
    while(x<len(string)):
        
        if(length==4):
            ans=ans+multiple_of_thousand[int(string[x])]
        elif(length==3):
            ans=ans+multiple_of_hundred[int(string[x])]
        elif(length==2):
            ans=ans+multiple_of_ten[int(string[x])]
        elif(length==1):
            ans=ans+multiple_of_one[int(string[x])]
        x+=1
        length-=1
    return ans    
for num in range(1,5000):
    print(num,":",convert_to_roman(num))

