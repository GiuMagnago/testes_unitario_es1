from Calculadora import Calculadora
from String import String
from ForceUser import ForceUser

#Testes classe Calculadora
def test_somar():
    c = Calculadora()
    assert c.somar(3, 5) == 8

def test_substrair():
    c = Calculadora()
    assert c.subtrait(1, 5) == -4

def test_multiplicar():
    c = Calculadora()
    assert c.multiplicar(3, 8) == 24

def test_dividir():
    c = Calculadora()
    assert c.dividir(5, 4) == 1.25


#Testes classe String
def test_checkChar():
    s = String()
    assert s.checkChar("aa123aa", "3") == 4

def test_checkChar2():
    s = String()
    assert s.checkChar("aa123aa", 'b') == -1

def test_length():
    s = String()
    assert s.length("12345") == 5

def test_charChange():
    s = String()
    assert s.charChange("abababa", 'b', 'c') == "acacaca"


# Teste classe ForceUser
def test_getLadoForca():
    f = ForceUser("Obi Wan", "azul")
    assert f.getLadoForca() == "Jedi"

def test_getLadoForca2():
    f = ForceUser("Darth Vader", "Vermelho")
    assert f.getLadoForca() == "Sith"

def test_getLadoForca3():
    f = ForceUser("Darth Revan", "Vemelho/Roxo")
    assert f.getLadoForca() == "Usuário da força sem lado definido"