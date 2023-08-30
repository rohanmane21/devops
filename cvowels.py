def count_vowels():
    s="rohanmane"
    count=0
    for i in s:
        if (i=='a'or i=='e'or i=='i' or i=='o' or i== 'u'or i=='A'or i=='E'or i=='I' or i=='O' or i== 'O'):
            count+=1
    if count== 0:
        print("No Vowels Found")
    else:
        print("Number of Vowels:",count)
count_vowels()

