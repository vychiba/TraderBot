import MetaTrader5 as mt5
import pandas as pd
import matplotlib.pyplot as plt


class MetaTrader:
    def __init__(self, account, password):
        self.account = account
        self.password = password

    def login(self):
        if not mt5.initialize():
            print("initialize() failed, error code =", mt5.last_error())
            quit()
        authorized = mt5.login(self.account, password=self.password)

        if not authorized:
            print("failed to connect at account #{}, error code: {}".format(self.account, mt5.last_error()))


class Grafico:
    def __init__(self):
        self.time_range = 100
        self.key = 0
        self.curve = 0
        self.fibo_list = []
        self.valor_inicial = 0
        self.tempos = []
        self.tabela = [0, 0]
        self.stop = 0
        self.take = 0
        self.lines = False
        self.first_looping = 1
        self.registro_tempo = 0
        self.key_fibo = 0
        self.file_saida = 'saida'
        self.file_entrada = 'entrada'
        self.mercado = 'GBPUSD'
        self.lote_value_cont = 0.1
        self.lote_value_corr = 0.03
        self.lote_peso = 1000
        self.time_frame = mt5.TIMEFRAME_M4
        self.sim = False
        self.facebook = False
        self.init_pregao = '04:00:00'
        self.end_pregao = '15:40:00'

        self.time_list = []
        self.open_list = []
        self.close_list = []
        self.n = ''

        self.months = 6
        self.ponto = 0
        self.ponto_inicial = 210
        self.ponto_final = 60
        self.time_range = 50
        self.high_list = []
        self.low_list = []

    def grafico_contruction(self, rates_frame):

        for i in range(0, self.time_range):

            time_const = rates_frame.time[i]
            high_const = rates_frame.high[i]
            low_const = rates_frame.low[i]
            open_const = rates_frame.open[i]
            close_const = rates_frame.close[i]

            self.open_list.append(open_const)
            self.close_list.append(close_const)
            self.time_list.append(time_const)

            if open_const > close_const:
                color = 'red'
            elif open_const < close_const:
                color = 'green'
            else:
                color = 'gray'

            plt.plot([time_const, time_const], [high_const, low_const], color=color)
            plt.plot([time_const, time_const], [open_const, close_const], linewidth=3, color=color)
            plt.title('GBPUSD')

    def fibonacci(self):
        total_list = self.open_list + self.close_list

        total = max(total_list) - min(total_list)

        if self.open_list.index(max(self.open_list)) > self.close_list.index(min(self.close_list)):
            one_hundred = min(total_list)
            seventy = 0.236 * total + min(total_list)
            sexty = 0.382 * total + min(total_list)
            fifty = 0.5 * total + min(total_list)
            thirty = 0.618 * total + min(total_list)
            tweenty = 0.764 * total + min(total_list)
            zero = max(total_list)
            neg_hundred = zero + total * 0.382 ** 2
            neg_hundred_sexty = zero + total * 0.382
            pos_hundred = one_hundred - total * 0.382 ** 2
            pos_hundred_sexty = one_hundred - total * 0.382

            fibo_list_f = [one_hundred, zero, seventy, sexty, fifty, thirty, tweenty, pos_hundred,
                           pos_hundred_sexty, neg_hundred, neg_hundred_sexty]

            curve_f = 1

            self.fibo_list, self.curve = fibo_list_f, curve_f

        else:
            one_hundred = max(total_list)
            seventy = 0.764 * total + min(total_list)
            sexty = 0.618 * total + min(total_list)
            fifty = 0.5 * total + min(total_list)
            thirty = 0.382 * total + min(total_list)
            tweenty = 0.236 * total + min(total_list)
            zero = min(total_list)
            neg_hundred = zero - total * 0.382 ** 2
            neg_hundred_sexty = zero - total * 0.382
            pos_hundred = one_hundred + total * 0.382 ** 2
            pos_hundred_sexty = one_hundred + total * 0.382

            fibo_list_f = [one_hundred, zero, seventy, sexty, fifty, thirty, tweenty, pos_hundred,
                           pos_hundred_sexty, neg_hundred, neg_hundred_sexty]

            curve_f = -1

            self.fibo_list, self.curve = fibo_list_f, curve_f

    def timer_att_fibolines_4min(self):

        if self.n[-4] == '4' or self.first_looping:

            self.fibonacci()

            self.first_looping = False

    def plot_fibo(self):
        for line in range(2, 4):
            plt.axhline(self.fibo_list[line], linestyle="--", linewidth=0.5)
        for line in range(5, 11):
            plt.axhline(self.fibo_list[line], linestyle="--", linewidth=0.5)
        plt.axhline(self.fibo_list[0], linestyle="--", color='k', linewidth=0.5)
        plt.axhline(self.fibo_list[1], linestyle="--", color='k', linewidth=0.5)
        plt.axhline(self.fibo_list[4], linestyle="--", color='k', linewidth=0.5)

    def media_movel(self, rates_frame):
        print(rates_frame)

    def processo(self):
        plt.ion()

        while True:
            rates = mt5.copy_rates_from_pos(self.mercado, self.time_frame, 0, self.time_range)
            rates_frame = pd.DataFrame(rates)
            rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')

            self.time_list = []
            self.open_list = []
            self.close_list = []

            self.grafico_contruction(rates_frame)

            self.n = str(self.time_list[-1]).replace('-', ' ').replace(':', ' ')

            self.timer_att_fibolines_4min()

            self.plot_fibo()

            plt.pause(0.00001)
            plt.clf()

            print(Grafico.close_list)

    def grafico_simulador(self, rates_frame):
        plt.ion()

        for i in range(0, self.time_range):

            time_const = rates_frame.time[i]
            high_const = rates_frame.high[i]
            low_const = rates_frame.low[i]
            open_const = rates_frame.open[i]
            close_const = rates_frame.close[i]

            self.open_list.append(open_const)
            self.close_list.append(close_const)
            self.time_list.append(time_const)
            self.high_list.append(high_const)
            self.low_list.append(low_const)

            if open_const > close_const:
                color = 'red'
            elif open_const < close_const:
                color = 'green'
            else:
                color = 'gray'

            plt.plot([time_const, time_const], [high_const, low_const], color=color)
            plt.plot([time_const, time_const], [open_const, close_const], linewidth=3, color=color)

    def simulador(self):

        days = self.months * 20

        for i in range(0, days):
            self.valor_inicial = 0
            self.tempos = []
            self.stop = 0
            self.take = 0
            self.lines = False

            self.first_looping = 1
            self.registro_tempo = 0
            self.key_fibo = 0

            self.ponto = self.ponto_inicial

            while self.ponto >= self.ponto_final:
                # get 10 GBPUSD D1 bars from the current day

                rates = mt5.copy_rates_from_pos(self.mercado, self.time_frame, self.ponto, self.time_range)
                self.ponto -= 1

                # create DataFrame out of the obtained data
                rates_frame = pd.DataFrame(rates)

                # convert time in seconds into the datetime format
                rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')

                self.time_list = []
                self.open_list = []
                self.close_list = []
                self.high_list = []
                self.low_list = []

                # Montagem e atualização do gráfico
                self.grafico_simulador(rates_frame)

                self.media_movel(rates_frame)

                # str do tempo
                self.n = str(self.time_list[-1]).replace('-', ' ').replace(':', ' ')

                # Atualização dos valores das linhas de Fibonacci
                self.timer_att_fibolines_4min()

                # Plotagem das linhas de Fibonacci
                self.plot_fibo()

                plt.pause(.0001)
                plt.clf()


MetaTrader = MetaTrader(50484595, "1ne3zFYQ")
MetaTrader.login()

Grafico = Grafico()
Grafico.simulador()
