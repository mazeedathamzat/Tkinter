import tkinter as tk

class PongGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PONG GAME by PythonGeeks")
        self.root.geometry("600x400")
        self.root.configure(bg="yellow")

        self.left_paddle = tk.Canvas(self.root, width=10, height=70, bg="red")
        self.left_paddle.place(x=10, y=165)

        self.right_paddle = tk.Canvas(self.root, width=10, height=70, bg="white")
        self.right_paddle.place(x=580, y=165)

        self.ball = tk.Canvas(self.root, width=10, height=10, bg="green")
        self.ball.place(x=295, y=195)

        self.ball_direction_x = 2
        self.ball_direction_y = 2

        self.root.bind("<KeyPress-w>", self.left_paddle_up)
        self.root.bind("<KeyPress-s>", self.left_paddle_down)
        self.root.bind("<KeyPress-Up>", self.right_paddle_up)
        self.root.bind("<KeyPress-Down>", self.right_paddle_down)

        self.game_loop()

    def left_paddle_up(self, event):
        self.left_paddle.move(0, -20)

    def left_paddle_down(self, event):
        self.left_paddle.move(0, 20)

    def right_paddle_up(self, event):
        self.right_paddle.move(0, -20)

    def right_paddle_down(self, event):
        self.right_paddle.move(0, 20)

    def game_loop(self):
        while True:
            self.ball.move(self.ball_direction_x, self.ball_direction_y)
            self.root.update()

            ball_pos = self.ball.coords(self.ball)
            if ball_pos[1] <= 0 or ball_pos[3] >= 400:
                self.ball_direction_y *= -1

            if ball_pos[0] <= 0 or ball_pos[2] >= 600:
                self.ball_direction_x *= -1

            self.root.after(10)  # Add a delay to control game speed

    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
        game = PongGame()
        game.run()