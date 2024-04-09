numero_acl = input("Ingrese el número de ACL IPv4: ")
if numero_acl.isdigit():
    numero_acl = int(numero_acl)
    if 1 <= numero_acl <= 99:
        print(f"El número {numero_acl} corresponde a una ACL Estándar.")
    elif 100 <= numero_acl <= 199:
        print(f"El número {numero_acl} corresponde a una ACL Extendida.")
    else:
        print("El número no corresponde a una lista de acceso.")
else:
    print("El número de ACL IPv4 debe ser un valor numérico.")
