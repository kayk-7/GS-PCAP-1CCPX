def analisar_tendencia(riscos_ciclos):

    primeiro_risco = riscos_ciclos[0]
    ultimo_risco = riscos_ciclos[-1]

    if ultimo_risco > primeiro_risco:
        return "A missão apresentou tendência de piora."

    elif ultimo_risco < primeiro_risco:
        return "A missão apresentou tendência de melhora."

    else:
        return "A missão permaneceu estável em relação ao início."

def avaliar_risco(ciclo):
    if ciclo <= 2:
        return "MISSAO ESTAVEL"
    elif ciclo <= 5:
        return "MISSAO EM ATENCAO"
    else:
        return "MISSAO CRITICA"

def analisar_temperatura(temp):

    if temp < 18:
        return "ATENCAO | Temperatura abaixo do recomendado | verificar controle térmico da missão.", 1

    elif temp <= 30:
        return "NORMAL | Temperatura estável", 0

    elif temp <= 35:
        return "ATENCAO | Temperatura elevada", 1

    else:
        return "CRITICO | Risco de superaquecimento | verificar controle térmico da missão.", 2

def analisar_comunicacao(com):

    if com < 30:
        return "CRITICO | Comunicação com a base em nível crítico | tentar restabelecer contato com a base." , 2

    elif com < 60:
        return "ATENCAO | Comunicação instável", 1

    else:
        return "NORMAL | Comunicação estável", 0

def analisar_bateria(bat):

    if bat < 20:
        return "CRITICO | Bateria em nível crítico | ativar modo de economia de energia.", 2

    elif bat < 50:
        return "ATENCAO | Bateria abaixo do recomendado", 1

    else:
        return "NORMAL | Energia estável", 0

def analisar_oxigenio(oxi):

    if oxi < 80:
        return "CRITICO | Oxigênio em nível crítico | acionar protocolo de suporte à vida.", 2

    elif oxi < 90:
        return "ATENCAO | Oxigênio abaixo do ideal", 1

    else:
        return "NORMAL | Oxigênio adequado", 0

def analisar_estabilidade(est):

    if est < 40:
        return "CRITICO | Estabilidade operacional crítica | reduzir operações não essenciais.", 2

    elif est < 70:
        return "ATENCAO | Estabilidade operacional reduzida", 1

    else:
        return "NORMAL | Estabilidade operacional adequada", 0


#---AREA MONITORADAS---
areas_monitoradas = [
 "Temperatura interna",
 "Comunicação com a base",
 "Sistema de energia",
 "Suporte de oxigênio",
 "Estabilidade operacional"
]


#---TABELA---
dados_missao = [
 [24, 92, 88, 96, 90],
 [27, 80, 72, 94, 85],
 [31, 65, 58, 91, 70],
 [36, 42, 38, 87, 55],
 [39, 28, 19, 78, 35],
 [45, 48, 30, 80, 40],
 [34, 55, 32, 82, 50]
]


print("""
============================================================
MISSION DATA ANALYTICS 
============================================================
Missão: Project Rocket Mitigation 
Equipe: Equipe Bravo
Quantidade de ciclos analisados: 7
============================================================
""")


#---LISTA PARA IDENTIFICAR QUAL CICLO FOI O MAIS PERIGOSO---
lista_riscos=[]


#---LISTA PARA SOMA DE PERIGO DOS CICLOS---
lista_pontos = []


ciclos_criticos=0

ciclo_atual=0

for ciclo in dados_missao:
    ciclo_atual += 1
    temperatura = ciclo[0]
    comunicacao = ciclo[1]
    bateria = ciclo[2]
    oxigenio = ciclo[3]
    estabilidade = ciclo[4]

    temp_status, temp_pontos = analisar_temperatura(temperatura)

    com_status, com_pontos = analisar_comunicacao(comunicacao)

    bat_status, bat_pontos = analisar_bateria(bateria)

    oxi_status, oxi_pontos = analisar_oxigenio(oxigenio)

    est_status, est_pontos = analisar_estabilidade(estabilidade)

    lista_pontosfor = [temp_pontos, com_pontos, bat_pontos, oxi_pontos, est_pontos]



    risco_total = (temp_pontos + com_pontos + bat_pontos + oxi_pontos + est_pontos)

    lista_riscos.append(risco_total)

    lista_pontos.append(lista_pontosfor)


    print(f"""CICLO ATUAL: {ciclo_atual} 
    Temperatura: {temperatura}°C {temp_status} 
    Comunicacao: {comunicacao}% {com_status} 
    Bateria: {bateria}% {bat_status} 
    Oxigenio: {oxigenio}% {oxi_status} 
    Estabilidade: {estabilidade}% {est_status} 
    
    Pontuação de risco do ciclo: {risco_total}
    Classificação do ciclo: {avaliar_risco(risco_total)}
    
    """)


    if risco_total >5:
        ciclos_criticos += 1

pont_total_temp=0
pont_total_com=0
pont_total_bat=0
pont_total_oxi=0
pont_total_est=0

for riscos in lista_pontos:
    pont_total_temp += riscos[0]
    pont_total_com += riscos[1]
    pont_total_bat += riscos[2]
    pont_total_oxi += riscos[3]
    pont_total_est += riscos[4]


#---TABELA COM A AREA MAIS AFETADA---
lista_da_area_mais_afetada = [pont_total_temp, pont_total_com, pont_total_bat, pont_total_oxi, pont_total_est]

index_area_afetada = lista_da_area_mais_afetada.index(max(lista_da_area_mais_afetada))


#-==-IDENTIFICACAO DE CICLO MAIS PERIGOSO-==-
maior_pontuacao = max(lista_riscos)

indice_ciclo_critico = lista_riscos.index(maior_pontuacao)

ciclo_mais_critico = indice_ciclo_critico + 1

risco_medio_missao = sum(lista_riscos) / len(lista_riscos)

quantidade_critica= lista_riscos[indice_ciclo_critico]/2


#-==-MEDIA DOS VALORES DA MISSAO INTEIRA-==-
temp_valores = [linha[0] for linha in dados_missao]
media_temp = sum(temp_valores) / len(temp_valores)

com_valores = [linha[1] for linha in dados_missao]
media_com = sum(com_valores) / len(com_valores)

bat_valores = [linha[2] for linha in dados_missao]
media_bat = sum(bat_valores) / len(bat_valores)

oxi_valores = [linha[3] for linha in dados_missao]
media_oxi = sum(oxi_valores) / len(oxi_valores)

est_valores = [linha[4] for linha in dados_missao]
media_est = sum(est_valores) / len(est_valores)


print(f"""
============================================================
RELATÓRIO FINAL DA MISSÃO
============================================================
Missão: Project Rocket Mitigation 
Equipe: Equipe Bravo

Quantidade de ciclos analisados:{ciclo_atual}

Média de temperatura: {media_temp:.2f}°C
Média de comunicação: {media_com:.2f}%
Média de bateria: {media_bat:.2f}%
Média de oxigênio: {media_oxi:.2f}%
Média de estabilidade: {media_est:.2f}%

Ciclo mais crítico: {ciclo_mais_critico}
Maior pontuação de risco: {maior_pontuacao}
Risco médio da missão: {risco_medio_missao:.2f}
Quantidade de críticos: {quantidade_critica:.0f}

Tendência da missão:
{analisar_tendencia(lista_riscos)}
Quantidade de ciclos críticos: {ciclos_criticos}

Pontuação acumulada por área:
Temperatura interna: {lista_da_area_mais_afetada[0]} pontos
Comunicação com a base: {lista_da_area_mais_afetada[1]} pontos
Sistema de energia: {lista_da_area_mais_afetada[2]} pontos
Suporte de oxigênio: {lista_da_area_mais_afetada[3]} pontos
Estabilidade operacional: {lista_da_area_mais_afetada[4]} pontos

Área mais afetada:
{areas_monitoradas[index_area_afetada]}

""")