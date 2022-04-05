#Qual melhor cotação
# Real para peso argentino 
class Melhorcambio:
    def __init__(self,peso_cotacao,taxa,real =0):
        self.real = real
        self.taxa = taxa
        self.peso_cotacao = peso_cotacao
        self.operacao = []
        
        
    def peso_receber(self):
        peso_receber = self.real * self.peso_cotacao
        self.operacao.append(["Valo Receber em peso",peso_receber])
        self.valor_apaga = peso_receber
    def taxa_peso(self): 
        taxa_peso = self.taxa * self.peso_cotacao
        self.operacao.append(["Valor da taxa em peso:",taxa_peso])
        self.taxa_apaga = taxa_peso

    def valor_total(self): 
        total = self.taxa_apaga + self.valor_apaga
        self.operacao.append(["Total a paga",total])

    #taxa_dois falta melhor na Exceções e  lógica
    def taxa_dois(self,taxa_soma):
        perguta = input("Soma Taxa do primeiro valor como segundo para saber total [s] uo [n]:")
        if perguta.upper() == "S":
            s = self.valor_apaga + (taxa_soma * self.peso_cotacao) 
            return self.operacao.append(["Total + Taxa",s])
        elif perguta.upper() == "N":
            print('pense bem')


           
    def resumo(self):
        print(f"Teste programa de cotação ")
        print(f'Valor para enviar:R${self.real:6.2f}')
        for o in self.operacao:
            print(f"{o[0]} {o[1]}  ")

  
               
