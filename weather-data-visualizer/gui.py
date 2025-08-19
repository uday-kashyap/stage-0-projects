import io
import sys
from tkinter import *
from PIL import Image, ImageTk
from weather_utils import Weather, Forecast
from utils.config import get_api_key

class WeatherApp(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.resizable(False, False)
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
        self.info_layout = Frame(self.info_panel, bg="SystemButtonFace", relief=SUNKEN, borderwidth=2)
        self.info_layout.pack(fill=BOTH, expand=True, padx= 10, pady=10)

    def load_feature_icons(self):
        weather_img = Image.open("weather_feature.png").resize((40,40), Image.LANCZOS)
        self.weather_icon = ImageTk.PhotoImage(weather_img)
        self.weather_button = Button(self.feature_panel, image=self.weather_icon, command=lambda: self.set_mode("Weather"))
        self.weather_button.pack(side=TOP, fill=Y, pady=5, padx=3)
        plot_img = Image.open("plot_feature.png").resize((35,35), Image.LANCZOS)
        self.plot_icon = ImageTk.PhotoImage(plot_img)
        self.plot_button = Button(self.feature_panel, image=self.plot_icon, command=lambda: self.set_mode("Forecast"))
        self.plot_button.pack(side=TOP, fill=Y, padx=3)

    def set_mode(self, mode: str):
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

    def weather_info_ui(self, status: str, error_message=None):

        def customize_temperature_font(temp_val, row_pos, col_pos=1):
            if temp_val>=30:
                Label(self.info_layout, text=f"{temp_val}°C", font="lucida 10 bold", fg="red").grid(row=row_pos, column=col_pos)
            elif temp_val>25:
                Label(self.info_layout, text=f"{temp_val}°C", font="lucida 10 bold", fg="orange").grid(row=row_pos, column=col_pos)
            elif temp_val<=7:
                Label(self.info_layout, text=f"{temp_val}°C", font="lucida 10 bold", fg="blue").grid(row=row_pos, column=col_pos)
            else:
                Label(self.info_layout, text=f"{temp_val}°C", font="lucida 10 bold", fg="#524309").grid(row=row_pos, column=col_pos)

        if status == "Success":

            # Set and display the information in UI
            Label(self.info_layout, text=f"Current Weather:", font="lucida 10 bold").grid(row=0, column=0, sticky="w")
            customize_temperature_font(self.temperature, row_pos=0)
            Label(self.info_layout, text=f"Condition:", font="lucida 10 bold").grid(row=1, column=0, sticky="w")
            Label(self.info_layout, text=f"{self.condition}", font="agencyfb 10 bold").grid(row=1,column=1)
            Label(self.info_layout, text=f"Feels Like:", font="lucida 10 bold").grid(row=2, column=0, sticky="w")
            customize_temperature_font(self.feels_like, row_pos=2)
            Label(self.info_layout, text=f"Humidity:", font="lucida 10 bold").grid(row=3, column=0, sticky="w")
            Label(self.info_layout, text=f"{self.humidity}%", font="agencyfb 10 bold").grid(row=3, column=1)

        else:
            error_message = Label(self.info_layout, text=error_message)
            error_message.pack()


    def forecast_info_ui(self):
        pass

    def get_info(self):

        # Clear previous content
        for widget in self.info_layout.winfo_children():
            widget.destroy()

        API_KEY = get_api_key()

        # Error handling on GUI logic
        buffer = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = buffer

        try:
            if self.active_mode == "Weather":

                # Fetch the weather data
                weather = Weather(API_KEY)
                weather_data = weather.get_weather(self.city_name.get())

                if weather_data:
                    self.city = weather_data[0]
                    self.country_code = weather_data[1]
                    self.temperature = weather_data[2]
                    self.condition = weather_data[3]
                    self.feels_like = weather_data[4]
                    self.humidity = weather_data[5]
                    self.weather_info_ui(status="Success")
                else:
                    self.weather_info_ui(status="Error", error_message=buffer.getvalue().strip())
            else:
                #TODO: forecast plotting logic
                pass

        # Restore real stdout
        finally:
            sys.stdout = sys_stdout

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