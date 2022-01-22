#!/usr/bin/python

import tkinter as tk
from tkinter import PhotoImage, font
import requests

HEIGHT = 550
WIDTH = 750


def test_function(entry):
    print("This is the entry: ", entry)


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        wind = weather['wind']['speed']
        deg = weather['wind']['deg']
        lon = weather['coord']['lon']
        lat = weather['coord']['lat']
        humidity = weather['main']['humidity']
        clouds = weather['clouds']['all']
        pressure = weather['main']['pressure']

        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s \nWind: %s \nWind Degrees: %s \nLongitude: %s \nLatitude: %s \nHumidity: %s \nClouds: %s \nPressure: %s' % (name, desc, temp, wind, deg, lon, lat, humidity, clouds, pressure)
    except:
    	final_str = 'There was a problem \nretrieving \nthat information!'

    return final_str


def get_weather(city):
    weather_key = '09d6460ea31397c2967253b2d5a849fe'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


root = tk.Tk()
root.title('Meteo pod Bogiem')
#photo = iconbitmap(file = "ben.ico")
#root.iconphoto(False, photo)


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# background_image = tk.PhotoImage(file='drzewiec.png')
# background_label = tk.Label(root, image=background_image)
background_label = tk.Label(root, bg="#a17e41")
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#a17e41", bd=5)
frame.place(relx=0.5, rely=0.055, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40, bg="#000000", fg="#a17e41", insertbackground='white')
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="City/Weather", font=40, bg='#000000', fg="#a17e41", 
	activebackground="#a17e41", activeforeground='#cccccc', command=lambda:  get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#a17e41", bd=10)
lower_frame.place(relx=0.5, rely=0.20, relwidth=0.9, relheight=0.75, anchor='n')


label = tk.Label(lower_frame, font=('ITC Avant Garde Gothic Pro', 20), bg='#000000', fg="#a17e41")
label.place(relwidth=1, relheight=1)


root.resizable(False, False)
root.mainloop()
