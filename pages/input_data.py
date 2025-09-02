import streamlit as st
import pandas as pd

st.subheader("Исходные данные")
st.markdown("""***В данном проекте ИД синтетические, сгенерированы на основе нормального распределения с добавлением выбросов.***""")

st.markdown("""Исходными данными (ИД) для проведениея анализа являются результаты испытаний образцов на разрывной машине.

Термообработка образцов:  
*Закалка 880°C - масло*  
*Отпуск 540°C - вода*
""")

st.markdown("""Образцы соответствуют требованиями **ГОСТ 1497-84**.""")

st.link_button("ГОСТ 1497-84", "https://engineerexpert.ru/wp-content/uploads/docs/gost_1497-84.pdf")

st.image("image/cylindrical_sample.png", caption="Пропорциональные цилиндрические образцы")

#Загрузка данных
df_initial = st.session_state.df_initial

#Вывод первых 5 строк
st.write("Первые 5 строк данных:")
st.dataframe(df_initial.head(), width=800)

st.write("Общая информация о данных")
#Общая информация
info_data = {
    'Параметр': df_initial.columns,
    'Тип данных': df_initial.dtypes.values,
    'Количество строк': df_initial.count().values,
    'Количество пропусков в данных': df_initial.isnull().sum().values,
}

info_df = pd.DataFrame(info_data)
st.dataframe(info_df)

st.markdown("""
Первичный анализ данных:

* Датафрейм содержет: 5 столбцов и 500 строк  
* В датафрейме нет пропущенных значений *Nan*  
* Названия столбцов соответствуют единому стилю
* Типы данных в столбцах *float64*

""")

st.markdown("""Медианные значения ИД""")

median_data = {
    'Параметр': df_initial.columns,
    'Медианные величины': [df_initial['d_0'].median(),
                           df_initial['l_0'].median(),
                           df_initial['d_k'].median(),
                           df_initial['l_k'].median(),
                           round(df_initial['P_max'].median(), 2)],
    'Единицы измерения' : ['мм',
                           'мм',
                           'мм',
                           'мм',
                           'Н']                           
}


median_data_df = pd.DataFrame(median_data)

st.dataframe(median_data_df)




