contraseña = input("introdusca la contraseña: ")

if contraseña == "python123":
    print("aceso permitodo")
else:
    print("contraseña incorrecta")
    intentos = 2
    print("*tines 2 intentos mas* ")
    while intentos > 0:
        contraseña = input("introdusca la contraseña: ")
        if contraseña == "python123":
            print("aceso permitodo")
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"contraseña incorrecta, te quedan {intentos} intentos")
            else:
                print("has agotado todos los intentos, aceso denegado")