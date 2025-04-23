import numpy as np
import streamlit as st

st.set_page_config(page_title="Gradiente Conjugado y SOR - Solver", layout="centered")
st.title("🔧 Resolución de Sistemas Lineales")

st.markdown("""
Este programa resuelve un sistema de ecuaciones lineales \(Ax = b\) usando:
- **Método del Gradiente Conjugado (CG)**
- **Método de Sobre-Relajación Sucesiva (SOR)**

Puedes usar el sistema por defecto o ingresar tu propia matriz y vector.
""")

st.subheader("📌 Matriz A (3x3)")
def_matrix = [[4, 3, 0], [3, 4, -1], [0, -1, 4]]
A = []
for i in range(3):
    A.append([
        st.number_input(f"A[{i+1},{j+1}]", value=float(def_matrix[i][j]), key=f"a{i}{j}") for j in range(3)
    ])
A = np.array(A)

st.subheader("📌 Vector b (3x1)")
def_b = [24, 30, -24]
b = np.array([
    st.number_input(f"b[{i+1}]", value=float(def_b[i]), key=f"b{i}") for i in range(3)
])

x0 = np.zeros(3)
tol = st.number_input("🎯 Tolerancia", value=1e-4, format="%e")
max_iter = st.number_input("🔁 Iteraciones máximas", value=100, step=1)

method = st.selectbox("🧮 Método", ["Gradiente Conjugado", "SOR"])

if method == "Gradiente Conjugado":
    st.subheader("🚀 Gradiente Conjugado")
    if st.button("Resolver con CG"):
        r = b - A @ x0
        p = r.copy()
        x = x0.copy()
        output = []

        for k in range(max_iter):
            Ap = A @ p
            alpha = np.dot(r, r) / np.dot(p, Ap)
            x_new = x + alpha * p
            r_new = r - alpha * Ap
            output.append((k+1, x_new.copy(), np.linalg.norm(r_new)))

            if np.linalg.norm(r_new) < tol:
                break

            beta = np.dot(r_new, r_new) / np.dot(r, r)
            p = r_new + beta * p
            r = r_new
            x = x_new

        st.success("✅ Solución encontrada")
        st.write("### 🔢 Resultado final")
        st.write("x =", x_new)
        st.write(f"Con error final: {np.linalg.norm(r_new):.2e} en {k+1} iteraciones")

        st.write("### 📈 Iteraciones")
        for iter_num, x_val, err in output:
            st.write(f"Iteración {iter_num}: x = {x_val.round(5)} | Error = {err:.2e}")

elif method == "SOR":
    st.subheader("🚀 Sobre-Relajación Sucesiva (SOR)")
    omega = st.number_input("⚙️ Factor de relajación ω", min_value=0.1, max_value=2.0, value=1.25, step=0.05)

    if st.button("Resolver con SOR"):
        x = x0.copy()
        output = []

        for k in range(max_iter):
            x_old = x.copy()
            for i in range(3):
                sigma = sum(A[i][j] * x[j] for j in range(3) if j != i)
                x[i] = (1 - omega) * x[i] + (omega / A[i][i]) * (b[i] - sigma)
            err = np.linalg.norm(x - x_old)
            output.append((k+1, x.copy(), err))
            if err < tol:
                break

        st.success("✅ Solución encontrada")
        st.write("### 🔢 Resultado final")
        st.write("x =", x)
        st.write(f"Con error final: {err:.2e} en {k+1} iteraciones")

        st.write("### 📈 Iteraciones")
        for iter_num, x_val, err in output:
            st.write(f"Iteración {iter_num}: x = {x_val.round(5)} | Error = {err:.2e}")
