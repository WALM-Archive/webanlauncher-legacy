from tkinter import *
import customtkinter
from CTkMessagebox import CTkMessagebox
import webbrowser
import wget
import os
import shutil
import time

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark

des = customtkinter.CTk()  # create CTk window like you do with the Tk window
des.geometry("800x500")
#des.iconbitmap('logo.ico')
icon = PhotoImage(file='logo.png')
des.iconphoto(False, icon)
des.title("WebAnLiMaks Launcher")
des.resizable(width = False, height = False)

game = 'none'
qiwi_webmast = 'https://qiwi.com/n/WEBMAST2007'
tg_webmast = 'https://t.me/webmast_webanlimaks'
youtube_webmast = 'https://www.youtube.com/@webanlimaks/videos'
donal_maksimys = 'https://www.donationalerts.com/r/maksimys_'
tg_maksimys = 'https://t.me/Original_Maksimys'
youtube_maksimys = 'https://www.youtube.com/@Maksimys_/videos'
about_anonymous = 'https://evembar.github.io/webanlimaks/-Anonymous-chapter-full.html'

def about_webanlimaks_launcher():
    CTkMessagebox(title="WebAnLiMaks Launcher", message=" WebAnLiMaks Launcher\nРазработал - WebMast \nЯзык - Python 3\nWebAnLiMaks 2023", icon = 'logo.png')

def mail_issue():
    CTkMessagebox(title="WebAnLiMaks Launcher", message=" По любым вопросам писать на этот адрес\n lbhnik12@gmail.com", icon = 'gmail.png')

def radiobutton_event():
    print(radio_var.get())
    LauncherAPI.getver(version = radio_var.get)

def get_play():
    global radio_var, radiobutton_1, radiobutton_2, radiotext
    if game == 'none':
        check_clas.configure(text = 'Состояние: ошибка')
        CTkMessagebox(title="WebAnLiMaks Launcher", message="Не указана игра", icon="cancel")
    else:
        radiotext = customtkinter.CTkLabel(des, text='Версия: ',  font = ('Colibri', 20))
        radiotext.place(x=400, y=100)

        radio_var = IntVar(value=0)
        radiobutton_1 = customtkinter.CTkRadioButton(des, text="1.0",
                                                    command=radiobutton_event, variable= radio_var, value=10)
        radiobutton_1.place(x=500,y = 100)

        radiobutton_2 = customtkinter.CTkRadioButton(des, text="1.1",
                                                    command=radiobutton_event, variable= radio_var, value=11)
        radiobutton_2.place(x=500,y=130)

def play():
    global anonymous_ver
    check_clas.configure(text = 'Состояние: Запуск игры')
    des.update()
    des.after(1000)
    if game == 'none':
        check_clas.configure(text = 'Состояние: ошибка')
        CTkMessagebox(title="WebAnLiMaks Launcher", message="Не указана игра", icon="cancel")
    else:
        if os.path.isdir('Anonymous-full'):
            os.chdir('Anonymous-full')
            sost = os.system('start anonymous.exe')
            if sost == 0:
                check_clas.configure(text = 'Состояние: успешный запуск')
                des.update()
            elif sost == 1:
                check_clas.configure('Состояние: ошибка\n во время запуска')
                des.update()
        elif os.path.isfile('anonymous_windows.webanlimax'):
            if os.path.isfile('anonymous_windows.zip'):
                os.remove('anonymous_windows.zip')
            os.rename("anonymous_windows.webanlimax","anonymous_windows.zip")
            shutil.unpack_archive("anonymous_windows.zip")
            check_clas.configure(text = 'Состояние: Распаковка')
            des.update()
            os.remove('anonymous_windows.zip')
            os.chdir('Anonymous-full')
            sost = os.system('start anonymous.exe')
            if sost == 0:
                check_clas.configure(text = 'Состояние: успешный запуск')
                des.update()
            elif sost == 1:
                check_clas.configure('Состояние: ошибка\n во время запуска')
                des.update()
        elif os.path.isfile('anonymous.exe'):
            sost = os.system('start anonymous.exe')
            if sost == 0:
                check_clas.configure(text = 'Состояние: успешный запуск')
                des.update()
            elif sost == 1:
                check_clas.configure('Состояние: ошибка\n во время запуска')
                des.update()
        else:
            check_clas.configure(text = 'Скачиваем дистрибутив\nигры')
            des.update()
            if anonymous_ver == 10:
                wget.download('https://github.com/evembar/webanlauncher/releases/download/o/anonymous_windows.webanlimax')
            else:
                    wget.download('https://github.com/evembar/webanlauncher/releases/download/1.1/anonymous_windows.webanlimax')
            if os.path.isfile('anonymous_windows.zip'):
                os.remove('anonymous_windows.zip')
            os.rename("anonymous_windows.webanlimax","anonymous_windows.zip")
            shutil.unpack_archive("anonymous_windows.zip")
            check_clas.configure(text = 'Состояние: Распаковка')
            des.update()
            os.remove('anonymous_windows.zip')
            os.chdir('Anonymous-full')
            sost = os.system('start anonymous.exe')
            if sost == 0:
                check_clas.configure(text = 'Состояние: успешный запуск')
                des.update()
            elif sost == 1:
                check_clas.configure('Состояние: ошибка\n во время запуска')
                des.update()



def anonymous_selected():
    global game
    voted_text.configure(text = 'Выбрана игра: Anonymous. In search of snus full version')
    voted_text.place(x = 20, y = 55)
    check_clas.configure(text = 'Состояние: Готов к запуску')
    game = 'anonymous'

def get_webmast_qiwi():
    webbrowser.open_new_tab(qiwi_webmast)

def get_donal_maksimys():
    webbrowser.open_new_tab(donal_maksimys)

def get_tg_webmast():
    webbrowser.open_new_tab(tg_webmast)

def get_youtube_webmast():
    webbrowser.open_new_tab(youtube_webmast)

def get_tg_maksimys():
    webbrowser.open_new_tab(tg_maksimys)

def get_youtube_maksimys():
    webbrowser.open_new_tab(youtube_maksimys)

def get_about_anonymous():
    webbrowser.open_new_tab(about_anonymous)

anonymous_poster = PhotoImage(file='src/anonymous_poster.png')
tg = PhotoImage(file = 'src/telegram.png')
youtube = PhotoImage(file='src/youtube.png')
donal = PhotoImage(file='src/donal.png')
qiwi = PhotoImage(file='src/qiwi.png')


class LauncherAPI:
    global anonymous_ver, radio_var, radiobutton_1, radiobutton_2, radiotext
    def getver(version):
        global anonymous_ver, radio_var, radiobutton_1, radiobutton_2, radiotext
        anonymous_ver = version
        radiotext.place_forget()
        radiobutton_1.place_forget()
        radiobutton_2.place_forget()
        play()

anonymous_poster_button = customtkinter.CTkButton(des, image = anonymous_poster, text='', command = anonymous_selected)
anonymous_poster_button.place(x = 20, y = 100)

more_anonymous_button = customtkinter.CTkButton(des, text = 'Об игре', command=get_about_anonymous)
more_anonymous_button.place(x = 100, y = 315)

qiwi_webmast_button = customtkinter.CTkButton(des, image = qiwi, text = '', width = 50, height = 50, command=get_webmast_qiwi)
qiwi_webmast_button.place(x = 25, y = 430)

donal_maksimys_button = customtkinter.CTkButton(des, image = donal, text = '', width = 50, height = 50, command = get_donal_maksimys)
donal_maksimys_button.place(x = 165, y = 430)

tg_webmast_button = customtkinter.CTkButton(des, image = tg, text = '', width = 25, height = 25, command = get_tg_webmast)
tg_webmast_button.place(x = 285, y = 430)

youtube_webmast_button = customtkinter.CTkButton(des, image = youtube, text = '', width = 25, height = 25, command = get_youtube_webmast)
youtube_webmast_button.place(x = 285, y = 465)

tg_maksimys_button = customtkinter.CTkButton(des, image = tg, text = '', width = 25, height = 25, command = get_tg_maksimys)
tg_maksimys_button.place(x = 435, y = 430)

youtube_maksimys_button = customtkinter.CTkButton(des, image = youtube, text = '', width = 25, height = 25, command = get_youtube_maksimys)
youtube_maksimys_button.place(x = 435, y = 465)


play_button = customtkinter.CTkButton(des, text = 'Играть', font = ('Colibri', 20), width = 100, height = 50, command = get_play)
play_button.place(x = 690, y = 430)

about_webanlimaks_launcher_button = customtkinter.CTkButton(des, text = 'О нас', font = ('Colibri', 20), width = 50, height = 50, command = about_webanlimaks_launcher)
about_webanlimaks_launcher_button.place(x = 610, y = 430)

about_webanlimaks_launcher_button = customtkinter.CTkButton(des, text = 'Почта', font = ('Colibri', 20), width = 50, height = 50, command = mail_issue)
about_webanlimaks_launcher_button.place(x = 520, y = 430)


voted_text = customtkinter.CTkLabel(des, font = ('Arial', 18))

poder_den_text = customtkinter.CTkLabel(des, text='Поддержите нас рублём', font = ('Colibri', 20))
poder_den_text.place(x = 20, y = 370)

poder_den_text2 = customtkinter.CTkLabel(des, text='Мы в соц. сетях', font = ('Colibri', 20))
poder_den_text2.place(x = 270, y = 370)

vote_text = customtkinter.CTkLabel(des, text = 'Выберите игру для запуска', font = ('Colibri', 20))
vote_text.place(x = 20, y = 20)

webmast_maksimys_text = customtkinter.CTkLabel(des, text = 'WebMast                  Maksimys', font = ('Arial', 16))
webmast_maksimys_text.place(x = 25, y = 393)

webmast_maksimys_text2 = customtkinter.CTkLabel(des, text = 'WebMast                  Maksimys', font = ('Arial', 16))
webmast_maksimys_text2.place(x = 275, y = 393)

check_clas = customtkinter.CTkLabel(des, text = 'Состояние: Не выбрана игра', font = ('Arial', 20))
check_clas.place(x = 535, y = 350)

progressbar =  customtkinter.CTkProgressBar(des, orientation="horizontal", mode="indeterminate")
progressbar.place(x = 550, y = 400)
progressbar.start()

des.mainloop()
