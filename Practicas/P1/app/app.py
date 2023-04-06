#./app/app.py
from flask import Flask
from flask import render_template
import random
import re

app = Flask(__name__)
          
@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/erastotenes/<int:n>')
def erastotenes(n):
  lista = list(range(2, n+1))

  i = 0
  while(lista[i]*lista[i] <= n):
    # Mientras el cuadrado del elemento actual sea menor que el ultimo elemento
    for j in lista:
        if j <= lista[i]:
            # Cada iteracion del while hace que el for comience desde el primer elemento. 
            # Esto es para omitir los numeros primos ya encontrados
            continue
        elif j % lista[i] == 0:
            # Si un numero es divisible entre el elemento actual del while
            # de ser asi, entonces eliminarlo de la lista (esto altera la lista)
            lista.remove(j)
        else:
            # Si no es divisible, entonces omitirlo (no hacer nada)
            pass
    i += 1 # Incrementa al siguiente elemento de la lista (que ha sido alterada)

    return lista

@app.route('/fibonacci/<int:n>')
def fibonacci(n):

  output = open('./outputej2.txt','w')
    
  resultado = str(fib(n))
  output.write(resultado)
  output.close()
  return resultado


@app.route('/corchetes')
def corchetes():
  lista = ""

  tama = random.randint(2,20)
  for i in range(tama):
        n = random.randint(0,100)
        if n <= 50:
            lista+="["
        else:
            lista+="]"
  return(str(comprobarCorchetes(lista)))


@app.route('/expresiones/<cadena>/<int:expReg>')
def expReg(cadena,expReg):
    if expReg==1:
      return str(palabraMayuscula(cadena))
    elif expReg == 2:
      return str(correoValido(cadena))
    elif expReg == 3:
      return str(tarjetaCredito(cadena))
    else:
      return "Numnero incorrecto"  
    
@app.errorhandler(404)
def error_404_handler(e):
    return render_template('404.html'), 404

@app.route('/pollo')
def imagen  ():
    return render_template('pollo.html')

def fib(n):

	if n <= 1:
		return n

	return fib(n - 1) + fib(n - 2)

def comprobarCorchetes(myStr):
  brackets = ['[]'] 
  while any(x in myStr for x in brackets): 
      for br in brackets: 
         myStr = myStr.replace(br, '') 
  return not myStr

def palabraMayuscula(cadena):
    return bool(re.match(r"[\w\s]+[A-Z]", cadena))

def correoValido(cadena):
    return bool(re.match(r"^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,3})$", cadena))

def tarjetaCredito(cadena):
    return bool(re.match(r"^\d{4}([\ -]?)\d{4}\1\d{4}\1\d{4}$", cadena))