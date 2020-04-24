from tkinter import *
from datetime import datetime
from pytz import timezone
import requests, json


def binclock():
    curr_time = datetime.now()
    local['text'] = curr_time.strftime('%a  %b %m, %Y')

    # global hour1, hour2, minute1, minute2, sec1, sec2
    # coverts each digit in current time to a binary string representation with leading zeros
    hour1 = str(bin(int(str(curr_time.hour).zfill(2)[0]))[2:]).zfill(2)
    hour2 = str(bin(int(str(curr_time.hour).zfill(2)[1]))[2:]).zfill(4)
    minute1 = str(bin(int(str(curr_time.minute).zfill(2)[0]))[2:]).zfill(3)
    minute2 = str(bin(int(str(curr_time.minute).zfill(2)[1]))[2:]).zfill(4)
    sec1 = str(bin(int(str(curr_time.second).zfill(2)[0]))[2:]).zfill(3)
    sec2 = str(bin(int(str(curr_time.second).zfill(2)[1]))[2:]).zfill(4)

    on = 'white'
    off = 'gray'

    def seconds(sec1, sec2, on, off):
        if sec1[0] == '1':
            bc_canvas.itemconfig(secT1, fill=on)
        else:
            bc_canvas.itemconfig(secT1, fill=off)

        if sec1[1] == '1':
            bc_canvas.itemconfig(secT2, fill=on)
        else:
            bc_canvas.itemconfig(secT2, fill=off)

        if sec1[2] == '1':
            bc_canvas.itemconfig(secT3, fill=on)
        else:
            bc_canvas.itemconfig(secT3, fill=off)

        if sec2[0] == '1':
            bc_canvas.itemconfig(sec01, fill=on)
        else:
            bc_canvas.itemconfig(sec01, fill=off)

        if sec2[1] == '1':
            bc_canvas.itemconfig(sec02, fill=on)
        else:
            bc_canvas.itemconfig(sec02, fill=off)

        if sec2[2] == '1':
            bc_canvas.itemconfig(sec03, fill=on)
        else:
            bc_canvas.itemconfig(sec03, fill=off)

        if sec2[3] == '1':
            bc_canvas.itemconfig(sec04, fill=on)
        else:
            bc_canvas.itemconfig(sec04, fill=off)

    def minutes(minute1, minute2, on, off):

        if minute1[0] == '1':
            bc_canvas.itemconfig(minT1, fill=on)
        else:
            bc_canvas.itemconfig(minT1, fill=off)

        if minute1[1] == '1':
            bc_canvas.itemconfig(minT2, fill=on)
        else:
            bc_canvas.itemconfig(minT2, fill=off)

        if minute1[2] == '1':
            bc_canvas.itemconfig(minT3, fill=on)
        else:
            bc_canvas.itemconfig(minT3, fill=off)

        if minute2[0] == '1':
            bc_canvas.itemconfig(min01, fill=on)
        else:
            bc_canvas.itemconfig(min01, fill=off)

        if minute2[1] == '1':
            bc_canvas.itemconfig(min02, fill=on)
        else:
            bc_canvas.itemconfig(min02, fill=off)

        if minute2[2] == '1':
            bc_canvas.itemconfig(min03, fill=on)
        else:
            bc_canvas.itemconfig(min03, fill=off)

        if minute2[3] == '1':
            bc_canvas.itemconfig(min04, fill=on)
        else:
            bc_canvas.itemconfig(min04, fill=off)

    def hours(hour1, hour2, on, off):

        if hour1[0] == '1':
            bc_canvas.itemconfig(hrT1, fill=on)
        else:
            bc_canvas.itemconfig(hrT1, fill=off)

        if hour1[1] == '1':
            bc_canvas.itemconfig(hrT2, fill=on)
        else:
            bc_canvas.itemconfig(hrT2, fill=off)

        if hour2[0] == '1':
            bc_canvas.itemconfig(hr01, fill=on)
        else:
            bc_canvas.itemconfig(hr01, fill=off)
        if hour2[1] == '1':
            bc_canvas.itemconfig(hr02, fill=on)
        else:
            bc_canvas.itemconfig(hr02, fill=off)

        if hour2[2] == '1':
            bc_canvas.itemconfig(hr03, fill=on)
        else:
            bc_canvas.itemconfig(hr03, fill=off)

        if hour2[3] == '1':
            bc_canvas.itemconfig(hr04, fill=on)
        else:
            bc_canvas.itemconfig(hr04, fill=off)

    seconds(sec1, sec2, on, off)
    minutes(minute1, minute2, on, off)
    hours(hour1, hour2, on, off)


def tzclock():
    utc_time = datetime.now(timezone('utc'))
    fmt = '%H:%M'

    zulu = utc_time.strftime(fmt)
    est = utc_time.astimezone(timezone('US/Eastern')).strftime(fmt)
    cst = utc_time.astimezone(timezone('US/Central')).strftime(fmt)
    mst = utc_time.astimezone(timezone('US/Mountain')).strftime(fmt)
    pst = utc_time.astimezone(timezone('US/Pacific')).strftime(fmt)
    ak = utc_time.astimezone(timezone('US/Alaska')).strftime(fmt)
    hawaii = utc_time.astimezone(timezone('US/Hawaii')).strftime(fmt)
    jp = utc_time.astimezone(timezone('Asia/Tokyo')).strftime(fmt)
    ger = utc_time.astimezone(timezone('Europe/Berlin')).strftime(fmt)
    bang = utc_time.astimezone(timezone('Asia/Bangkok')).strftime(fmt)
    syd = utc_time.astimezone(timezone('Australia/Sydney')).strftime(fmt)
    lond = utc_time.astimezone(timezone('Europe/London')).strftime(fmt)

    if 0 <= utc_time.second <= 29:
        tz_est['text'] = 'Eastern: ' + est
        tz_cst['text'] = 'Central: ' + cst
        tz_mst['text'] = 'Mountain: ' + mst
        tz_pst['text'] = 'Pacific: ' + pst
        tz_ak['text'] = 'Alaska: ' + ak
        tz_hi['text'] = 'Hawaii: ' + hawaii
        tz_title['text'] = '     U S Times     '
    else:
        tz_hi['text'] = 'UTC: ' + zulu
        tz_ak['text'] = 'London: ' + lond
        tz_pst['text'] = 'Berlin: ' + ger
        tz_mst['text'] = 'Bangkok: ' + bang
        tz_cst['text'] = 'Tokyo: ' + jp
        tz_est['text'] = 'Sydney: ' + syd
        tz_title['text'] = 'International Times'


def weather(curr_time):
    # # Enter your API key here
    # api_key = ""
    #
    # # base urls for Openweathermap.org
    # base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # forecast = "http://api.openweathermap.org/data/2.5/forecast?"
    #
    # cities = [('Laurel', 'Maryland'), ('Huntsville',  'Alabama'), ('Atlanta','Georgia'), ('Las Vegas',  'Nevada')]
    # city_res = {}
    #
    # forecast_url = forecast + "&q=" + cities[0][0] + "," + cities[0][1] + "&APPID=" + api_key
    #
    # def temp_con(temp):
    #     degree_sign = u"\N{DEGREE SIGN}"
    #     k_to_f = int(temp * 1.8 - 459.57) # converts Kelvin to Fahrenheit
    #     return str(k_to_f) + degree_sign
    #
    # # retrives the current weather of all locations in the cities list and saves the results to a dictionary
    # for location in cities:
    #     (city_name, state_name) = location
    #     complete_url = base_url + "&q=" + city_name + "," + state_name + "&APPID=" + api_key # constructs the required query url
    #     response = requests.get(complete_url)
    #     results = response.json()
    #
    #     if results["cod"] == 200:
    #         curr_weat = results["main"]
    #         curr_temp = temp_con(curr_weat["temp"])
    #         curr_hum = str(y["humidity"]) + '%'
    #         descr = results["weather"][0]["description"]
    #
    #     city_res[city_name] = curr_temp, curr_hum, descr
    #
    # five_day = requests.get(forecast_url)
    # fday_res = five_day.json()
    # fmt = '%Y-%m-%d'
    # check = curr_time.strftime(fmt)
    # curr_date = (curr_time + timedelta(days=1)).strftime(fmt)
    i = curr_time.second
    city_msg = ' Las Vegas 30 90% Rain   Huntsville  70  65% Clear  Atlanta  80   90%  Clouds  '
    if i < len(city_msg):
        cities_info['text'] = city_msg[i:] + city_msg[:i]









def change():
    curr_time = datetime.now()
    binclock()
    tzclock()
    weather(curr_time)

    bc_canvas.update()
    # weat_canvas.update()

    bc_canvas.after(200, change)


# ====================== Layout =====================================================================#
main_window = Tk()
main_window.configure(bg='black')
main_window.geometry('600x1080')

# creates the different canvases 
bc_canvas = Canvas(main_window, width=300, height=420, bd=0, highlightthickness=0, bg="black")
weat_canvas = Canvas(main_window, width=300, height=420, bd=0, highlightthickness=0, bg="black")
msg_canvas = Canvas(main_window, width=600, height=155, bd=0, highlightthickness=0, bg="blue")
ph2_canvas = Canvas(main_window, width=300, height=420, bd=0, highlightthickness=0, bg='green')
ph3_canvas = Canvas(main_window, width=300, height=140, bd=0, highlightthickness=0, bg="red")
ph4_canvas = Canvas(main_window, width=300, height=280, bd=0, highlightthickness=0, bg="gray")

# positions the canvases 
bc_canvas.grid(row=0, column=0)
weat_canvas.grid(row=0, column=1)
msg_canvas.grid(row=1, column=0, columnspan=2)
ph2_canvas.grid(row=2, column=1, rowspan=2)
ph3_canvas.grid(row=2, column=0)
ph4_canvas.grid(row=3, column=0)

# creates the rectangles used for the binary clock
b = 'gray'
#
hrT1 = bc_canvas.create_rectangle(20, 110, 40, 130, fill=b)
hrT2 = bc_canvas.create_rectangle(20, 140, 40, 160, fill=b)
hr01 = bc_canvas.create_rectangle(50, 50, 70, 70, fill=b)
hr02 = bc_canvas.create_rectangle(50, 80, 70, 100, fill=b)
hr03 = bc_canvas.create_rectangle(50, 110, 70, 130, fill=b)
hr04 = bc_canvas.create_rectangle(50, 140, 70, 160, fill=b)
minT1 = bc_canvas.create_rectangle(80, 80, 100, 100, fill=b)
minT2 = bc_canvas.create_rectangle(80, 110, 100, 130, fill=b)
minT3 = bc_canvas.create_rectangle(80, 140, 100, 160, fill=b)
min01 = bc_canvas.create_rectangle(110, 50, 130, 70, fill=b)
min02 = bc_canvas.create_rectangle(110, 80, 130, 100, fill=b)
min03 = bc_canvas.create_rectangle(110, 110, 130, 130, fill=b)
min04 = bc_canvas.create_rectangle(110, 140, 130, 160, fill=b)
secT1 = bc_canvas.create_rectangle(140, 80, 160, 100, fill=b)
secT2 = bc_canvas.create_rectangle(140, 110, 160, 130, fill=b)
secT3 = bc_canvas.create_rectangle(140, 140, 160, 160, fill=b)
sec01 = bc_canvas.create_rectangle(170, 50, 190, 70, fill=b)
sec02 = bc_canvas.create_rectangle(170, 80, 190, 100, fill=b)
sec03 = bc_canvas.create_rectangle(170, 110, 190, 130, fill=b)
sec04 = bc_canvas.create_rectangle(170, 140, 190, 160, fill=b)
#
local = Label(bc_canvas, text='Apr 22, 2020', fg='white', bg='black', font='arial 12 bold', anchor=W, justify=LEFT)
bc_canvas.create_window(120, 20, window=local, anchor=CENTER)

# bc_canvas.create_line(345, 80, 345, 170, fill='white', width=4)

# creates labels for the timezone clock

tz_est = Label(bc_canvas, text=' ', fg='white', bg='black', font='arial 12 bold', anchor=W, justify=LEFT)
tz_cst = Label(bc_canvas, text=' ', fg='white', bg='black', font='arial 12 bold', anchor=W, justify=LEFT)
tz_mst = Label(bc_canvas, text=' ', fg='white', bg='black', font='arial 12 bold', anchor=W, justify=LEFT)
tz_pst = Label(bc_canvas, text=' ', fg='white', bg='black', font='arial 12 bold', anchor=W, justify=LEFT)
tz_ak = Label(bc_canvas, text=' ', fg='white', bg='black', font='arial 12 bold', anchor=W, justify=LEFT)
tz_hi = Label(bc_canvas, text=' ', fg='white', bg='black', font='arial 12 bold', anchor=W, justify=LEFT)
tz_title = Label(bc_canvas, text=' ', fg='white', bg='black', font='arial 10 bold', anchor=W, justify=LEFT)

bc_canvas.create_line(20, 180, 200, 180, fill='white', width=3)

bc_canvas.create_window(100, 200, window=tz_title, anchor=CENTER)
bc_canvas.create_window(50, 235, window=tz_hi, anchor=W)
bc_canvas.create_window(50, 265, window=tz_ak, anchor=W)
bc_canvas.create_window(50, 295, window=tz_pst, anchor=W)
bc_canvas.create_window(50, 325, window=tz_mst, anchor=W)
bc_canvas.create_window(50, 355, window=tz_cst, anchor=W)
bc_canvas.create_window(50, 385, window=tz_est, anchor=W)

# Creates labels and frames for the weather

pri_temp = Frame(weat_canvas, bg='black', width=200, height=150, bd=0)
next_temp = Frame(weat_canvas, bg='black', width=200, height=165, bd=0)
cities_temp = Frame(weat_canvas, bg='black', width=250, height=50, bd=0)

main_temp = Label(pri_temp, text='30' + u'\N{DEGREE SIGN}', bg='black', fg='white', font='arial 58 bold')
main_hum = Label(pri_temp, text='Humidity: 10%', bg='black', fg='white', font='arial 12 bold')
main_desc = Label(pri_temp, text='Thunderstorm', bg='black', fg='white', font='arial 14 bold')
main_desc.place(x=100, y=25, anchor=CENTER)
main_temp.place(x=100, y=85, anchor=CENTER)
main_hum.place(x=100, y=140, anchor=CENTER)

next_day = Label(next_temp, text='Sat  30' + u'\N{DEGREE SIGN} ' + 'Thunderstorm', bg='black', fg='white',
                 font='arial 12 bold',
                 anchor=W, justify=LEFT)
next_day1 = Label(next_temp, text='Sun  30' + u'\N{DEGREE SIGN} ' + 'Rain', bg='black', fg='white',
                  font='arial 12 bold',
                  anchor=W, justify=LEFT)
next_day2 = Label(next_temp, text='Mon  30' + u'\N{DEGREE SIGN} ' + 'Clouds', bg='black', fg='white',
                  font='arial 12 bold',
                  anchor=W, justify=LEFT)
next_day3 = Label(next_temp, text='Tues  30' + u'\N{DEGREE SIGN} ' + 'Clear', bg='black', fg='white',
                  font='arial 12 bold',
                  anchor=W, justify=LEFT)
next_day4 = Label(next_temp, text='Wed  30' + u'\N{DEGREE SIGN} ' + 'Thunderstorm', bg='black', fg='white',
                  font='arial 12 bold',
                  anchor=W, justify=LEFT)
next_day.place(x=10, y=25, anchor=W)
next_day1.place(x=10, y=55, anchor=W)
next_day2.place(x=10, y=85, anchor=W)
next_day3.place(x=10, y=115, anchor=W)
next_day4.place(x=10, y=145, anchor=W)

cities_info = Label(cities_temp, text=' ', bg='black', fg='white', font='arial 12 bold',
                    anchor=W, justify=LEFT, width=23, height=1)
cities_info.place(x=125, y=25, anchor=CENTER)

weat_canvas.create_window(160, 85, window=pri_temp)
weat_canvas.create_window(160, 270, window=next_temp)
weat_canvas.create_window(160, 380, window=cities_temp)

weat_canvas.create_line(25, 180, 280, 180, fill='white', width=3)

# ====================================== End of Layout =====================================================#

# TODO: code timezone clocks
# TODO: code weather function --- degree_sign = u"\N{DEGREE SIGN}"
# TODO: code some sort of information presentation functions (quotes, news, ... ?)

# binclock()
change()
main_window.mainloop()
