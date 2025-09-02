import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import plotly.express as px
import utils.visualization as vis
import utils.constants as const
import utils.calculations as calc
from IPython.display import display

st.subheader(f"Расчет относительного сужения ${r'\psi'}$")

tab1, tab2, tab3 = st.tabs([
    "Распределение относительного сужения",
    "Проверка распределения",
    "Расчет базисных значений"
])

df = st.session_state.df

with tab1:
    st.header("Расчет среднего значения относительного сужения")
    
    #Визуализация гистограммы
    hist_psi = vis.general_graph(
        df['psi'],
        const.title_psi,
        const.x_title_psi,
        check_line_mean=True,
        check_3_sigma=True
    )
    
    st.plotly_chart(hist_psi)
    
    #Визуализация боксплота
    box_psi = vis.box(
        df['psi'],
        const.title_psi,
        const.x_title_psi
    )
    
    st.plotly_chart(box_psi)

    st.markdown(f"Среднее значение относительного сужения ${r'\psi'} = 45.51{r'\%'} $")
    
    with st.expander("Формулы расчета"):
        st.markdown(f"Относительное сужение ${r'\psi'}$ вычисляется по формуле")
        st.latex(r'''
        \psi = \frac{(F_0 - F_k) \cdot 100}{F_0},''')
        st.markdown(f"где ${r'F_0'}$ - площадь поперечного сечения образца до испытания. Вычисляется по формуле")
        st.latex(r'''
            {F_0} = \frac{\pi \cdot {d_0}^2}{4},
            ''')
        st.markdown(f"${r'd_0'}$ - диаметр рабочей части цилиндрического образца до испытания. Задается распределением ИД.")
        st.markdown(f"${r'F_k'}$ - площадь поперечного сечения образца после испытания. Вычисляется по формуле:")
        st.latex(r'''{F_k} = \frac{\pi \cdot {d_k}^2}{4},''')
        st.markdown(f"${r'd_k'}$ - диаметр рабочей части цилиндрического образца после испытания. Задается распределением ИД.")

with tab2:
    
    st.header("Проверка распределения относительного сужения")
    
    import utils.text_basis

    #Проверка нормальности распределения
    calc.check_test(calc.test_normal(df['psi']), r'\psi')

with tab3:
    
    st.header("Расчет базисных значений относительного сужения")

    #Расчет базисов 
    psi_basis = calc.calculate_basis(df['psi'])
    
    #Визуализация базисов на гистограмме
    #А базис
    psi_basis_a = vis.general_graph(
        df['psi'],
        title=const.title_psi + const.title_basis_a,
        x_title=const.x_title_psi,
        check_line_mean=True,
        check_basis=True,
        basis=psi_basis['A_basis'],
        type_basis=f'{const.title_basis_a} = {psi_basis['A_basis']} %'
    )
    
    st.plotly_chart(psi_basis_a)
    
    #В базис
    psi_basis_b = vis.general_graph(
        df['psi'],
        title=const.title_psi + const.title_basis_b,
        x_title=const.x_title_psi,
        check_line_mean=True,
        check_basis=True,
        basis=psi_basis['B_basis'],
        type_basis=f'{const.title_basis_b} = {psi_basis['B_basis']} %'
    )
    
    st.plotly_chart(psi_basis_b)

    st.markdown(f"Вычисленные значения базисов относительного сужения ${r'\psi'}$:")
    st.markdown(f"* **А-базис** ${r'\psi'} = 42.41 {r'\%'}$ - выше этого значения находятся не менее 99% всей совокупности значений с достоверностью 95%.")
    st.markdown(f"* **B-базис** ${r'\psi'} = 43.78 {r'\%'}$ - выше этого значения находятся не менее 90% всей совокупности значений с достоверностью 95%.")
    with st.expander("Формулы расчета"):
        import utils.formuls_basis




   