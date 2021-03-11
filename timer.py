import datetime as datetime
from datetime import timedelta
import grafico as graf

# init trading (t1)
# end trading (t2)

# One Trade phase


def timer_pregao(t1, t2):

    time1 = datetime.time.fromisoformat(t1)
    time2 = datetime.time.fromisoformat(t2)

    time_now = datetime.time.fromisoformat(datetime.datetime.now().strftime("%H:%M:%S"))

    if time2 > time_now > time1:
        return True

    else:
        return False

# Two Trades phases


def timer_pregao_2(t1, t2, t3, t4):

    time1 = datetime.time.fromisoformat(t1)
    time2 = datetime.time.fromisoformat(t2)
    time3 = datetime.time.fromisoformat(t3)
    time4 = datetime.time.fromisoformat(t4)

    time_now = datetime.time.fromisoformat(datetime.datetime.now().strftime("%H:%M:%S"))

    if time2 > time_now > time1:
        return True

    elif time4 > time_now > time3:
        return True

    else:
        return False

# Time control for timeframe = 4 minute


def timer_att_fibolines_4min(n_value, first_looping_value, open_list_value, close_list_value, fibo_list_value, curve_value):

    if n_value[-4] == '4' or first_looping_value:

        fibo_list_f, curve_f = graf.fibonacci(open_list_value, close_list_value)

        first_looping_f = False

        return fibo_list_f, curve_f, first_looping_f

    else:
        fibo_list_f, curve_f, first_looping_f = fibo_list_value, curve_value, first_looping_value

        return fibo_list_f, curve_f, first_looping_f

# Time control for timeframe = 1 minute


def timer_att_fibolines_1min(n_value, first_looping_value, open_list_value, close_list_value, fibo_list_value, curve_value):

    if n_value[-4] == '0' or first_looping_value:
        # Montagem das linhas de Fibonacci
        fibo_list_f, curve_f = graf.fibonacci(open_list_value, close_list_value)

        first_looping_f = False

        return fibo_list_f, curve_f, first_looping_f

    else:
        fibo_list_f, curve_f, first_looping_f = fibo_list_value, curve_value, first_looping_value

        return fibo_list_f, curve_f, first_looping_f

# Time control for Simulations


def delta_time_trade_simulation(trade_time):
    time1 = datetime.time.isoformat(datetime.time(trade_time, 0, 0))
    time2 = datetime.time.isoformat(datetime.datetime.now().time())
    time3 = timedelta(hours=trade_time)
    time4 = timedelta(minutes=datetime.datetime.now().minute, hours=datetime.datetime.now().hour)

    if time2 > time1:
        delta = time4 - time3
    else:
        delta = time3 - time4

    minutos = datetime.datetime.strptime(str(delta), '%H:%M:%S').time().minute
    horas = datetime.datetime.strptime(str(delta), '%H:%M:%S').time().hour

    total_points = int(horas) * 15 + int(minutos) // 4

    print(total_points)

    return total_points
