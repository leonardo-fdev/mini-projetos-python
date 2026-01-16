def solicitar_numero(mensagem):
  while True:
    try:
      return(int(input(mensagem)))
    
    except ValueError:
      print("Digite um número válido")
    
  


def entrar_no_cassino():
       
       while True:
        nome = input("Digite seu nome: ").strip()
        if not nome:
          print(" Nome não pode estar vazio⚠️.\n")
        
        elif nome.isdigit():
          print("  O nome não pode conter apenas números⚠️.\n")       
        
        else:
          break
       
       print("\nOlá, ", nome)

       idade = solicitar_numero("\nDigite sua idade: ")

       if idade >= 18:
        print("✅ Seja Bem vindo!")
                
       else:
         acompanhado_pelos_pais = input("Esta acompanhado pelos pais?  s/n \n")
         if acompanhado_pelos_pais.lower() == "s":
          print("👨‍👩‍👧Sejam Bem vindos")
                    
         elif acompanhado_pelos_pais.lower() == "n":
          print("🔞Proibido menores de idade")
                    
         else:
          print("⚠️Digite somente 's'ou'n' ⚠️")
  
  
 

def lanchonete():
 while True:
  
        print('''\n================= CARDÁPIO =================
          
          1 - COMBO LANCHE + REFRI = $45,50
          2 - LANCHE = 40,00
          3 - REFRI = 20,00

          4 - Voltar

          ''')

        total = 0
        cardapio = {1: 45.50, 2: 40.00, 3: 20.00}

        while True:
                escolha = solicitar_numero("Escolha uma opção: ")
                if escolha in cardapio:
                    total += cardapio[escolha]
                    print(f"Total: R${total:.2f}")

                    continuar = input("Deseja continuar? (s/n) ")
                    if continuar.lower() != 's':
                        print(f"Valor total final: R${total:.2f}")
                        break

                elif escolha == 4:
                    break


def menu_principal():
  
 

    print('''\n=================== INICIO ====================== 
         
CASSINO & LANCHONETE
         
 1 - Entrar no cassino
 2 - Comprar comidas e bebidas
 3 - Sair                                  
 
    ''') 

    try:
    
          opcao = solicitar_numero("Digite um número: ")

          if opcao == 1:
            entrar_no_cassino()
        
          elif opcao == 2:
            lanchonete()
        
          elif opcao == 3:
            print("👋 Saindo... Obrigado pela visita!")
            
        
          else:
            print("Opção inválida, tente novamente.")
         
    except ValueError:
      print("Digite um valor válido")
      
menu_principal()
      
      
            
        

 
