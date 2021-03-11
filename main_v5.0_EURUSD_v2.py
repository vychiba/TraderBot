import MetaTrader5 as mt5
import matplotlib.pyplot as plt
import pandas as pd
import grafico as graf
import metodos_v4 as met
import timer as tm

# Connection with MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# Data on MetaTrader 5 version
print(mt5.version())

# User informations
account = "********"
authorized = mt5.login(account, password="********")

if not authorized:
    print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))

# Establish a plot routine with Matplotlib
plt.ion()

# Setting initial code informations
time_range = 100
key = 0
curve = 0
fibo_list = []
valor_inicial = 0
tempos = []
tabela = [0, 0]

stop_lose = 0
stop_gain = 0
stop_lines = False

first_looping = 1
registro_tempo = 0
key_fibo = 0

# Save print graphs file names
file_saida = "saida"
file_entrada = "entrada"

# Trade informations
mercado = "EURUSD"
lote_value_cont = 0.1
lote_value_corr = 0.03
lote_peso = 1000
time_frame = mt5.TIMEFRAME_M4
init_pregao = '00:00:00'
end_pregao = '23:59:00'

# Simulation: True or False
sim = False

# Facebook mesages: True or False
facebook = False

# Core Looping
while True:

    # Rates data
    rates = mt5.copy_rates_from_pos(mercado, time_frame, 0, time_range)

    rates_frame = pd.DataFrame(rates)

    rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')

    time_list = []
    open_list = []
    close_list = []

    # Building and Updating graph
    graf.grafico(time_range, rates_frame, open_list, close_list, time_list)

    # Time
    time = str(time_list[-1]).replace('-', ' ').replace(':', ' ')

    # Updating the Fibonacci lines value
    fibo_list, curve, first_looping = tm.timer_att_fibolines_4min(time, first_looping, open_list, close_list, fibo_list, curve)

    # Plot Fibonacci lines
    graf.plot_fibo(fibo_list)

    # STRATEGIES

    # Reversal Downturn Trend (23,6% -> 61,8%)

    if tm.timer_pregao(init_pregao, end_pregao) and curve == -1 and key == 0 and registro_tempo != time and (open_list[-1] < fibo_list[5] or (fibo_list[4] > open_list[-2] >= fibo_list[5] and fibo_list[4] > close_list[-2] >= fibo_list[5])) and close_list[-1] > fibo_list[5] + 0.20 * (fibo_list[4] - fibo_list[5]):

        stop_gain = fibo_list[3] - 0.20 * (fibo_list[3] - fibo_list[4])
        stop_lose = fibo_list[1] - 0.2 * (fibo_list[6] - fibo_list[1])

        key, stop_lines, valor_inicial, registro_tempo = met.compra_init(1, f'/Users/vychi/Desktop/graficos/{file_entrada}/{time}', close_list, open_list, time, stop_gain, stop_lose, mercado, lote_value_corr, sim, facebook)

    if stop_lines:
        plt.axhline(stop_gain, color='green', linewidth=0.5)
        plt.axhline(stop_lose, color='red', linewidth=0.5)

    if key == 1 and mt5.symbol_info_tick(mercado).bid >= stop_gain:

        key, stop_lines, registro_tempo, tabela = met.venda_lucro(1, f'/Users/vychi/Desktop/graficos/{file_saida}/{time}', f'/Users/vychi/Desktop/graficos/Dados/historico_{mercado}.csv', close_list, open_list, time_list, time, tabela, valor_inicial, mercado, lote_value_corr, lote_peso, sim, facebook)
        fibo_list, curve = graf.fibonacci(open_list, close_list)

    if key == 1 and mt5.symbol_info_tick(mercado).bid <= stop_lose:

        key, stop_lines, registro_tempo, tabela = met.venda_perda(1, f'/Users/vychi/Desktop/graficos/{file_saida}/{time}', f'/Users/vychi/Desktop/graficos/Dados/historico_{mercado}.csv', close_list, open_list, time_list, time, tabela, valor_inicial, mercado, lote_value_corr, lote_peso, sim, facebook)
        fibo_list, curve = graf.fibonacci(open_list, close_list)

    # Reversal Upturn Trend (23,6% -> 61,8%)

    if tm.timer_pregao(init_pregao, end_pregao) and curve == 1 and key == 0 and registro_tempo != time and (open_list[-1] > fibo_list[5] or (fibo_list[4] < open_list[-2] <= fibo_list[5] and fibo_list[4] < close_list[-2] <= fibo_list[5])) and close_list[-1] < fibo_list[5] - 0.20 * (fibo_list[5] - fibo_list[4]):

        stop_gain = fibo_list[3] + 0.20 * (fibo_list[4] - fibo_list[3])
        stop_lose = fibo_list[1] + 0.2 * (fibo_list[1] - fibo_list[6])

        key, stop_lines, valor_inicial, registro_tempo = met.venda_init(2, f'/Users/vychi/Desktop/graficos/{file_entrada}/{time}', close_list, open_list, time, stop_gain, stop_lose, mercado, lote_value_corr, sim, facebook)

    if stop_lines:
        plt.axhline(stop_gain, color='green', linewidth=0.5)
        plt.axhline(stop_lose, color='red', linewidth=0.5)

    if key == 2 and mt5.symbol_info_tick(mercado).ask <= stop_gain:

        key, stop_lines, registro_tempo, tabela = met.compra_lucro(2, f'/Users/vychi/Desktop/graficos/{file_saida}/{time}', f'/Users/vychi/Desktop/graficos/Dados/historico_{mercado}.csv', close_list, open_list, time_list, time, tabela, valor_inicial, mercado, lote_value_corr, lote_peso, sim, facebook)
        fibo_list, curve = graf.fibonacci(open_list, close_list)

    if key == 2 and mt5.symbol_info_tick(mercado).ask >= stop_lose:

        key, stop_lines, registro_tempo, tabela = met.compra_perda(2, f'/Users/vychi/Desktop/graficos/{file_saida}/{time}', f'/Users/vychi/Desktop/graficos/Dados/historico_{mercado}.csv', close_list, open_list, time_list, time, tabela, valor_inicial, mercado, lote_value_corr, lote_peso, sim, facebook)
        fibo_list, curve = graf.fibonacci(open_list, close_list)

    # Continued upward movement

    if tm.timer_pregao(init_pregao, end_pregao) and curve == 1 and key == 0 and registro_tempo != time and (((open_list[-2] < fibo_list[1] or open_list[-3] > fibo_list[1]) and close_list[-2] > fibo_list[1] + 0.15 * (fibo_list[9] - fibo_list[1])) or close_list[-2] > fibo_list[9]):

        stop_gain = fibo_list[1] + (fibo_list[10] - fibo_list[1]) - 0.1 * (fibo_list[10] - fibo_list[9])
        stop_lose = fibo_list[5] - 0.40 * (fibo_list[6] - fibo_list[5])

        key, stop_lines, valor_inicial, registro_tempo = met.compra_init(3, f'/Users/vychi/Desktop/graficos/{file_entrada}/{time}', close_list, open_list, time, stop_gain, stop_lose, mercado, lote_value_cont, sim, facebook)

    if stop_lines:
        plt.axhline(stop_gain, color='green', linewidth=0.5)
        plt.axhline(stop_lose, color='red', linewidth=0.5)

    if key == 3 and mt5.symbol_info_tick(mercado).bid >= stop_gain:

        key, stop_lines, registro_tempo, tabela = met.venda_lucro(3, f'/Users/vychi/Desktop/graficos/{file_saida}/{time}', f'/Users/vychi/Desktop/graficos/Dados/historico_{mercado}.csv', close_list, open_list, time_list, time, tabela, valor_inicial, mercado, lote_value_cont, lote_peso, sim, facebook)
        fibo_list, curve = graf.fibonacci(open_list, close_list)

    if key == 3 and mt5.symbol_info_tick(mercado).bid <= stop_lose:

        key, stop_lines, registro_tempo, tabela = met.venda_perda(3, f'/Users/vychi/Desktop/graficos/{file_saida}/{time}', f'/Users/vychi/Desktop/graficos/Dados/historico_{mercado}.csv', close_list, open_list, time_list, time, tabela, valor_inicial, mercado, lote_value_cont, lote_peso, sim, facebook)
        fibo_list, curve = graf.fibonacci(open_list, close_list)

    # Continued downward movement

    if tm.timer_pregao(init_pregao, end_pregao) and curve == -1 and key == 0 and registro_tempo != time and (((open_list[-2] > fibo_list[1] or open_list[-3] < fibo_list[1]) and close_list[-2] < fibo_list[1] - 0.15 * (fibo_list[1] - fibo_list[9])) or close_list[-2] < fibo_list[9]):

        stop_gain = fibo_list[1] - (fibo_list[1] - fibo_list[10]) + 0.1 * (fibo_list[9] - fibo_list[10])
        stop_lose = fibo_list[5] + 0.40 * (fibo_list[5] - fibo_list[6])

        key, stop_lines, valor_inicial, registro_tempo = met.venda_init(4, f'/Users/vychi/Desktop/graficos/{file_entrada}/{time}', close_list, open_list, time, stop_gain, stop_lose, mercado, lote_value_cont, sim, facebook)

    if stop_lines:
        plt.axhline(stop_gain, color='green', linewidth=0.5)
        plt.axhline(stop_lose, color='red', linewidth=0.5)

    if key == 4 and mt5.symbol_info_tick(mercado).ask <= stop_gain:

        key, stop_lines, registro_tempo, tabela = met.compra_lucro(4, f'/Users/vychi/Desktop/graficos/{file_saida}/{time}', f'/Users/vychi/Desktop/graficos/Dados/historico_{mercado}.csv', close_list, open_list, time_list, time, tabela, valor_inicial, mercado, lote_value_cont, lote_peso, sim, facebook)
        fibo_list, curve = graf.fibonacci(open_list, close_list)

    if key == 4 and mt5.symbol_info_tick(mercado).ask >= stop_lose:

        key, stop_lines, registro_tempo, tabela = met.compra_perda(4, f'/Users/vychi/Desktop/graficos/{file_saida}/{time}', f'/Users/vychi/Desktop/graficos/Dados/historico_{mercado}.csv', close_list, open_list, time_list, time, tabela, valor_inicial, mercado, lote_value_cont, lote_peso, sim, facebook)
        fibo_list, curve = graf.fibonacci(open_list, close_list)

    plt.pause(0.1)
    plt.clf()

