import keyboard
import tkinter as tk
import os
from PIL import ImageTk, Image

class tkinterWindow(tk.Tk):
    def __init__(self, auto_unfocus=True):
        tk.Tk.__init__(self)
        self.path = os.path.dirname(os.path.abspath(__file__))
        # self.iconphoto(False, tk.PhotoImage(file=f'{self.path[:-17]}/Ressources/jarvis_icon.png'))
        self.x, self.y = 1065, 240
        self.length, self.height = 200, 200
        self.auto_unfocus = auto_unfocus
        self.title("Jarvis")
        self.configure(bg="grey1")
        image = tk.PhotoImage(file=f'{self.path[:-17]}/Ressources/jarvis_icon.png').subsample(30, 30)
        label = tk.Label(self, image=image, bd=0)
        label.image = image
        label.place(x=10, y=10)
        # self.buttons = [tkinterButton(self, i) for i in range(5)]
        # self.labels = [tkinterLabel(self, i) for i in range(2)]
        # self.scales = [tkinterScale(self, i) for i in range(1)]
        # self.canvas = [tkinterCanvas(self, i) for i in range(2)]
        # self.entrys = [tkinterEntry(self, i) for i in range(1)]
        # self.objects = [self.buttons, self.labels, self.scales, self.canvas, self.entrys]
        self.geometry("{}x{}+{}+{}".format(str(self.length), str(self.height), str(self.x), str(self.y)))
        self.bind('<Button-3>', self.menu)
        self.bind('<ButtonPress-1>', self.start_move)
        self.bind('<ButtonRelease-1>', self.stop_move)
        if self.auto_unfocus: self.bind('<ButtonRelease>', self.unfocus)
        self.bind("<B1-Motion>", self.drag)
        self.attributes('-alpha',0.7)
        self.overrideredirect(True)
        self.resizable(width=True, height=True)
        self.refresh()

    def refresh(self):
        self.attributes("-topmost", True)
        self.update()

    def menu(self, event):
        print('menu')

    def unfocus(self, event):
        keyboard.press('alt')
        keyboard.press('tab')
        keyboard.release('alt')
        keyboard.release('tab')

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None
        if self.auto_unfocus: self.unfocus('event')

    def drag(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

# def main():
#     app = tkinterWindow(auto_unfocus=False)
#     while not keyboard.is_pressed('ctrl+maj+c'):
#         try: app.refresh()
#         except: break
#     try: app.destroy()
#     except: pass
#
# main()
