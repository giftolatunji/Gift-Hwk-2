def swap_list(myList):
   length = len(myList)
   if length >= 1:
       if length % 2 == 0:
           x = int(length // 2)
           value = myList[length - 1]
           myList[length-1] = myList[x-1]
           myList[x-1] = value
       else:
           x = int(length // 2)
           value = myList[length - 1]
           myList[length - 1] = myList[x]
           myList[x] = value
   return myList

