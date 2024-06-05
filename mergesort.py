def mergeSort(unsortedList):
  if len(unsortedList) >= 1:
    mid = len(unsortedList) // 2
    left = unsortedList[:mid]
    right = unsortedList[mid:]

    mergeSort(left)
    mergeSort(right)

    l = r = 0
    i = 0
    while l < len(left) and r < len(right):
      if left[l] <= right[r]:
        unsortedList[i] = left[l]  # Direct assignment
        l += 1
      else:
        unsortedList[i] = right[r]  # Direct assignment
        r += 1
      i += 1

    while l < len(left):
      unsortedList[i] = left[l]
      l += 1
      i += 1

    while r < len(right):
      unsortedList[i] = right[r]
      r += 1
      i += 1


import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
mergeSort(my_list)
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
