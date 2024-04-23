class BankAccount:
    def __init__(self,numer,waluta,__saldo,__wlasciciel):
        self.numer= numer
        self.waluta= waluta
        self.__saldo = __saldo
        self.__wlasciciel=__wlasciciel
    
    
    def get_saldo(self):
        return self.__saldo
        
    def set_saldo(self,__saldo):
         self.__saldo = __saldo

    def get_wlasciciel(self):
        return self.__wlasciciel
    
    def set_wlasciciel(self,__wlasciciel):
        self.__wlasciciel=__wlasciciel

    def __str__(self) :
       return f"Konto o numerze {self.numer} nalezy do Pana {self.__wlasciciel}, Saldo wynosi{self.__saldo} w {self.waluta}"
    def __len__(self):
        return len(self.__saldo)
kont= BankAccount("2141251515212", "euro","4214","jacob")
print(len(kont))