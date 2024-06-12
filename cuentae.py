class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # __ para hacer el atributo privado

    def depositar(self, cantidad):
        # Lógica para depositar dinero en la cuenta
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        # Lógica para retirar dinero de la cuenta
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def obtener_saldo(self):
        return self.__saldo

# Crear una instancia de CuentaBancaria con un saldo inicial
mi_cuenta = CuentaBancaria(1000)

# Intentar acceder directamente al atributo privado (esto dará un error)
try:
    print(mi_cuenta.__saldo)  # Esto causará un AttributeError
except AttributeError as e:
    print(e)

# Usar los métodos públicos para interactuar con el saldo
mi_cuenta.depositar(500)
print(mi_cuenta.obtener_saldo())  # Output: 1500

mi_cuenta.retirar(200)
print(mi_cuenta.obtener_saldo())  # Output: 1300

mi_cuenta.retirar(2000)  # Intentar retirar más de lo que hay en la cuenta
print(mi_cuenta.obtener_saldo())  # Output: 1300 (no cambia debido a fondos insuficientes)
