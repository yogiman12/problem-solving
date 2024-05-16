number = int(input())
team : int = 0
for _ in range(number):
    if input().count('1')>1:
        team  += 1
print(team)