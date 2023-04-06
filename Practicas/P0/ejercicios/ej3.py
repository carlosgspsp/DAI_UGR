import random

def comprobar(myStr):
    brackets = ['[]'] 
    while any(x in myStr for x in brackets): 
        for br in brackets: 
            myStr = myStr.replace(br, '') 
    return not myStr


if __name__ == '__main__':

    lista = ""

    tama = random.randint(2,20)
    for i in range(tama):
        n = random.randint(0,100)
        if n <= 50:
            lista+="["
        else:
            lista+="]"
    print("numero de caracteres = "+ str(tama))
    print(lista)
    print(comprobar(lista))



