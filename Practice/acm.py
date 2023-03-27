

n , k = map(int, input().split())

members = list(map(int, input().split()))

count = 0
for i in members:
    if (5-i>=k):
        count+=1

print(count//3)
