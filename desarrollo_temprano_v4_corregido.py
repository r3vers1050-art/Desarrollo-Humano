import streamlit as st
import pandas as pd
import numpy as np

# Configuración de página de Streamlit
st.set_page_config(
    page_title="Primeros Pasos - Guía Interactiva del Desarrollo Infantil",
    page_icon="👶",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializar estado de sesión para navegación
if "selected_page" not in st.session_state:
    st.session_state.selected_page = "🏠 Portada de Entrada"

# Estilo CSS personalizado para mejorar el aspecto visual (diseño amigable y profesional)
st.markdown("""
<style>
    .main-title {
        color: #FF6F61;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-weight: 700;
        text-align: center;
        margin-bottom: 20px;
    }
    .section-header {
        color: #4A90E2;
        border-bottom: 2px solid #4A90E2;
        padding-bottom: 10px;
        margin-top: 30px;
        margin-bottom: 15px;
        font-weight: 600;
    }
    .concept-box {
        background-color: #F7F9FC;
        border-left: 5px solid #FFD166;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 15px;
    }
    .example-box {
        background-color: #E8F5E9;
        border-left: 5px solid #4CAF50;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 15px;
    }
    .challenge-box {
        background-color: #FFF3E0;
        border: 1px dashed #FF9800;
        padding: 20px;
        border-radius: 8px;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .citation {
        color: #888888;
        font-size: 0.85em;
        vertical-align: super;
        font-weight: bold;
    }
    .card-title {
        color: #FF6F61;
        font-size: 1.3em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .card-text {
        color: #555555;
        font-size: 0.95em;
        margin-bottom: 15px;
        height: 80px;
    }
</style>
""", unsafe_allow_html=True)

# Callback para actualizar navegación
def navegar_a(pagina):
    st.session_state.selected_page = pagina

# --- MENÚ LATERAL -- Nicely integrated with st.session_state ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/baby.png", width=90)
    st.markdown("<h2 style='text-align: center; color: #FF6F61;'>Menú Principal</h2>", unsafe_allow_html=True)
    
    # Crear la botonera de radio sincronizada con el estado de sesión
    opciones = [
        "🏠 Portada de Entrada",
        "🏃 Desarrollo Físico",
        "🧠 Desarrollo Cognitivo",
        "❤️ Desarrollo Socioafectivo",
        "🗣️ Desarrollo Lingüístico",
        "📚 Referencias Bibliográficas"
    ]
    
    index_seleccionado = opciones.index(st.session_state.selected_page)
    
    opcion = st.radio(
        "Selecciona un apartado del desarrollo:",
        opciones,
        index=index_seleccionado,
        key="sidebar_radio"
    )
    
    # Sincronizar estado si el usuario usa el radio del menú lateral
    if opcion != st.session_state.selected_page:
        st.session_state.selected_page = opcion
        st.rerun()
    
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; font-size: 0.8em; color: #777;'>"
        "Guía interactiva basada estrictamente en los capítulos 3, 4, 5 y 6 de Papalia y cols."
        "</p>",
        unsafe_allow_html=True
    )

# --- 1. PORTADA O PÁGINA DE ENTRADA (LANDING PAGE) ---
if st.session_state.selected_page == "🏠 Portada de Entrada":
    st.markdown("<h1 class='main-title'>👶 Primeros Pasos: Guía del Desarrollo Temprano</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #555;'>Explora de forma científica, interactiva y práctica los primeros tres años de vida de tu bebé</h4>", unsafe_allow_html=True)
    
    st.markdown("""
    Bienvenido a **Primeros Pasos**, una aplicación interactiva diseñada para padres, educadores y cuidadores. 
    Los primeros tres años de vida representan una ventana de oportunidad crítica donde el desarrollo físico, cerebral y social del niño 
    sienta las bases para todo su potencial futuro <span class='citation'>[105]</span>. 
    Esta plataforma te ofrece explicaciones sencillas fundamentadas en la ciencia, simuladores clínicos, trivias y herramientas de autoevaluación.
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 class='section-header'>🌟 Selecciona una Dimensión para Explorar</h3>", unsafe_allow_html=True)
    st.markdown("Haz clic en cualquiera de las 4 divisiones del desarrollo para conocer sus principales rasgos, teorías explicativas y retos:")
    
    # Grid de 4 divisiones principales
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background-color: #F7F9FC; border-radius: 8px; padding: 20px; border-top: 4px solid #FF6F61; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);'>
            <div class='card-title'>🏃 Desarrollo Físico</div>
            <div class='card-text'>Comprende los procesos de nacimiento, las características clínicas del recién nacido (neonato), los principios del crecimiento cefalocaudal y proximodistal, y los patrones del desarrollo motriz.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Explorar Desarrollo Físico", key="btn_fisico"):
            st.session_state.selected_page = "🏃 Desarrollo Físico"
            st.rerun()
            
    with col2:
        st.markdown("""
        <div style='background-color: #F7F9FC; border-radius: 8px; padding: 20px; border-top: 4px solid #4A90E2; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);'>
            <div class='card-title'>🧠 Desarrollo Cognitivo</div>
            <div class='card-text'>Explora el desarrollo del pensamiento a través de 6 enfoques científicos: conductista, psicométrico (escala HOME), piagetiano (sensoriomotriz), procesamiento de información, neurociencias y contextual social.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Explorar Desarrollo Cognitivo", key="btn_cognitivo"):
            st.session_state.selected_page = "🧠 Desarrollo Cognitivo"
            st.rerun()
            
    with col3:
        st.markdown("""
        <div style='background-color: #F7F9FC; border-radius: 8px; padding: 20px; border-top: 4px solid #4CAF50; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);'>
            <div class='card-title'>❤️ Desarrollo Socioafectivo</div>
            <div class='card-text'>Estudia los fundamentos emocionales, el surgimiento del temperamento, el autoconcepto, los terribles dos años (autonomía), el desarrollo del apego con cuidadores, la interacción con pares y el maltrato.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Explorar Desarrollo Socioafectivo", key="btn_socio"):
            st.session_state.selected_page = "❤️ Desarrollo Socioafectivo"
            st.rerun()
            
    with col4:
        st.markdown("""
        <div style='background-color: #F7F9FC; border-radius: 8px; padding: 20px; border-top: 4px solid #FFD166; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);'>
            <div class='card-title'>🗣️ Desarrollo Lingüístico</div>
            <div class='card-text'>Sigue el viaje comunicativo del bebé desde el llanto, el arrullo y el balbuceo prelingüístico, hasta las primeras palabras, holofrases, el habla telegráfica y las mejores pautas para estimular el habla.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Explorar Desarrollo Lingüístico", key="btn_ling"):
            st.session_state.selected_page = "🗣️ Desarrollo Lingüístico"
            st.rerun()

    st.markdown("<h3 class='section-header'>📈 Recomendador Dinámico por Edad</h3>", unsafe_allow_html=True)
    st.markdown("Selecciona la edad de tu bebé en meses para ver un resumen instantáneo de los hitos característicos descritos por la ciencia:")
    
    edad = st.slider("Edad de tu bebé (meses):", 0, 36, 6)
    
    if edad <= 3:
        f_info = "Sostiene la cabeza erguida brevemente al estar boca abajo [132]. Su campo de visión es de aprox. 30 cm [127]."
        c_info = "Aprende por condicionamiento operante y habituación [175, 181]. Reacciones circulares primarias (su cuerpo) [203]."
        s_info = "Aparece la sonrisa social (2 meses) [306]. Está abierto a la estimulación y curiosidad de su entorno [297]."
        r_info = "Practica el 'cuidado de canguro' para regular la temperatura y el ritmo cardiaco [74]. Respóndele rápido a su llanto para sembrar confianza básica [331]."
    elif edad <= 8:
        f_info = "Logra rodar sobre sí mismo [134]. Sostiene objetos de tamaño moderado como sonajas [133]. Se sienta con apoyo [134]."
        c_info = "Aparecen reacciones circulares secundarias (interacción con objetos) [204, 209]. Comienza a asociar la vista y el oído [235]."
        s_info = "Aparecen risas y expresiones diferenciadas de enojo, tristeza, temor o sorpresa [298, 308]. Participa en juegos sociales [298]."
        r_info = "Proporciónale sonajas y juguetes texturizados seguros [204]. Háblale mirándolo a los ojos de forma afectuosa [301]."
    elif edad <= 12:
        f_info = "Logra sentarse solo [134], gatea o se arrastra de forma autónoma [137]. Se para sosteniéndose de muebles [138]."
        c_info = "Coordinación de esquemas dirigidos a metas [205]. Desarrolla atención conjunta [236]. Aparece la noción de permanencia del objeto [225]."
        s_info = "Siente timidez ante extraños y ansiedad ante la separación [298, 342]. Usa referenciación social en situaciones dudosas [137, 348]."
        r_info = "Juega a esconder objetos y que los busque [225]. Mantén tu hogar a prueba de bebés para que explore el piso con total seguridad y libertad [198]."
    elif edad <= 18:
        f_info = "Aprende a caminar solo [138]. Logra subir escaleras con apoyo (paso a paso) [139]. Usa prensión de pinza [133]."
        c_info = "Reacciones circulares terciarias (experimentación activa, ensayo y error) [206, 212]. Comienza a entender símbolos [213, 224]."
        s_info = "Muestra conducta altruista espontánea y empatía [312, 313]. Explora teniendo a sus cuidadores como base segura [299, 339]."
        r_info = "Ofrécele juguetes de encajar figuras geométricas [206]. Léele en voz alta de forma dialógica, haciéndole preguntas sobre las ilustraciones [280]."
    elif edad <= 24:
        f_info = "Corre, salta y sube escaleras con mayor soltura [139]. Construye torres de dos o tres bloques de juguete [133, 135]."
        c_info = "Representación mental y combinaciones mentales para resolver problemas (evita el ensayo y error previo) [213]. Imitación diferida [220]."
        s_info = "Surge el autoconcepto y la autoconciencia (se reconoce al espejo) [351, 355]. Época del negativismo ('¡NO!') para autoafirmarse [356]."
        r_info = "Permítele tomar decisiones sencillas para fomentar su autonomía [356]. Usa recordatorios gentiles y límites claros en lugar de castigos rígidos [356, 368]."
    else:
        f_info = "Salta en su lugar, se equilibra en un pie [135, 139]. Puede copiar trazos de un círculo con lápiz [133, 135]."
        c_info = "Combina palabras en frases estructuradas [268]. Su memoria explícita y de trabajo se vuelven mucho más duraderas y eficientes [257, 260]."
        s_info = "Aparecen emociones autoevaluativas (orgullo, culpa, vergüenza) tras internalizar las normas de conducta social [307, 309, 362]."
        r_info = "Fomenta la cooperación receptiva involucrándolo de manera divertida en tareas sencillas del hogar [367]. Fomenta el juego e imitación mutua con otros niños [377]."

    col_h1, col_h2 = st.columns(2)
    with col_h1:
        st.markdown(f"""
        <div class='concept-box'>
            <h4 style='color: #4A90E2; margin-top: 0;'>📝 Hitos del Desarrollo para la etapa seleccionada ({edad} meses)</h4>
            <ul>
                <li><strong>Físico y Motriz:</strong> {f_info}</li>
                <li><strong>Cognoscitivo:</strong> {c_info}</li>
                <li><strong>Socioafectivo:</strong> {s_info}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col_h2:
        st.markdown(f"""
        <div class='example-box'>
            <h4 style='color: #4CAF50; margin-top: 0;'>💡 Ideas de Crianza y Estimulación Basadas en Evidencia</h4>
            <p>{r_info}</p>
        </div>
        """, unsafe_allow_html=True)

# --- 2. DESARROLLO FÍSICO ---
elif st.session_state.selected_page == "🏃 Desarrollo Físico":
    st.markdown("<h1 class='main-title'>🏃 Dimensión 1: Desarrollo Físico</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    El crecimiento y el desarrollo motor temprano avanzan siguiendo ritmos biológicos asombrosos y predecibles, desde el nacimiento, 
    ajustándose a principios direccionales y viéndose moldeados por la maduración del sistema nervioso <span class='citation'>[51, 85, 94]</span>.
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📌 Nacimiento y Neonato", "📏 Leyes del Crecimiento", "🧠 Desarrollo Motriz"])
    
    with tab1:
        st.markdown("""
        ### El Nacimiento y las Características del Recién Nacido
        
        #### Características Físicas del Neonato:
        *   **Talla y Peso Promedio**: Al nacer, el recién nacido (neonato) promedio en Estados Unidos mide unos **50 centímetros** y pesa **3.5 kilogramos** <span class='citation'>[52]</span>. Al nacer, el 95% de los bebés nacidos a término pesan entre 2.5 y 4.5 kg, y miden entre 45 y 55 cm <span class='citation'>[52]</span>.
        *   **Pérdida de Peso**: Durante los primeros días, los neonatos bajan hasta el 10% del peso corporal, principalmente por pérdida de líquidos, la cual recuperan entre los 10 y 14 días de vida <span class='citation'>[52]</span>.
        *   **Cabeza Grande**: Su cabeza es desproporcionadamente grande, equivaliendo a **una cuarta parte (1/4)** de toda su estatura <span class='citation'>[53]</span>.
        *   **Fontanelas (Molleras)**: Placas óseas del cráneo que no se han fusionado, unidas por membranas flexibles que facilitan el paso del bebé por el canal de parto <span class='citation'>[54]</span>. Se cierran en su totalidad a los 18 meses <span class='citation'>[54]</span>.
        *   **Piel y Recubrimientos**: Muchos neonatos nacen cubiertos por un vello fino temporal llamado **lanugo** <span class='citation'>[55]</span> y una grasa protectora contra infecciones llamada **vérnix caseosa** <span class='citation'>[55]</span>.
        *   **Ictericia Neonatal**: Coloración amarillenta de la piel y los ojos debido a la inmadurez de su hígado <span class='citation'>[59]</span>. Afecta a cerca de la mitad de los bebés a término <span class='citation'>[59]</span>, aparece a los 3-4 días y generalmente se resuelve de forma natural <span class='citation'>[59]</span>.
        *   **Meconio**: Sustancia pegajosa de desecho, de color negroverdoso, acumulada en el tracto intestinal fetal y que es expulsada de forma instintiva en los primeros días <span class='citation'>[58]</span>.
        """, unsafe_allow_html=True)
        
        # INTERACTIVO: SIMULADOR DE EVALUACIÓN CLÍNICA APGAR
        st.markdown("<div class='challenge-box'>", unsafe_allow_html=True)
        st.markdown("### 🧮 Simulador Clínico: Cálculo de la Escala de Apgar")
        st.markdown("""
        La Dra. Virginia Apgar ideó en 1953 un método de evaluación rápida para evaluar la adaptación del neonato al nacer (se toma a **1 minuto y a los 5 minutos** tras el parto) <span class='citation'>[61]</span>. 
        Evalúa 5 dimensiones con puntajes de 0 a 2. ¡Selecciona los síntomas observados y calcula el estado clínico del bebé!
        """, unsafe_allow_html=True)
        
        c_col1, c_col2 = st.columns(2)
        with c_col1:
            apariencia = st.selectbox("Apariencia (Color de piel):", [
                "0 - Azulado, pálido",
                "1 - Cuerpo rosado, extremidades azuladas (Acrocianosis)",
                "2 - Completamente rosado"
            ], index=1)
            
            pulso = st.selectbox("Pulso (Frecuencia cardiaca):", [
                "0 - Ausente",
                "1 - Lenta (Menos de 100 latidos por minuto)",
                "2 - Rápida (Más de 100 latidos por minuto)"
            ], index=2)
            
            gestos = st.selectbox("Gestos (Irritabilidad refleja):", [
                "0 - Sin respuesta a estímulos",
                "1 - Muecas ligeras",
                "2 - Tose, estornuda o llora con vigor"
            ], index=2)
            
        with c_col2:
            actividad = st.selectbox("Actividad (Tono muscular):", [
                "0 - Flácido, sin fuerza",
                "1 - Flexiones débiles en las extremidades",
                "2 - Firme, activo y con movimiento voluntario"
            ], index=1)
            
            respiracion = st.selectbox("Respiración (Esfuerzo respiratorio):", [
                "0 - Ausente",
                "1 - Irregular, lenta o quejumbrosa",
                "2 - Buena, acompañada de llanto fuerte"
            ], index=2)
            
        ap_val = int(apariencia[0])
        pu_val = int(pulso[0])
        ge_val = int(gestos[0])
        ac_val = int(actividad[0])
        re_val = int(respiracion[0])
        score = ap_val + pu_val + ge_val + ac_val + re_val
        
        st.markdown(f"<h3 style='text-align: center; color: #FF6F61;'>Puntuación de Apgar: {score} / 10</h3>", unsafe_allow_html=True)
        
        if score >= 7:
            st.success(f"🎉 **Resultado de {score}: Adaptación Óptima.** El neonato se encuentra en un estado de salud de excelente a bueno, requiriendo únicamente cuidados de rutina [61].")
        elif score >= 5:
            st.warning(f"⚠️ **Resultado de {score}: Dificultad Moderada.** El recién nacido requiere asistencia respiratoria, estimulación o ventilación asistida para estabilizarse [61].")
        else:
            st.error(f"🚨 **Resultado de {score}: Emergencia Médica.** El bebé requiere maniobras de reanimación y estabilización médica inmediata para salvar su vida [61].")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with tab2:
        st.markdown("""
        ### Patrones y Leyes Direccionales del Crecimiento
        
        El crecimiento del cuerpo y la maduración de las habilidades motrices proceden de acuerdo con dos principios direccionales biológicos universales <span class='citation'>[14, 85, 132]</span>:
        
        1.  **Principio Cefalocaudal (De arriba a abajo)**:
            *   **Definición**: El crecimiento y desarrollo motor avanzan desde la cabeza hacia las partes inferiores del cuerpo <span class='citation'>[85]</span>.
            *   **Explicación científica**: Debido a que el encéfalo crece a una velocidad inmensa antes del nacimiento, la cabeza del recién nacido es sumamente grande en comparación al tronco y las piernas <span class='citation'>[85]</span>. 
            *   **Secuencia motriz**: El bebé aprende primero a sostener erguida la cabeza (3-4 meses) antes de poder sentarse sin ayuda (6 meses), y mucho antes de poder pararse y caminar solo [132, 134].
            
        2.  **Principio Proximodistal (De adentro hacia afuera)**:
            *   **Definición**: El crecimiento y control motriz se desarrollan desde el eje central del cuerpo hacia el exterior (extremidades) <span class='citation'>[86]</span>.
            *   **Explicación científica**: Durante la gestación, el tronco y la cabeza se forman antes que los brazos y las piernas, y estos antes que los dedos de las manos y los pies <span class='citation'>[25, 86]</span>.
            *   **Secuencia motriz**: El infante primero controla la dirección de todo su brazo estirándolo de forma imprecisa para acercarse a un juguete (4 meses) antes de poder cerrarlo con un agarre palmar amplio, y mucho antes de lograr la precisión de pinza (pulgar e índice) para asimilar objetos diminutos (10-12 meses) [133, 140].
        """, unsafe_allow_html=True)
        
    with tab3:
        st.markdown("""
        ### Teorías y Patrones del Desarrollo Motriz
        
        #### Hitos del Desarrollo Motriz:
        Las habilidades motoras se desarrollan en una secuencia predecible marcada por hitos sistemáticos en los que el dominio de una habilidad prepara al niño para abordar la siguiente <span class='citation'>[129]</span>. Las habilidades se dividen en **motoras gruesas** (músculos grandes como pararse o caminar) y **motoras finas** (músculos pequeños y coordinación ojo-mano como asir objetos) <span class='citation'>[131]</span>.
        
        #### La Teoría de los Sistemas Dinámicos de Esther Thelen (TSD):
        Thelen refutó la visión reduccionista de que el desarrollo motriz es puramente automático y programado de forma genética <span class='citation'>[148]</span>. Ella demostró que:
        *   El infante, su cuerpo y su medio ambiente físico forman un **sistema dinámico interconectado** <span class='citation'>[149]</span>.
        *   Los movimientos motores se autoorganizan en función de la **fuerza muscular, el peso corporal, el nivel de energía del bebé, su motivación psicológica y la superficie física** sobre la cual se desplaza <span class='citation'>[149]</span>.
        *   *Ejemplo científico*: El **reflejo de marcha** innato de los recién nacidos desaparece al cuarto mes de vida debido a que sus piernas ganan grasa y peso más rápido que la fuerza de sus músculos, lo que les impide levantar las piernas contra la gravedad <span class='citation'>[150]</span>. Thelen probó esto sumergiendo a bebés de 5 meses en agua tibia: al reducir el efecto de la gravedad, ¡el reflejo de marcha se reanudaba instantáneamente! <span class='citation'>[150]</span>.
        
        #### La Teoría Ecológica de la Percepción (Gibson & Gibson):
        *   Propone que el desarrollo de la locomoción depende de que aumente la sensibilidad del niño para ajustar sus acciones físicas a los retos y características de su entorno <span class='citation'>[143]</span>.
        *   **Aprender a aprender**: Adolph demostró que los bebés no memorizan cómo moverse, sino que en cada fase (gatear y luego caminar) aprenden a evaluar activamente los límites de su cuerpo frente al espacio físico (rampas, escalones, pendientes) <span class='citation'>[143, 144]</span>.
        *   **El Abismo Visual**: Walk y Gibson diseñaron una mesa de vidrio transparente que simulaba un vacío pronunciado <span class='citation'>[142, 146]</span>. Comprobaron que los bebés de 6 meses que ya contaban con semanas de experiencia gateando se rehusaban de forma tajante a avanzar sobre el área de abismo visual a pesar de los llamados afectuosos de sus madres, demostrando una desarrollada percepción de profundidad y autocuidado físico <span class='citation'>[137, 142]</span>.
        """, unsafe_allow_html=True)
        
        # TRIVIA REFLEJOS INNATOS
        st.markdown("<div class='challenge-box'>", unsafe_allow_html=True)
        st.markdown("### 🧩 Trivia Interactiva de Reflejos Neonatales")
        st.markdown("Los reflejos innatos e involuntarios indican el estado de salud neurológica del bebé [112]. ¡A ver si logras identificar el reflejo correcto!")
        
        pregunta_r = st.radio(
            "Al caerse, desequilibrarse o escuchar un ruido sumamente fuerte, el recién nacido extiende los brazos, abre los dedos, arquea la espalda y echa la cabeza hacia atrás de forma refleja. ¿Qué reflejo es?",
            ["Reflejo Darwiniano (Prensión)", "Reflejo de Moro", "Reflejo de Búsqueda", "Reflejo de Babinski"]
        )
        
        if st.button("Evaluar Reflejo"):
            if pregunta_r == "Reflejo de Moro":
                st.success("🎉 **¡Excelente! Es el Reflejo de Moro.** Se trata de una conducta involuntaria primitiva que suele desaparecer alrededor del tercer mes de vida cuando se desarrolla el control cortical voluntario del cerebro [114, 118].")
            else:
                st.error("Incorrecto. Inténtalo de nuevo. Pista: Es una reacción de sobresalto ante el desequilibrio o ruidos.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- 3. DESARROLLO COGNITIVO ---
elif st.session_state.selected_page == "🧠 Desarrollo Cognitivo":
    st.markdown("<h1 class='main-title'>🧠 Dimensión 2: Desarrollo Cognitivo</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    La forma en que los infantes aprenden a pensar, resolver problemas, recordar y comunicarse se estudia a través de **seis enfoques científicos** <span class='citation'>[169, 172]</span>. 
    Selecciona un enfoque en el panel inferior para explorar sus hallazgos, experimentos clásicos y pruebas interactivas:
    """, unsafe_allow_html=True)
    
    enf_elegido = st.selectbox("Elige un Enfoque Cognitivo:", [
        "Enfoque Conductista (Mecanismos básicos)",
        "Enfoque Psicométrico (Medición y HOME)",
        "Enfoque Piagetiano (Etapa Sensoriomotriz)",
        "Enfoque del Procesamiento de la Información (Eficiencia mental)",
        "Enfoque de las Neurociencias (Estructuras de Memoria)",
        "Enfoque Contextual Social (Vygotsky y Cuidadores)"
    ])
    
    if "Conductista" in enf_elegido:
        st.markdown("""
        ### Enfoque Conductista: Condicionamiento y Aprendizaje
        Se interesa por los mecanismos más puros del aprendizaje: cómo la experiencia directa moldea y modifica el comportamiento <span class='citation'>[173]</span>.
        
        *   **Condicionamiento Clásico**: El bebé asocia un estímulo que antes era neutro con otro estímulo que desencadena una respuesta biológica reflejada (ej. parpadear al ver la cámara antes de que brille el flash) <span class='citation'>[175, 182]</span>.
        *   **Condicionamiento Operante**: Se basa en las consecuencias de las acciones. Una conducta que es reforzada positivamente (con afecto, risas, sonrisas) tiende a repetirse (ej. balbucear para recibir atención cariñosa) <span class='citation'>[178]</span>.
        
        #### La Memoria en los Bebés: El Experimento de Rovee-Collier:
        *   Carolyn Rovee-Collier ató un listón del tobillo de bebés de 2 a 6 meses a un móvil colgante colocado en su cuna <span class='citation'>[181]</span>. Los bebés aprendieron por condicionamiento operante que al patear activaban el agradable movimiento del móvil <span class='citation'>[181]</span>.
        *   Al retirar el móvil y regresar días después, los bebés de 2 meses recordaban la conducta y pateaban con vigor durante **dos días** <span class='citation'>[181]</span>. A los 18 meses, ¡lograban retener el recuerdo durante **13 semanas**! <span class='citation'>[181]</span>. Demostró que los bebés recuerdan igual que los adultos, pero por periodos más cortos y muy dependientes de las claves del contexto original <span class='citation'>[183, 184]</span>.
        """, unsafe_allow_html=True)
        
    elif "Psicométrico" in enf_elegido:
        st.markdown("""
        ### Enfoque Psicométrico: Bayley y la Estimulación Familiar
        Intenta medir de forma cuantitativa los factores de la inteligencia (razonamiento, comprensión) para pronosticar el desempeño cognoscitivo futuro <span class='citation'>[188]</span>.
        
        *   **Escalas de Bayley (Bayley-III)**: Evaluación de un mes a tres años y medio que califica el rendimiento del niño en cinco ámbitos: cognoscitivo, lingüístico, motriz, socioemocional y conducta adaptativa <span class='citation'>[189]</span>. No predice el CI escolar (excepto por la habituación), pero detecta alteraciones neurológicas tempranas <span class='citation'>[189, 192]</span>.
        
        #### La Escala HOME y las 7 Condiciones de Competencia en el Hogar:
        La escala HOME (Home Observation for Measurement of the Environment) evalúa mediante entrevistas y observaciones directas la estimulación del hogar <span class='citation'>[190]</span>. Bradley e investigadores identificaron **7 condiciones clave en el hogar** que estimulan de forma contundente la inteligencia temprana <span class='citation'>[195]</span>:
        1. Alentar la exploración activa del entorno seguro [195].
        2. Enseñar de forma lúdica habilidades cognoscitivas y sociales básicas [195].
        3. Celebrar y elogiar los adelantos del desarrollo [195].
        4. Guiar de manera sensible la práctica y ampliación de las destrezas [195].
        5. Proteger al niño de desaprobaciones constantes, hostigamiento o castigo [195].
        6. Comunicarse de forma plena, sensible y cariñosa [195].
        7. Encauzar la conducta de forma consistente estableciendo límites claros [195].
        """, unsafe_allow_html=True)
        
        # INTERACTIVO: AUTOEVALUACIÓN DE ESTIMULACIÓN HOME
        st.markdown("<div class='challenge-box'>", unsafe_allow_html=True)
        st.markdown("### 🏠 Autoevaluación de Estimulación en el Hogar (Basada en HOME)")
        st.markdown("Evalúa qué tan estimulante es tu hogar marcando las condiciones que implementan habitualmente con su bebé:")
        
        h1 = st.checkbox("1. Creamos y facilitamos espacios seguros y libres en el piso para que el bebé explore sin confinamiento constante [198].")
        h2 = st.checkbox("2. Jugamos activamente con el bebé, enseñándole habilidades como encajar formas, apilar o clasificar juguetes [195].")
        h3 = st.checkbox("3. Elogiamos y celebramos con sonrisas y mimos cada hito motriz o cognitivo superado [195].")
        h4 = st.checkbox("4. Le guiamos pacientemente y repetimos de forma suave las actividades cuando se le dificulta realizarlas solo [195].")
        h5 = st.checkbox("5. Evitamos por completo las palmadas, gritos, humillaciones u hostigamiento disciplinario [195].")
        h6 = st.checkbox("6. Respondemos de forma sensible a sus balbuceos y le hablamos de forma directa todo el tiempo [195, 198].")
        h7 = st.checkbox("7. Establecemos límites claros y consistentes para encauzar su conducta con amor y firmeza [195].")
        
        puntos = sum([h1, h2, h3, h4, h5, h6, h7])
        st.markdown(f"**Puntuación de Estimulación en tu Hogar: {puntos} / 7**")
        
        if puntos == 7:
            st.success("🌟 **Excelente entorno enriquecido.** Tu hogar cuenta con todas las pautas de crianza idóneas recomendadas por la escala HOME para impulsar el desarrollo intelectual y social [195].")
        elif puntos >= 5:
            st.info("👍 **Buen nivel de estimulación.** Tus bases son fuertes. Revisa los puntos que faltan para ver cómo incorporar nuevas pautas lúdicas o de comunicación sensible en la rutina diaria [195].")
        else:
            st.warning("⚠️ **Áreas de mejora identificadas.** Sería de gran beneficio para tu bebé enriquecer sus espacios de juego seguros, hablarle de forma constante y centrarse en respuestas afectuosas ante sus balbuceos y progresos [195, 198].")
        st.markdown("</div>", unsafe_allow_html=True)
        
    elif "Piagetiano" in enf_elegido:
        st.markdown("""
        ### Enfoque Piagetiano: La Etapa Sensoriomotriz (0 a 2 años)
        Jean Piaget demostró que los bebés aprenden sobre ellos y el mundo coordinando sus sentidos con sus movimientos corporales <span class='citation'>[197]</span>. Pasan por **6 subetapas** marcadas por el surgimiento de esquemas y **Reacciones Circulares** <span class='citation'>[200, 201]</span>:
        
        1.  **Uso de Reflejos (0 a 1 mes)**: Los infantes ejercitan sus reflejos de succión o búsqueda involuntarios y adquieren un control inicial de los mismos, modificando su esquema de succión [202, 208].
        2.  **Reacciones Circulares Primarias (1 a 4 meses)**: Repiten deliberadamente conductas corporales placenteras que ocurrieron antes al azar (ej. chuparse el dedo) [203, 209].
        3.  **Reacciones Circulares Secundarias (4 a 8 meses)**: Repiten acciones voluntarias para obtener respuestas e incentivos interesantes fuera de su cuerpo (ej. agitar repetidamente una sonaja) [204, 209].
        4.  **Coordinación de Esquemas Secundarios (8 a 12 meses)**: Conducta deliberada y dirigida a metas. Coordinan esquemas aprendidos para resolver un problema (ej. gatear y empujar un obstáculo para alcanzar un juguete) [205, 210].
        5.  **Reacciones Circulares Terciarias (12 a 18 meses)**: Experimentación activa. El niño varía de forma deliberada sus acciones para ver diferentes resultados por ensayo y error (ej. arrojar juguetes al suelo desde distintas alturas) [206, 212].
        6.  **Combinaciones Mentales (18 a 24 meses)**: Capacidad representacional. Pueden pensar en actos y simularlos mentalmente antes de ejecutarlos, abandonando el laborioso método de ensayo y error [207, 213].
        
        #### Permanencia del Objeto:
        Piaget afirmaba que los bebés menores de 8 meses no entienden que un objeto sigue existiendo si no está a la vista <span class='citation'>[225]</span>. El entendimiento gradual de la **permanencia del objeto** se consolida totalmente hacia la sexta subetapa (18-24 meses) <span class='citation'>[225, 285]</span>.
        """, unsafe_allow_html=True)
        
        # AUTOEVALUACIÓN INTERACTIVA: PIAGET EN EL JUEGO
        st.markdown("<div class='challenge-box'>", unsafe_allow_html=True)
        st.markdown("### 🧩 Identificador del Juego Piagetiano")
        p_opt = st.radio(
            "Tu bebé de 6 meses sacude de manera continua una sonaja de plástico con cascabeles. Al oír el sonido sonríe, la detiene, la vuelve a sacudir con fuerza y ríe con júbilo. ¿En qué subetapa y reacción circular se encuentra?",
            ["Subetapa 2: Reacción Circular Primaria", "Subetapa 3: Reacción Circular Secundaria", "Subetapa 5: Reacción Circular Terciaria"]
        )
        if st.button("Enviar Respuesta"):
            if p_opt == "Subetapa 3: Reacción Circular Secundaria":
                st.success("🎉 **¡Perfecto! Se trata de una Reacción Circular Secundaria (Subetapa 3).** El bebé dirige su acción voluntaria hacia un objeto de su entorno para reproducir un efecto sonoro agradable que descubrió por accidente en primer lugar [204, 209, 211].")
            else:
                st.error("Incorrecto. Inténtalo de nuevo. Pista: La acción se dirige hacia un objeto fuera de su cuerpo (entorno), no a una parte corporal de sí mismo.")
        st.markdown("</div>", unsafe_allow_html=True)
        
    elif "Procesamiento" in enf_elegido:
        st.markdown("""
        ### Enfoque del Procesamiento de la Información
        Analiza las capacidades mentales de forma microscópica, midiendo y haciendo inferencias sobre la atención, habituación, memoria y transferencia sensorial <span class='citation'>[230, 231]</span>.
        
        *   **Habituación**: Disminución o cese del interés del infante ante la exposición repetida de un estímulo familiar (ej. el bebé deja de prestar atención a un dibujo tras mirarlo varias veces) <span class='citation'>[231, 232]</span>.
        *   **Deshabituación**: Recuperación inmediata del interés y atención del bebé al presentársele un estímulo novedoso que rompe su habituación <span class='citation'>[231, 232]</span>.
        *   **Velocidad de Procesamiento y Preferencia de Novedad**: Los bebés que se habitúan más rápido y que demuestran una fuerte preferencia por la novedad (fijar la atención en cosas que no conocen) muestran signos de un procesamiento más rápido de imágenes mentales <span class='citation'>[231, 233]</span>. Se correlacionan positivamente con un Coeficiente Intelectual (CI) más alto en la infancia tardía <span class='citation'>[231, 237]</span>.
        *   **Transferencia entre Modalidades**: Capacidad de usar la información adquirida con un sentido para guiar otro (ej. identificar solo con la vista un juguete que previamente succionaron con los ojos vendados) <span class='citation'>[235]</span>.
        *   **Atención Conjunta**: Aparece a los 10-12 meses cuando el infante sigue la mirada y el dedo del adulto señalando un objeto [236]. Su presencia predice un vocabulario más amplio a los 18 meses [236].
        """, unsafe_allow_html=True)
        
    elif "Neurociencias" in enf_elegido:
        st.markdown("""
        ### Enfoque de las Neurociencias Cognoscitivas
        Identifica qué estructuras físicas del encéfalo gobiernan tareas y memorias específicas en los primeros tres años de vida <span class='citation'>[174, 257]</span>:
        
        #### Dos Sistemas Diferenciados de Memoria a Largo Plazo:
        1.  **Memoria Implícita (Temprana e Inconsciente)**:
            *   *Estructuras*: Tallo cerebral, puente de Varolio y cerebelo <span class='citation'>[257, 275]</span>.
            *   *Concepto*: Memoria inconsciente de hábitos, destrezas motoras y respuestas reflejadas <span class='citation'>[257]</span>. Permite al bebé saber patear para mover el móvil de Rovee-Collier sin esfuerzo consciente <span class='citation'>[257]</span>.
        2.  **Memoria Explícita / Declarativa (Tardía y Consciente)**:
            *   *Estructuras*: Hipocampo y corteza temporal <span class='citation'>[257, 259]</span>.
            *   *Concepto*: Recuerdo intencional y deliberado de hechos, nombres, sucesos y rostros que se pueden declarar de forma verbal o simbólica <span class='citation'>[257]</span>. Su maduración gradual explica por qué los bebés pequeños padecen de amnesia infantil y por qué a finales del año son capaces de recordar e imitar conductas diferidas [180, 220].
            
        #### Memoria de Trabajo y Corteza Prefrontal (6 a 12 meses):
        *   La **Memoria de Trabajo** es el almacén a corto plazo de información activa en proceso en el cerebro <span class='citation'>[260]</span>. 
        *   Su desarrollo depende de la maduración de la corteza prefrontal lateral <span class='citation'>[ diamond, 260]</span>. Esto le otorga al bebé de 12 meses el autocontrol para evitar errores de búsqueda de objetos ocultos al inhibir el impulso impulsivo previo <span class='citation'>[261]</span>.
        """, unsafe_allow_html=True)
        
    elif "Contextual" in enf_elegido:
        st.markdown("""
        ### Enfoque Contextual Social: Participación Guiada
        Estudia cómo los patrones culturales y sociales inciden de forma contundente en el aprendizaje informal del bebé <span class='citation'>[262]</span>.
        
        *   **Participación Guiada (Vygotsky)**: Se refiere a las interacciones recíprocas estructuradas entre el adulto y el niño, ayudando a este último a 'salvar la brecha' entre su propia comprensión y el entendimiento cultural maduro <span class='citation'>[262]</span>.
        *   **Diferencias Culturales (Estudio Rogoff)**:
            *   *Comunidades urbanas occidentales de clase media*: Las madres asumen el juego de los bebés con alta estimulación verbal, tratándolos como pares comunicativos, elogiándolos con entusiasmo <span class='citation'>[263]</span>.
            *   *Comunidades rurales (ej. Pueblo Maya en Guatemala o Aldea en India)*: Los niños aprenden de manera informal observando y participando directamente en el mundo de trabajo diario de los adultos, recibiendo demostraciones no verbales de los cuidadores y asumiendo la práctica de forma autónoma <span class='citation'>[263, 264]</span>.
        """, unsafe_allow_html=True)

# --- 4. DESARROLLO SOCIOAFECTIVO ---
elif st.session_state.selected_page == "❤️ Desarrollo Socioafectivo":
    st.markdown("<h1 class='main-title'>❤️ Dimensión 3: Desarrollo Socioafectivo</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    La personalidad es la mezcla relativamente constante de emociones, temperamento, pensamiento y conducta que hace único a tu bebé <span class='citation'>[295]</span>. 
    Se construye a través de su sintonía afectiva en el entorno familiar, las interacciones sociales con otros niños y el cuidado sensible de su comunidad <span class='citation'>[295, 330]</span>.
    """, unsafe_allow_html=True)
    
    tab_sa1, tab_sa2, tab_sa3 = st.tabs(["📋 Fundamentos Afectivos", "👶 Autonomía y el Yo", "🏠 Entorno, Cuidado y Maltrato"])
    
    with tab_sa1:
        st.markdown("""
        ### Emociones, Sintonía Emocional y Temperamento
        
        #### Cronología del Desarrollo de las Emociones:
        *   **Nacimiento a 6 meses (Emociones Primarias)**: Los bebés muestran respuestas fisiológicas y difusas de interés, satisfacción y aflicción <span class='citation'>[305]</span>, las cuales se diferencian en enojo, tristeza, sorpresa, temor y repugnancia <span class='citation'>[308]</span>.
        *   **15 a 24 meses (Emociones Autoconscientes)**: Con la llegada de la autoconciencia conceptual, aparecen emociones como el bochorno ligero, la envidia y la empatía activa hacia los demás <span class='citation'>[307, 308, 311, 312]</span>.
        *   **2.5 a 3 años (Emociones Autoevaluativas)**: Al internalizar las normas, reglas y metas sociales, el niño es capaz de evaluar sus acciones y sentir **orgullo, culpa y vergüenza** <span class='citation'>[307, 309]</span>.
        
        #### El Temperamento y la Sintonía con Padres (Bondad de Ajuste):
        El temperamento es la base biológica innata sobre la cual se erige la personalidad <span class='citation'>[316, 318]</span>. El estudio longitudinal de Nueva York (NYLS) identificó tres perfiles temperamentales básicos <span class='citation'>[321, 385]</span>:
        *   **Niños Fáciles (40%)**: De estado de ánimo alegre por lo general, ritmos biológicos regulares y abiertos a aceptar nuevas experiencias y alimentos con facilidad <span class='citation'>[319, 321]</span>.
        *   **Niños Difíciles (10%)**: De emociones más intensas e irritables, ritmos biológicos irregulares y que reaccionan con fuertes pataletas o berrinches ante el cambio de rutinas <span class='citation'>[319, 321]</span>.
        *   **Niños Lentos para Animarse (15%)**: Apáticos, de reacciones iniciales ligeramente negativas o lentas ante la novedad, pero que asimilan y se adaptan gradualmente tras exposiciones repetidas <span class='citation'>[319, 321]</span>.
        *   **La Bondad de Ajuste (Goodness of Fit)**: Se refiere a qué tan bien sintonizan el estilo innato del bebé con las exigencias y prácticas de crianza de los cuidadores <span class='citation'>[325]</span>. El éxito y la armonía psicosocial dependen de que los padres conozcan y respeten el temperamento de su hijo en vez de forzarlo <span class='citation'>[325]</span>.
        
        #### Regulación Mutua y Referenciación Social:
        *   **Regulación Mutua**: Sincronía interactiva donde el cuidador y el bebé se comunican sus estados afectivos y responden de forma recíproca y sensible a las demandas del otro <span class='citation'>[343, 344]</span>. Las madres deprimidas rompen esta sintonía, provocando que los bebés se sientan tristes, frustrados y con problemas futuros de autorregulación emocional <span class='citation'>[343, 347, 389]</span>.
        *   **Referenciación Social**: Proceso en el cual, ante una situación ambigua o un objeto desconocido (ej. un juguete que vibra, una plaza de juegos o un perro), el bebé de 12 meses mira a su madre buscando señales en su rostro (sonrisas, advertencias) para regular e imitar la respuesta emocional del adulto <span class='citation'>[137, 348, 389]</span>.
        """, unsafe_allow_html=True)
        
    with tab_sa2:
        st.markdown("""
        ### El Surgimiento del Yo, Apego y Autonomía
        
        #### El Sentido del Yo:
        *   El autoconcepto (imagen total de nuestras capacidades y rasgos) surge perceptualmente de forma gradual entre los 4 y 10 meses <span class='citation'>[351, 390]</span>. 
        *   **La tarea del colorete**: El autorreconocimiento visual se consolida hacia los 18 meses de vida <span class='citation'>[353, 355]</span>. Si colocas colorete rojo en la nariz del bebé y lo colocas ante el espejo, si se toca su propia nariz, demuestra que entiende que la imagen reflejada es suya, no de otro bebé <span class='citation'>[355]</span>.
        
        #### Apego y Strange Situation (Mary Ainsworth):
        El apego es el vínculo emocional duradero y recíproco entre el bebé y su cuidador, que fomenta la supervivencia <span class='citation'>[336]</span>. Ainsworth diseñó la **Situación Extraña** para evaluar los patrones de apego del bebé de un año <span class='citation'>[337, 338, 387]</span>:
        *   **Apego Seguro**: El bebé llora o se inquieta al salir el cuidador, pero en el reencuentro corre hacia él de inmediato para buscar consuelo y se calma rápidamente, usando al adulto como base segura para explorar <span class='citation'>[337]</span>.
        *   **Apego Evasivo**: No se inmuta ante la salida del cuidador y lo ignora o evita con frialdad al regresar, manteniendo un alto estrés interno <span class='citation'>[337, 338]</span>.
        *   **Apego Ambivalente / Resistente**: Muestra gran ansiedad previa; al regresar el cuidador busca la cercanía pero simultáneamente patea, se resiste o arquea la espalda con enojo, siendo muy difícil de consolar <span class='citation'>[337, 338]</span>.
        *   **Apego Desorganizado / Desorientado**: Muestra conductas contradictorias, temerosas o confusas (como acercarse dándole la espalda o quedarse congelado con la mirada perdida), común en entornos con negligencia o maltrato <span class='citation'>[337, 338]</span>.
        
        #### Autonomía frente a Vergüenza y Duda (Los Terribles Dos Años):
        *   De acuerdo con Erik Erikson, tras resolver la confianza básica mediante sintonía responsiva [331], la segunda etapa psicosocial (18 meses a 3 años) se centra en la **Autonomía frente a la Vergüenza y la Duda** <span class='citation'>[332, 355]</span>.
        *   Los berrinches y el negativismo constante (decir '¡NO!') son intentos sanos y normales de autoafirmarse como individuos separados de sus padres <span class='citation'>[356]</span>. Si se les reprime de forma constante o se les humilla, se siembra la duda perpetua en sus capacidades y la vergüenza ante sus impulsos <span class='citation'>[356]</span>.
        """, unsafe_allow_html=True)
        
        # INTERACTIVO: SIMULADOR DE CRISIS "TERRIBLES DOS"
        st.markdown("<div class='challenge-box'>", unsafe_allow_html=True)
        st.markdown("### 🎭 Simulador de Decisiones de Crianza: Los Terribles Dos Años")
        st.markdown("""
        Tu hijo de 2 años se opone tajantemente a lavarse los dientes en la noche, gritando '¡NO!' y apartándote la mano. 
        ¿Cómo respondes para guiar su autonomía en lugar de fomentar la vergüenza o duda?
        """, unsafe_allow_html=True)
        
        opcion_b = st.selectbox("Elige tu respuesta de crianza:", [
            "A. Lo obligas físicamente, sujetándole la cabeza mientras le restriegas el cepillo con fuerza y le dices que se calle de inmediato.",
            "B. Le explicas de forma calmada que hay que lavarse los dientes, y le das a elegir entre cepillarse él solo primero o que tú lo asistas jugando a los astronautas con cepillos de colores.",
            "C. Cedes por completo ante su berrinche y dejas que se acueste sin lavar con tal de que no grite ni llore."
        ], index=1)
        
        if st.button("Evaluar Estrategia de Crianza"):
            if opcion_b.startswith("A"):
                st.error("❌ **Efecto de Vergüenza y Duda (Erikson)**: Usar la fuerza rígida y la hostilidad reprime sus impulsos de autoafirmación independientes, provocando que dude de su capacidad para participar activamente y sembrando vergüenza en su autocontrol de esfínteres o higiene [356].")
            elif opcion_b.startswith("B"):
                st.success("🎉 **¡Excelente! Sintonía de Autonomía (Erikson)**: No transiges con la regla de higiene (salud), pero le ofreces poder de decisión (elegir cepillo o método) y fomentas su práctica con diversión. Guías su autonomía de forma constructiva, sentando las bases de la autorregulación [195, 356, 363].")
            else:
                st.warning("⚠️ **Estrategia Inconsistente (Permisiva)**: Ceder ante el berrinche no le ayuda a internalizar las metas o normas de higiene, dificultando el progreso de su autorregulación. Los límites consistentes con amor son necesarios en su desarrollo [356, 363].")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with tab3:
        st.markdown("""
        ### Contexto Familiar, Guarderías y Maltrato Infantil
        
        #### Interacción con Pares (Hermanos y otros niños):
        *   **Hermanos**: Sientan un pilar fundamental en la socialización temprana <span class='citation'>[373]</span>. Los berrinches y disputas entre hermanos menores (que se elevan a partir de los 18 meses) enseñan de forma constructiva empatía, intenciones de los otros, y cómo negociar y llegar a acuerdos en un entorno afectivo seguro <span class='citation'>[374, 375]</span>.
        *   **Sociabilidad con otros niños**: De los 6 a 12 meses, los bebés ríen y balbucean ante otros de su tamaño [376]. De los 1.5 a 3 años, muestran un fuerte interés por imitarse mutuamente (jugar a seguir al líder), coordinar el juego compartido y resolver disputas negociando [377].
        
        #### Guarderías de Alta Calidad:
        Los estudios de largo plazo del NICHD demostraron que las características socioeconómicas y la sensibilidad cariñosa de la familia en el hogar tienen un impacto diez veces mayor en el desarrollo temprano del niño que el hecho de asistir o no a una guardería fuera de casa <span class='citation'>[102, 381]</span>. No obstante, para garantizar un desarrollo cognoscitivo y social óptimo, asegúrate de que la guardería elegida cumpla con los estándares de la Academia Americana de Pediatría (AAP) <span class='citation'>[380, 381]</span>:
        *   **Baja proporción de niños por cuidador**: Máximo 3 a 4 bebés menores de un año por cada adulto <span class='citation'>[381]</span>.
        *   **Cuidadores altamente cálidos, estables, sensibles y capacitados** en el desarrollo infantil <span class='citation'>[380, 381]</span>.
        *   **Espacios seguros, interiores y exteriores limpios** con abundantes juguetes didácticos <span class='citation'>[381]</span>.
        *   **Programa de juego libre y estructurado** al propio ritmo del bebé <span class='citation'>[381]</span>.
        
        #### Maltrato: Abuso y Negligencia:
        Se define como cualquier acción u omisión voluntaria de los cuidadores que atente contra el bienestar físico, mental y emocional del niño <span class='citation'>[382]</span>:
        *   **Abuso Físico**: Golpes, sacudidas o quemaduras deliberadas <span class='citation'>[382]</span>.
        *   **Negligencia (Suele ser la más frecuente)**: Omisión voluntaria de satisfacer las necesidades básicas vitales del niño (comida, vestido, atención médica, protección activa y supervisión) <span class='citation'>[382, 383]</span>.
        *   **Abuso Sexual**: Cualquier involucramiento sexual con el infante <span class='citation'>[382]</span>.
        *   **Maltrato Emocional**: Rechazo constante, humillaciones verbales, privar de afecto o aislamiento social severo <span class='citation'>[382]</span>.
        """, unsafe_allow_html=True)
        
        # INTERACTIVO: CHECKLIST DE GUARDERÍA
        st.markdown("<div class='challenge-box'>", unsafe_allow_html=True)
        st.markdown("### 🏫 Lista de Cotejo de Guarderías de Alta Calidad (AAP)")
        st.markdown("Si estás evaluando una guardería para tu bebé, marca las condiciones que cumple para medir su calidad de estimulación:")
        
        g1 = st.checkbox("La guardería cuenta con licencia del estado vigente y rigurosa prevención de incendios [381].")
        g2 = st.checkbox("La proporción es baja: máximo de 3 a 4 bebés por cada cuidador adulto [381].")
        g3 = st.checkbox("Los cuidadores son estables (baja rotación) y responden de inmediato con calidez y sintonía al llanto del bebé [381].")
        g4 = st.checkbox("El entorno es higiénico, seguro, amplio y cuenta con abundantes materiales y juguetes para el ritmo del infante [381].")
        g5 = st.checkbox("El programa fomenta la lectura interactiva diaria en voz alta y el juego compartido [381].")
        
        puntos_g = sum([g1, g2, g3, g4, g5])
        st.markdown(f"**Puntuación de Calidad de la Guardería: {puntos_g} / 5**")
        
        if puntos_g == 5:
            st.success("🏫 **Guardería de alta calidad de nivel excelente.** Proporciona un entorno sensible e idóneo para complementar el desarrollo psicosocial y cognitivo de tu bebé [381].")
        elif puntos_g >= 3:
            st.info("👍 **Calidad aceptable.** Procura conversar con el personal para solventar los aspectos que faltan por marcar o buscar alternativas que fortalezcan estos rubros [381].")
        else:
            st.warning("⚠️ **Atención.** Las guarderías con bajos estándares de estimulación o con demasiados niños por cuidador pueden comprometer la seguridad emocional de tu bebé, elevando sus niveles de cortisol y estrés diario [380, 381].")
        st.markdown("</div>", unsafe_allow_html=True)

# --- 5. DESARROLLO LINGÜÍSTICO ---
elif st.session_state.selected_page == "🗣️ Desarrollo Lingüístico":
    st.markdown("<h1 class='main-title'>🗣️ Dimensión 4: Desarrollo Lingüístico</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    La adquisición de la lengua materna es uno de los logros más deslumbrantes de los primeros tres años, transformando de manera activa las 
    estructuras y conexiones neurales del cerebro del bebé mediante la interacción social activa con sus cuidadores <span class='citation'>[268, 275, 277]</span>.
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### La Cronología de la Comunicación Infantil
        
        La adquisición del lenguaje se divide de forma predecible en dos etapas fundamentales <span class='citation'>[268]</span>:
        
        #### 1. Habla Prelingüística (Nacimiento a 10 meses):
        Abarca el uso de sonidos pre-lingüísticos para comunicar necesidades, sentimientos y llamar la atención <span class='citation'>[268]</span>:
        *   **Llanto**: Primer medio reflejo de comunicación para denotar hambre, incomodidad o dolor [267].
        *   **Arrullos y Risas (6 semanas a 3 meses)**: Emisión de sonidos vocálicos simples y cantarines (ej. 'uuh', 'aah') al sentirse relajado [267, 268].
        *   **Juegos con Sonidos (3 a 6 meses)**: El bebé experimenta activamente con la modulación de su voz [267].
        *   **Balbuceo (6 a 10 meses)**: Repetición de sílabas consonante-vocal encadenadas (ej. 'ma-ma-ma', 'da-da-da', 'ba-ba-ba') <span class='citation'>[267, 268]</span>. No es lenguaje intencional al inicio, sino imitación activa de la entonación y sonidos locales de los cuidadores <span class='citation'>[268]</span>.
        *   **Gestos Sociales (9 a 12 meses)**: Se comunica apuntando con el índice, moviendo la mano para decir adiós o asintiendo <span class='citation'>[267, 268]</span>.
        
        #### 2. Habla Lingüística (10 a 24 meses):
        *   **Primeras Palabras (10 a 14 meses)**: Emisión voluntaria de fonemas con significado representacional claro (ej. dice 'mamá' para llamar a su madre biológica) <span class='citation'>[268]</span>.
        *   **Holofrases (10 a 18 meses)**: El uso de una sola palabra para comunicar un pensamiento complejo completo de acuerdo con el contexto (ej. dice '¡Miel!' para significar 'quiero que me des ese tarro de miel ahora') <span class='citation'>[268, 272]</span>.
        *   **Habla Telegráfica (18 a 24 meses)**: Primeras frases sencillas uniendo solo las palabras esenciales de su idea, omitiendo artículos y verbos auxiliares (ej. 'bebé pan' por 'quiero que mamá me dé pan') <span class='citation'>[272]</span>.
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        ### Prácticas de Crianza que Potencian el Lenguaje
        
        El lenguaje es un acto intrínsecamente social que requiere un trato directo con un interlocutor en la vida real <span class='citation'>[277]</span>. Los bebés sordos imitan el lenguaje de señas en la misma secuencia lúdica que los oyentes imitan el habla (balbuceo con las manos) <span class='citation'>[274]</span>. Sin embargo, los bebés expuestos a idiomas solo a través de la televisión no adquieren vocabulario ni fonemas <span class='citation'>[277]</span>.
        
        #### Pautas de Estimulación de los Cuidadores:
        *   **Atención Conjunta y Señalamiento**: Seguir la mirada de tu bebé y nombrar en voz alta el objeto que está viendo o señalando acelera de forma asombrosa la asimilación de su vocabulario receptivo [278].
        *   **Lectura en Voz Alta**: Leerle libros ilustrados de forma interactiva desde los primeros meses promueve el alfabetismo posterior, ayuda a discernir el sonido de las letras y asocia significados ricos a la comunicación [280].
        *   **Habla Dirigida a Niños (Maternés / Parentese)**: Hablarle al bebé de forma lenta, simplificando frases, usando un tono agudo y modulando de forma exagerada las vocales capta su atención neural y le ayuda a discriminar los fonemas principales de su idioma de forma mucho más eficaz [280].
        """, unsafe_allow_html=True)
        
    # JUEGO INTERACTIVO: ASOCIACIÓN DE HITOS DEL LENGUAJE
    st.markdown("<div class='challenge-box'>", unsafe_allow_html=True)
    st.markdown("### 🧩 Juego Interactivo: El Orden del Habla")
    st.markdown("Asocia cada comportamiento de tu bebé con el rango de edad típico descrito por la ciencia:")
    
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        q_coo = st.selectbox("Arrullos vocálicos simples cantarines (ej. 'uuh', 'aah'):", [
            "6 semanas a 3 meses", "6 a 10 meses", "10 a 14 meses", "18 a 24 meses"
        ], index=0)
        
        q_bab = st.selectbox("Balbuceos encadenados consonante-vocal (ej. 'da-da-da'):", [
            "6 semanas a 3 meses", "6 a 10 meses", "10 a 14 meses", "18 a 24 meses"
        ], index=1)
        
    with col_l2:
        q_hol = st.selectbox("Primeras palabras individuales u holofrases con significado (ej. '¡Biberón!'):", [
            "6 semanas a 3 meses", "6 a 10 meses", "10 a 14 meses", "18 a 24 meses"
        ], index=2)
        
        q_tel = st.selectbox("Habla telegráfica combinando palabras esenciales (ej. 'papá agua'):", [
            "6 semanas a 3 meses", "6 a 10 meses", "10 a 14 meses", "18 a 24 meses"
        ], index=3)
        
    if st.button("Comprobar Respuestas Lingüísticas"):
        is_ok = True
        errs = []
        
        if q_coo != "6 semanas a 3 meses":
            is_ok = False
            errs.append("Arrullos")
        if q_bab != "6 a 10 meses":
            is_ok = False
            errs.append("Balbuceos")
        if q_hol != "10 a 14 meses":
            is_ok = False
            errs.append("Primeras palabras")
        if q_tel != "18 a 24 meses":
            is_ok = False
            errs.append("Habla telegráfica")
            
        if is_ok:
            st.success("🎉 **¡Perfecto! Has ordenado la línea de tiempo del lenguaje correctamente.** Entiendes las fases lógicas del habla prelingüística y lingüística del desarrollo infantil [267, 268].")
        else:
            st.error(f"⚠️ **Hay discrepancias en tu orden.** Revisa los rangos de edad seleccionados para: {', '.join(errs)}. ¡Pista: los arrullos ocurren en los primeros meses antes de balbucear consonantes!")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 6. REFERENCIAS BIBLIOGRÁFICAS ---
elif st.session_state.selected_page == "📚 Referencias Bibliográficas":
    st.markdown("<h1 class='main-title'>📚 Referencias Bibliográficas</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    Todos los hitos, explicaciones, experimentos científicos y datos de la presente aplicación interactiva están estrictamente respaldados en la obra clásica de psicología evolutiva:
    
    *   **Papalia, D. E., Feldman, R. D., y Martorell, G. (2012).** *Desarrollo Humano* (12ª ed.). McGraw-Hill Interamericana.
        *   **Capítulo 3**: Formación de una nueva vida (Gesta prenatal, concepción, herencia y medio ambiente).
        *   **Capítulo 4**: Nacimiento y desarrollo físico en los primeros tres años (Neonato, Apgar, crecimiento, principios y teorías motoras de Thelen y Gibson).
        *   **Capítulo 5**: Desarrollo cognoscitivo en los primeros tres años (Seis enfoques de la cognición, HOME, Bayley, Piaget, Procesamiento de información y lenguaje).
        *   **Capítulo 6**: Desarrollo psicosocial en los primeros tres años (Emociones, temperamento, apego, confianza, autonomía, socialización y maltrato).
        
    *Nota explicativa: El formato de citación utilizado en la aplicación (por ejemplo, [12]) corresponde directamente a la numeración del pasaje textual original del libro de texto presente en el notebook de consulta del usuario, asegurando un 100% de trazabilidad y confiabilidad científica contra sus fuentes originales.*
    """, unsafe_allow_html=True)
