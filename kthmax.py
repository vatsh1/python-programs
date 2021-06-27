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

def getkth(arr,n,k):
	while (k != 0):
		minmax = getMinMax(arr,n)
		minn = minmax.min
		k = k-1
		if k!=0:
			arr.remove(minn)
			n = n-1
	return minn

arr = list(map(int,input().split()))
k = int(input())
n = len(arr)
t = getkth(arr,n,k)
print("minimum number is: ", t)
#print("maximum number is: ", minmax.max)





T = int(input())
Villains_list = []
while(T != 0):
    T = T - 1
    result = 0
    N = int(input())
    Villains_list = list(map(int, input().split()))     
    Player_list = list(map(int, input().split()))
    Villains_list.sort(reverse = True)
    Player_list.sort(reverse = True)
    length = len(Player_list)
    i = 0
    while(i < length-1):                
        if(Player_list[i] < Villains_list[i]):
            result = 121
        i = i + 1

    if(result != 0):
        print("LOSE")
    else:
        print("WIN") 