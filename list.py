def squareList(begValue, endValue):

    lst = []
    lstValue = 0

    for i in range(begValue, endValue + 1):
        lstValue = i
        square = lstValue**2

        lst.append(square)

    for i in lst:
        if i%2 == 0:
            evenLst.append(i)
        else:
            oddLst.append(i)

    return lst,evenLst,oddLst
        


begInput = int(input('enter the beginning range value: '))
endInput = int(input('enter the end range value: '))



evenLst = []
oddLst = []


print("list of square values: ",squareList(begInput, endInput))  
print("odd number of squres list: ",oddLst)
print("even number of squres list: ", evenLst)

 

  

   




     





      

       

        




          






 

 

 




  
















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































