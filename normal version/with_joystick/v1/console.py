import keyboard
import tkinter as tk
from PIL import ImageTk, Image
import time
import os


"""!! In Menu class from tkinter, add this line in unpost function : if hasattr(self.master, 'unfocus_allowed'): self.master.unfocus_allowed = True"""

class Tkinter_window(tk.Tk):
    def __init__(self, auto_unfocus=True):
        tk.Tk.__init__(self)
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.auto_unfocus = auto_unfocus
        self.title("Jarvis")
        self.x, self.y = 1065, 240
        self.length, self.height = 200, 200
        self.bg_opacity = 0.7
        self.geometry("{}x{}+{}+{}".format(str(self.length), str(self.height), str(self.x), str(self.y)))
        self.bg, self.fg = 'grey1', 'white'
        self.configure(bg=self.bg)
        self.image = tk.PhotoImage(file=f'{self.path[:-17]}/Ressources/jarvis_icon.png').subsample(30, 30)
        icon = tk.Label(self, image=self.image, bd=0)
        icon.image = self.image
        icon.place(x=10, y=10)
        self.labels_counter = -1
        self.title = Tkinter_label(self, 'Jarvis Console', x=50, y=26, fg='dodger blue', bold=True, size=11)
        self.labels = []
        self.important_messages = []
        self.define_menu()
        self.hidden, self.dragged, self.unfocus_allowed, self.last_loop_state = False, False, True, False

        self.bind('<Button-3>', self.popup_menu)
        self.bind('<ButtonPress-1>', self.press_click)
        self.bind('<ButtonRelease-1>', self.release_click)
        if self.auto_unfocus: self.bind('<ButtonRelease>', self.unfocus)
        self.bind("<B1-Motion>", self.drag)
        self.bind('<Control_L>C', self.kill_jarvis)
        self.bind('<Delete>', self.kill_jarvis)
        self.bind('<Control_L>A', self.add_label)
        self.attributes('-alpha', self.bg_opacity)
        self.overrideredirect(True)
        self.resizable(width=True, height=True)
        self.refresh()

    def refresh(self):
        # try:
        if keyboard.is_pressed('ctrl+maj+h'):
            if self.last_loop_state == None:
                self.hide_unhide()
                self.last_loop_state = 'hidden'
        else: self.last_loop_state = None

        self.attributes("-topmost", True)
        self.update()
        # except:  pass

    def define_menu(self):
        self.menu = tk.Menu(self, tearoff=0)
        self.menu.add_command(label='Hide', command=self.hide_unhide)
        self.menu.add_command(label='Clear', command=self.clear)
        self.menu.add_command(label='Change color', command=self.change_color)
        self.menu.add_command(label='Change opacity', command=self.change_opacity)
        self.menu.add_command(label='Kill Jarvis', command=self.kill_jarvis)

    def popup_menu(self, event):
        self.unfocus_allowed = False
        self.menu.post(event.x_root, event.y_root)

    def hide_unhide(self, *args):
        self.unfocus_allowed = True
        if self.hidden:
            self.x, self.y, self.height, self.hidden = self.winfo_x() - 175, self.winfo_y(), self.height + 150, False
            self.menu.entryconfigure(0, label="Hide")
        else:
            self.x, self.y, self.height, self.hidden = 1240, self.winfo_y(), self.height - 150, True
            self.menu.entryconfigure(0, label="Unhide")
        self.geometry("{}x{}+{}+{}".format(str(self.length), str(self.height), str(self.x), str(self.y)))

    def unfocus(self, *args):
        if self.unfocus_allowed:
            keyboard.press('alt')
            keyboard.press('tab')
            keyboard.release('alt')
            keyboard.release('tab')

    def press_click(self, event):
        self.x = event.x
        self.y = event.y

    def release_click(self, event):
        if self.hidden and not self.dragged:
            self.hide_unhide()
        else: self.x, self.y = self.winfo_x(), self.winfo_y()
        self.dragged = False
        self.geometry("{}x{}+{}+{}".format(str(self.length), str(self.height), str(self.x), str(self.y)))
        if self.auto_unfocus: self.unfocus('event')

    def drag(self, event):
        self.dragged = True
        deltay = event.y - self.y
        y = self.winfo_y() + deltay
        if not self.hidden:
            deltax = event.x - self.x
            x = self.winfo_x() + deltax
        else:
            x = self.winfo_x()
        self.geometry(f"+{x}+{y}")

    def add_label(self, *args, text='test', type='normal'):
        if type == 'error': color = 'red'
        elif type == 'warning': color = 'orange'
        elif type == 'arduino': color = 'dodger blue'
        else: color = self.fg
        if self.labels_counter <= 7:
            if len(text)<27: self.labels.append(Tkinter_label(self, text, fg=color, type=type))
            else:
                self.labels.append(Tkinter_label(self, text[:27], fg=color, type=type))
                self.labels.append(Tkinter_label(self, text[27:], fg=color, type=type))
        else:
            cut = self.labels[0]
            if cut['bg'] == 'red' or cut['bg'] == 'orange': self.important_messages.append(cut['text'])
            cut.destroy()
            self.labels.pop(0)
            self.labels_counter -= 1
            for label in self.labels :
                label.y = label.y-18
                label.place(x=label.x, y=label.y)
            self.labels.append(Tkinter_label(self, text, fg=color, type=type))

        self.refresh()

    def clear(self):
        self.unfocus_allowed = True
        n = len(self.labels)
        for i in range(n):
            self.labels[0].destroy()
            self.labels.pop(0)
        self.labels_counter = 0

    def change_color(self):
        Tkinter_scale(self, type='color')

    def change_opacity(self):
        Tkinter_scale(self, type='opacity')

    def kill_jarvis(self, *args):
        self.destroy()
        print('Jarvis died :(')
        os._exit(0)

    def kill_console(self, *args):
        try: self.destroy()
        except: pass


class Tkinter_label(tk.Label):
    def __init__(self, app, text, x=10, y=45, fg=None, bg=None, size=10, bold=False, type='normal'):
        tk.Label.__init__(self, app)
        self.app = app
        self.type = type
        if bg == None: bg = self.app.bg
        if fg == None: fg = self.app.fg
        if bold: bold='bold'
        elif not bold: bold=''
        self.x, self.y = x, y+18*self.app.labels_counter
        self.fg, self.bg, self.text = fg, bg, text
        self.config(text=self.text, fg=self.fg, bg=self.bg, font=f'monospace {size} {bold}')
        self.place(x=self.x, y=self.y)
        self.app.labels_counter += 1


class Tkinter_scale(tk.Scale):
    def __init__(self, app, type):
        tk.Scale.__init__(self, app)
        self.app = app
        bg_num = int(''.join([i for i in list(self.app.bg) if i.isdigit()]))
        fg = 'grey'+str(int(100-bg_num))
        if type == 'color':
            self.set(bg_num)
            command = self.send_color_value
        elif type == 'opacity':
            self.set(self.app.bg_opacity*100)
            command = self.send_opacity_value
        self.config(orient='horizontal', from_=0,  to=99, cursor='hand2', font='monospace 10',
                    resolution=2, length=185,
                    bg=self.app.bg, fg=fg, troughcolor=self.app.bg, command=command)
        self.bind('<ButtonRelease-1>', self.kill)
        self.app.unbind('<ButtonRelease-1>')
        self.app.unbind('<ButtonPress-1>')
        self.app.unbind("<B1-Motion>")
        self.app.unfocus_allowed = False
        self.place(x=5, y=150)

    def send_color_value(self, value):
        value = int(value)
        self.app.bg = f'grey{value}'
        self.app.configure(bg=self.app.bg)
        self.app.title.config(bg=self.app.bg)
        bg_num = int(''.join([i for i in list(self.app.bg) if i.isdigit()]))
        self.app.fg = 'grey'+str(int(100-bg_num))
        self.config(bg=self.app.bg, fg=self.app.fg, troughcolor=self.app.bg)
        for label in self.app.labels:
            label.config(bg=self.app.bg)
            if label.type == 'normal': label.config(fg=self.app.fg)

    def send_opacity_value(self, value):
        self.app.bg_opacity = int(value)/100
        self.app.attributes('-alpha', self.app.bg_opacity)

    def kill(self, event):
        self.app.bind('<ButtonPress-1>', self.app.press_click)
        self.app.bind('<ButtonRelease-1>', self.app.release_click)
        self.app.bind("<B1-Motion>", self.app.drag)
        self.app.unfocus_allowed = True
        if self.app.auto_unfocus: self.app.unfocus()
        self.destroy()
