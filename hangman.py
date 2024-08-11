from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random

a=Tk()
a.title('Hangman')
a.geometry('900x600')
a.configure(bg="black")
def c():
    a.destroy()
    window=Tk()
    window.title('Hangman-GUESS CITIES')
    word_list=['MUMBAI','DELHI','BANGLORE','HYDRABAD','AHMEDABAD','CHENNAI','KOLKATA','SURAT','PUNE','JAIPUR','AMRITSAR','ALLAHABAD','RANCHI',
               'LUCKNOW','KANPUR','NAGPUR','INDORE','THANE','BHOPAL','PATNA','AGRA','VARANASI','SRINAGAR','RAIPUR','KOTA','JHANSI']
                 
    photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"),
    PhotoImage(file="images/hang3.png"), PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"),
    PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"), PhotoImage(file="images/hang8.png"),
    PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]






    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        numberOfGuesses =0
        global the_word
        the_word=random.choice(word_list)
        the_word_withSpaces = " ".join(the_word)
        lblWord.set(' '.join("_"*len(the_word)))

    def guess(letter):
      global numberOfGuesses
      if numberOfGuesses<11:	
        txt = list(the_word_withSpaces)
        guessed = list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
          for c in range(len(txt)):
            if txt[c]==letter:
              guessed[c]=letter
            lblWord.set("".join(guessed))
            if lblWord.get()==the_word_withSpaces:
              messagebox.showinfo("Hangman","You guessed it!")
              exit()
        else:
          numberOfGuesses += 1
          imgLabel.config(image=photos[numberOfGuesses])
          if numberOfGuesses==11:
              messagebox.showwarning("Hangman","Game Over")
              mll=Label(window,text="Correct word is:",font=('Copper Black',14)).grid()
              ml=Label(window,text=the_word,font=('Arial Black',14)).grid()



    imgLabel=Label(window)
    imgLabel.grid(row=0, column=0, columnspan=6, padx=20, pady=60)


      
    lblWord = StringVar()
    Label(window, textvariable  =lblWord,font=('consolas 24 bold')).grid(row=0, column=3 ,columnspan=6,padx=10)
    n=0

    def k1(c, c1, c2):
      Label(window, text=c, font=('Helvetica 18'), width=8, relief='groove', bg="black",fg='white').grid(row=c1, column=c2)
      return guess(c)

    for c in ascii_uppercase:
      Button(window, text=c, command=lambda c=c, n=n: k1(c, 1+n//9, n%9), font=('Helvetica 18'), width=8,relief='groove').grid(row=1+n//9,column=n%9)
      n+=1
      



    newGame()
    window.mainloop()

def f():
    a.destroy()
    window=Tk()
    window.title('Hangman-GUESS FRUITS')
    word_list=['POMEGRANATE','PINEAPPLE','AVOCADO','JACKFRUIT','WATERMELON','MUSKMELON','STRAWBERRY','BLUEBERRY','BLACKBERRY']       
    photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"),
    PhotoImage(file="images/hang3.png"), PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"),
    PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"), PhotoImage(file="images/hang8.png"),
    PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]






    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        numberOfGuesses =0
        global the_word
        the_word=random.choice(word_list)
        the_word_withSpaces = " ".join(the_word)
        lblWord.set(' '.join("_"*len(the_word)))

    def guess(letter):
      global numberOfGuesses
      if numberOfGuesses<11:	
        txt = list(the_word_withSpaces)
        guessed = list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
          for c in range(len(txt)):
            if txt[c]==letter:
              guessed[c]=letter
            lblWord.set("".join(guessed))
            if lblWord.get()==the_word_withSpaces:
              messagebox.showinfo("Hangman","You guessed it!")
              exit()
        else:
          numberOfGuesses += 1
          imgLabel.config(image=photos[numberOfGuesses])
          if numberOfGuesses==11:
              messagebox.showwarning("Hangman","Game Over")
              mll=Label(window,text="Correct word is:",font=('Copper Black',14)).grid()
              ml=Label(window,text=the_word,font=('Arial Black',14)).grid()



    imgLabel=Label(window)
    imgLabel.grid(row=0, column=0, columnspan=6, padx=20, pady=60)


      
    lblWord = StringVar()
    Label(window, textvariable  =lblWord,font=('consolas 24 bold')).grid(row=0, column=3 ,columnspan=6,padx=10)
    n=0

    def k1(c, c1, c2):
      Label(window, text=c, font=('Helvetica 18'),width=8, relief='groove', bg="black",fg='white').grid(row=c1, column=c2)
      return guess(c)

    for c in ascii_uppercase:
      Button(window, text=c, command=lambda c=c, n=n: k1(c, 1+n//9, n%9), font=('Helvetica 18'),width=8,relief='groove').grid(row=1+n//9,column=n%9)
      n+=1
      



    newGame()
    window.mainloop()


def z():
    a.destroy()
    window=Tk()
    window.title('Hangman-GUESS ANIMALS')
    word_list=['POLARBEAR','JACKAL','CROCODILE','CHIMPANZEE','GORILLA','CHEETAH','MOUNTAINLION']       
    photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"),
    PhotoImage(file="images/hang3.png"), PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"),
    PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"), PhotoImage(file="images/hang8.png"),
    PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]






    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        numberOfGuesses =0
        global the_word
        the_word=random.choice(word_list)
        the_word_withSpaces = " ".join(the_word)
        lblWord.set(' '.join("_"*len(the_word)))

    def guess(letter):
      global numberOfGuesses
      if numberOfGuesses<11:	
        txt = list(the_word_withSpaces)
        guessed = list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
          for c in range(len(txt)):
            if txt[c]==letter:
              guessed[c]=letter
            lblWord.set("".join(guessed))
            if lblWord.get()==the_word_withSpaces:
              messagebox.showinfo("Hangman","You guessed it!")
              exit()
        else:
          numberOfGuesses += 1
          imgLabel.config(image=photos[numberOfGuesses])
          if numberOfGuesses==11:
            messagebox.showwarning("Hangman","Game Over")
            mll=Label(window,text="Correct word is:",font=('Copper Black',14)).grid()
            ml=Label(window,text=the_word,font=('Arial Black',14)).grid()




    imgLabel=Label(window)
    imgLabel.grid(row=0, column=0, columnspan=6, padx=20, pady=60)


      
    lblWord = StringVar()
    Label(window, textvariable  =lblWord,font=('consolas 24 bold')).grid(row=0, column=3 ,columnspan=6,padx=10)
    n=0

    def k1(c, c1, c2):
      Label(window, text=c, font=('Helvetica 18'),width=8, relief='groove', bg="black",fg='white').grid(row=c1, column=c2)
      return guess(c)

    for c in ascii_uppercase:
      Button(window, text=c, command=lambda c=c, n=n: k1(c, 1+n//9, n%9), font=('Helvetica 18'),width=8,relief='groove').grid(row=1+n//9,column=n%9)
      n+=1
      



    newGame()
    window.mainloop()

Label(a,text='HANGMAN',font=('Papyrus',70),bg='black',fg='#567189').pack()
Label(a,text='Rules:You have "11" lives to guess the word',font=('Ink Free',31),bg='black',fg='white').pack()
Label(a,text='Select one category',font=('Bradley Hand ITC',30),bg='black',fg='white').pack()
Button(a,text='Animals',command=z,font=('Forte',20),width=10,bg='black',fg='white').pack(padx=30,pady=10)
Button(a,text='Fruits',command=f,font=('Forte',20),width=10,bg='black',fg='white').pack(padx=30,pady=10)
Button(a,text='Cities',command=c,font=('Forte',20),width=10,bg='black',fg='white').pack(padx=30,pady=10)


a.mainloop()