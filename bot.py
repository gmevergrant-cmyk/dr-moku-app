import streamlit as st

# 1. TUS DATOS DE PRUEBA (Los mismos que en la otra app)
datos_japones = [
    {"caracter": "し", "romaji": "shi", "pista": "Looks like a fishing SHI-hook.", "tipo": "Hiragana"},
    {"caracter": "く", "romaji": "ku", "pista": "Looks like the beak of a KU-ckoo bird.", "tipo": "Hiragana"},
    {"caracter": "シ", "romaji": "shi", "pista": "SHI-mmering stars in the night sky.", "tipo": "Katakana"},
    {"caracter": "ク", "romaji": "ku", "pista": "A KU-kri knife ready to slice.", "tipo": "Katakana"}
]

st.set_page_config(page_title="Tutor Dr. Moku", page_icon="🎓")
st.title("🎓 Tu Tutor de Japonés")
st.markdown("Pregúntame por cualquier letra (ej: 'sh' o 'ku') o pídeme el 'truco' de un carácter.")

if "historial" not in st.session_state:
    st.session_state.historial = [
        {"role": "assistant", "content": "¡Hola! Soy tu tutor. Puedo darte el truco mnemotécnico de las letras que estamos estudiando. ¿Por cuál quieres empezar?"}
    ]

for mensaje in st.session_state.historial:
    with st.chat_message(mensaje["role"]):
        st.write(mensaje["content"])

if prompt := st.chat_input("Escribe una letra o carácter..."):
    # Guardar mensaje del usuario
    st.chat_message("user").write(prompt)
    st.session_state.historial.append({"role": "user", "content": prompt})
    
    # --- LÓGICA DEL TUTOR INTELIGENTE ---
    respuesta = "Lo siento, todavía no tengo esa letra en mi base de datos. ¡Dile a Bob que me mande el Excel pronto! 😅"
    
    # Buscamos si lo que ha escrito el usuario está en nuestro diccionario
    for item in datos_japones:
        # Si el usuario escribe el sonido (shi) o el dibujo (し)
        if prompt.lower() in item["romaji"].lower() or prompt in item["caracter"]:
            respuesta = f"¡Ah, la letra **{item['caracter']}** ({item['romaji']})! Su truco mnemotécnico es: *'{item['pista']}'*. Es de tipo {item['tipo']}."
            break
    
    # Si el usuario pregunta por la lista completa
    if "lista" in prompt.lower() or "todas" in prompt.lower():
        respuesta = "Actualmente tengo estas 4 letras de prueba: " + ", ".join([d['caracter'] for d in datos_japones])

    # Guardar y mostrar respuesta del bot
    st.chat_message("assistant").write(respuesta)
    st.session_state.historial.append({"role": "assistant", "content": respuesta})