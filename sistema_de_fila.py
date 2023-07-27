import string
import random

class fila:
    
    def __init__(self):
        self.pessoas = []
        self.p_prioridade = [] 
        self.caixa = ['Caixa 1', 'Caixa 2', 'Caixa 3', 'Caixa 4']
        self.senhas_priot = []
        self.senhas_normais = []

    def escolha(self):
        nome = input('Bem vindo ao sistema de fila! Digite seu nome: ')
        escolha = input('Escolha sua prioridade: [P]rioridade ou [N]ormal: ').lower()
        
        if escolha == 'p':
            self.p_prioridade.append(nome)
            print(f'{nome} seu atendimento é PRIORIDADE, aguarde sua vez na fila.')
            print(f'Número de pessoas prioridades na sua frente {self.tamanho_p()}')
            print(f'Sua senha é: {self.senha_p()}')
        elif escolha == 'n':
            self.pessoas.append(nome)
            print(f'{nome} seu atendimento é NORMAL, aguarde sua vez na fila.')
            print(f'Número de pessoas sem prioridade na sua frente {self.tamanho_n()}')
            print(f'Sua senha é: {self.senha_n()}')
    
    def senha_p(self, size = 5, chars = string.digits):
        prioridade = 'P-'
        senha_gerada = prioridade + ''.join(random.choice(chars) for _ in range(size))
        self.senhas_priot.append(senha_gerada)
        return senha_gerada
    
    def senha_n(self, size = 5, chars = string.digits):
        prioridade = 'N-'
        senha_gerada = prioridade + ''.join(random.choice(chars) for _ in range(size))
        self.senhas_normais.append(senha_gerada)
        return senha_gerada
        
    def direcionador(self):
        try:
            atendimento = input('Aperte [P] para chamar o próximo cliente prioritário ou [N] para chamar normal').lower()
            if atendimento == 'p':
                if self.p_prioridade == 0:
                    return 'Fila vazia!'
                else:
                    cliente = self.p_prioridade.pop(0)
                    guiche = self.caixa.pop(0)
                    self.caixa.append(guiche)
                    return (f'Atendendo o cliente PRIORITÁRIO: {cliente} no {guiche}')
            elif atendimento == 'n':
                if self.pessoas == 0:
                    return 'Fila vazia!'
                else:
                    cliente = self.pessoas.pop(0)
                    guiche = self.caixa.pop(0)
                    self.caixa.append(guiche)
                    return (f'Atendendo o cliente: {cliente} no {guiche}')
            else:
                return 'Atendente indíponivel!'
        except IndexError:
            return 'Fila vazia !'
        
    def tamanho_p(self):
        return len(self.p_prioridade)
    
    def tamanho_n(self):
        return len(self.pessoas)
    
    def caixas(self):
        caixas = iter(self.caixa)
        print(next(caixas))

fila = fila()

fila.escolha()
fila.direcionador()