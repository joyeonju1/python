# 2

from tkinter import *
from random import *

class Ball :
    def __init__ (self, court, x1, y1, x2, y2) :
        # 공의 시작 좌표 초기화
        self.x1 = x1                            
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
        self.x1_start = x1 
        self.y1_start = y1
        self.x2_start = x2
        self.y2_start = y2

        # 공의 이동 거리 초기화
        self.x_speed = 10
        self.y_speed = 10
	
	# 공의 가로, 세로 길이 초기화
        self.width = x2 - x1
        self.height = y2 - y1

	# Court 클래스 객체 저장
        self.court = court

	# Court 클래스의 캔버스 저장
        self.canvas = court.canvas

	# 캔버스에 공 생성
        self.ball = self.canvas.create_oval(x1, y1, x2, y2, fill = "yellow")
        
        
    # 공 움직이기 메소드
    def move_ball(self) :
        
        
        # 위쪽 벽 충돌하면 방향 바꾸기
        if self.y1 <= 5 :
            self.y1 = 5
            self.y_speed *= -1

        # 아래쪽 벽 충돌하면 방향 바꾸기
        if self.y1 >= (self.court.height - (self.height - 5)) :
            self.y1 = self.court.height - (self.height - 5)
            self.y_speed *= -1
        
        # 공 이동 좌표 저장
	# x_speed만큼 x 좌표 변경 – 양수 : 오른쪽, 음수 : 왼쪽
        self.x1 += self.x_speed
	# y_speed만큼 y 좌표 변경 – 양수 : 아래쪽, 음수 : 위쪽
        self.y1 += self.y_speed
        self.x2 = self.x1 + self.width
        self.y2 = self.y1 + self.height
        
        # 공 위치 변경
        self.canvas.coords(self.ball, self.x1, self.y1, self.x2, self.y2)

    # 공 멈추기 메소드  
    def stop_ball(self) :
        self.x_speed = 0
        self.y_speed = 0

    # 공 다시 움직이기 메소드
    def start_ball(self) :

        # 공 시작 방향
        if randint(0, 1) :
            self.x_speed = 10
        else :
            self.x_speed = -10

        if randint(0, 1) :
            self.y_speed = 10
        else :
            self.y_speed = -10
            
        self.x1 = self.x1_start
        self.x2 = self.x2_start
        self.y1 = self.y1_start
        self.y2 = self.y2_start
        
        self.canvas.coords(self.ball, self.x1, self.y1, self.x2, self.y2)
