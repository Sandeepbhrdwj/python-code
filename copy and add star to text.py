import pyperclip
text=pyperclip.paste()
#print(text)
nt=''
for i in text.split('\n'):
    #print(i)
    nt=nt+'* '+i+'\n'
pyperclip.copy(nt)
