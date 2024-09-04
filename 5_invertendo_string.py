def inverter_string(string):
    """Inverte os caracteres de uma string.

    Args:
        string (str): A string a ser invertida.

    Returns:
        str: A string invertida.
    """

    if not isinstance(string, str):
        raise TypeError("O argumento deve ser uma string.")

    return string[::-1]

# Entrada do usuário
string = input("Digite uma string: ")

try:
    string_invertida = inverter_string(string)
    print("String invertida:", string_invertida)
except TypeError as e:
    print("Erro:", e)
