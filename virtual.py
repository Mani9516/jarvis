import streamlit as st
import datetime
import pyttsx3
import wikipedia
import speech_recognition as sr
import os
import webbrowser

def get_response(input_text):
    if input_text.lower() in ["hello", "hey"]:
        return "Hello! How can I assist you?"
    elif input_text.lower() == "what is the time":
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        return f"The time is {current_time}."
    elif input_text.lower().startswith("what is "):
        person = input_text.replace('what is ', '')
        try:
            info = wikipedia.summary(person, sentences=1)
            return info
        except wikipedia.exceptions.DisambiguationError as e:
            return f"Which {person} are you referring to? Please provide more context."
    elif input_text.lower() == "goodbye":
        return "Goodbye! Have a great day."
    elif input_text.lower() == "open google":
        webbrowser.open_new_tab("https://www.google.com")
        return "Google opened in your default browser."
    elif input_text.lower() == "open camera":
        os.system("start microsoft.windows.camera:")
        return "Camera opened."
    elif input_text.lower() == "open visual studio":
        os.system("start devenv")
        return "Visual Studio opened."
    elif input_text.lower() == "open whatsapp":
        # Replace the command with the appropriate one for your system
        os.system("start whatsapp")
        return "WhatsApp application opened."
    elif input_text.lower() == "open instagram":
        webbrowser.open_new_tab("https://www.instagram.com/")
        return "Instagram opened in your default browser."
    elif input_text.lower() == "open notepad":
        os.system("start notepad")
        return "Notepad opened."
    elif input_text.lower() == "open calculator":
        os.system("start calc")
        return "Calculator opened."
    # Add more commands for opening other installed applications here
    else:
        return "I'm sorry, I didn't understand that."

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(device_index=1)
    with microphone as source:
        st.write("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        st.write("Recognizing...")
        result = recognizer.recognize_google(audio)
        return result
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return "Recognition request failed: " + str(e)
    return None

def main():
    st.markdown("<h1 style='text-align: center; color: white;'>J.A.R.V.I.S</h1>", unsafe_allow_html=True)

    st.image("C:\Users\mani chourasiya\Downloads\gso7gr28.png",
             use_column_width=None)

    # Create the input form
    with st.form("message-form"):
        with st.container():
            input_message = st.text_input("You:", "")
            send_button = st.form_submit_button("Send")

    # Process the form submission
    if send_button or input_message:
        if input_message:
            user_input = input_message
        else:
            user_input = recognize_speech()

        response = get_response(user_input)

        speak(response)

        # Clear input text after sending message
        st.empty()

if __name__ == "__main__":
    main()
