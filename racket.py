# 3
from tkinter import *
from ball import *
from court import *

class Racket :
    def __init__ (self, court, x, y, img, w = 53, h = 121) :
        self.canvas = court.canvas
        self.img = PhotoImage(file = img)
        self.rocket = self.canvas.create_image(x, y, image = self.img)
        self.x = x
        self.y = y
        self.x_start = x
        self.y_start = y
        self.width = w
        self.height = h
        self.speed = 25

    # 라켓 위치 초기화 메소드
    def start_position(self) :
        self.x = self.x_start
        self.y = self.y_start
        self.canvas.coords(self.rocket, self.x, self.y)

    # 라켓 위로 이동 메소드
    def move_up(self, event) :      
        self.y -= self.speed
        self.canvas.coords(self.rocket, self.x, self.y)

    # 라켓 아래로 이동 메소드
    def move_down(self, event) :
        self.y += self.speed
        self.canvas.coords(self.rocket, self.x, self.y)

    # 충돌 감지 메소드
    def dectect_collision(self, ball) :

        # 라켓 변수 
        left, top = self.x, self.y
        right, bottom = left + self.width, top + self.height

        # 충돌 감지
        if ball.y2 > top and ball.y1 < bottom and ball.x2 > left and ball.x1 < right :
            # 오른쪽에 충돌
            if left < ball.x2 and (ball.y2 > top or ball.y1 < bottom) :
                # 튀는 각도 랜덤
                ball.x1 -= randint(0, 10)
                # 공 왼쪽으로 이동
                ball.x_speed *= -1
            # 왼쪽에 충돌
            if right > ball.x1 and (bottom > ball.y1 or top < ball.y2) :
                # 튀는 각도 랜덤
                ball.x1 += randint(0, 10)
