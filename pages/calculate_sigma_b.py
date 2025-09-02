                    #Расчет предела прочности
import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import plotly.express as px
import utils.visualization as vis
import utils.constants as const
import utils.calculations as calc

st.subheader(f"Расчет предела прочности ${r'\sigma_b'}$")


tab1, tab2, tab3 = st.tabs([
    "Распределение предела прочности",
    "Проверка распределения",
    "Расчет базисных значений"
])

df = st.session_state.df

with tab1:
    st.header("Расчет среднего значения предела прочности")
    
        #Визуализация гистограммы
    hist_sigma_b = vis.general_graph(
        df['sigma_b'],
        const.title_sigma_b,
        const.x_title_sigma_b,
        check_line_mean=True,
        check_3_sigma=True
    )
    
    st.plotly_chart(hist_sigma_b)
    
    #Визуализация боксплота
    box_sigma_b = vis.box(
        df['sigma_b'],
        const.title_sigma_b,
        const.x_title_sigma_b
    )
    
    st.plotly_chart(box_sigma_b)

    st.markdown(f"Среднее значение предела прочности ${r'\sigma_b'} = 1080.43 (МПа)$")

    with st.expander("Формулы расчета"):
            st.markdown(f"Предел прочности ${r'\sigma_b'}$ вычисляется по формуле")
            st.latex(r'''
            {\sigma_b} = \frac{P_{\text{max}}}{F_0},
            ''')
            st.markdown(f"где $P_{{{'max'}}}$ - наибольшее усилие, предшествующее разрыву образца. Задается распределением ИД.")
            st.markdown(f"${r'F_0'}$ - площадь поперечного сечения образца до испытания. Вычисляется по формуле")
            #st.markdown(r"$F_0 = \frac{\pi \cdot d_0^2}{4}$")
            st.latex(r'''
            {F_0} = \frac{\pi \cdot {d_0}^2}{4},
            ''')
            st.markdown(f"${r'd_0'}$ - диаметр рабочей части цилиндрического образца до испытания. Задается распределением ИД.")


with tab2:
    
    st.header("Проверка распределения предела прочности")

    import utils.text_basis

    #Проверка нормальности распределения для предела прочности
    calc.check_test(calc.test_normal(df['sigma_b']), r'\sigma_b')
    
with tab3: 
    st.header("Расчет базисных значений предела прочности")

        #Расчет базисов предела прочности
    sigma_b_basis = calc.calculate_basis(df['sigma_b'])
    
    #Визуализация базисов на гистограмме
    #А базис
    sigma_b_basis_a = vis.general_graph(
        df['sigma_b'],
        title=const.title_sigma_b + const.title_basis_a,
        x_title=const.x_title_sigma_b,
        check_line_mean=True,
        check_basis=True,
        basis=sigma_b_basis['A_basis'],
        type_basis=f'{const.title_basis_a} = {sigma_b_basis['A_basis']} МПа'
    )
    
    st.plotly_chart(sigma_b_basis_a)
    
    #В базис
    sigma_b_basis_b = vis.general_graph(
        df['sigma_b'],
        title=const.title_sigma_b + const.title_basis_b,
        x_title=const.x_title_sigma_b,
        check_line_mean=True,
        check_basis=True,
        basis=sigma_b_basis['B_basis'],
        type_basis=f'{const.title_basis_b} = {sigma_b_basis['B_basis']} МПа'
    )
    
    st.plotly_chart(sigma_b_basis_b)

    st.markdown(f"Вычисленные значения базисов предела прочности ${r'\sigma_b'}$:")
    st.markdown(f"* **А-базис** ${r'\sigma_b'} = 1033.68 (МПа)$ - выше этого значения находятся не менее 99% всей совокупности значений с достоверностью 95%.")
    st.markdown(f"* **B-базис** ${r'\sigma_b'} = 1054.25 (МПа)$ - выше этого значения находятся не менее 90% #всей совокупности значений с достоверностью 95%.")
    with st.expander("Формулы расчета"):
        import utils.formuls_basis
        