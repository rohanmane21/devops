def calculate_average():
    lst=[]
    n=int(input("Enter number of elements : "))
    for i in range(0,n):
        ele=int(input())
        lst.append(ele)
    sum =0
    avg=0
    for i in lst:
        sum+=i
        avg=sum/n
    print(avg)
calculate_average()

