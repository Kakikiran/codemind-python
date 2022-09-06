a=int(input())
b=int(input())
# proper factor sum A
sum_a = 0
for i in range (1,a):
    if a % i == 0:
        sum_a += i
# proper factor sum B
sum_b = 0
for i in range (1,b):
    if b % i == 0:
        sum_b += i
#condition
if sum_a == b and sum_b == a:
    print("Amicable")
else:
    print("Not Amicable")