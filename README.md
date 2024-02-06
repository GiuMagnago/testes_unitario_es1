# testes_unitario_es1

Utilizei a ferramenta do pytest (Python) para realização da atividade, para instalá-la, basta digitar no terminal "pip install pytest".<br>
A execução dos testes é extremamente simples, após instalar a ferramenta pytest, basta digitar no terminal "pytest .\test.py", ele vai rodar todos os testes e mostrar o resultados deles.<br>
Caso deseje testar casos de erro, é só ir no arquivo test.py e alterar os resultados nas últimas linhas de cada função de teste. Abaixo está um exemplo na função somar da classe Calculadora:<br>

## Teste sucederá
def test_somar():<br>
&ensp;&ensp;c = Calculadora()<br>
&ensp;&ensp;assert c.somar(3, 5) == 8<br>

## Teste falhará
def test_somar():<br>
&ensp;&ensp;c = Calculadora()<br>
&ensp;&ensp;assert c.somar(3, 5) == 6<br>
