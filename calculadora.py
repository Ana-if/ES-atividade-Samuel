import os

def somar(a, b): return a + b
def subtrair(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): 
    return a / b if b != 0 else "Erro: Divisão por zero!"

def exibir_menu():
    print("\n" + "="*25)
    print("   CALCULADORA SIMPLES   ")
    print("="*25)
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")
    print("="*25)

def executar():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '0':
            print("Encerrando o programa... Até logo!")
            break

        if opcao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Primeiro número: "))
                num2 = float(input("Segundo número: "))

                if opcao == '1':
                    print(f"-> Resultado: {num1} + {num2} = {somar(num1, num2)}")
                elif opcao == '2':
                    print(f"-> Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
                elif opcao == '3':
                    print(f"-> Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
                elif opcao == '4':
                    print(f"-> Resultado: {num1} / {num2} = {dividir(num1, num2)}")
            
            except ValueError:
                print("Erro: Por favor, insira apenas números válidos.")
        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")
    

if __name__ == "__main__":
    executar()
