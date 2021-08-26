from app import session
from app import Pay
import os

def select_f():

    print("----------- Choose an option -----------")
    print("1. Id contrato")
    print("2. Id cliente")
    print("----------------------------------------\n")

    opc = int(input("Ingresa una opción: "))
    os.system('CLS')

    if opc == 1:
        id = int(input("Ingresa el número de contrato: "))
        payments = session.query(Pay).filter(
            Pay.id_contrato == id
        )

    elif opc == 2:
        id = int(input("Ingresa el número de cliente: "))
        payments = session.query(Pay).filter(
            Pay.id_cliente == id
        )

    else: 
        print("Opción fuera de rango")

    if (opc == 1) or (opc == 2):
        print("id_pago \t id_contrato \t id_cliente \t fecha \t \t \t monto")
        for pay in payments:
            print(pay.id_pago,"\t\t",pay.id_contrato,"\t\t",pay.id_cliente,"\t\t", pay.fecha,"\t\t", pay.monto)
    