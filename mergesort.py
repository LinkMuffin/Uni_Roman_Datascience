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



def animate(frame_number):
  # Simulate sorting process by modifying data partially
  # based on the frame number (replace with actual merge logic)
  global data_to_sort
  sorted_part = frame_number * len(data_to_sort) // 10  # Adjust factor for speed
  data_to_sort[:sorted_part] = sorted(data_to_sort[:sorted_part])
  line.set_ydata(data_to_sort)
  return line,

fig, ax = plt.subplots()
data_to_sort = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(data_to_sort))
line, = ax.plot(x, data_to_sort)
ax.set_ylim(min(data_to_sort) - 5, max(data_to_sort) + 5)
ax.set_title('Merge Sort Visualization')
ax.set_xlabel('Position')
ax.set_ylabel('Value')

animation = FuncAnimation(fig, animate, frames=11, interval=100)  # Adjust frames and interval
plt.show()

