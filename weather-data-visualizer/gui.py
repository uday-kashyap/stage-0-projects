from tkinter import *

class WeatherApp(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.title("Weather App - By Uday Kashyap")
        self.iconbitmap("weather.ico")
        self.feature_panel = Frame(self, bg="lightgrey", borderwidth=2, relief=SOLID, width=50)
        self.feature_panel.pack(side=LEFT, fill=Y) 
        self.info_panel = Frame(self, bg="white", borderwidth=2, relief=SOLID)
        self.info_panel.pack(fill=BOTH, expand=True)

if __name__ == '__main__':
    WeatherApp().mainloop()