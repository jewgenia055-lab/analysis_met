import streamlit as st
import pandas as pd
import utils.constants as const
from utils.data_processing import index_d_d
import utils.calculations as calc


#Настройка страницы
st.set_page_config(page_title="Расчетные характеристики 30ХГСА", layout="centered")

#Загрузка исходных данных 
if 'df' not in st.session_state:
    pd.set_option('display.max_colwidth', None) 
    #Исходный датафрейм (первое прочтение)
    st.session_state.df_initial = pd.read_csv("data/metal_data.csv")

    #Предобработка данных (очищение от выбросов)
    st.session_state.df_clean = None
    
    #Для расчета
    st.session_state.df = None

    #Базисы
    st.session_state.df_basis = None
    
    st.session_state.data_loaded = True


                #Удаление выбросов
df_initial = st.session_state.df_initial

#Индексы выбросов столбца d_0
index_del_d_0 = index_d_d(df_initial['d_0'], const.d_d_diam)

#Индексы выбросов столбца l_0
index_del_l_0 = index_d_d(df_initial['l_0'], const.d_d_len)

#Индексы выбросов столбца l_k
index_del_l_k = index_d_d(df_initial['l_k'], df_initial['l_k'].std() * 3)

#Индексы выбросов столбца P_max
index_del_P_max = index_d_d(df_initial['P_max'], df_initial['P_max'].std() * 3)

index_del = list(index_del_d_0) + list(index_del_l_0) + list(index_del_l_k) + list(index_del_P_max)

df_clean = st.session_state.df_initial.copy(deep=True)

#Удаление выбросов
df_clean = df_clean.drop(index=index_del).reset_index(drop=True)

#Перезапись датафрейма
st.session_state.df_clean = df_clean


                #Заполнение расчетами

df = st.session_state.df_clean.copy(deep=True)

#Вычисление площади поперечного сечения образца до приложения нагрузки
df['F_0'] = df['d_0'].apply(calc.area).round(2)

#Вычисление площади поперечного сечения образца после приложения нагрузки
df['F_k'] = df['d_k'].apply(calc.area).round(2)

#Расчет предела прочности
df['sigma_b'] = (df['P_max'] / df['F_0']).round(2)

#Вычисление удлинения
df['delta'] = (((df['l_k'] - df['l_0']) / df['l_0']) * 100).round(2)

#Вычисление удлинения
df['psi'] = (((df['F_0'] - df['F_k']) / df['F_0']) * 100).round(2)

#Перезапись датафрейма
st.session_state.df = df

            #Базисы

#Предел прочности
sigma_b_basis = calc.calculate_basis(df['sigma_b'])
#Отн удлинен
delta_basis = calc.calculate_basis(df['delta'])
#Отн сужен
psi_basis = calc.calculate_basis(df['psi'])

df_basis = pd.DataFrame(
    {
        'Среднее значение': [round(df['sigma_b'].mean(), 2),
                             round(df['delta'].mean(), 2),
                             round(df['psi'].mean(), 2)],
        
        'А-базис': [sigma_b_basis['A_basis'],
                    delta_basis['A_basis'],
                    psi_basis['A_basis']],
        
        'В-базис': [sigma_b_basis['B_basis'],
                    delta_basis['B_basis'],
                    psi_basis['B_basis']]
    },
    
    index=['Предел прочности σ_b, МПа',
           'Относительное удлинение δ, %',
           'Относительное сужение ψ, %']
)

st.session_state.df_basis = df_basis


                #Страницы проекта

pages = {
    "Введение": [
        st.Page("pages/project.py", title="Описание проекта"),
        st.Page("pages/thermins.py", title="Термины и определения"),
        st.Page("pages/untils.py", title="Обозначения и единицы измерения величин"),
        st.Page("pages/input_data.py", title="Исходные данные")
    ],

    "Предварительная обработка данных" : [
        st.Page("pages/emission_processing.py", title="Предварительная обработка данных"),
        st.Page("pages/check_emission_processing.py", title="Проверка после предварительной обработки")
    ],
        
    "Расчет механических характеристик": [
        st.Page("pages/calculate_sigma_b.py", title="Расчет предела прочности"),
        st.Page("pages/calculate_delta.py", title="Расчет относительного удлинения"),
        st.Page("pages/calculate_psi.py", title="Расчет относительного сужения"),
        
    ],

    "Выводы" : [
        st.Page("pages/conclusions.py", title="Выводы"),
        st.Page("pages/pivot_table.py", title="Сводная таблица")
        
    ]
    
}

pg = st.navigation(pages)
pg.run()