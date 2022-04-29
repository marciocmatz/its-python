# Classes Abstratas
from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._saldo = saldo
        self._conta = conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa ser numérico.')
        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do deposito precisa ser numérico.')
        self._saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass

# ##############################


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo Insuficiente')
            return
        self.saldo -= valor


conta1 = ContaPoupanca(111, 1, 1000)
