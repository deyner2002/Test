import requests


def EsPrimo(arg):
   reqprimo = requests.post("http://127.0.0.1:8000/IsPrime?numero="+arg)
   print(reqprimo.json())
   return reqprimo.json()

def Fibonacci(arg):
    reqfibonacci = requests.post("http://127.0.0.1:8000/fibonacci?posicionFinal="+arg)
    print(reqfibonacci.json())
    return reqfibonacci.json()
