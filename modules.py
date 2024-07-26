# This library was made by https://github.com/561fffDemon

from pystyle import Colorate
import shutil

class Drawer():
    def __init__(self):
        pass
    def rgbGrad(self,colors, steps=10):
        gradient = []
        num_colors = len(colors)

        steps_per_color = steps // (num_colors - 1)

        for i in range(num_colors - 1):
            rgb1 = colors[i]
            rgb2 = colors[i + 1]

            r_diff = (rgb2[0] - rgb1[0]) / steps_per_color
            g_diff = (rgb2[1] - rgb1[1]) / steps_per_color
            b_diff = (rgb2[2] - rgb1[2]) / steps_per_color

            for j in range(steps_per_color):
                r = int(rgb1[0] + (r_diff * j))
                g = int(rgb1[1] + (g_diff * j))
                b = int(rgb1[2] + (b_diff * j))
                gradient.append(f"{r};{g};{b}")
                # print(r,g,b)

        gradient.append(f"{colors[-1][0]};{colors[-1][1]};{colors[-1][2]}")

        return gradient

    def CenterColor(self,colors,steps,text,type):
        centered = ""
        txt = self.gradientText(colors,steps,text,type)
        spaces = 0
        string = text.split("\n")[0].center(shutil.get_terminal_size().columns)
        for i in string:
            if i == " ":
                spaces += 1
            else:
                break
        for i in txt.split("\n"):
            centered += (" " * spaces) + i + "\n"
        return centered
    
    def type_effect(self,text,sleep):
        from time import sleep as sl
        import sys

        for letter in text:
            print(letter, end='')
            sys.stdout.flush()
            sl(sleep)

    def Center(self,s):
        centered = ""
        for i in s.split("\n"):
            centered += i.center(shutil.get_terminal_size().columns) + "\n"
        print(centered,end="")

    def gradientText(self,colors,steps,text,type):
        gradient = self.rgbGrad(colors,steps)
        types = {
            "V": Colorate.Vertical,
            "H": Colorate.Horizontal,
            "D": Colorate.Diagonal,
            "DB": Colorate.DiagonalBackwards
        }

        if types.get(type):
            return types[type](gradient, text)
        else:
            return f"{types['V'](gradient, 'Incorrect type, Type can be V - Vertical & H - Horizontal', 1)}"
        
    def converting(self,dist):
        new = []
        for i in dist:
            new.append([i[0],i[1],i[2]])
        return new