# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:46:30 2015

@author: viniciusra
"""
import random

print ('Vamos jogar?')
print ('Regras do jogo:')
print ('papel cobre pedra')
print ('papel refuta spock')
print ('spock vaporiza pedra')
print ('spock esmaga tesoura')
print ('tesoura corta papel')
print ('tesoura decapita lagarto')
print ('lagarto envenena spock')
print ('lagarto come papel')
print ('pedra quebra tesoura')
print ('pedra esmaga lagarto')

pontuacao_minha = 0
pontuacao_pc = 0
pp="papel"
p = 'pedra'
t = 'tesoura'
sp= 'spock'
l = 'lagarto'
computador = [pp, p, t, sp, l]

pedra=0
spock=0
lagarto=0
tesoura=0
papel=0

while pontuacao_minha != 3 and pontuacao_pc != 3:
    x=raw_input('escolha sua opcao\n')
    pc = random.choice(computador)
    print ('o pc escolheu', pc)
    
    if pc == pp and ( x == 'pedra' or x=='spock'):
        pontuacao_pc +=1
        print('vacilou!')
        
    if pc == pp and (x == 'tesoura' or x == 'lagarto'):
        pontuacao_minha +=1
        print ('ae zika')
        
    if pc == sp and (x == 'pedra' or x == 'tesoura'):
        pontuacao_pc += 1
        print ('putz')
    
    if pc == sp and (x == 'lagarto' or x == 'papel'):
        pontuacao_minha += 1
        print('booa')
        
    if pc == t and (x== 'papel' or x == 'lagarto'):
        pontuacao_pc += 1
        print ('vixee')
        
    if pc == t and (x == 'pedra' or x == 'spock'):
        pontuacao_minha += 1 
        print ('vai segurando!')
        
    if pc == l and (x == 'spock' or x == 'papel'):
        pontuacao_pc += 1
        print ('deu ruim')
        
    if pc == l and (x == 'pedra' or x == 'tesoura'):
        pontuacao_minha += 1
        print ('mlkao sem freio !')
        
    if pc == p and (x == 'tesoura' or x == 'lagarto'):
        pontuacao_pc += 1
        print('que feio')
        
    if pc == p and (x == 'papel' or x == 'spock'):
        pontuacao_minha += 1
        print ('olha isso')
        
if pontuacao_minha == 3 or pontuacao_pc == 3:
    print ('o jogo terminou!')
    print ('seu placar foi:', pontuacao_minha )
    print ('o pc fez:', pontuacao_pc)
 