"""
Números Felizes
Contribuição de: Marianna Reis
Você está resolvendo este problema.
Este problema foi utilizado em 420 Dojo(s).

Para saber se um número é feliz, você deve obter o quadrado de cada dígito deste número, em seguida você faz a soma desses resultados. A seguir o mesmo procedimento deve ser feito com o valor resultante desta soma. Se ao repetir o procedimento diversas vezes obtivermos o valor 1, o número inicial é considerado feliz.

Tomamos o 7, que é um número feliz:

7² = 49
4² + 9² = 97
9² + 7² = 130
1² + 3² + 0² = 10
1² + 0² = 1
Podemos observar nesse exemplo que os números 49, 97, 130 e 10 também são felizes. Existem infinitos números felizes.

E um número triste? Como sabemos que um número não será feliz?

Desenvolva um programa que determine se um número é feliz ou triste.


TDD
"""


def calc_pow(num: int) -> int:
    """
          Recebe um numero e deve retornar o numero ao quadrado
    """
    return pow(num, 2)


def map_number(value: str) -> list:
    """
    Map number recebe
    """
    return list(map(int, value))


def sum_digits_calculated(lista: list) -> int:
    soma = 0
    for item in lista:
        quadrado = calc_pow(item)
        soma += quadrado
    return soma


def is_happy(num: int) -> bool:
    final_number = num

    if type(num) is not int:
        return False

    seen_numbers = []
    while final_number != 1:
        # print(final_number)
        digits = map_number(str(final_number))
        final_number = sum_digits_calculated(digits)

        if final_number in seen_numbers:
            return False

        seen_numbers.append(final_number)

    # print(final_number)
    return True


def main():
    nums = [4, 123, 19, 32, '4']
    for n in nums:
        print(n)
        result = is_happy(n)
        if result:
            print("Número Feliz")
        else:
            print("Número Triste")


if __name__ == '__main__':
    main()
