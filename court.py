from tkinter import *

class Court :

    def __init__(self, window, width, height, img) :

        # 캔버스 생성
        self.canvas = Canvas(window, width = width, height = height)

	# 경기장 이미지 생성
        self.img = PhotoImage(file = img)
        self.canvas.create_image(width/2, height/2, image = self.img)

 	# 경기장의 가로, 세로 길이 초기화
        self.width = width
        self.height = height
        
	# 캔버스 배치
        self.canvas.pack()

 	# 글꼴 속성 저장
        my_font = ("consolas", 50)

	# 텍스트 생성
        self.board = self.canvas.create_text(width/2, 65, font = my_font, fill = "white")
        
    # 점수 표시 메소드
    def draw_score(self, score1, score2) :

	# 점수를 문자열로 저장
        scores = str(score1) + " : " + str(score2)

        # 점수 변경
        self.canvas.itemconfigure(self.board, text = scores)
