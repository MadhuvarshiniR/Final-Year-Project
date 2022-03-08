def give(n,x):
    y = n-x
    count = 0
    while(True):
        if(x==y or x<=0 or y<=0):
            break
        elif (x-y>0):
            x = x-y
            count+=1
        elif(y-x >0):
            y= y-x
            count+=1
        
    print(count)

inp = input()
inp = inp.split(" ")
give(int(inp[0]),int(inp[1]))
