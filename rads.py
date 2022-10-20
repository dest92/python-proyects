print("Welcome")
print("to rad/s-rpm")
print("conversor")


print("1- Rad to RPM")
print("2- RPM to Rad")

menu = int(input())

if menu == 1:
     rad = float(input("RAD: "))
     radrpm = float((rad*60) / (2*3.14))
     print("RPM: ",radrpm )
     
if menu == 2:
    
    rpm = float(input("RPM:"))
    rpmrad = rpm * (3.14/30)
    print("RAD: ",rpmrad)
          