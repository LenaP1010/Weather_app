from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderInsufficientPrivileges
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk


root=Tk()
root.title("Weather App")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")
root.resizable(False,False)



# Создание метки для отображения часового пояса
timezone_label = Label(root, text="", font=("Arial", 15), bg="#57adff")
timezone_label.pack(pady=20)

def getWeather():
    city = textfield.get()
    
    if not city:
        messagebox.showerror("Ошибка", "Пожалуйста, введите название города.")
        return

    try:
        geolocator = Nominatim(user_agent="weather.py", timeout=10)
        location = geolocator.geocode(city)
        
        if location is None:
            messagebox.showerror("Ошибка", "Город не найден. Попробуйте еще раз.")
            return

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        if not result:
            messagebox.showerror("Ошибка", "Не удалось определить часовой пояс.")
            return

        timezone_label.config(text=result)
        long_lat.config(text=f"{round(location.latitude,4)}°N, {round(location.longitude,4)}°E")

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)

        # Запрос погоды
        api_key = "5294e4d99e8548759f841234241611"  # Замените на свой ключ API
        api = f"http://api.weatherapi.com/v1/current.json?key={'5294e4d99e8548759f841234241611'}&q={city}"  # Исправленный запрос
        response = requests.get(api, timeout=10)

        # Проверка статуса ответа
        if response.status_code != 200:
            messagebox.showerror("Ошибка", f"Не удалось получить данные с API. Код состояния: {response.status_code}")
            return
        
        json_data = response.json()

        # Проверка наличия необходимых данных
        if 'current' in json_data:
            temp = json_data['current']['temp_c']  # Температура в Цельсиях
            humidity = json_data['current']['humidity']
            pressure = json_data['current']['pressure_mb']  # Давление в мбар
            wind = json_data['current']['wind_kph']  # Скорость ветра в км/ч
            

            # Обновление Labels с данными о погоде
            label_temp.config(text=f"Температура: {temp}°C")
            label_humidity.config(text=f"Влажность: {humidity}%")
            label_pressure.config(text=f"Давление: {pressure} мбар")
            label_wind.config(text=f"Скорость ветра: {wind} км/ч")
            label_description.config(text=f"Описание: {description}")
        else:
            messagebox.showerror("Ошибка", "Не удалось получить актуальные данные о погоде.")

    except GeocoderTimedOut:
        messagebox.showerror("Ошибка", "Время ожидания превышено. Попробуйте еще раз.")
    except GeocoderInsufficientPrivileges:
        messagebox.showerror("Ошибка", "Недостаточные привилегии для доступа к геокодеру.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

# Добавьте соответствующие Labels для отображения информации о погоде
label_temp = Label(root, font=('Helvetica', 11), fg="white", bg="#203243")
label_temp.place(x=50, y=120)

label_humidity = Label(root, font=('Helvetica', 11), fg="white", bg="#203243")
label_humidity.place(x=50, y=140)

label_pressure = Label(root, font=('Helvetica', 11), fg="white", bg="#203243")
label_pressure.place(x=50, y=160)

label_wind = Label(root, font=('Helvetica', 11), fg="white", bg="#203243")
label_wind.place(x=50, y=180)

label_description = Label(root, font=('Helvetica', 11), fg="white", bg="#203243")
label_description.place(x=50, y=200)

#Label
label1=Label(root,text="Температура",font=('Helvetica',11),fg="white",bg="#203243")
label1.place(x=50,y=120)

label2=Label(root,text="Влажность",font=('Helvetica',11),fg="white",bg="#203243")
label2.place(x=50,y=140)

label3=Label(root,text="Давление",font=('Helvetica',11),fg="white",bg="#203243")
label3.place(x=50,y=160)

label4=Label(root,text="Скорость ветра",font=('Helvetica',11),fg="white",bg="#203243")
label4.place(x=50,y=180)

label5=Label(root,text="Описание",font=('Helvetica',11),fg="white",bg="#203243")
label5.place(x=50,y=200)


##search box
Search_image=PhotoImage(file="images/Rounded Rectangle 3.png")
myimage=Label(image=Search_image,bg="#57adff")
myimage.place(x=270,y=120)

weat_image=PhotoImage(file="images/Layer 7.png")
weatherimage=Label(root,image=weat_image,bg="#203243")
weatherimage.place(x=290,y=127)

textfield=tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'), bg="#203243", border=0, fg="white")
textfield.place(x=370,y=130)
textfield.focus()

Search_icon=PhotoImage(file="images/Layer 6.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=getWeather)
myimage_icon.place(x=645,y=125)



##Bottom box
frame=Frame(root,width=900,height=180,bg="#212120")
frame.pack(side=BOTTOM)

#bottom boxes
firstbox=PhotoImage(file="images/Rounded Rectangle 2.png")
secondbox=PhotoImage(file="images/Rounded Rectangle 2 copy.png")

Label(frame,image=firstbox,bg="#1e1112").place(x=30,y=20)
Label(frame,image=secondbox,bg="#003153").place(x=300,y=30)
Label(frame,image=secondbox,bg="#003153").place(x=400,y=30)
Label(frame,image=secondbox,bg="#003153").place(x=500,y=30)
Label(frame,image=secondbox,bg="#003153").place(x=600,y=30)
Label(frame,image=secondbox,bg="#003153").place(x=700,y=30)
Label(frame,image=secondbox,bg="#003153").place(x=800,y=30)


#clock (here we will place time)
clock=Label(root,font=("Helvetica",30,'bold'),fg="white",bg="#57adff")
clock.place(x=30,y=20)


#timezone
long_lat=Label(root,font=("Helvetica",20,'bold'),fg="white",bg="#57adff")
long_lat.place(x=700,y=20)



long_lat=Label(root,font=("Helvetica",10),fg="white",bg="#57adff")
long_lat.place(x=700,y=50)


























root.mainloop()
