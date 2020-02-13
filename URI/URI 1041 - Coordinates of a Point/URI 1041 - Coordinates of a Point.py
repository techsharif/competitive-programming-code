zero = 0

x , y =  list(map(float, input().strip().split(" "))) 

if x == zero and y == zero:
    print("Origem")
elif x == zero:
    print("Eixo Y")
elif y == zero:
    print("Eixo X")
elif x > zero and y > zero:
    print("Q1")
elif x < zero and y > zero:
    print("Q2")
elif x < zero and y < zero:
    print("Q3")
else:
    print("Q4")