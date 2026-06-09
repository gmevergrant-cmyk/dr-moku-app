import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Dr. Moku's Flashcards Clone", page_icon="🏮", layout="centered")

st.title("🏮 Dr. Moku's Mnemonics App")
st.markdown("Aprende el silabario japonés en tiempo récord usando trucos visuales.")

# 2. Base de datos ficticia de mnemotecnias (Hiragana y Katakana)
# Nota: Puedes ampliar esta lista con todo el alfabeto.
datos_japones = {
    "Hiragana": [
        {"caracter": "し", "romaji": "shi", "pista": "Looks like a fishing SHI-hook.", "tipo": "Hiragana"},
        {"caracter": "く", "romaji": "ku", "pista": "Looks like the beak of a KU-ckoo bird.", "tipo": "Hiragana"},
        {"caracter": "ま", "romaji": "ma", "pista": "Looks like a MA-st of a ship with sails.", "tipo": "Hiragana"},
        {"caracter": "わ", "romaji": "wa", "pista": "A WA-terful wave splashing a wall.", "tipo": "Hiragana"}
    ],
    "Katakana": [
        {"caracter": "シ", "romaji": "shi", "pista": "SHI-mmering stars in the night sky.", "tipo": "Katakana"},
        {"caracter": "ク", "romaji": "ku", "pista": "A KU-kri knife ready to slice.", "tipo": "Katakana"}
    ]
}
# Busca esta sección en tu código y añade más letras como estas:
datos_japones = {
    "Hiragana": [
        {"caracter": "し", "romaji": "shi", "pista": "Looks like a fishing SHI-hook.", "tipo": "Hiragana"},
        {"caracter": "く", "romaji": "ku", "pista": "Looks like the beak of a KU-ckoo bird.", "tipo": "Hiragana"},
        {"caracter": "ま", "romaji": "ma", "pista": "Looks like a MA-st of a ship with sails.", "tipo": "Hiragana"},
        {"caracter": "わ", "romaji": "wa", "pista": "A WA-terful wave splashing a wall.", "tipo": "Hiragana"}
    ],
    "Katakana": [
        {"caracter": "シ", "romaji": "shi", "pista": "SHI-mmering stars in the night sky.", "tipo": "Katakana"},
        {"caracter": "ク", "romaji": "ku", "pista": "A KU-kri knife ready to slice.", "tipo": "Katakana"},
        {"caracter": "マ", "romaji": "ma", "pista": "Looks like a MA-ndolin angle.", "tipo": "Katakana"},
        {"caracter": "ワ", "romaji": "wa", "pista": "Looks like a WA-ter tap hanging over.", "tipo": "Katakana"},
        {"caracter": "ハ", "romaji": "ha", "pista": "Looks like a HA-tt (hat) or a roof.", "tipo": "Katakana"}
    ]
}
# 3. Barra lateral para filtros
with st.sidebar:
    st.header("⚙️ Configuración")
    silabario = st.selectbox("Elige el silabario:", ["Hiragana", "Katakana"])
    
    st.markdown("---")
    st.markdown("💡 **Instrucciones:** Mira el carácter, piensa en su sonido, haz clic en *'Ver Truco Mnemotécnico'* y comprueba si has acertado.")

# Obtener la lista de tarjetas seleccionada
lista_actual = datos_japones[silabario]

# 4. Inicializar variables de estado (Session State)
if "indice_tarjeta" not in st.session_state or st.session_state.get("silabario_anterior") != silabario:
    st.session_state.indice_tarjeta = 0
    st.session_state.mostrar_reverso = False
    st.session_state.silabario_anterior = silabario
    if "aciertos" not in st.session_state:
        st.session_state.aciertos = 0

# Asegurar que el índice no se salga de los límites si cambia la lista
if st.session_state.indice_tarjeta >= len(lista_actual):
    st.session_state.indice_tarjeta = 0

tarjeta_actual = lista_actual[st.session_state.indice_tarjeta]

# 5. Marcador de progreso en pantalla
col_progreso, col_puntos = st.columns(2)
with col_progreso:
    st.write(f"**Tarjeta:** {st.session_state.indice_tarjeta + 1} de {len(lista_actual)}")
with col_puntos:
    st.write(f"**Letras dominadas:** ⭐ {st.session_state.aciertos}")

st.markdown("---")

# 6. Renderizado de la Tarjeta (Diseño Visual Emulado)
# Usamos un contenedor con borde para simular la tarjeta física
with st.container(border=True):
    st.markdown("<br>", unsafe_allow_html=True)
    # Mostramos el carácter japonés gigante en el centro
    st.markdown(f"<h1 style='text-align: center; font-size: 100px; color: #FF4B4B;'>{tarjeta_actual['caracter']}</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Lógica del Reverso de la Tarjeta
    if st.session_state.mostrar_reverso:
        st.markdown(f"<h3 style='text-align: center;'>Pronunciación: <span style='color: #1F77B4;'>{tarjeta_actual['romaji'].upper()}</span></h3>", unsafe_allow_html=True)
        st.info(f"💡 **Mnemonic Pista:** {tarjeta_actual['pista']}")
    else:
        st.markdown("<h3 style='text-align: center; color: gray;'>¿Te acuerdas de cómo suena?</h3>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 7. Botones de Interacción y Control de Flujo
col_rev, col_sig, col_bien = st.columns(3)

with col_rev:
    if st.button("🔄 Voltear Tarjeta", use_container_width=True):
        st.session_state.mostrar_reverso = not st.session_state.mostrar_reverso
        st.rerun()

with col_bien:
    if st.button("✅ ¡Me la sé!", use_container_width=True, type="primary"):
        st.session_state.aciertos += 1
        # Avanzar automáticamente a la siguiente
        st.session_state.indice_tarjeta = (st.session_state.indice_tarjeta + 1) % len(lista_actual)
        st.session_state.mostrar_reverso = False
        st.rerun()

with col_sig:
    if st.button("➡️ Siguiente Letra", use_container_width=True):
        st.session_state.indice_tarjeta = (st.session_state.indice_tarjeta + 1) % len(lista_actual)
        st.session_state.mostrar_reverso = False
        st.rerun()