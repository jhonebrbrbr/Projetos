#Exibição nome do programa e entrada das informações

print("Programa Calculo de Energia \n")

nome_equipamento = input("\n Digite  o nome do equipamento: \n")
potencia_equipamento = float(input("\n Digite a potência do equipamento em Watts (W): \n"))
uso_diario = int(input("\n Digite a quantidade de horas(média) em que o equipamento é utilizado : \n"))


#processamento do consumo mensal

consumo_mensal = (potencia_equipamento * uso_diario * 30 ) / 1000

#Saída dos dados e questionamento se deseja exibir ou não o valor em R$ do consumo

print(f"\n O consumo mensal para o equipamento {nome_equipamento} utilizando em média "
      f"{uso_diario}hrs por dia na potência de {potencia_equipamento:.2f} watts " 
      f"é de {consumo_mensal:.2f} KW/mês")

exibir_consumo_reais = input("\n Deseja exibir o consumo estimado em R$ (considerando R$ 0,75 Kw/h)? " \
                                "Digite S para sim ou " \
                                "qualquer outra letra para encerrar \n")

if exibir_consumo_reais == 'S' or exibir_consumo_reais == 's':
    consumo_em_reais = consumo_mensal * 0.75
    print(f"\n O consumo estimado mensal é de R$ {consumo_em_reais:.2f}")

input("\n Digite enter para encerrar")


       