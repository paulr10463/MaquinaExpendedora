from MaquinaExpendedora import Expendedora

def main():

    xpendedora = Expendedora()
    monedas = input("Ingrese las monedas (5, 10, 25 o 50) separadas por un espacio, y un \"#\" separado por un espacio al final: ").split(" ")
    print("##########################################")
    print("############ R E S U L T A D O ###########")
    print("##########################################\n")
    print(xpendedora.procesar_monedas(monedas))
    print("\n######################################")
    print("## G R A C I A S   P O R   U S A R ##")
    print("######################################")

if __name__ == "__main__":
    main()