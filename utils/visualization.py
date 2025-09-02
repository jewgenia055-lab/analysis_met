import plotly.express as px
import pandas as pd

#Функция добавления статистик на график
#ser - Series 
#fig - фигура на которую наносятся статистики

def add_stat_annotations(ser, fig):
    
    #Аннотация со статистикой
    fig.add_annotation(
        x=1, y=0.98,
        xref="paper", yref="paper",
        text=f"<b>Статистика:</b><br>"
             f"μ = {ser.mean():.2f}<br>"
             f"σ = {ser.std():.2f}<br>",

        showarrow=False,
        bgcolor="white",
        bordercolor="black",
        borderwidth=1,
        borderpad=4,
        font=dict(size=10)
    )
    return fig

#Функция определения 3сигм
#ser - Series для построения гистограммы
#fig - фигура на которую наносятся линии 3 сигм

def sigm(ser, fig):
    
    #Линии для 3 сигм
    fig.add_vline(
        x=ser.mean() + 3 * ser.std(),
        line_dash="dot",
        line_color="orange",
        annotation_text="+3σ",
        annotation_position="top"
    )
    
    fig.add_vline(
        x=ser.mean() - 3 * ser.std(),
        line_dash="dot",
        line_color="orange",
        annotation_text="-3σ",
        annotation_position="top"
    )

    #Закраска области между границами
    fig.add_vrect(
        x0=ser.mean() - 3 * ser.std(),
        x1=ser.mean() + 3 * ser.std(),
        fillcolor="green",
        opacity=0.1
    )

    return fig

#Функция определения допусков
#ser - Series 
#fig - фигура на которую наносятся линии допусков
#d_d - предельное отклонение размеров

def line_d_d(ser, fig, d_d):
    
    #Линии для отклонений размеров
    fig.add_vline(
        x=ser.mean() + d_d,
        line_dash='dashdot',
        line_color='black',
        annotation=dict(
            text=f"{ser.mean():.0f}+{d_d}",
            #textangle=-90,
            bgcolor="rgba(255, 255, 255, 0.8)"
        ),
        #annotation_text=f"{ser.mean():.0f}+{d_d}",
        annotation_position='top'
    )

        #Закраска области между границами
    fig.add_vrect(
        x0=ser.mean() + d_d,
        x1=ser.max(),
        fillcolor="red",
        opacity=0.1
    )


    fig.add_vline(
        x=ser.mean() - d_d,
        line_dash='dashdot',
        line_color='black',
        annotation=dict(
            text=f"{ser.mean():.0f}-{d_d}",
            #textangle=-90,
            bgcolor="rgba(255, 255, 255, 0.8)"
        ),
        #annotation_text=f"{ser.mean():.0f}-{d_d}",
        annotation_position='top'
    )


    #Закраска области между границами
    fig.add_vrect(
        x0=ser.min(),
        x1=ser.mean() - d_d,
        fillcolor="red",
        opacity=0.1
    )

    return fig

#Функция создания гистограмм
#ser - Series для построения гистограммы
#title - название графика
#x_title - подпись оси x
#y_title - подпись оси y

def hist(ser, title, x_title):
    
    #Создание гистограммы
    fig = px.histogram(
        x=ser,
        title=f'Распределение {title}'        
    )

    #Подписи осей
    fig.update_layout(
        xaxis_title=x_title,
        yaxis_title='Количество образцов'
    )
    
    return fig

#Функция добавления линии матожидания
#ser - Series
#fig_hist - фигура гистограммы

def line_mean(ser, fig):

    #Добавление линии матожидания
    fig.add_vline(
        x=ser.mean(),
        line_dash="solid",
        line_color="red", 
        annotation_text="Мат.ожидание",
        annotation_position="top"
    )
    
    return fig

#Функция создания графиков
#ser - Series
#title - название графика
#x_title - подпись оси x
#y_title - подпись оси y
#d_d - предельное отклонение размеров
#check_3_sigma - наносить/не наносить линии трех сигм на график
#check_line_mean - наносить/не наносить линию матожидания
#check_basis - наносить/не наносить базисы
#basis - значение бзиса
#type_basis - тип базиса

def general_graph(ser, title, x_title,
                  d_d=None, check_line_mean=False,
                  check_3_sigma=False, check_basis=False,
                  basis=None, type_basis=None):
    
  
    #Создание гистограммы
    fig_hist = hist(ser, title, x_title)
    
    #Линия матожидания
    if check_line_mean is not False:
        fig_hist = line_mean(ser, fig_hist)

    #Добавление линий 3 сигм
    if check_3_sigma is not False:
        fig_hist = sigm(ser, fig_hist)
    
    #Добавление аннотаций
    fig_hist = add_stat_annotations(ser, fig_hist)

    #Добавление линий отклонений размеров
    if d_d is not None:
        fig_hist = line_d_d(ser, fig_hist, d_d)

    #Добавление базисов
    if check_basis is not False:
        fig_hist = plot_basis(ser, fig_hist, basis, type_basis)   

    
    return fig_hist

#Функция создания боксплота
#ser - Series для построения боксплота
#title - название боксплота
#x_title - подпись оси x
#d_d - предельное отклонение размеров
#check_3_sigma - наносить/не наносить линии трех сигм на график


def box(ser, title, x_title, d_d=None, check_3_sigma=False):
    
    #Создание боксплота
    fig = px.box(
        x=ser,
        title=f'Диаграмма размаха {title}'
    )
    
    #Подписи осей
    fig.update_layout(
        xaxis_title=x_title,
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)
    )
    
    #Добавление линий отклонений размеров
    if d_d is not None:
        fig = line_d_d(ser, fig, d_d)
    
    #Добавление линий 3 сигм
    if check_3_sigma is not False:
        fig = sigm(ser, fig)

    return fig

#Функция отрисовки базисов
#ser - Series
#fig - гистограмма
#basis - pначение базиса
#type_basis - тип базиса

def plot_basis(ser, fig, basis, type_basis):

    #Задание цветов для базисов
    if 'A' in type_basis:
        color = '#AB63FA'
    else:
        color = '#19D3F3'
        
   
    #Вертикальная линия базиса
    fig.add_vline(
        x=basis,
        line_width=3,
        line_dash="dash", 
        line_color=color, 
        annotation=dict(
            text=type_basis,
            textangle=-90,
            bgcolor="rgba(255, 255, 255, 0.8)"
        ),
        annotation_position="left"
        )


    
    #Закраска области между границами
    fig.add_vrect(
        x0=basis,
        x1=ser.max() + 1,
        fillcolor=color,
        opacity=0.1
   )

    return fig

