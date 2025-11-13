import streamlit as st
import numpy as np

def calcular_probabilidad(glucosa, bmi, edad, actividad, dieta, antecedentes):
    g = glucosa / 200
    b = bmi / 50
    e = edad / 100
    a = 1 - (actividad / 10)
    d = 1 - (dieta / 10)
    f = antecedentes  

    z = (
        3.0 * g +       
        2.5 * b +         
        1.5 * f +         
        1.2 * e +          
        0.8 * a +          
        0.6 * d +           
        2.0 * (b * f) +     
        1.5 * (g * f) +    
        1.0 * (g * b)       
    )

    prob = 1 / (1 + np.exp(-z + 5))

    return np.clip(prob, 0, 1)


st.set_page_config(page_title="Predicción de Riesgo de Diabetes Tipo 2", page_icon="🩺")

st.title("Predicción de Riesgo de Diabetes Tipo 2")
st.write("Aplicación desarrollada para estimar la *probabilidad de desarrollar diabetes tipo 2* "
         "basada en factores de riesgo clínicos y de estilo de vida.")

st.markdown("---")

edad = st.slider("Edad", 15, 80, 30)
glucosa = st.slider("Nivel de glucosa en sangre (mg/dL)", 70, 200, 100)
bmi = st.slider("Índice de Masa Corporal (IMC)", 15.0, 45.0, 25.0)
actividad = st.slider("Nivel de actividad física (1 = baja, 10 = alta)", 1, 10, 5)
dieta = st.slider("Calidad de la alimentación (1 = mala, 10 = saludable)", 1, 10, 6)
antecedentes = st.selectbox("¿Antecedentes familiares de diabetes tipo 2?", ["No", "Sí"])

antecedentes_valor = 1 if antecedentes == "Sí" else 0

if st.button("Calcular riesgo"):
    prob = calcular_probabilidad(glucosa, bmi, edad, actividad, dieta, antecedentes_valor)

    if prob < 0.3:
        riesgo = "🟢 Bajo"
    elif prob < 0.6:
        riesgo = "🟠 Moderado"
    else:
        riesgo = "🔴 Alto"

    st.markdown("---")
    st.subheader("Resultado del Análisis")
    st.write(f"*Probabilidad estimada:* {prob*100:.2f}%")
    st.write(f"*Nivel de riesgo:* {riesgo}")

    st.markdown("### Recomendaciones:")
    if riesgo == "🟢 Bajo":
        st.success("Tu riesgo actual es bajo, debes mantener una dieta equilibrada y actividad física regular.")
    elif riesgo == "🟠 Moderado":
        st.warning("Tu riesgo es moderado recomendamos aumentar la actividad física y mejorar los hábitos alimenticios.")
    else:
        st.error("Tu riesgo es alto, porfavor cude a un control médico y realiza pruebas adicionales para prevenir complicaciones.")

