"""

Exercício 2: Contando caracteres
Escreva uma função chamada contar_caracteres que receba
uma string como argumento e retorne um dicionário com a
contagem de cada caractere. Por exemplo, se a string for
"banana", a função deve retornar {'b': 1, 'a': 3, 'n': 2}.

"""


def contar_caracteres(string: str) -> dict[str, int]:

    caracteres_contados: dict[str, int] = dict()

    for caracter in string:

        if caracteres_contados.get(caracter):

            repeti_caracter = caracteres_contados[caracter]
            caracteres_contados[caracter] = repeti_caracter + 1

        else:
            caracteres_contados[caracter] = 1

    return caracteres_contados


def executar_programa() -> None:
    while True:
        texto = str(input(
            'Digite uma cadeia de caracteres para contar.\n'
            '0 -> para sair\n\t\t'
        ))

        if texto == '0':
            print('Fim da execução.\n')
            break

        contagem = contar_caracteres(texto)
        print(f'\n{contagem}', end='\n\n')


executar_programa()