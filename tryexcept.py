while True:
    try:
        number = int(input("Digite um número para dividí-lo por um:"))
        result = 1/number
    except ZeroDivisionError:
        print("Digite um número diferente de Zero")
    except ValueError:
        print('Digite um número válido.')
    except Exception as err:
        print(f"Erro genérico: {err=}")
    else:
        print(result)
        break
    finally:
        print("Yan Victor Sampaio do Nascimento.")
