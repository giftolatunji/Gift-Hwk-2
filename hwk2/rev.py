def reverse_list(myList):
    newList = []
    i = len(myList) - 1
    while (i >= 0):
      newList.append(myList[i])
      i = i-1
    return newList

