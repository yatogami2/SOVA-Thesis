from win32com.client import Dispatch
import time

def speak(str1):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str1)

r_String = []

def rec_String():
    user_input = input("Enter Text: ")
    r_String.append(user_input)
    print(f'Your Words are: "{user_input}"')
    return user_input  # Return the user input from the function

while True:
    user_input = rec_String()  # Get the user input and store it in the 'user_input' variable
    text2speech = input("Do you want me to read your string (yes/no): ").lower()

    if text2speech == 'yes':
        speak(user_input)
        time.sleep(5)
        break
    elif text2speech == 'no':
        break
