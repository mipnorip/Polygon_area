from main import main as parser
from tkinter import *

class Gui():
    def __init__(self) -> None:
        self.result = True
        self.root = Tk()
        self.root.title("Рисование многоугольников")
        self.root.resizable(width=False, height=False)
        self.root['bg'] = 'white'
        self.canvas = Canvas(master=self.root, width=500, height=500, bg='white')
        self.button = Button(text='Ось координат', width=10, height=3, command=self.lines)
        self.button.grid_location(40, 50)
        self.button.pack()
        self.convert()
        self.lines()
        #self.draw()
        self.canvas.pack()
        mainloop()

    def convert(self) -> None:
        self.N, data, self.S = parser()
        self.data = []
        plus = 250

        for i in data:
            self.data.append([int(i[0])*10 + plus, 500 - int(i[1])*10 - plus])

    def lines(self) -> None:
        self.canvas.create_rectangle(0,0,501,501, fill='white', outline='white')
        if self.result:
            self.canvas.create_line(250,0,250,500,fill='white') # Линия координат x
            self.canvas.create_line(0,250,500,250,fill='white') # Линия координат y
        else:
            self.canvas.create_line(250,0,250,500,fill='black') # Линия координат x
            self.canvas.create_line(0,250,500,250,fill='black') # Линия координат y
        self.result = not self.result
        self.draw()

        """
        for i in range(500)[10::20]:
            if i != 250:
                self.canvas.create_text(255,i , text=f'{250-i}', fill='black', anchor=W, font=("Purisa", 8))

        for i in range(500)[::30]:
            if i != 250:
                self.canvas.create_text(i,255, text=f'{i-250}', fill='black', anchor=N, font=("Purisa", 8))
        """

    def draw(self) -> None:
        for i in range(self.N - 1):
            self.canvas.create_line(self.data[i][0],self.data[i][1],self.data[i+1][0],self.data[i+1][1], fill='green')
            self.canvas.create_text(self.data[i][0],self.data[i][1] - 8, text=i+1, fill='gray')   
            if i == self.N-2:
                self.canvas.create_line(self.data[self.N-1][0], self.data[self.N-1][1], self.data[0][0], self.data[0][1], fill='green')   
                self.canvas.create_text(self.data[self.N-1][0], self.data[self.N-1][1] - 8, text=i+2, fill='gray')    

            #self.canvas.create_text(self.data[i][0], 260, text=f'{i}')
            #self.canvas.create_text(255, self.data[i][1], text=f'{i}')
        ble = 480
        l = 0
        for i in reversed(range(self.N)):
            self.canvas.create_text(500, ble, text=f"{self.N - l} : {(self.data[i][0] - 250) // 5 ,(self.data[i][1] - 250) // -5}", anchor=SE)
            ble -= 20
            l += 1

        self.canvas.create_text(500, 500, text=f"S = {self.S}",
              anchor=SE, fill="black")

Gui()