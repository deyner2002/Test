import pytest
from methods import EsPrimo,Fibonacci



@pytest.mark.parametrize(
    "input, expected",
    [
        #se ingresa 8 y se espera 21 (correcto)
        ("8",21),
        #se ingresa 8 y se espera 22 
        ("8",22),
        #se ingresa 9 y se espera 21
        ("9",21),
        #se ingresan caracteres y se espera 21
        ("ocho",21),
        #se ingresa un decimal y se espera 21
        ("8.1",21),
    ]
)

def test_fovonacci(input,expected):
    assert Fibonacci(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        #Se envia primo y se espera true
        ("3",True),
        #Se envia par y se espera false
        ("4",False),
        #Se envia par y se espera true
        ("4",True),
        #Se envia primo y se espera false
        ("3",False),
        #Se envian caracteres y se espera true
        ("tres",True),
        #Se envian caracteres y se espera false
        ("tres",False),
        #Se envia numero decimal y se espera true
        ("3.3",True),
        #Se envia numero decimal y se espera false
        ("4.4",True),
        
        
           
    ]
)

def test_fovonacci(input,expected):
    assert EsPrimo(input) == expected















"""""
@pytest.mark.parametrize(
    "input, expected",
    [
        #Se espera primo
        ("4",True),
        #se espera par
        ("3",False),
    ]
)

def test_es_primo(input,expected):
    assert EsPrimo(input) == expected



"""""










