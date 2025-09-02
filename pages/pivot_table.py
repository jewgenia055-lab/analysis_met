                    #Итоговая таблица результатов расчета
import streamlit as st
import pandas as pd

st.subheader("Сводная таблица результатов расчета")
df_basis = st.session_state.df_basis
st.dataframe(df_basis)