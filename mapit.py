import webbrowser
import pyperclip
text=pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/'+text)
