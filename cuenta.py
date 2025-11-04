import random

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.account_number = random.randint(10000000, 99999999)
        self.transactions = []

    def __repr__(self):
        return "Cuenta de %s (#%d). Saldo: $%.2f" % (self.name, self.account_number, self.balance)

    def show_balance(self):
        print("Saldo actual: $%.2f" % self.balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Monto de depósito inválido")
            return
        print("Depositando $%.2f" % amount)
        self.balance += amount
        self.transactions.append(f"Depósito: ${amount:.2f}")
        self.show_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            print("Fondos insuficientes")
            return
        print("Retirando $%.2f" % amount)
        self.balance -= amount
        self.transactions.append(f"Retiro: ${amount:.2f}")
        self.show_balance()

    def mostrar_historial(self):
        print("Historial de movimientos:")
        if not self.transactions:
            print("No hay transacciones registradas.")
        else:
            for transaccion in self.transactions:
                print(transaccion)

# Ejemplo de uso
mi_cuenta = BankAccount("Brahian", 500)
print(mi_cuenta)
mi_cuenta.show_balance()
mi_cuenta.deposit(1000)
mi_cuenta.withdraw(300)
mi_cuenta.mostrar_historial()
print(mi_cuenta)
