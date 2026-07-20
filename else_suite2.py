group1=[1,2,3,4,5]
search=int(input("enter element to search:"))
for element in group1:
             if search==element:
                 print("element found in group")
                 break
else:
    print("Element not found in group")
