from tkinter import *
from datetime import datetime
from pytz import timezone
from collections import defaultdict, Counter
import requests, json, random, speedtest

ticker = 0
last_seen = 60
city_msg = 'Temperature of cities will update soon    '


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
    global city_msg
    # Enter your API key here
    api_key = "c28f59a9bb82459a0013c88d372071a2"

    # base urls for Openweathermap.org
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    forecast = "http://api.openweathermap.org/data/2.5/forecast?"

    cities = [('Laurel', 'Maryland'), ('Huntsville', 'Alabama'), ('Atlanta', 'Georgia'), ('Las Vegas', 'Nevada')]
    city_res = {}

    forecast_url = forecast + '&q=' + cities[0][0] + ',' + cities[0][1] + '&APPID=' + api_key

    def temp_con(temp):
        degree_sign = u"\N{DEGREE SIGN}"
        k_to_f = int(temp * 1.8 - 459.57)  # converts Kelvin to Fahrenheit
        return str(k_to_f) + degree_sign

    # Retrieves Current weather for cities in cities list every hour
    if curr_time.minute == 0 and curr_time.second == 0:
        # retrieves the current weather of all locations in the cities list and saves the results to a dictionary
        for location in cities:
            (city_name, state_name) = location
            complete_url = base_url + '&q=' + city_name + ',' + state_name + '&APPID=' + api_key  # required query url
            response = requests.get(complete_url)
            results = response.json()

            if results["cod"] == 200:
                curr_weat = results["main"]
                curr_temp = temp_con(curr_weat["temp"])
                curr_hum = str(curr_weat["humidity"]) + '%'
                descr = results["weather"][0]["main"]

            city_res[city_name] = curr_temp, curr_hum, descr

        main_temp['text'] = city_res['Laurel'][0]
        main_hum['text'] = 'Humidity:  ' + city_res['Laurel'][1]
        main_desc['text'] = city_res['Laurel'][2]

        spacer = ' ' * 3
        gap = ' ' * 7
        hum = 'Humidity: '
        city_msg = gap + 'Huntsville' + spacer + city_res['Huntsville'][0] + spacer + city_res['Huntsville'][2] \
                   + spacer + hum + city_res['Huntsville'][1] + gap + 'Atlanta' + spacer + city_res['Atlanta'][0] \
                   + spacer + city_res['Atlanta'][2] + spacer + hum + city_res['Atlanta'][1] + gap \
                   + 'Las Vegas' + spacer + city_res['Las Vegas'][0] + spacer + city_res['Las Vegas'][2] \
                   + spacer + hum + city_res['Las Vegas'][1]

        # Retrieves the weather for the next five days
        five_day = requests.get(forecast_url)
        fday_res = five_day.json()
        fmt = '%Y-%m-%d'
        check = curr_time.strftime(fmt)

        upcoming = []
        final = []
        for_res = defaultdict(list)

        for item in fday_res['list']:
            day = item['dt_txt'].split()
            temp_date = day[0]
            my_date = day[0].split('-')
            for_temp = item['main']['temp']
            for_weat = item['weather'][0]['main']

            if check != temp_date:
                weekday = datetime(int(my_date[0]), int(my_date[1]), int(my_date[2])).strftime('%a')
                data = weekday, for_temp, for_weat
                upcoming.append(data)

        for day_of_week, degrees, weather_type in upcoming:
            conditions = degrees, weather_type
            for_res[day_of_week].append(conditions)

        for day_next in for_res:
            temp_hi = []
            temp_type = []
            for pattern in for_res[day_next]:
                temp_hi.append(pattern[0])
                temp_type.append(pattern[1])
            counts = dict(Counter(temp_type))
            fin_type = list(counts.keys())[list(counts.values()).index(max(counts.values()))]

            day_fin = day_next, temp_con(max(temp_hi)), fin_type

            final.append(day_fin)

        next_day['text'] = '  '.join(final[0])
        next_day1['text'] = '  '.join(final[1])
        next_day2['text'] = '  '.join(final[2])
        next_day3['text'] = '  '.join(final[3])
        next_day4['text'] = '  '.join(final[4])

    global ticker

    ticker += 1
    if ticker <= len(city_msg):
        cities_info['text'] = city_msg[ticker:] + city_msg[:ticker]
    else:
        ticker = 0
        cities_info['text'] = city_msg


def message(curr_time):
    motd = ['With Great Power Comes Great Responsibility.', 'Desinty! Destiny! No Escaping That For Me!',
            'All That is Gold Does Not Glitter / Not All Those Who Wander Are Lost.',
            'Fear Is The Mind-Killer. Fear Is The Little-Death That Brings Total Obliteration.',
            'To Err Is Human; To Really Screw Up Requires The Root Password.',
            'If You Only Knew The Power Of The Dark Side', 'No Matter Where You Go... There You Are',
            'What\'s The Point In Being Grown Up If You Can\'t Be Childish Sometimes?', 'You Have No Power Over Me.',
            'Fear Leads To Anger; Anger Leads To Hate; Hate Leads To Suffering.',
            'Pinky, Are You Pondering What I\'m Pondering', 'Ideas Are Bulletproof',
            'Facts Do Not Cease To Exist Because They Are Ignored.',
            'I\'m Not Anti-Social, I\'m Just Not User-Friendly',
            'A Conclusion is The Place Where You Got Tired Of Thinking', 'Why So Serious?',
            'I Will Not Be Pushed, Filed, Stamped, Indexed, Briefed, Debriefed, or Numbered.  My Life is My Own',
            'To Learn Which Questions Are Unanswerable, And Not Answer Them: This Skill Is Most Needful In Times '
            'Of Stress and Darkness.', 'Try Not. DO. Or Do Not. There Is No Try.', 'There Can Be Only One',
            'A Strange Game.  The Only Winning Move Is Not To Play',
            'He Who Breaks A Thing To Find Out What It Is, Has Left The Path Of Wisdom',
            'Reality Is Merely An Illusion, Albeit A Very Persistent One',
            'We Do Not Follow Maps To Buried Treasure, And X Never, Ever Marks The Spot.',
            'Fantasy Is The Impossible Made Probable. Science Fiction Is The Improbable Made Possible']

    # Randomly choices an quote from the list every 15 minutes with a slot machine-like effect
    if curr_time.minute % 15 == 0 and curr_time.second == 0:
        quote_msg['text'] = random.choice(motd)


def speed(curr_time):
    st = speedtest.Speedtest()

    if curr_time.minute == 0 and curr_time.second == 0:
        down_res = (st.download() / 1000) / 1000
        up_res = (st.upload() / 1000) / 1000
        ping_res = st.results.ping

        down_msg['text'] = str(int(down_res))
        up_msg['text'] = str(int(up_res))
        ping_msg['text'] = str(int(ping_res))

        asof_msg['text'] = str(curr_time.second) + ' minutes ago'



def change():
    curr_time = datetime.now()
    binclock()
    tzclock()
    weather(curr_time)
    message(curr_time)
    speed(curr_time)

    bc_canvas.update()

    bc_canvas.after(200, change)



# ====================== Layout =====================================================================#
main_window = Tk()
main_window.configure(bg='black')
main_window.geometry('600x1080')

# creates the different canvases 
bc_canvas = Canvas(main_window, width=290, height=420, bd=0, highlightthickness=2, bg='black')
weat_canvas = Canvas(main_window, width=280, height=420, bd=0, highlightthickness=2, bg='black')
msg_canvas = Canvas(main_window, width=580, height=155, bd=3, highlightthickness=2, bg='black')
speed_canvas = Canvas(main_window, width=580, height=150, bd=3, highlightthickness=2, bg='black')
ph_canvas = Canvas(main_window, width=580, height=15, bd=0, highlightthickness=0, bg='black')
ph2_canvas = Canvas(main_window, width=580, height=15, bd=0, highlightthickness=0, bg='black')
ph3_canvas = Canvas(main_window, width=580, height=15, bd=0, highlightthickness=0, bg='black')
ph4_canvas = Canvas(main_window, width=290, height=140, bd=0, highlightthickness=0, bg='green')
ph5_canvas = Canvas(main_window, width=290, height=140, bd=0, highlightthickness=0, bg='red')

# positions the canvases 
bc_canvas.grid(row=0, column=0)
weat_canvas.grid(row=0, column=1)
ph_canvas.grid(row=1, column=0, columnspan=2)
msg_canvas.grid(row=2, column=0, columnspan=2)
ph2_canvas.grid(row=3, column=0, columnspan=2)
speed_canvas.grid(row=4, column=0, columnspan=2)
ph3_canvas.grid(row=5, column=0, columnspan=2)
# ph4_canvas.grid(row=6, column=0)
# ph5_canvas.grid(row=6, column=1)

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
cities_temp = Frame(weat_canvas, bg='black', width=230, height=50, bd=0)

deg = u'\N{DEGREE SIGN}'
main_temp = Label(pri_temp, text='30' + deg, bg='black', fg='white', font='arial 58 bold')
main_hum = Label(pri_temp, text='Humidity: 10%', bg='black', fg='white', font='arial 12 bold')
main_desc = Label(pri_temp, text='Thunderstorm', bg='black', fg='white', font='arial 14 bold')
main_desc.place(x=100, y=25, anchor=CENTER)
main_temp.place(x=100, y=85, anchor=CENTER)
main_hum.place(x=100, y=140, anchor=CENTER)

next_day = Label(next_temp, text='Sat  30' + deg + ' Thunderstorm', bg='black', fg='white',
                 font='arial 12 bold',
                 anchor=W, justify=LEFT)
next_day1 = Label(next_temp, text='Sun  30' + deg + ' Rain', bg='black', fg='white',
                  font='arial 12 bold',
                  anchor=W, justify=LEFT)
next_day2 = Label(next_temp, text='Mon  30' + deg + ' Clouds', bg='black', fg='white',
                  font='arial 12 bold',
                  anchor=W, justify=LEFT)
next_day3 = Label(next_temp, text='Tues  30' + deg + ' Clear', bg='black', fg='white',
                  font='arial 12 bold',
                  anchor=W, justify=LEFT)
next_day4 = Label(next_temp, text='Wed  30' + deg + ' Thunderstorm', bg='black', fg='white',
                  font='arial 12 bold',
                  anchor=W, justify=LEFT)
next_day.place(x=10, y=25, anchor=W)
next_day1.place(x=10, y=55, anchor=W)
next_day2.place(x=10, y=85, anchor=W)
next_day3.place(x=10, y=115, anchor=W)
next_day4.place(x=10, y=145, anchor=W)

cities_info = Label(cities_temp, text=' ', bg='black', fg='white', font='arial 12 bold',
                    anchor=W, justify=LEFT, width=23, height=1)
cities_info.place(x=90, y=25, anchor=CENTER)

weat_canvas.create_window(160, 85, window=pri_temp)
weat_canvas.create_window(160, 270, window=next_temp)
weat_canvas.create_window(160, 380, window=cities_temp)

weat_canvas.create_line(25, 180, 260, 180, fill='white', width=3)

# Creates label to display a random message

quote_msg = Label(msg_canvas, text='The Ability To Speak Does Not Make You Intelligent ', bg='black', fg='white',
                  font='arial 18 bold', anchor=W, justify=LEFT, width=38, height=3, wraplength=580)
msg_canvas.create_window(300, 75, window=quote_msg)
msg_canvas.create_line(10, 15, 580, 15, fill='white', width=3)
msg_canvas.create_line(10, 140, 580, 140, fill='white', width=3)

down_speed = Frame(speed_canvas, bg='black', width=190, height=160, bd=0, highlightcolor="white", highlightthickness=2)
up_speed = Frame(speed_canvas, bg='black', width=190, height=160, bd=0, highlightcolor="white", highlightthickness=2)
ping_speed = Frame(speed_canvas, bg='black', width=190, height=160, bd=0, highlightcolor="white", highlightthickness=2)
speed_canvas.create_window(100, 80, window=down_speed)
speed_canvas.create_window(295, 80, window=up_speed)
speed_canvas.create_window(490, 80, window=ping_speed)

ping_label = Label(ping_speed, text='Ping', bg='black', fg='white', font='arial 14 bold', anchor=W,
                   justify=CENTER)
ping_label.place(x=95, y=20, anchor=CENTER)
down_label = Label(down_speed, text='Download', bg='black', fg='white', font='arial 14 bold', anchor=W,
                   justify=LEFT)
down_label.place(x=95, y=20, anchor=CENTER)
up_label = Label(up_speed, text='Upload', bg='black', fg='white', font='arial 14 bold', anchor=W,
                 justify=LEFT)
up_label.place(x=95, y=20, anchor=CENTER)

ping_msg = Label(ping_speed, text='6', bg='black', fg='white', font='arial 45 bold', anchor=W,
                 justify=CENTER)
ping_msg.place(x=95, y=75, anchor=CENTER)
down_msg = Label(down_speed, text='188', bg='black', fg='white', font='arial 45 bold', anchor=W,
                 justify=CENTER)
down_msg.place(x=95, y=75, anchor=CENTER)
up_msg = Label(up_speed, text='14', bg='black', fg='white', font='arial 45 bold', anchor=W,
               justify=CENTER)
up_msg.place(x=95, y=75, anchor=CENTER)
ping_unit = Label(ping_speed, text='ms', bg='black', fg='white', font='arial 12 bold', anchor=W,
                  justify=CENTER)
ping_unit.place(x=95, y=115, anchor=CENTER)
down_unit = Label(down_speed, text='Mbps', bg='black', fg='white', font='arial 12 bold', anchor=W,
                  justify=CENTER)
down_unit.place(x=95, y=115, anchor=CENTER)
up_unit = Label(up_speed, text='Mbps', bg='black', fg='white', font='arial 12 bold', anchor=W,
                justify=CENTER)
up_unit.place(x=95, y=115, anchor=CENTER)
asof_label = Label(up_speed, text='As of: ', bg='black', fg='white', font='arial 10 bold', anchor=W,
                   justify=CENTER)
asof_label.place(x=35, y=140, anchor=CENTER)
asof_msg = Label(up_speed, text='59 minutes ago', bg='black', fg='white', font='arial 10 bold', anchor=W,
                 justify=CENTER)
asof_msg.place(x=106, y=140, anchor=CENTER)

# ====================================== End of Layout =====================================================#


# TODO: code weather function --- degree_sign = u"\N{DEGREE SIGN}"
# TODO: code some sort of information presentation functions (quotes, news, ... ?)

# main_window.attributes("-fullscreen", True)
change()
main_window.mainloop()
