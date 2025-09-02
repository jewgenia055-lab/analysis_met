                                #Предварительная обработка данных
import streamlit as st
import pandas as pd
import plotly.express as px
import utils.visualization as vis
import utils.constants as const
from utils.data_processing import index_d_d

st.subheader("Предварительная обработка значений - проверка на наличие выбросов")

st.markdown(f"По **ГОСТ 1497-84** площадь поперечного сечения образцов ${r'F_0'}$ до приложения нагрузки допускается определять по номинальным размерам при условии соответствия отклонениий таблице.")
st.link_button("ГОСТ 1497-84", "https://engineerexpert.ru/wp-content/uploads/docs/gost_1497-84.pdf")
 
st.image("image/table_d_d.png", caption="Таблица отклонений размеров образцов")

st.markdown(f"Поскольку ${r'd_0 = 25 мм'}$, а ${r'l_0 = 125 мм'}$ (медианные значения), то выбросами в линейных размерах до приложения нагрузки считаются значения:")

st.markdown(f"*  ${r'd_0'}$ ${r'\pm'}$ ${r'0.05 (мм)'}$;")
st.markdown(f"*  ${r'l_0'}$ ${r'\pm'}$ ${r'0.105 (мм)'}$.")

st.markdown(f"Выбросами в линейных размерах после приложения нагрузки ${r'd_k'}$, ${r'l_k'}$ и максимальном усилии разрыва $P_{{{'max'}}}$ считаются значения более ${r'\pm'}$ 3${r'\sigma'}$.")


df_initial = st.session_state.df_initial
df_clean = st.session_state.df_clean


                            #Перенос основного кода из Юпитера

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    f"${r'd_0'}$",
    f"${r'd_k'}$",
    f"${r'l_0'}$",
    f"${r'l_k'}$",
    f"$P_{{{'max'}}}$"
])

with tab1:
    st.header(f"${r'd_0'} - $ Диаметр цилиндрического образца до испытания")
    #Визуализация гистограммы
    hist_d_0 = vis.general_graph(
        df_initial['d_0'],
        const.title_d_0,
        const.x_title_d_0,    
        d_d = const.d_d_diam,
        check_line_mean=True
    )
    
    st.plotly_chart(hist_d_0)

    #Визуализация боксплота
    box_d_0 = vis.box(
        df_initial['d_0'],
        const.title_d_0,
        const.x_title_d_0,
        d_d = const.d_d_diam
    )

    st.plotly_chart(box_d_0)

    st.markdown(f"* В ИД есть выбросы - диаметры вне допуска ${r'd_0'}$ ${r'\pm'}$  ${r'0.05 (мм)'}$.") 
    
    st.markdown(f"Выбросы ${r'd_0'}$ удаляются из анализа.")
    

    #Проверка удаления - визуализация гистограммы
    hist_d_0 = vis.general_graph(
        df_clean['d_0'],
        const.title_d_0,
        const.x_title_d_0,
        check_line_mean=True
    )

    st.plotly_chart(hist_d_0)
    st.markdown(f"* Средний диаметр образцов до испытаний  ${r'd_0 = 25 (мм)'}$.") 
    st.markdown(f"* Выбросы - диаметры вне допуска ${r'd_0'}$ ${r'\pm'}$  ${r'0.05 (мм)'}$ удалены.")
    
with tab2:
    st.header(f"${r'd_k'} - $ Диаметр цилиндрического образца после испытания")

    #Визуализация гистограммы
    hist_d_k = vis.general_graph(
        df_initial['d_k'],
        const.title_d_k,
        const.x_title_d_k,
        check_line_mean=True,
        check_3_sigma=True
    )

    st.plotly_chart(hist_d_k)

    #Визуализация боксплота
    box_d_k = vis.box(
        df_initial['d_k'],
        const.title_d_k,
        const.x_title_d_k,
        check_3_sigma=True
    )

    st.plotly_chart(box_d_k)

    st.markdown(f"* Средний диаметр образцов после испытаний  ${r'd_k = 18.45 (мм)'}$.")
    st.markdown("""* Выбросов нет.""")

    
with tab3:
    st.header(f"${r'l_0'} - $ Длина цилиндрического образца до испытания")
    
    #Визуализация гистограммы
    hist_l_0 = vis.general_graph(
        df_initial['l_0'],
        const.title_l_0,
        const.x_title_l_0,    
        d_d = const.d_d_len,
        check_line_mean=True
    )
    
    st.plotly_chart(hist_l_0)

    #Визуализация боксплота
    box_l_0 = vis.box(
        df_initial['l_0'],
        const.title_l_0,
        const.x_title_l_0,
        d_d = const.d_d_len
    )

    st.plotly_chart(box_l_0)

      
    st.markdown(f"* В ИД есть выбросы - длины вне допуска ${r'l_0'}$ ${r'\pm'}$  ${r'0.105 (мм)'}$.") 
    
    st.markdown(f"Выбросы ${r'l_0'}$ удаляются из анализа.")

    #Проверка удаления - визуализация гистограммы
    hist_l_0 = vis.general_graph(
        df_clean['l_0'],
        const.title_l_0,
        const.x_title_l_0,
        check_line_mean=True
    )

    st.plotly_chart(hist_l_0)
    st.markdown(f"* Средняя длина образцов до испытаний  ${r'l_0 = 125 (мм)'}$.")
    st.markdown(f"* Выбросы - длины вне допуска ${r'l_0'}$ ${r'\pm'}$  ${r'0.105 (мм)'}$ удалены.")

with tab4:
    st.header(f"${r'l_k'} - $ Длина цилиндрического образца после испытания")
    
    #Визуализация гистограммы
    hist_l_k = vis.general_graph(
        df_initial['l_k'],
        const.title_l_k,
        const.x_title_l_k,
        check_line_mean=True,
        check_3_sigma=True
    )
    
    st.plotly_chart(hist_l_k)

    #Визуализация боксплота
    box_l_k = vis.box(
        df_initial['l_k'],
        const.title_l_k,
        const.x_title_l_k,
        check_3_sigma=True
    )

    st.plotly_chart(box_l_k)

     
    st.markdown(f"* В ИД есть выбросы - длины вне допуска ${r'l_k'}$ ${r'\pm'}$ 3${r'\sigma'}$.") 
    
    st.markdown(f"Выбросы ${r'l_k'}$ удаляются из анализа.")
    
    #Проверка удаления - визуализация гистограммы
    hist_l_k = vis.general_graph(
        df_clean['l_k'],
        const.title_l_k,
        const.x_title_l_k,
        check_line_mean=True,
    )

    st.plotly_chart(hist_l_k)
    st.markdown(f"* Средняя длина образцов после испытаний  ${r'l_k = 137.38 (мм)'}$.") 
    st.markdown(f"* Выбросы - длины вне допуска ${r'l_k'}$ ${r'\pm'}$ 3${r'\sigma'}$ удалены.")
    
with tab5:
    st.header(f"$P_{{{'max'}}} - $ Максимальное усилие разрыва")
    
    #Визуализация гистограммы
    hist_P_max = vis.general_graph(
        df_initial['P_max'],
        const.title_P_max,
        const.x_title_P_max,
        check_line_mean=True,
        check_3_sigma=True
    )
    
    st.plotly_chart(hist_P_max)

    #Визуализация боксплота
    box_P_max = vis.box(
        df_initial['P_max'],
        const.title_P_max,
        const.x_title_P_max,
        check_3_sigma=True
    )

    st.plotly_chart(box_P_max) 
    
    st.markdown(f"* В ИД есть выбросы - значения вне диапазона $P_{{{'max'}}}$ ${r'\pm'}$ 3${r'\sigma'}$.") 
    
    st.markdown(f"Выбросы $P_{{{'max'}}}$ удаляются из анализа.")

    #Проверка удаления - визуализация гистограммы
    hist_P_max = vis.general_graph(
        df_clean['P_max'],
        const.title_P_max,
        const.x_title_P_max,
        check_line_mean=True,
    )

    st.plotly_chart(hist_P_max)
    st.markdown(f"* Среднее усилие растяжения образцов $P_{{{'max'}}} = 53 0407.84 (H)$.")
    st.markdown(f"* Выбросы - усилия вне допуска $P_{{{'max'}}}$ ${r'\pm'}$ 3${r'\sigma'}$ удалены.")




