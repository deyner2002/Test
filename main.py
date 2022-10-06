from fastapi import FastAPI
from math import sqrt

app = FastAPI()

posts = []


@app.get('/hello')
def get_hello():
    return {'Hello FastAPI'}

@app.post('/IsPrime')
def is_Prime(numero: int):
    for n in range(2,numero):
        if numero % n == 0:
            print("No es primo ",n, "es divisor")
            return False
    print("Es primo")
    return True


def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

@app.post('/fibonacci')
def Fibonacci(posicionFinal: int):
    n = 1
    numero = int
    while n <= posicionFinal:
        cur = int(F(n))
        print(cur)
        numero = cur
        n += 1
    return numero

@app.get('/hola')
def read_root():
    return 'hello world'
