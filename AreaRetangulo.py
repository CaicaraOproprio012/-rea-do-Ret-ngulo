def calcular_area_retangulo():
    print("=== CÁLCULO DA ÁREA DE UM RETÂNGULO ===")
    
    try:
        base = float(input("Informe o valor da base (em unidades): "))
        altura = float(input("Informe o valor da altura (em unidades): "))
        
        area = base * altura
        
        print(f"\nA área do retângulo é: {area:.2f} unidades²")
    
    except ValueError:
        print("\n⚠️ Erro: Digite apenas números válidos para base e altura.")


if __name__ == "__main__":
    calcular_area_retangulo()
