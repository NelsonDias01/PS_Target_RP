# Definindo as variaveis
distancia = 100 # em km
vel_carro = 110 # em km/h
vel_caminhao = 80 # em km/h
tempo_pedagio = 5/60 # em horas (5 minutos)

# Calculando o tempo que levam para se encontrar
tempo = distancia / (vel_carro + vel_caminhao)
tempo_caminhao = tempo + (2 * tempo_pedagio)

# Descobrimos a distancia pecorrida por cada veiculo
dist_carro = vel_carro * tempo
dist_caminhao = vel_caminhao * tempo_caminhao

# Informa qual estava mais proximo.
if dist_carro < dist_caminhao:
    print("O carro está mais próximo de Ribeirão Preto.")
else:
    print("O caminhão está mais próximo de Ribeirão Preto.")
