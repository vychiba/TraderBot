import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

# Graph sizes

figure(figsize=(3, 3))

# Plots graph simulation


def grafico_simulador(time_range, rates_frame, open_list, close_list, time_list, high_list, low_list):
    for i in range(0, time_range):

        time_const = rates_frame.time[i]
        high_const = rates_frame.high[i]
        low_const = rates_frame.low[i]
        open_const = rates_frame.open[i]
        close_const = rates_frame.close[i]

        open_list.append(open_const)
        close_list.append(close_const)
        time_list.append(time_const)
        high_list.append(high_const)
        low_list.append(low_const)

        if open_const > close_const:
            color = 'red'
        elif open_const < close_const:
            color = 'green'
        else:
            color = 'gray'

        plt.plot([time_const, time_const], [high_const, low_const], color=color)
        plt.plot([time_const, time_const], [open_const, close_const], linewidth=3, color=color)

# Plots graph


def grafico(time_range, rates_frame, open_list, close_list, time_list):
    for i in range(0, time_range):

        time_const = rates_frame.time[i]
        high_const = rates_frame.high[i]
        low_const = rates_frame.low[i]
        open_const = rates_frame.open[i]
        close_const = rates_frame.close[i]

        open_list.append(open_const)
        close_list.append(close_const)
        time_list.append(time_const)

        if open_const > close_const:
            color = 'red'
        elif open_const < close_const:
            color = 'green'
        else:
            color = 'gray'

        plt.plot([time_const, time_const], [high_const, low_const], color=color)
        plt.plot([time_const, time_const], [open_const, close_const], linewidth=3, color=color)
        plt.title('GBPUSD')

# Creates Fibonacci Lines


def fibonacci(open_list, close_list):
    total_list = open_list + close_list

    total = max(total_list) - min(total_list)

    if open_list.index(max(open_list)) > close_list.index(min(close_list)):
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

        fibo_list_f = [one_hundred, zero, seventy, sexty, fifty, thirty, tweenty, pos_hundred \
            , pos_hundred_sexty, neg_hundred, neg_hundred_sexty]

        curve_f = 1

        return fibo_list_f, curve_f

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

        fibo_list_f = [one_hundred, zero, seventy, sexty, fifty, thirty, tweenty, pos_hundred \
            , pos_hundred_sexty, neg_hundred, neg_hundred_sexty]

        curve_f = -1

        return fibo_list_f, curve_f

# Plots Fibonacci Lines


def plot_fibo(fibo_list):
    for line in range(2, 4):
        plt.axhline(fibo_list[line], linestyle="--", linewidth=0.5)
    for line in range(5, 11):
        plt.axhline(fibo_list[line], linestyle="--", linewidth=0.5)
    plt.axhline(fibo_list[0], linestyle="--", color='k', linewidth=0.5)
    plt.axhline(fibo_list[1], linestyle="--", color='k', linewidth=0.5)
    plt.axhline(fibo_list[4], linestyle="--", color='k', linewidth=0.5)
