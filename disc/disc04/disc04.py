def insect_combinatorics (n,m):
    def walk(x,y):
        if x==n and y==m:
            return 1
        elif x>n or y>m:
            return 0
        else :
            return walk(x+1,y)+walk(x,y+1)
         
          
    return insect_combinatorics(1,1)

def max_product(list):
    def jilu(i,list):
        if i<len(list):
            list[i]=[list[i] * list[i + 1] for i in range(0, len(list) - 1, 2)]
            return jilu(i+1,list)
        elif  i==len(list)-1:
            return list.index(max(list))
        
    

        
        
 
    return jilu(0,list)
