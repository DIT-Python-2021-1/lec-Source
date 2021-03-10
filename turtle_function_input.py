<<<<<<< HEAD
# turtle graphic 함수(def), input 함수 사용하기
=======
# turtle graphic 함수 사용하기
>>>>>>> c4ff00c9581906b18dd2fffa73dcd876e95d178c
import turtle

# c = ["red", "green", "blue", "yellow"]  # circle color
# print(len(c))  # color list의 크기
m = 0  # move 길이
# r = 30  # circle 반지름 크기
def myTurtleMake(tur, color, move, radius):
    global m  # 함수 밖의 전역변수 m 사용
    tur.color(color)
    tur.circle(int(radius))
    m = int(m) + 50
    t.goto(m, 0)
    return tur

while True:
    c = input("색깔 : ")
<<<<<<< HEAD
    if c=='q':
        print('bye bye')
        exit(0)
    else:
        m = input("이동거리 : ")
        r = input("원의 반지름은 :")
        print("----------------------")
        t = turtle.Turtle()  # Turtle 객체 하나 생성
        myTurtleMake(t, c, m, r)  # 함수 호출
=======
    m = input("이동거리 : ")
    r = input("원의 반지름은 :")
    print("----------------------")
    t = turtle.Turtle()  # Turtle 객체 하나 생성
    myTurtleMake(t, c, m, r)  # 함수 호출
>>>>>>> c4ff00c9581906b18dd2fffa73dcd876e95d178c

turtle.mainloop()
turtle.bye()

# t = turtle.Turtle()  # Turtle 객체 하나 생성
#
# t.color("red")
# t.circle(50)
# t.goto(50, 0)
#
# t.color("green")
# t.circle(50)
# t.goto(100, 0)
#
# t.color("blue")
# t.circle(50)
# t.goto(150, 0)
#
# turtle.mainloop()
# turtle.bye()
#


