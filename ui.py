# requests library to contact with backend api
import tkinter as tk
import requests
from PIL import Image, ImageTk  # pip install pillow
from PIL.Image import Resampling
# key = 1be6b0270a7c38e83aa51db5a32459f6

root = tk.Tk()
root.title("Global Weather Monitor")
root.geometry("600x500")

def format_response(weather):
    try:
        city = weather['name']
        condition = weather['weather'][0]['description']
        temperature = weather['main']['temp']
        final_str = 'City:%s\nCondition:%s\nTemperature:%s'%(city, condition, temperature)
    except:
        final_str = "problem retrieving information"
    return  final_str

def get_weather(city):
    key = '1be6b0270a7c38e83aa51db5a32459f6'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params)
    # print(response.json())
    weather = response.json()
    result['text'] = format_response(weather)
    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)


def open_image(icon):
    size = int(frame_two.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete('all')
    weather_icon.create_image(0, 0, anchor='nw', image=img)
    weather_icon.image = img


img = Image.open('bg.jpg')
img = img.resize((600, 500), Resampling.LANCZOS)
img_photo = ImageTk.PhotoImage(img)
bg_lbl = tk.Label(root, image=img_photo)
bg_lbl.place(x=0, y=0, width=600, height=500)


frame_one = tk.Frame(bg_lbl, bg="#42c2f4", bd=5)
frame_one.place(x=80, y=60, width=450, height=50)

txt_box = tk.Entry(frame_one, font=('times new roman', 25), width=17)
txt_box.grid(row=0, column=0, sticky='w')

btn = tk.Button(frame_one, text='get weather', fg='green', font=('times new roman', 16, 'bold'), command=lambda: get_weather(txt_box.get()))
btn.grid(row=0, column=1, padx=20)

frame_two = tk.Frame(bg_lbl, bg="sky blue", bd=5)
frame_two.place(x=80, y=130, width=450, height=300)

result = tk.Label(frame_two, font=40, bg='white', justify='left', anchor='nw')
result.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(result, bg='white', bd=0)
weather_icon.place(relx=0.75, rely=0, relwidth=1, relheight=0.5)

root.mainloop()