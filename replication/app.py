import speech_recognition as sr
import pyaudio

# Pretty self explanatory here

def main():
    r = sr.Recognizer()

    with sr.Microphone() as src:
        r.adjust_for_ambient_noise(src)

        print('ok 3 2 1 lets jam\n')

        audio = r.listen(src)

        try:
            print(f'heres your stupid transcript are you happy now:\n{r.recognize_google(audio)}')
        
        except Exception as e:
            print(f'Error: {str(e)}')

if __name__ == "__main__":
    main()