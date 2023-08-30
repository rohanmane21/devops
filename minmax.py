def find_max_min():
    lst=[]
    n=int(input("Enter number of elements : "))
    for i in range(0,n):
        ele=int(input())
        lst.append(ele)
    maximum=max(lst)
    minimum=min(lst)
    print("MAX MIN :",(maximum,minimum))
find_max_min()

