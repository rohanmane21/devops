def power_list():
   test_list = [6, 9, 1, 8, 4, 7]
   print("The original list is : " + str(test_list))
   res = []
   for i,ele in enumerate(test_list):
    res.append(ele ** i) 
   print("Powered elements : " + str(res))
power_list()
