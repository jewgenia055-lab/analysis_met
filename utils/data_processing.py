import pandas as pd

#Функция индексов отклонений размеров
#ser - Series для построения гистограммы
#d_d - предельное отклонение размеров

def index_d_d(ser, d_d):
    
    #Индексы значений менее нижней границы отклонений
    index_bot_d_d = list(ser[ser <= ser.mean() - d_d].index)
    
    #Индексы значений больше верхней границы отклонений
    index_top_d_d = list(ser[ser >= ser.mean() + d_d].index)

    return index_bot_d_d + index_top_d_d