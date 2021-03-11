import matplotlib.pyplot as plt
import MetaTrader5 as mt5
import mensagem as msg
import pandas as pd

# Init Buy Process


def compra_init(key_value, file, close_list_value, open_list_value, n_value, stop_gain_value, stop_lose_value,
                mercado_value, lote_value, sim_value, facebook_value):

    # Metatrader5 command

    key_f = key_value
    valor_inicial_f = mt5.symbol_info_tick(mercado_value).ask
    pontos_f = mt5.symbol_info(mercado_value).point

    # Simulation process

    if sim_value:
        print(f"|Processo de COMPRA iniciado|\n - VALOR DE ENTRADA = {valor_inicial_f}\n "
              f"- KEY = {key_f};\n - open_list[-1] = {open_list_value[-1]};\n - open_list[-2] = {open_list_value[-2]};\n "
              f"- close_list[-1] = {close_list_value[-1]};\n - close_list[-2] = {close_list_value[-2]}")
        print("-" * 12)

    # Real Trade process

    else:
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": mercado_value,
            "volume": lote_value,
            "type": mt5.ORDER_TYPE_BUY,
            "price": valor_inicial_f,
            "sl": stop_lose_value - 40 * pontos_f,
            "tp": stop_gain_value + 40 * pontos_f,
            "deviation": 20,
            "magic": 234000,
            "comment": "python script open",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        mt5.order_send(request)

        # Facebook message trade alert

        if facebook_value:

            msg.mensagem(f"|Processo de COMPRA iniciado|\n - VALOR DE ENTRADA = {valor_inicial_f}\n "
                         f"- KEY = {key_f};\n - open_list[-1] = {open_list_value[-1]};\n - open_list[-2] = {open_list_value[-2]};\n "
                         f"- close_list[-1] = {close_list_value[-1]};\n - close_list[-2] = {close_list_value[-2]}")

            msg.mensagem("-" * 12)

        print(f"|Processo de COMPRA iniciado|\n - VALOR DE ENTRADA = {valor_inicial_f}\n "
              f"- KEY = {key_f};\n - open_list[-1] = {open_list_value[-1]};\n - open_list[-2] = {open_list_value[-2]};\n "
              f"- close_list[-1] = {close_list_value[-1]};\n - close_list[-2] = {close_list_value[-2]}")
        print("-" * 12)

    stop_lines_f = True
    registro_tempo_f = n_value
    plt.savefig(file)

    return key_f, stop_lines_f, valor_inicial_f, registro_tempo_f


# Init Sell Process


def venda_init(key_value, file, close_list_value, open_list_value, n_value, stop_gain_value, stop_lose_value,
               mercado_value, lote_value, sim_value, facebook_value):

    # Metatrader5 command

    key_f = key_value
    valor_inicial_f = mt5.symbol_info_tick(mercado_value).bid
    pontos_f = mt5.symbol_info(mercado_value).point

    # Simulation process

    if sim_value:
        print(f"|Processo de VENDA iniciado|\n - VALOR DE ENTRADA = {valor_inicial_f}\n "
              f"- KEY = {key_f};\n - open_list[-1] = {open_list_value[-1]};\n - open_list[-2] = {open_list_value[-2]};\n "
              f"- close_list[-1] = {close_list_value[-1]};\n - close_list[-2] = {close_list_value[-2]}")
        print("-" * 12)

    # Real Trade process

    else:

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": mercado_value,
            "volume": lote_value,
            "type": mt5.ORDER_TYPE_SELL,
            "price": valor_inicial_f,
            "sl": stop_lose_value + 40 * pontos_f,
            "tp": stop_gain_value - 40 * pontos_f,
            "deviation": 20,
            "magic": 234000,
            "comment": "python script open",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        mt5.order_send(request)

        # Facebook message trade alert

        if facebook_value:

            msg.mensagem(f"|Processo de VENDA iniciado|\n - VALOR DE ENTRADA = {valor_inicial_f}\n "
                        f"- KEY = {key_f};\n - open_list[-1] = {open_list_value[-1]};\n - open_list[-2] = {open_list_value[-2]};\n "
                        f"- close_list[-1] = {close_list_value[-1]};\n - close_list[-2] = {close_list_value[-2]}")
            msg.mensagem("-" * 12)

        print(f"|Processo de VENDA iniciado|\n - VALOR DE ENTRADA = {valor_inicial_f}\n "
              f"- KEY = {key_f};\n - open_list[-1] = {open_list_value[-1]};\n - open_list[-2] = {open_list_value[-2]};\n "
              f"- close_list[-1] = {close_list_value[-1]};\n - close_list[-2] = {close_list_value[-2]}")
        print("-" * 12)

    stop_lines_f = True
    registro_tempo_f = n_value
    plt.savefig(file)

    return key_f, stop_lines_f, valor_inicial_f, registro_tempo_f

# Sell Profit


def venda_lucro(key_value, file, file_hist, close_list_value, open_list_value, time_list_value, n_value, tabela_value, valor_inicial_value,
                mercado_value, lote_value, lote_price, sim_value, facebook_value):

    # Metatrader5 command

    key_f = 0
    valor_atual_f = mt5.symbol_info_tick(mercado_value).bid
    resultado_f = valor_atual_f - valor_inicial_value

    # Simulation process

    if sim_value:

        lucro = resultado_f * lote_price * lote_value * 0.78

        tabela_value[0] += 1

        print(
            f"|LUCRO: Processo de VENDA|\n - FECHAMENTO = {close_list_value[-1]}\n - RESULTADO = +{resultado_f}\n "
            f"- KEY = {key_f};\n - open_list[-1] = {open_list_value[-1]};\n - open_list[-2] = {open_list_value[-2]};\n "
            f"- close_list[-1] = {close_list_value[-1]};\n - close_list[-2] = {close_list_value[-2]}")

        print(f'LUCRO: {lucro}')
        print(f'LUCRO: {tabela_value[0]}; PERDA: {tabela_value[1]}')
        print("-" * 12)
        print(f"QUANTIA = {mt5.account_info()._asdict()['balance']}")
        print("-" * 12)

    # Real Trade process

    else:

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": mercado_value,
            "volume": lote_value,
            "type": mt5.ORDER_TYPE_SELL,
            "price": valor_atual_f,
            "deviation": 20,
            "magic": 234000,
            "comment": "python script open",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        mt5.order_send(request)

        lucro = resultado_f * lote_price * lote_value * 0.78
        tempo = time_list_value[-1]

        df_dados = pd.DataFrame({'key': [key_value], 'Lucro': [lucro], 'Data': [tempo], 'Boolean': [sim_value]})
        with open(file_hist, 'a') as f:
            df_dados.to_csv(f, header=False, index=False)
        tabela_value[0] += 1

        # Facebook message trade alert

        if facebook_value:

            msg.mensagem(
                f"|LUCRO: Processo de VENDA|\n - FECHAMENTO = {close_list_value[-1]}\n - RESULTADO = +{resultado_f}\n "
                f"- KEY = {key_f};\n - open_list[-1] = {open_list_value[-1]};\n - open_list[-2] = {open_list_value[-2]};\n "
                f"- close_list[-1] = {close_list_value[-1]};\n - close_list[-2] = {close_list_value[-2]}")

            msg.mensagem(f'LUCRO: {lucro}')
            msg.mensagem(f'LUCRO: {tabela_value[0]}; PERDA: {tabela_value[1]}')
            msg.mensagem("-" * 12)
            msg.mensagem(f"QUANTIA = {mt5.account_info()._asdict()['balance']}")
            msg.mensagem("-" * 12)

        print(
            f"|LUCRO: Processo de VENDA|\n - FECHAMENTO = {close_list_value[-1]}\n - RESULTADO = +{resultado_f}\n "
            f"- KEY = {key_f};\n - open_list[-1] = {open_list_value[-1]};\n - open_list[-2] = {open_list_value[-2]};\n "
            f"- close_list[-1] = {close_list_value[-1]};\n - close_list[-2] = {close_list_value[-2]}")

        print(f'LUCRO: {lucro}')
        print(f'LUCRO: {tabela_value[0]}; PERDA: {tabela_value[1]}')
        print("-" * 12)
        print(f"QUANTIA = {mt5.account_info()._asdict()['balance']}")
        print("-" * 12)

    stop_lines_f = False
    registro_tempo_f = n_value
    plt.savefig(file)

    return key_f, stop_lines_f, registro_tempo_f, tabela_value

# Buy Profit


def compra_lucro(key_value, file, file_hist, close_list_value, open_list_value, time_list_value, n_value, tabela_value, valor_inicial_value,
                 mercado_value, lote_value, lote_price, sim_value, facebook_value):

    # Metatrader5 command

    key_f = 0
    valor_atual_f = mt5.symbol_info_tick(mercado_value).ask
    resultado_f = valor_inicial_value - valor_atual_f

    # Simulation process

    if sim_value:

        lucro = resultado_f * lote_price * lote_value * 0.78

        tabela_value[0] += 1

        print(
            f"|LUCRO: Processo de COMPRA|\n - FECHAMENTO = {close_list_value[-1]}\n - RESULTADO = +{resultado_f}\n "
            f"- KEY = {key_f};\n - open_list[-1] = {open_list_value[-1]};\n - open_list[-2] = {open_list_value[-2]};\n "
            f"- close_list[-1] = {close_list_value[-1]};\n - close_list[-2] = {close_list_value[-2]}")

        print(f'LUCRO: {lucro}')
        print(f'LUCRO: {tabela_value[0]}; PERDA: {tabela_value[1]}')
        print("-" * 12)
        print(f"QUANTIA = {mt5.account_info()._asdict()['balance']}")
        print("-" * 12)

    # Real Trade process

    else:
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": mercado_value,
            "volume": lote_value,
            "type": mt5.ORDER_TYPE_BUY,
            "price": valor_atual_f,
            "deviation": 20,
            "magic": 234000,
            "comment": "python script open",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        mt5.order_send(request)

        lucro = resultado_f * lote_price * lote_value * 0.78
        tempo = time_list_value[-1]

        df_dados = pd.DataFrame({'key': [key_value], 'Lucro': [lucro], 'Data': [tempo], 'Boolean': [sim_value]})
        with open(file_hist, 'a') as f:
            df_dados.to_csv(f, header=False, index=False)

        tabela_value[0] += 1

        # Facebook message trade alert

        if facebook_value:

            msg.mensagem(
                f"|LUCRO: Processo de COMPRA|\n - FECHAMENTO = {close_list_value[-1]}\n - RESULTADO = +{resultado_f}\n "
                f"- KEY = {key_f};\n - open_list[-1] = {open_list_value[-1]};\n - open_list[-2] = {open_list_value[-2]};\n "
                f"- close_list[-1] = {close_list_value[-1]};\n - close_list[-2] = {close_list_value[-2]}")

            msg.mensagem(f'LUCRO: {lucro}')
            msg.mensagem(f'LUCRO: {tabela_value[0]}; PERDA: {tabela_value[1]}')
            msg.mensagem("-" * 12)
            msg.mensagem(f"QUANTIA = {mt5.account_info()._asdict()['balance']}")
            msg.mensagem("-" * 12)

        print(
            f"|LUCRO: Processo de COMPRA|\n - FECHAMENTO = {close_list_value[-1]}\n - RESULTADO = +{resultado_f}\n "
            f"- KEY = {key_f};\n - open_list[-1] = {open_list_value[-1]};\n - open_list[-2] = {open_list_value[-2]};\n "
            f"- close_list[-1] = {close_list_value[-1]};\n - close_list[-2] = {close_list_value[-2]}")

        print(f'LUCRO: {lucro}')
        print(f'LUCRO: {tabela_value[0]}; PERDA: {tabela_value[1]}')
        print("-" * 12)
        print(f"QUANTIA = {mt5.account_info()._asdict()['balance']}")
        print("-" * 12)

    stop_lines_f = False
    registro_tempo_f = n_value
    plt.savefig(file)

    return key_f, stop_lines_f, registro_tempo_f, tabela_value

# Sell Loss


def venda_perda(key_value, file, file_hist, close_list_value, open_list_value, time_list_value, n_value, tabela_value, valor_inicial_value,
                mercado_value, lote_value, lote_price, sim_value, facebook_value):

    # Metatrader5 command

    key_f = 0
    valor_atual_f = mt5.symbol_info_tick(mercado_value).bid
    resultado_f = valor_atual_f - valor_inicial_value

    # Simulation process

    if sim_value:

        lucro = resultado_f * lote_price * lote_value * 0.78

        tabela_value[1] += 1

        print(
            f"|PERDA: Processo de VENDA|\n - FECHAMENTO = {close_list_value[-1]}\n - RESULTADO = {resultado_f}\n "
            f"- KEY = {key_f};\n - open_list[-1] = {open_list_value[-1]};\n - open_list[-2] = {open_list_value[-2]};\n "
            f"- close_list[-1] = {close_list_value[-1]};\n - close_list[-2] = {close_list_value[-2]}")

        print(f'PERDA: {lucro}')
        print(f'LUCRO: {tabela_value[0]}; PERDA: {tabela_value[1]}')
        print("-" * 12)
        print(f"QUANTIA = {mt5.account_info()._asdict()['balance']}")
        print("-" * 12)

    # Real Trade process

    else:
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": mercado_value,
            "volume": lote_value,
            "type": mt5.ORDER_TYPE_SELL,
            "price": valor_atual_f,
            "deviation": 20,
            "magic": 234000,
            "comment": "python script open",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        mt5.order_send(request)

        lucro = resultado_f * lote_price * lote_value * 0.78
        tempo = time_list_value[-1]

        df_dados = pd.DataFrame({'key': [key_value], 'Lucro': [lucro], 'Data': [tempo], 'Boolean': [sim_value]})
        with open(file_hist, 'a') as f:
            df_dados.to_csv(f, header=False, index=False)

        tabela_value[1] += 1

        # Facebook message trade alert

        if facebook_value:

            msg.mensagem(
                f"|PERDA: Processo de VENDA|\n - FECHAMENTO = {close_list_value[-1]}\n - RESULTADO = {resultado_f}\n "
                f"- KEY = {key_f};\n - open_list[-1] = {open_list_value[-1]};\n - open_list[-2] = {open_list_value[-2]};\n "
                f"- close_list[-1] = {close_list_value[-1]};\n - close_list[-2] = {close_list_value[-2]}")

            msg.mensagem(f'PERDA: {lucro}')
            msg.mensagem(f'LUCRO: {tabela_value[0]}; PERDA: {tabela_value[1]}')
            msg.mensagem("-" * 12)
            msg.mensagem(f"QUANTIA = {mt5.account_info()._asdict()['balance']}")
            msg.mensagem("-" * 12)

        print(
            f"|PERDA: Processo de VENDA|\n - FECHAMENTO = {close_list_value[-1]}\n - RESULTADO = {resultado_f}\n "
            f"- KEY = {key_f};\n - open_list[-1] = {open_list_value[-1]};\n - open_list[-2] = {open_list_value[-2]};\n "
            f"- close_list[-1] = {close_list_value[-1]};\n - close_list[-2] = {close_list_value[-2]}")

        print(f'PERDA: {lucro}')
        print(f'LUCRO: {tabela_value[0]}; PERDA: {tabela_value[1]}')
        print("-" * 12)
        print(f"QUANTIA = {mt5.account_info()._asdict()['balance']}")
        print("-" * 12)

    stop_lines_f = False
    registro_tempo_f = n_value
    plt.savefig(file)

    return key_f, stop_lines_f, registro_tempo_f, tabela_value

# Buy Loss


def compra_perda(key_value, file, file_hist, close_list_value, open_list_value, time_list_value, n_value, tabela_value, valor_inicial_value,
                 mercado_value, lote_value, lote_price, sim_value, facebook_value):

    # Metatrader5 command

    key_f = 0
    valor_atual_f = mt5.symbol_info_tick(mercado_value).ask
    resultado_f = valor_inicial_value - valor_atual_f

    # Simulation process

    if sim_value:

        lucro = resultado_f * lote_price * lote_value * 0.78

        tabela_value[1] += 1

        print(
            f"|PERDA: Processo de COMPRA|\n - FECHAMENTO = {close_list_value[-1]}\n - RESULTADO = {resultado_f}\n "
            f"- KEY = {key_f};\n - open_list[-1] = {open_list_value[-1]};\n - open_list[-2] = {open_list_value[-2]};\n "
            f"- close_list[-1] = {close_list_value[-1]};\n - close_list[-2] = {close_list_value[-2]}")

        print(f'PERDA: {lucro}')
        print(f'LUCRO: {tabela_value[0]}; PERDA: {tabela_value[1]}')
        print("-" * 12)
        print(f"QUANTIA = {mt5.account_info()._asdict()['balance']}")
        print("-" * 12)

    # Real Trade process

    else:

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": mercado_value,
            "volume": lote_value,
            "type": mt5.ORDER_TYPE_BUY,
            "price": valor_atual_f,
            "deviation": 20,
            "magic": 234000,
            "comment": "python script open",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        mt5.order_send(request)

        lucro = resultado_f * lote_price * lote_value * 0.78
        tempo = time_list_value[-1]

        df_dados = pd.DataFrame({'key': [key_value], 'Lucro': [lucro], 'Data': [tempo], 'Boolean': [sim_value]})
        with open(file_hist, 'a') as f:
            df_dados.to_csv(f, header=False, index=False)

        tabela_value[1] += 1

        # Facebook message trade alert

        if facebook_value:

            msg.mensagem(
                f"|PERDA: Processo de COMPRA|\n - FECHAMENTO = {close_list_value[-1]}\n - RESULTADO = {resultado_f}\n "
                f"- KEY = {key_f};\n - open_list[-1] = {open_list_value[-1]};\n - open_list[-2] = {open_list_value[-2]};\n "
                f"- close_list[-1] = {close_list_value[-1]};\n - close_list[-2] = {close_list_value[-2]}")

            msg.mensagem(f'PERDA: {lucro}')
            msg.mensagem(f'LUCRO: {tabela_value[0]}; PERDA: {tabela_value[1]}')
            msg.mensagem("-" * 12)
            msg.mensagem(f"QUANTIA = {mt5.account_info()._asdict()['balance']}")
            msg.mensagem("-" * 12)

        print(
            f"|PERDA: Processo de COMPRA|\n - FECHAMENTO = {close_list_value[-1]}\n - RESULTADO = {resultado_f}\n "
            f"- KEY = {key_f};\n - open_list[-1] = {open_list_value[-1]};\n - open_list[-2] = {open_list_value[-2]};\n "
            f"- close_list[-1] = {close_list_value[-1]};\n - close_list[-2] = {close_list_value[-2]}")

        print(f'PERDA: {lucro}')
        print(f'LUCRO: {tabela_value[0]}; PERDA: {tabela_value[1]}')
        print("-" * 12)
        print(f"QUANTIA = {mt5.account_info()._asdict()['balance']}")
        print("-" * 12)

    stop_lines_f = False
    registro_tempo_f = n_value
    plt.savefig(file)

    return key_f, stop_lines_f, registro_tempo_f, tabela_value
