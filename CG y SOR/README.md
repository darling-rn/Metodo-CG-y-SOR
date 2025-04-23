# 🔧 Solver de Sistemas Lineales con Gradiente Conjugado y SOR

Este proyecto es una aplicación web interactiva hecha con **Python + Streamlit** que resuelve sistemas de ecuaciones lineales de la forma:

\[
Ax = b
\]

Usa dos métodos iterativos:

- **Gradiente Conjugado (CG)** – rápido y eficiente para matrices simétricas definidas positivas.
- **Sobre-Relajación Sucesiva (SOR)** – ideal para sistemas generados por métodos de diferencias finitas o EDPs.

## 📌 Ejemplo por defecto

\[
A =
\begin{bmatrix}
4 & 3 & 0 \\
3 & 4 & -1 \\
0 & -1 & 4 \\
\end{bmatrix},
\quad
b =
\begin{bmatrix}
24 \\
30 \\
-24 \\
\end{bmatrix}
\]

La solución esperada es:

\[
x = \begin{bmatrix} 3 \\ 4 \\ -5 \end{bmatrix}
\]

## 🚀 ¿Cómo usar?

### 1. Clona el repositorio

```bash
git clone https://github.com/tu_usuario/cg-sor-solver.git
cd cg-sor-solver
```

### 2. Instala dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecuta la app

```bash
streamlit run app.py
```

## 🧠 Acerca de los métodos

### Gradiente Conjugado (CG)
- Ideal para matrices simétricas y definidas positivas.
- Convergencia rápida sin necesidad de almacenar matrices completas.

### Sobre-Relajación Sucesiva (SOR)
- Extiende el método de Gauss-Seidel con un factor ω.
- Puede acelerar la convergencia para sistemas grandes si ω está bien elegido.

## 🛠 Tecnologías utilizadas

- Python 3.8+
- NumPy
- Streamlit

## 📚 Fuentes

- Burden & Faires – *Análisis Numérico*
- Chapra & Canale – *Métodos Numéricos para Ingenieros*
- https://numpy.org/doc/
- https://docs.streamlit.io/

## 💡 Autor

Desarrollado por Carlos como parte de un proyecto académico de comparación entre métodos numéricos iterativos.
