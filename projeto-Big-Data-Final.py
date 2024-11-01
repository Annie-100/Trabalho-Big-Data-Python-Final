import pandas as pd
# Global DataFrame variable

df = None
def criar():
    global df
    df = pd.read_excel('/content/Trablaho de Tópicos de Big Data em Python(2)(planilha) 1 - Copy (1).xlsx')
    display(df.head())
    def apagar_coluna_vazia():
        global df
        if df is not None:
           df.dropna(how="all", axis=1, inplace=True)
           display(df)
        else:
            print("Primeiro, crie a tabela com a opção 1.") 
            def apagar_linha_marcada():
                global df
                if df is not None:
                    df.drop(1, axis=0, inplace=True)
                    display(df)
                else:
                 print("Primeiro, crie a tabela com a opção 1.")
                 def especifico():
                    global df
                    if df is not None:
                       print(df.loc[2, 'Vendas de Janeiro'])
                       display(df.loc[2])
                    else:
                       print("Primeiro, crie a tabela com a opção 1.")
                       def mes():
                          global df
                          if df is not None:
                             mes = df[['Vendas de Janeiro']]
                             display(mes)
                          else:
                             print("Primeiro, crie a tabela com a opção 1.")
                             def quantidade():
                                global df
                                if df is not None:
                                   display(df.head(10))
                                else:
                                   print("Primeiro, crie a tabela com a opção 1.")
                                   def inserir():
                                    global df
                                    if df is not None:
                                       x = input("digite o nome do arquivo")
                                       produtos = pd.read_excel(x)
                                       display(produtos)
                                       df = pd.concat([df, produtos], ignore_index=True)
                                       display(df)
                                    else:
                                       print("Primeiro, crie a tabela com a opção 1.")

                                       # User interaction loop

                                       while True:
                                          opcao = input('''Programa teste de BD
                                                        1.Criar tabela
                                                        2.apagar colona vazia
                                                        3.apagar linha especificar 
                                                        4.Valor especifico
                                                        5.procurar mes
                                                        6.Quantidade desejada
                                                        7.inserir
                                                        8.Terminar programa
                                                        Digite uma opção:''')
                                          if opcao == '1':
                                             criar()
                                          elif opcao == '2':
                                             apagar_coluna_vazia()
                                          elif opcao == '3':
                                             apagar_linha_marcada()
                                          elif opcao == '4':
                                             especifico()
                                          elif opcao == '5':
                                             mes()
                                          elif opcao == '6':
                                             quantidade()
                                          elif opcao == '7':
                                             inserir()
                                          elif opcao == '8':
                                             print('Fim da execução do programa.')
                                             break
                                          else:
                                             print('Opção inválida!\n')
                                          

                                             










