class ForceUser():
    def __init__(self, nome, corSabre):
        self.nome = nome
        self.corSabre = corSabre
    
    def getLadoForca(self):
        if (self.corSabre.upper() == "AZUL" or self.corSabre.upper() == "VERDE"):
            return "Jedi"
        elif (self.corSabre.upper() == "VERMELHO"):
            return "Sith"
        else:
            return "Usuário da força sem lado definido"