from cs50 import get_float

count =0
while True:
    change = get_float("Change: ")
    if change>=0:
        break

change = change*100


if change>=25:
    count+= change//25
    change = change % 25

if change>=10:
    count+= change//10
    change = change % 10

if change>=5:
    count+= change//5
    change = change % 5

if change>=1:
    count+= change//1
    change = change % 1


count = int(count)
print(count)
