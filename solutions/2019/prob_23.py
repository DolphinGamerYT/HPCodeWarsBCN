n = int(input())

if n == 1:
    print('x')
elif n % 2 == 0:
    for x in range(n//2):
        print(" " * x + "\\" + " " * 2*(n//2-(x+1)) + "/")
    for x in range(n//2):
        print(" " * (n//2-(x+1)) + "/" + " " * 2*x + "\\")
elif (n % 2) == 1:
    for i in range(n//2):
        print(" " * i + "\\" + " " * (2*(n//2-(i+1))+1) + "/")
    print(" " * ((n//2)) + "X")
    for i in range(n//2):
        print(" " * (n//2-(i+1)) + "/" + " " * ((2*i)+1) + "\\")
