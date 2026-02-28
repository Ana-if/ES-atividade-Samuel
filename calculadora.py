import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")
    return a / b


def exibir_menu():
    print("=" * 25)
    print("   CALCULADORA SIMPLES   ")
    print("=" * 25)
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")
    print("=" * 25)


def obter_numeros():
    try:
        num1 = float(input("Primeiro número: "))
        num2 = float(input("Segundo número: "))
        return num1, num2
    except ValueError:
        print("Erro: Insira apenas números válidos.")
        return None, None


def executar():
    while True:
        limpar_tela()
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '0':
            print("Encerrando o programa... Até logo!")
            break

        if opcao in ['1', '2', '3', '4']:
            num1, num2 = obter_numeros()

            if num1 is None:
                input("\nPressione Enter para continuar...")
                continue

            try:
                if opcao == '1':
                    resultado = somar(num1, num2)
                    operacao = "+"
                elif opcao == '2':
                    resultado = subtrair(num1, num2)
                    operacao = "-"
                elif opcao == '3':
                    resultado = multiplicar(num1, num2)
                    operacao = "*"
                elif opcao == '4':
                    resultado = dividir(num1, num2)
                    operacao = "/"

                print(f"\n-> Resultado: {num1} {operacao} {num2} = {resultado}")

            except ZeroDivisionError as e:
                print(f"Erro: {e}")

        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    executar()
