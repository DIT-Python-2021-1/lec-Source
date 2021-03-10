# turtle graphic 함수 사용하기
import turtle

c = ["red", "green", "blue", "black"]  # circle color
print(len(c))  # color list의 크기
m = 0  # move 길이
r = 20  # circle 반지름 크기
t = turtle.Turtle()  # Turtle 객체 하나 생성
t.shape("turtle")


def myTurtleMake(tur, color, move, radius):
    global m  # 함수 밖의 전역변수 m 사용
    for i in range(0, len(color)):
        tur.color(color[i])
        tur.circle(radius)
        m = m + 50
        t.goto(m + radius, 0)
    return tur


myTurtleMake(t, c, m, r)  # 함수 호출

turtle.mainloop()
turtle.bye()

# t.shape("turtle")
# t.color("red")
# t.circle(50)
#
# t.goto(50, 0)
# t.shape("turtle")
# t.color("green")
# t.circle(50)
#
# t.goto(100, 0)
# t.shape("turtle")
# t.color("blue")
# t.circle(50)
