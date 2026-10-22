import speech_recognition as sr
import pyttsx3
import webbrowser
import pyautogui
import time
import os

# ==========================================
# INISIALISASI TEXT TO SPEECH
# ==========================================

engine = pyttsx3.init()

def speak(text):

    # AI berbicara
    engine.say(text)
    engine.runAndWait()


# ==========================================
# FUNGSI MENDENGARKAN SUARA
# ==========================================

def listen_command():

    listener = sr.Recognizer()

    with sr.Microphone() as source:

        print("AI mendengarkan...")
        speak("Saya mendengarkan")

        # Mengurangi noise sekitar
        listener.adjust_for_ambient_noise(source, duration=1)

        print("Silakan bicara...")

        try:

            # Mendengarkan suara user
            voice = listener.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

        except:

            print("Tidak ada suara")
            return ""

    try:

        # Mengubah suara menjadi text
        command = listener.recognize_google(
            voice,
            language='en-US'
        )

        command = command.lower()

        print("Perintah :", command)

        return command

    except sr.UnknownValueError:

        print("Suara tidak dikenali")
        return ""

    except sr.RequestError:

        print("Koneksi internet bermasalah")
        return ""

    except Exception as e:

        print("ERROR :", e)
        return ""


# ==========================================
# MEMBUKA GOOGLE DAN SEARCH
# ==========================================

def search_google(keyword):

    speak(f"Mencari {keyword} di Google")

    webbrowser.open("https://www.google.com")

    time.sleep(3)

    pyautogui.write(keyword)

    pyautogui.press("enter")


# ==========================================
# MEMBUKA APLIKASI
# ==========================================

def open_application(command):

    # MEMBUKA CHROME
    if "chrome" in command:

        speak("Membuka Google Chrome")

        chrome_path = (
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        )

        os.startfile(chrome_path)

    # MEMBUKA NOTEPAD
    elif "notepad" in command:

        speak("Membuka Notepad")

        os.system("notepad")

    # MEMBUKA CALCULATOR
    elif "calculator" in command:

        speak("Membuka Calculator")

        os.system("calc")

    else:

        speak("Aplikasi tidak ditemukan")


# ==========================================
# MENJALANKAN AI
# ==========================================

def run_assistant():

    speak("Halo, AI Assistant siap digunakan")

    while True:

        command = listen_command()

        # Jika command kosong
        if command == "":
            continue

        # ==================================
        # GOOGLE SEARCH
        # ==================================

        if "search" in command:

            keyword = command.replace("search", "")

            search_google(keyword)

        # ==================================
        # MEMBUKA APLIKASI
        # ==================================

        elif "open" in command:

            open_application(command)

        # ==================================
        # KELUAR PROGRAM
        # ==================================

        elif "exit" in command:

            speak("Sampai jumpa")

            break

        else:

            print("Perintah tidak dikenali")


# ==========================================
# PROGRAM UTAMA
# ==========================================

run_assistant()