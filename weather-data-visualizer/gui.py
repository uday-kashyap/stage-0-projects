from tkinter import *
from PIL import Image, ImageTk

class WeatherApp(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.title("Weather App - By Uday Kashyap")
        self.iconbitmap("weather.ico")
        self.active_mode = "Weather"
        self.load_panels()
        self.display_searchbox()
        self.load_feature_icons()
        self.feature_ui()

    def load_panels(self):
        self.feature_panel = Frame(self, bg="lightgrey", borderwidth=2, relief=SOLID, width=50)
        self.feature_panel.pack(side=LEFT, fill=Y)
        self.feature_panel.pack_propagate(False)
        self.info_panel = Frame(self, bg="white", borderwidth=2, relief=SOLID)
        self.info_panel.pack(fill=BOTH, expand=True)
        self.searchbox_panel = Frame(self.info_panel, bg="white")
        self.searchbox_panel.pack(side=TOP)

    def load_feature_icons(self):
        weather_img = Image.open("weather_feature.png").resize((40,40), Image.LANCZOS)
        self.weather_icon = ImageTk.PhotoImage(weather_img)
        self.weather_button = Button(self.feature_panel, image=self.weather_icon, command=lambda: self.set_mode("Weather"))
        self.weather_button.pack(side=TOP, fill=Y, pady=5, padx=3)
        plot_img = Image.open("plot_feature.png").resize((35,35), Image.LANCZOS)
        self.plot_icon = ImageTk.PhotoImage(plot_img)
        self.plot_button = Button(self.feature_panel, image=self.plot_icon, command=lambda: self.set_mode("Forecast"))
        self.plot_button.pack(side=TOP, fill=Y, padx=3)

    def set_mode(self, mode):
        self.active_mode = mode
        self.search_button.config(text=f"Get {self.active_mode}")
        self.feature_ui()
        
    def feature_ui(self):
        if self.active_mode == "Weather":
            self.weather_button.config(bg="white")
            self.plot_button.config(bg="SystemButtonFace")
        else:
            self.weather_button.config(bg="SystemButtonFace")
            self.plot_button.config(bg="white")


    def get_info(self):
        # TODO: weather and forecast displaying logic
        pass

    def display_searchbox(self):

        def clear_placeholder(event):
            if self.city_name.get() == "Search for your city":
                self.city_searchbox.delete(0, END)

        self.city_name = StringVar()
        self.city_name.set("Search for your city")
        self.city_searchbox = Entry(self.searchbox_panel, textvariable=self.city_name, borderwidth=2, relief=SOLID)
        self.city_searchbox.pack(side=LEFT, pady=5, ipady=2)
        self.city_searchbox.bind("<Button-1>", clear_placeholder)
        self.search_button = Button(self.searchbox_panel, text= f"Get {self.active_mode}", command=self.get_info)
        self.search_button.pack(side=LEFT, padx=3)



if __name__ == '__main__':
    WeatherApp().mainloop()