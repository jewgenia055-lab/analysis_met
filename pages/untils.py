import streamlit as st
import pandas as pd

st.subheader("Обозначения и единицы измерения величин")

data = {
    'Параметр': [
        'Линейные размеры',
        'Площадь поперечного сечения', 
        'Относительное удлинение при растяжении после разрушения',
        'Относительное сужение при разрушении',
        'Максимальное усилие разрыва',
        'Временное сопротивление (предел прочности)'
    ],
    'Обозначение': [
        'l_0, l_k, d_0, d_k',
        'F_0, F_k',
        'delta',
        'psi',
        'P_max',
        'sigma_b'
    ],
    'Единицы измерения': [
        'мм',
        'мм²',
        '%',
        '%',
        'Н',
        'МПа'
    ]
}

df = pd.DataFrame(data)

st.markdown("### В документе применяются условные обозначения")
st.dataframe(
    df,
    hide_index=True,
    use_container_width=True,
    column_config={
        "Параметр": st.column_config.TextColumn(width="large"),
        "Обозначение": st.column_config.TextColumn(width="medium"),
        "Единицы измерения": st.column_config.TextColumn(width="small")
    }
)