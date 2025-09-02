import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import plotly.express as px
import utils.visualization as vis
import utils.constants as const
import utils.calculations as calc


st.subheader(f"Расчет относительного удлинения ${r'\delta'}$")

tab1, tab2, tab3 = st.tabs([
    "Распределение относительного удлинения",
    "Проверка распределения",
    "Расчет базисных значений"
])

df = st.session_state.df

with tab1:
    st.header("Расчет среднего значения относительного удлинения")

    #Визуализация гистограммы
    hist_delta = vis.general_graph(
        df['delta'],
        const.title_delta,
        const.x_title_delta,
        check_line_mean=True,
        check_3_sigma=True
    )
    
    st.plotly_chart(hist_delta)
    
    #Визуализация боксплота
    box_delta = vis.box(
        df['delta'],
        const.title_delta,
        const.x_title_delta
    )
    
    st.plotly_chart(box_delta)

    st.markdown(f"Среднее значение относительного удлинения ${r'\delta'} = 9.9{r'\%'} $")

    with st.expander("Формулы расчета"):
        st.markdown(f"Относительное удлинение ${r'\delta'}$ вычисляется по формуле")
        st.latex(r'''
        \delta = \frac{(l_k - l_0) \cdot 100}{l_0},''')
        st.markdown(f"где ${r'l_0'}$ - участок рабочей длины образца до испытания. Задается распределением ИД.") 
        st.markdown(f"${r'l_k'}$ - участок рабочей длины образца после испытания. Задается распределением ИД.")
with tab2:
    
    st.header("Проверка распределения относительного удлинения")
    import utils.text_basis

    #Проверка нормальности распределения для относительного удлинения
    calc.check_test(calc.test_normal(df['delta']), r'\delta')

with tab3:
    st.header("Расчет базисных значений относительного удлинения")

    #Расчет базисов относительного удлинения
    delta_basis = calc.calculate_basis(df['delta'])
    
    #Визуализация базисов на гистограмме
    #А базис
    delta_basis_a = vis.general_graph(
        df['delta'],
        title=const.title_delta + const.title_basis_a,
        x_title=const.x_title_delta,
        check_line_mean=True,
        check_basis=True,
        basis=delta_basis['A_basis'],
        type_basis=f'{const.title_basis_a} = {delta_basis['A_basis']} %'
    )
    
    st.plotly_chart(delta_basis_a)
    
    #В базис
    delta_basis_b = vis.general_graph(
        df['delta'],
        title=const.title_delta + const.title_basis_b,
        x_title=const.x_title_delta,
        check_line_mean=True,
        check_basis=True,
        basis=delta_basis['B_basis'],
        type_basis=f'{const.title_basis_b} = {delta_basis['B_basis']} %'
    )
    
    st.plotly_chart(delta_basis_b)

    st.markdown(f"Вычисленные значения базисов относительного удлинения ${r'\delta'}$:")
    st.markdown(f"* **А-базис** ${r'\delta'} = 4.93 {r'\%'}$ - выше этого значения находятся не менее 99% всей совокупности значений с достоверностью 95%.")
    st.markdown(f"* **B-базис** ${r'\delta'} = 7.12 {r'\%'}$ - выше этого значения находятся не менее 90% всей совокупности значений с достоверностью 95%.")
    with st.expander("Формулы расчета"):
        import utils.formuls_basis


    