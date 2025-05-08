import time
import os
import unicodedata
import sys  

biblioteca_livros = {}
processos_possiveis = ["Adicionar livros", "Listar livros", "Remover livros", "Atualizar quantidade de livros", "Registrar  empréstimos", "Exibir histórico de empréstimos","Sair"]
historico_emprestimo = []

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def normalizar(texto):
    return texto.strip().upper()

def lista_livros(biblioteca_livros):
    for indice, livro in enumerate(sorted(biblioteca_livros), start=1):
        print(f'{indice}º){livro}\n Quantidade disponível: {biblioteca_livros[f"{livro}"]["Quantidade disponível"]} unidades.\n Autor: {biblioteca_livros[f"{livro}"]["Autor"]} \n')
        
def menu():  
    while True:
        clear_terminal()
        print("Olá, seja bem-vindo a Biblioteca Alves!\n")   
        time.sleep(0.5)
        
        for indice, processos in enumerate(processos_possiveis,start=1):
            print(f'{indice}º) {processos}')
        
        try:
            escolha_menu = int(input("\nQual processo voce deseja realizar? (Digite o número em frente do processo respectivo que você deseja utilizar)\n"))
            
            if escolha_menu == 1:
                adicionar_livro(biblioteca_livros)
            elif escolha_menu == 2:
                listar_livro(biblioteca_livros)
            elif escolha_menu == 3:
                remover_livro(biblioteca_livros)
            elif escolha_menu == 4:
                atualizar_qtd(biblioteca_livros)
            elif escolha_menu == 5:
                registrar_empréstimo(biblioteca_livros)
            elif escolha_menu == 6:
                exibir_historico(historico_emprestimo)
                
            elif escolha_menu == len(processos_possiveis) - 1:
                print("Encerrando o sistema. Até mais!")
                sys.exit()
            else:
                print("Opção inválida. Tente novamente.")
                time.sleep(2)
                continue 
        except ValueError:
            print("Coloque apenas valores númericos e inteiros, tente novamente...")
            time.sleep(2)
            continue
        
        repetir = menu_perguntar_denovo(escolha_menu)
        if not repetir:
            break

def perguntar_denovo():
    
    while True:
        resposta = normalizar(input("\nVocê deseja realizar este processo mais uma vez? (S/N)\n"))
        
        resposta = unicodedata.normalize('NFKD', resposta).encode('ascii', 'ignore').decode('utf-8')

        if resposta in ['S', 'SIM']:
            return True
        elif resposta in ['N', 'NAO']:
            return False
        else:
            print("Coloque como resposta apenas: S ou N")
            
def menu_perguntar_denovo(escolha_menu):
    
    while True:
        clear_terminal() 
        time.sleep(0.5)
        
        resposta = normalizar(input(f"Você finalizou o {escolha_menu}º processo do menu atual.\nVocê deseja continuar e utilizar outros processos? (S/N)\n"))
        resposta = unicodedata.normalize('NFKD', resposta).encode('ascii', 'ignore').decode('utf-8')

        if resposta in ['S', 'SIM']:
            return True
        elif resposta in ['N', 'NAO']:
            return False
        else:
            print("Coloque como resposta apenas: S ou N")

def adicionar_livro(biblioteca_livros):
    
    while True:
        
        clear_terminal()
        try:
            escolha = input("Qual o nome do livro que voce deseja adicionar?\n\n").upper()
            qtd_disponivel= int(input(f"\nQual a quantidade do livro {escolha} que há disponível?\n\n"))
            autor = input(f"\nQual o nome do autor do livro?\n\n").upper()
            
            biblioteca_livros[escolha] = {
                "Quantidade disponível": qtd_disponivel,
                "Autor": autor                       
            }
        except ValueError:
            print("Digite apenas dígitos válidos!")
            time.sleep(2)
            continue
            
        print("\nO livro foi cadastrado com sucesso!")
        
        time.sleep(3)
        repetir = perguntar_denovo()
        if not repetir:
            break
        
            
        

def listar_livro(biblioteca_livros):
    

    if len(biblioteca_livros) == 0:
        print("Não há nenhum livro disponível no sistema!")
        
    lista_livros(biblioteca_livros)

def remover_livro(biblioteca_livros):
    
    while True:
        
        if len(biblioteca_livros) == 0:
            print("Não há nenhum livro disponível para se remover!")
            break
       
        clear_terminal()
        print("Os livros disponíveis para remover são:\n")
        lista_livros(biblioteca_livros)
        
        nome_livro = normalizar(input("\nQual livro você deseja remover?\n"))
        if nome_livro in biblioteca_livros:
            del biblioteca_livros[f'{nome_livro}']
            print(f'\nO livro {nome_livro} foi apagado com sucesso!!')
            time.sleep(2)
            
        else:
            print("Esse livro não existe no sistema ou foi digitado errado!")
            time.sleep(2)
            continue
            
        repetir = perguntar_denovo()
        if not repetir:
            break

def atualizar_qtd(biblioteca_livros):
    
    while True:
        clear_terminal()
        
        if len(biblioteca_livros) == 0:
            print("Não há nenhum livro disponível no sistema")
            break
        
        print("Qual livro voce deseja atualizar a quantidade?\n")
        lista_livros(biblioteca_livros)
            
        resposta = normalizar(input("\n"))
        
        if resposta not in biblioteca_livros:
            print("O livro digitado não existe ou foi digitado incorretamente, tente novamente...")
            time.sleep(1)
            continue
        else:
            try:
                qtd_nova = int(input("\nQual a quantidade nova?"))
            except ValueError:
                print("Digite apenas números válidos.")
                time.sleep(2)
                continue
            
            biblioteca_livros[resposta]["Quantidade disponível"] = qtd_nova
            print(f"A quantidade do livro {resposta} foi alterado para {qtd_nova} unidades.")
            time.sleep(3)
        
        repetir = perguntar_denovo()
        if not repetir:
            break 

def registrar_empréstimo(biblioteca_livros):
    
    while True:
        clear_terminal()
        
        if len(biblioteca_livros) == 0:
            print("Não há nenhum livro disponível no sistema")
            break
        try:
            print("Qual livro voce deseja fazer um empréstimo?\n")
            lista_livros(biblioteca_livros)
            nome_livro = normalizar(input(""))
            resposta = int(input("Qual a quantidade desejada?\n"))
            
            if nome_livro not in biblioteca_livros:
                print("\nEsse livro ou não está no nosso sistema, ou você digitou errado, tente novamente.")
                
                continue
        
            elif resposta > biblioteca_livros[f"{nome_livro}"]["Quantidade disponível"]:
                print("Não possuímos essa quantidade de livros, tente novamente")
                continue
            elif resposta <= 0:
                print("Dígito inválido, tente novamente")
                continue
            else:
                print(f"\nVocê fez um empréstimo de {resposta} unidades do livro: {nome_livro}")
                biblioteca_livros[nome_livro]["Quantidade disponível"] -= resposta
                
                if biblioteca_livros[f"{nome_livro}"]["Quantidade disponível"] == 0:
                    del biblioteca_livros[f"{nome_livro}"]  
                
                historico_emprestimo.append({
                    "Livro": nome_livro,
                    "Quantidade": resposta,
                    "Data": time.strftime("%d/%m/%Y %H:%M:%S")
                })
                
                repetir = perguntar_denovo()
                if not repetir:
                    break
                
        except ValueError:
            print("Digito inválido, tente novamente...")
            continue
        
        
def exibir_historico(historico_emprestimo):
    while True:
        clear_terminal()
        
        if len(historico_emprestimo) == 0:
            print("Não há histórico algum de qualquer empréstimo no sistema atualmente. Tente outro processo.")
            time.sleep(2)
            break

        print('Histórico de empréstimos:\n')
        for i, h in enumerate(reversed(historico_emprestimo), start=1):
            print(f"{i}º) Livro: {h['Livro']} | Quantidade: {h['Quantidade']} | Data: {h['Data']}")

        repetir = perguntar_denovo()
        if not repetir:
            break
            
def main():
    menu()
        
if __name__ == "__main__":
    main()