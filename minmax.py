class pair:
	def __init__(self):
		self.max = 0
		self.min = 0

def getMinMax(arr,n):
	minmax = pair()

	if n == 1:
		minmax.min = arr[0]
		minmax.max = arr[0]
		return minmax

	if arr[0] > arr[1]:
		minmax.min = arr[1]
		minmax.max = arr[0]
	else:
		minmax.min = arr[0]
		minmax.max = arr[1]

	for i in range(2,n):
		if arr[i] < minmax.min:
			minmax.min = arr[i]

		elif arr[i] > minmax.max:
			minmax.max = arr[i]
	return minmax

arr = list(map(int,input().split()))
n = len(arr)
minmax = getMinMax(arr,n)
print("minimum number is: ", minmax.min)
print("maximum number is: ", minmax.max)
