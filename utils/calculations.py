import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import utils.constants as const

#Функция вычисления площади поперечного сечения образца
#diam - диаметр образца
def area(diam):      
    return np.pi * (diam ** 2) / 4



#Функция расчета pvalue
#ser - Series для проверки распределения

def test_normal(ser):
            
    return stats.kstest(ser, 'norm', args=(ser.mean(), ser.std())).pvalue


#Функция проверки стат.теста Колмогорова-Смирнова
#p_value - вероятность получения критического или большего значения

def check_test(p_value, type_dist):
    df_check = pd.DataFrame.from_dict(
        {'p_value' : [f'{p_value:.3f}'], 'alpha' : [f'{const.alpha:.3f}']},
        orient='columns'   
    )
    
    st.dataframe(df_check.style.hide())
          
    if p_value > const.alpha:
        st.write('p_value > alpha')
        st.write(f"Нулевая гипотеза ${r'H_0'}$ не отвергается")
        st.write(f"Распределение ${type_dist}$ соответствует нормальному закону")
    else:
        st.write('p_value < alpha')
        st.write(f"Нулевая гипотеза ${r'H_0'}$ отвергается в пользу альтернативной")
        st.write(f"Распределение ${type_dist}$ не соответствует нормальному закону")


#Расчет коэффициентов базисов
#ser - Series
#n - размер выборки

def calculate_basis(ser):

    n = len(ser)
    #B-базис
    k_b = 1.282 + np.e ** (0.958 - 0.52 * np.log(n) + 3.19 / n)
    b_basis = round((ser.mean() - k_b * ser.std()), 2)
    

    #A-базис
    k_a = 2.326 + np.e ** (1.34 - 0.522 * np.log(n) + 3.87 / n)
    a_basis = round((ser.mean() - k_a * ser.std()), 2)
    
    return {'A_basis': a_basis, 'B_basis': b_basis}
