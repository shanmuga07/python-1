def findMedian( a , N , mean ):
 
    # Find sum of array elements
    sum = 0
    for i in range(N - 1):
        sum += a[i]
     
    return (mean * N) - sum
a = [25, 65, 80]
mean = 50
n = len(a)
print("The Median element : ", end = '')
print(findMedian(a, n+1, mean))
