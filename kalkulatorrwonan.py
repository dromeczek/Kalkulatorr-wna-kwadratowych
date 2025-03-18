import tkinter as tk
import math
def sito(n):
    sito=[True]*(n+1)

    sito[0]=sito[1]=False
    for i in range(2,int(n**0.5)+1):
        if sito[i]:
            for j in range(i*i,n+1,i):
                sito[j]=False
    return [i for i in range(n+1) if sito[i]]
def pierwiastek(n,sito):
    b={}
    for i in sito:
        while(n%i==0 and n>0):
            if i in b.keys():
                b[i]+=1
            else:
                b[i]=1
            n/=i
    wynik=1
    pierwiastek=1
  
    for i in b.keys():
        while(b[i]>=2):
            wynik*=i
            b[i]-=2
        if(b[i]==1):
            pierwiastek*=i
    return wynik,pierwiastek
def rownanie(a, b, c, sito):
    delta = b * b - 4 * a * c
    if delta < 0:
        wynik_label.config(text="Brak rozwiązań (delta < 0)")
    elif delta == 0:
        wynik_label.config(text=f"x = {-b / (2 * a)} (delta = 0)")
    else:
        pzd = pierwiastek(delta, sito)
        if pzd[1] == 1 and pzd[0] == 1:
            x1 = (-b - 1) / (2 * a)
            x2 = (-b + 1) / (2 * a)

            wynik_label.config(text=f"x₁ = {x1}\nx₂ = {x2}")
        elif pzd[1] == 1:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            print(pzd)
            wynik_label.config(text=f"x₁ = {x1}\nx₂ = {x2}")
        elif pzd[0] == 1:
            wynik_label.config(text=f"x₁ = (-{b} + √{pzd[1]}) / {2 * a}\nx₂ = (-{b} - √{pzd[1]}) / {2 * a}")
            
        else:
          
            wynik_label.config(text=f"x₁ = (-{b} + {pzd[0]}√{pzd[1]}) / {2 * a}\nx₂ = (-{b} - {pzd[0]}√{pzd[1]}) / {2 * a}")
def oblicz():
    try:
        a=int(entry1.get())
        b=int(entry2.get())
        c=int(entry3.get())
        if(a>b and a>c):
            max=a
        elif(b>a and b>c):
            max=b
        else:
            max=c
        z=sito(max**3)
        wynik=rownanie(a,b,c,z)
        
    except ValueError:
        wynik_label.config(text="Błąd")

root=tk.Tk()
root.title("Równania kwadratowe")
entry1=tk.Entry(root,width=5)
entry1.pack(side=tk.LEFT, padx=5)
label1=tk.Label(root,text="x\u00B2")
label1.pack(side=tk.LEFT)

entry2 =tk.Entry(root, width=5)
entry2.pack(side=tk.LEFT, padx=5)
label2=tk.Label(root,text="x")
label2.pack(side=tk.LEFT)

entry3=tk.Entry(root,width=5)
entry3.pack(side=tk.LEFT,padx=5)
btn=tk.Button(root,text="Oblicz",command=oblicz)
btn.pack(side=tk.LEFT, padx=10)
wynik_label=tk.Label(root,text="WYNIK: ")
wynik_label.pack(side=tk.LEFT)
root.mainloop()