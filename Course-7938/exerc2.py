string = input("digite um string: ")
for c in string:
    if c.isupper(): 
        print(f"caractere {c} é maiusculo")
    elif c.islower(): 
        print(f"caractere {c} é minusculo")
    elif c.isnumeric(): 
        print(f"caractere {c} é numero")
    else:
        print(f"caractere {c} é qualquer coisa")