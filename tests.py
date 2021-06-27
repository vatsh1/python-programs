def revlist(user):
	god = []
	a = len(user)
	k = a
	a=a-1
	for i in range(0,k):
		god.append(user[a])
		a = a-1
	return god

user = list(map(int,input().split()))
#user = list(input().split())
print(revlist(user))