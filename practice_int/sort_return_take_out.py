def ret_arr(arr):
    
    dp={}
    ans=0
    
    for item in arr:
        try:
            dp[item]+=1
        except:
            dp[item]=1
    for item in dp.values():
        if item==1:
            ans=-1
            break
        ans+=item//3
        if item%3==1 or item%3==2:
            ans+=1
    print(ans)

    #             ans+=1
    #     else:
    #         neg=-1
    # if neg!=-1:
    #     print(ans)
    # else:
    #     print(neg)
#test case 1: [2,3,4,3,2,2,4]

#test cases :
#test case 1: [2,3,4,3,2,2,4]
#     output:3
#explanation: we can pair the elements in the pairs of 2's or triads of three for example 2,2,2 ; 3,3,; 4,4
#hence the total output would be 3 we can take out the triads of 2 and the pairs of 3 and 4 together
# for item in random_list:
#    # checking the element in dictionary
#    if item in frequency:
#       # incrementing the counr
#       frequency[item] += 1
#    else:
#       # initializing the count
#       frequency[item] = 1

# # printing the frequency
# print(frequency)