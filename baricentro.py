
def Menu():
    print("Bienvenido a la calculadora de baricentros, qué desea hacer? \n")
    print("1- Calcular baricentro triángulo    2- Imprimir formulas")
    menu_option = int(input())
    
    if menu_option == 1:
      x1 =  int(input("Introduce el valor de x1: \n"))
      x2 =  int(input("Introduce el valor de x2: \n"))
      x3 =  int(input("Introduce el valor de x3: \n"))
      y1 =  int(input("Introduce el valor de y1: \n"))
      y2 =  int(input("Introduce el valor de y2: \n"))
      y3 =  int(input("Introduce el valor de y3: \n"))
        
      baricentro_triangX = round((x1+x2+x3)/3,2)
      baricentro_triangY = round((y1+y2+y3)/3,2)
      baricentro_final = (f"X:{baricentro_triangX},Y:{baricentro_triangY}")
      print(f"El baricentro del triangulo es: {baricentro_final} \n")
      Menu()
      
    if menu_option == 2:
        print("Formula triangulo = G(x1+x2+x3/3 , y1+y2+y3/3 \n")
        Menu()
Menu()
