from tkinter import *
from tkinter import ttk,messagebox
import googletrans as gt
from googletrans.constants import LANGUAGES
import textblob

root=Tk()
root.title('Translator')
root.geometry('900x450')

#function to change language selected
def changelang():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,changelang)

#translation function
def translate():
    global language
    try:
        text_=text1.get(1.0,END)
        c2=combo1.get()
        c3=combo2.get()
        if(text_):
            words=textblob.TextBlob(text_)
            lan=words.detect_language()
            for i,j in language.items():
                if (j==c3):
                    lan_=i
            words=words.translate(from_lang=lan,to=str(lan_))
            text2.delete(1.0,END)
            text2.insert(END,words)
    except Exception as e:
        messagebox.showerror('Translator','Something went wrong! Please try again')



language=gt.LANGUAGES
languageV=list(language.values())
language1=language.keys()

#combo box 1
combo1=ttk.Combobox(root,values=languageV,font='Roboto 14',state='r')
combo1.place(x=50,y=20)
combo1.set('English')

label1=Label(root,text='English',font='Segoe 20 bold',bg='white',width=18,bd=5,relief=GROOVE)
label1.place(x=50,y=70)

#input area
f=Frame(root,bg='black',bd=5)
f.place(x=50,y=130,width=310,height=200)

#words to be translated
text1=Text(f,font='Robote 16',bg='white',relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=300,height=190)
scrollbar1=Scrollbar(f)
scrollbar1.pack(side='right',fill='y')
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#combo box 2
combo2=ttk.Combobox(root,values=languageV,font='Roboto 14',state='r')
combo2.place(x=550,y=20)
combo2.set('Select Language')

label2=Label(root,text='English',font='Segoe 20 bold',bg='white',width=18,bd=5,relief=GROOVE)
label2.place(x=550,y=70)

#output area
f=Frame(root,bg='black',bd=5)
f.place(x=550,y=130,width=310,height=200)

#translation
text2=Text(f,font='Robote 16',bg='white',relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=300,height=190)
scrollbar2=Scrollbar(f)
scrollbar2.pack(side='right',fill='y')
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)


#translate button
translate_button=Button(root,text='Translate',font='Roboto 15 bold italic',activebackground='grey',cursor='hand2',bg='white',command=translate)
translate_button.place(x=400,y=180)


changelang()

root.configure(bg='white')
root.mainloop()
