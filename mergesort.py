def mergesort(arr):
	if len(arr) > 1:
		mid = len(arr) // 2
		left = arr[ :mid]
		right = arr[mid: ]
		mergesort(left)
		mergesort(right)
		i = j = k = 0
		a = len(left)
		b = len(right)
		while i < len(left) and j < len(right):
			if (left[i] < right[j]):
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(left):
			arr[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			arr[k] = right[j]
			j += 1
			k += 1
def printlist(arr):
	for i in range(len(arr)):
		print(arr[i], end =" ")
	print()
if __name__ == '__main__':
	arr = []
	n = int(input("Enter the no of elements = "))
	for i in range(0 , n):
		ele = int(input())
		arr.append(ele)
	print("Given array is ", end="\n")
	printlist(arr)
	mergesort(arr)
	print("Sorted array is :",end = "\n")
	printlist(arr)			
