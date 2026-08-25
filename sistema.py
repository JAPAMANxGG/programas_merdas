escolha = int(input("bem vindo ao sistema de Paulo, por favor escolha uma opção:" \
"\nOpção 1 = calculadora" \
"\nOpção 2 = conversor de temperatura"
"\nOpção 3 = conversor Dolar ou Real\n"))

if escolha == 1:

    num1 = float(input("digite primeiro numero: "))
    num2 = float(input("digite segundo numero: "))
    while True:
        print("escolha uma opção de operação")
        print("opção 1 = (+)")
        print("opção 2 = (-)")
        print("opção 3 = (*)")
        print("opção 4 = (/)")
        ope = input()

        if ope in ["1", "2", "3", "4"]:
            if ope == '1':
                print(num1,"+",num2,"=",num1+num2)
                break

            elif ope == '2':
                print(num1,"-",num2,"=",num1-num2)
                break

            elif ope == '3':
                print(num1,"*",num2,"=",num1*num2)
                break
                
            elif ope == '4':
                if num2 == 0:
                    print("Não pode ser divisivel por 0 tente novamente!")
                else:
                    print(num1,"/",num2,"=",num1/num2)
                    break

        else:
            print("operador invalido! As opçoes de operação vão de 1 a 4!")

if escolha == 2:
   temperatura = input("Digite C (Fahrenheit para Celsius) ou F (Celsius para Fahrenheit)\n")

   if temperatura == "C":
       fahr = float(input("informe quantos Fahrenheit quer converter: "))
       cel = (fahr - 32) / 1.8
       print(fahr,"°F e igual a",cel,"°C")

   elif temperatura == "F":
        cel = float(input("informe quantos Celsius quer converter: "))
        fahr = (cel * 1.8) + 32
        print(cel,"°C e igual a",fahr,"°F")
   else:
       print("Algo deu errado!")  

if escolha == 3:
   moeda = input("Digite D (Real para Dolar) ou R (Dolar para Real): ")

   if moeda == "D":
       Real = float(input("Quantos Reais quer converter?\n"))
       Dolar = Real / 5.22
       print(Real,"R$ equivalem a",Dolar,"$")

   elif moeda == "R":
       Dolar = float(input("Quantos Dolares quer converter?\n"))
       Real = Dolar * 5.22
       print(Dolar,"$ equivalem a",Real,"R$")