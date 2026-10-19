from datetime import date
from datetime import timedelta
def calcularData():
    dataHoje = date.today()
    numeroUser = int(input("\nSomar quantos dias?: "))
    dataResultado = dataHoje + timedelta(days=numeroUser)
    print("\nData: ", dataResultado)