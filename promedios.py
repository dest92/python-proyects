#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("Bienvenido/a")


alumno = input("Nombre del alumno: ")
print(f"Usted ha introducido al alumno {alumno}")
continuar = input("Desea continuar? Si/No ")
if continuar.lower() == "si" or continuar.lower() == "sí":
    print("Comience a ingresar las notas: ")
    nota1 = int(input(" Ingrese la primera nota:" ))
    nota2 = int(input("Ingrese la segunda nota:" ))
    nota3 = int(input("Ingrese la tercera nota:" ))
    sumadenotas = nota1 + nota2 + nota3
    promedio = sumadenotas // 3
    print("El promedio del alumno es de",promedio)
    if promedio >= 6:
        print("El alumno ha aprobado")
    
    if promedio <= 5:
        print("El alumno ha desaprobado")
    
  
  





# In[ ]:





# In[ ]:





# In[ ]:




