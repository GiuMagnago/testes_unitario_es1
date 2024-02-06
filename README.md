##testes_unitario_es1

Utilizei a ferramenta do pytest (Python) para realização da atividade, para instalá-la, basta digitar no terminal "pip install pytest".
A execução dos testes é extremamente simples, após instalar a ferramenta pytest, basta digitar no terminal "pytest .\test.py", ele vai rodar todos os testes e mostrar o resultados deles.
Caso deseje testar casos de erro, é só ir no arquivo test.py e alterar os resultados nas últimas linhas de cada função de teste. Abaixo está um exemplo na função somar da classe Calculadora:

#Teste sucederá
def test_somar():
    c = Calculadora()
    assert c.somar(3, 5) == 8

#Teste falhará
def test_somar():
    c = Calculadora()
    assert c.somar(3, 5) == 6
