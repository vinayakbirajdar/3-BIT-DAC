from tkinter import*
from math import *
root=Tk()
root.geometry("1300x750")
root.minsize(700,550)
def hello():
    v_1=Label(f2,text="vout = -vr{d0/2+d1/4+d2/8}",font=("comicsansms","40"),bg="white"
              ,fg="black")
    v_1.pack()
def hey():
    v_2=Label(f2,text="It is an 3 bit binary weighted DAC "
              "\nIt converts binary input into anlog output "
             "Further an \nI to V converter op amp is used "
             "\nRole of the op amp is to convert I into V",bg="black",fg="white",
              font=("Roman","30"))
    v_2.pack()
def hii():
    submit=ent.get()
    vb_3 =Label(f1,text=("the given referance vtg is :",(submit)))
                    
    vb_3.pack()
def cal():
    t1=int(ent.get())
    vb_4 =Label(f1,text=("the output is :" ,(0.875*t1)),font=("comicsansms","30")
                ,bg="black",fg="white")
    vb_4.pack()
    
us_1=Label(text="$Ref.Vtg$",font=("comicsansms","30"))
us_1.pack(side=BOTTOM)
ent=Entry()
ent.config(font=("ink free",30))
ent.pack(side=BOTTOM)
root.title("3 bit binary weighted DAC 1408")
photo=PhotoImage(file="//Users//vinayakbirajdar//Desktop//image//dac.png")
p_1=Label(image=photo)
p_1.pack(side=TOP)
f0 = Frame(root,borderwidth=3,bg="gray",relief="groove",width='100')
f0.pack(fill="y",side="left")
f1 = Frame(root,borderwidth=3,bg="gray",relief="groove",width='100')
f1.pack(fill="y",side="right")
f2 = Frame(root,borderwidth=3,bg="grey",relief="groove",width='100')
f2.pack(fill="x",side="top")
f3 = Frame(root,borderwidth=3,bg="grey",relief="groove",width='100')
f3.pack(fill="x",side="bottom")
t_1=Label(f3,text="As this is an binary weighted DAC the minimum input is [000] ,\nso here we "
          "are only going to calculate for maximun input[111]"
          "\nEntre the requried value for reference voltage below.."
          "\n and click the [vr submit] button on left",font=("comicsansms","30"),
          bg="white",fg="black")
t_1.pack()
b1=Button(f0,fg='red',text="#INFO#",font=("comicsansms","30")
                ,relief = GROOVE,bg="black",command=hey)
b1.pack(anchor="w")
b2=Button(f0,fg='red',text="#HINT#",font=("comicsansms","30")
                ,relief = GROOVE,bg="black",command=hello)
b2.pack()

b3=Button(f0,fg='red',text="Vr\nsubmit",font=("comicsansms","30")
                ,relief = GROOVE,bg="black",command=hii)
b3.pack()


b4=Button(f0,fg='red',text="calculate",font=("comicsansms","30")
                ,relief = GROOVE,bg="black",command=cal)
b4.pack()
b_1=Label(text="CREATED BY VINAYAK BIRAJDAR ROLL NO=03 [ELN S.Y]",font=("comicsansms","30"))
b_1.pack()
root.mainloop()
