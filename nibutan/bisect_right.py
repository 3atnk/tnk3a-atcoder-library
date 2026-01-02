array = []
left = 0
right = len(array)

while left < right:
  	middle = ((right - left) // 2) + left
		if key < array[middle] :
			right = middle
		else:
			left = middle + 1
