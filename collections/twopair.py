arr=[2,3,4,5,]

sum=int(input("enter sum :"))

for i in range(0,len(arr)):

    for j in range(i+1,len(arr)):

        cur_sum=arr[i]+arr[j]

        if sum==cur_sum:

            print(arr[i],arr[j])

            break