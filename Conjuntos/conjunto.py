class Conjunto():
    def __init__(self):
        self.listaConjunto = [None, None, None, None, None, None, None, None, None,]
        self.nomeConjunto = ""
        self.quant = 0     

    def getNomeConjunto(self, dados):
        self.nomeConjunto =  dados
        
    def getReceberConjunto(self, dados):
        aux = dados
        if aux in self.listaConjunto:
            
            print('\n Valor "' + aux  + '" já existe no conjunto')
        else:
            self.listaConjunto[self.quant] = dados
            self.quant += 1
        
            
    def setTamanhoConjunto(self):
        return print(' Tamanho do Conjunto: ' + str(self.quant))
        
    def show(self):
        if self.quant == 0:
            print (' Conjunto Vazio: ' + self.nomeConjunto + ' ={ }')
        else:
            aux = ''
            for i in range(self.quant):
                if i+1<self.quant:
                    aux = aux+self.listaConjunto[i]+', '
                else:
                    aux = aux+self.listaConjunto[i]
                
            print('{ ',aux,' }')
                
                
                
'''aux = dados
        self.listaConjunto[self.quant] = dados
        if dados in dados:
            print('Valor já existe no conjunto')
        else:
            self.quant += 1'''
