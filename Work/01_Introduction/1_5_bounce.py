# bounce.py
#
# Exercise 1.5
height = 100
bounce = 3/5
for n in range(10):
    height = height * bounce
    print(n+1, height)
