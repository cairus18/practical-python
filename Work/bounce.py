# bounce.py
#
# Exercise 1.5
height = 100
bounce = .6

for i in range(10):
    height *= bounce
    print(i + 1, round(height, 4))
