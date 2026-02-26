import streamlit as st
import time
import datetime

st.set_page_config(page_title="Para Ti mi meu❤️", page_icon="💌", layout="centered")

if "sorpresa_cargada" not in st.session_state:
    st.session_state.sorpresa_cargada = False
if "mensaje_mostrado" not in st.session_state:
    st.session_state.mensaje_mostrado = False
if "carta_mostrada" not in st.session_state:
    st.session_state.carta_mostrada = False
if "musica_mostrada" not in st.session_state:
    st.session_state.musica_mostrada = False

st.title("Feliz dia mi amor!")
st.subheader("Hice esto para ti, mi blanquita hermosa ❤️")

st.image("https://media3.giphy.com/media/Yy7BiuPbeaGXu/giphy.gif", width=300)

st.markdown("""
### ✨ Hola mi niña ✨  
Te hice esto con mucho cariño, te amo más de lo que imaginas.  
Gracias por ser el amor de mi vida, por cada momento hermoso juntos.  
Eres mi persona favorita en el mundo y cada día me haces más feliz.  
**¡Gracias por estar a mi lado!** ❤️
""")

fecha_san_valentin = datetime.datetime(2025, 2, 14, 0, 0, 0)
ahora = datetime.datetime.now()
tiempo_restante = fecha_san_valentin - ahora

if tiempo_restante.total_seconds() > 0:
    dias, horas, minutos = tiempo_restante.days, tiempo_restante.seconds // 3600, (tiempo_restante.seconds % 3600) // 60
    st.info(f"⏳ Falta **{dias} días, {horas} horas y {minutos} minutos** para el 14 de febrero")

if st.button("Carga tus sorpresas meu 🎁"):
    st.session_state.sorpresa_cargada = True  
    st.image("https://media0.giphy.com/media/Mlx5hjAPRMlYQ/giphy.gif")
    
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.05)
        progress.progress(i + 1)

    st.success("Listo mi bonita, ahora puedes abrir las sorpresas❤️")

if st.session_state.sorpresa_cargada and not st.session_state.mensaje_mostrado:
    if st.button("Mira estas animaciones bien aca xd lol"):
        st.balloons()
        st.snow()
        st.session_state.mensaje_mostrado = True  

if st.session_state.mensaje_mostrado and not st.session_state.carta_mostrada:
    if st.button("Ahora abre tu cartita 💌"):
        st.session_state.carta_mostrada = True
        st.markdown("""
        ## 💌 Carta para mi Nandy
        Mi amor, cada día a tu lado es un regalo increíble.  
        Eres mi luna en todas mis noches obscuras, mi felicidad en los momentos tristes,  
        y mi razón para sonreír siempre.  
        
          **Eres lo mejor que me ha pasado en la vida.**   
        Gracias por ser quien eres, por amarme y dejarme amarte.  
        ¡Quiero estar contigo para siempre, mi blanquita hermosa! 
        
        **Te amo con toda mi alma.**  
        """)

if st.session_state.carta_mostrada:
    if st.button("Nuestra foto especial 💑"):
        st.image("assets/imagen.jpg", caption="💞 Nuestra foto juntos 💞")

if st.session_state.carta_mostrada:
    if st.button("OMG quien es??🎶"):
        st.session_state.musica_mostrada = True
        st.success("Por cierto, me encontre a un amigo y te dejo un mensaje 🥷")
        st.audio("assets/audio.wav", format="audio/wav")
        st.image("https://media4.giphy.com/media/G3FNI3FneNjiw/giphy.gif")