def find_all_pairs(myarray, target):
    print("Input : ",myarray)
    for i in range(len(myarray)):
        j = i+1
        while(j<len(myarray)):
            if(myarray[i]+myarray[j] == target):
                print("(",myarray[i],",",myarray[j],")")
            j=j+1
        
nums = [1, 2, 3, 4, 6]
target = 5
find_all_pairs(nums,target)