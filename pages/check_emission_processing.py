                    #Проверка ИД после удаления выбросов
import streamlit as st
import pandas as pd
import utils.constants as const
from utils.data_processing import index_d_d

st.subheader("Проверка ИД после удаления выбросов")

st.markdown("""
В результате предварительной обработки ИД обнаружены и удалены выбросы. После удаления проверяется количество оставшихся образцов.
""")

df_clean = st.session_state.df_clean

#Общая информация
info_data = {
    'Параметр': df_clean.columns,
    'Тип данных': df_clean.dtypes.values,
    'Количество строк': df_clean.count().values,
    'Количество пропусков в данных': df_clean.isnull().sum().values,
}

info_df = pd.DataFrame(info_data)
st.dataframe(info_df)

st.markdown("""

* Число строк 453. Удалено 47 строк.
* Нет пропущенных значений *Nan*
* Названия столбцов соответствуют единому стилю
* Типы данных в столбцах *float64*.

При удалении выбросов данные не пострадали.
""")