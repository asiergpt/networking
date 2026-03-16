import streamlit as st
import streamlit.components.v1 as components
import base64
import os

def get_image_base64(path):
    try:
        if not os.path.exists(path):
            return ""
        with open(path, "rb") as f:
            return f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"
    except Exception:
        return ""

def show_networking():

    current_dir = os.path.dirname(__file__)
    img_hero = get_image_base64(os.path.join(current_dir, "networking_hero.png"))
    img_tag = f'<img src="{img_hero}" alt="Networking map">' if img_hero else ""

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500;600;700&family=Manrope:wght@300;400;500;600&display=swap');

    #MainMenu, header, footer { visibility: hidden; display: none; }

    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .main .block-container {
        background-color: #ffffff !important;
    }

    .block-container {
        padding: 2rem 2rem 2rem 2rem !important;
        max-width: 100% !important;
    }

    /* ---- HERO ---- */
    .net-hero {
        background: #0d0d0d;
        border-radius: 20px;
        padding: 32px 44px;
        border: 1px solid rgba(255,204,102,0.15);
        margin-bottom: 20px;
        transition: border-color 0.25s, box-shadow 0.25s;
        display: flex;
        align-items: center;
        gap: 32px;
        overflow: hidden;
        position: relative;
    }
    .net-hero:hover {
        border-color: rgba(255,204,102,0.6);
        box-shadow: 0 0 0 1px rgba(255,204,102,0.25), 0 0 28px rgba(255,204,102,0.12);
    }
    .net-hero-text { flex: 1; min-width: 0; }
    .net-hero-img {
        flex: 0 0 auto;
        width: clamp(180px, 30%, 320px);
        height: 220px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .net-hero-img img {
        width: 100%; height: 100%; object-fit: contain; border-radius: 0;
        animation: net-float 6s ease-in-out infinite;
        transition: transform 0.5s ease, filter 0.5s ease;
        filter: drop-shadow(0 8px 24px rgba(255,204,102,0.15));
    }
    .net-hero-img img:hover {
        transform: scale(1.06) rotate(-1deg) !important;
        animation-play-state: paused;
        filter: drop-shadow(0 12px 36px rgba(255,204,102,0.3));
    }
    @keyframes net-float {
        0%   { transform: translateY(0px) rotate(0deg); }
        25%  { transform: translateY(-6px) rotate(1deg); }
        50%  { transform: translateY(-10px) rotate(0deg); }
        75%  { transform: translateY(-6px) rotate(-1deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }
    .net-hero-title {
        font-family: 'Quicksand', sans-serif;
        font-size: 1.9rem; font-weight: 700;
        color: transparent;
        -webkit-text-stroke: 1.4px #ffcc66;
        text-shadow: 0 0 16px rgba(255,204,102,0.2);
        line-height: 1.1; margin-bottom: 10px;
    }
    .net-hero-sub {
        font-family: 'Manrope', sans-serif;
        font-size: 0.88rem; font-weight: 300;
        color: #999; line-height: 1.65;
    }

    /* ---- MIRO CONTAINER ---- */
    .net-miro-wrap {
        border-radius: 16px;
        overflow: hidden;
        border: 1px solid rgba(255,204,102,0.2);
        box-shadow: 0 8px 32px rgba(0,0,0,0.08);
        transition: border-color 0.25s, box-shadow 0.25s;
    }
    .net-miro-wrap:hover {
        border-color: rgba(255,204,102,0.5);
        box-shadow: 0 12px 40px rgba(255,204,102,0.1);
    }

    @media (max-width: 768px) {
        .net-hero { flex-direction: column; padding: 24px 20px; border-radius: 14px; gap: 20px; }
        .net-hero-img { width: 100%; height: 200px; }
        .net-hero-title { font-size: 1.5rem; }
        .net-hero-sub { font-size: 0.84rem; }
        .block-container { padding: 1rem !important; }
        .net-miro-wrap { border-radius: 10px; }
    }
    </style>
    """, unsafe_allow_html=True)

    # ---- HERO ----
    st.markdown(f"""
    <div class="net-hero">
        <div class="net-hero-text">
            <div class="net-hero-title">Mapa de Networking</div>
            <div class="net-hero-sub">
                Visualiza el ecosistema de conexiones estratégicas en el mercado ejecutivo vasco.
                Identifica los nodos clave, los puentes y las rutas de acceso a la alta dirección.
            </div>
            <a href="https://asierdorronsoro.streamlit.app/" target="_blank" style="
                display: inline-flex; align-items: center; gap: 8px; margin-top: 20px;
                font-family: 'Manrope', sans-serif; font-size: 0.65rem; font-weight: 600;
                letter-spacing: 2.5px; text-transform: uppercase;
                color: rgba(255,204,102,0.65) !important; -webkit-text-fill-color: rgba(255,204,102,0.65);
                border: 1px solid rgba(255,204,102,0.25); border-radius: 8px;
                padding: 8px 16px; text-decoration: none !important; background: transparent;
                transition: all 0.25s ease;
            "
            onmouseover="this.style.borderColor='rgba(255,204,102,0.7)';this.style.background='rgba(255,204,102,0.07)';this.style.webkitTextFillColor='#ffcc66';"
            onmouseout="this.style.borderColor='rgba(255,204,102,0.25)';this.style.background='transparent';this.style.webkitTextFillColor='rgba(255,204,102,0.65)';"
            >
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none">
                    <path d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
                          stroke="#ffcc66" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                ← Inicio
            </a>
        </div>
        <div class="net-hero-img">{img_tag}</div>
    </div>
    """, unsafe_allow_html=True)

    # ---- LEYENDA DESPLEGABLE ----
    with st.expander("📖 Cómo leer este mapa", expanded=True):
        st.markdown("""
        <style>
        .legend-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 12px;
            margin-bottom: 20px;
        }
        .legend-card {
            border-radius: 12px;
            padding: 14px 16px;
            border: 1px solid #eeeeee;
        }
        .legend-card-title {
            font-family: 'Quicksand', sans-serif;
            font-size: 0.92rem; font-weight: 700;
            color: #111; margin-bottom: 6px;
            display: flex; align-items: center; gap: 8px;
        }
        .legend-card-desc {
            font-family: 'Manrope', sans-serif;
            font-size: 0.82rem; color: #666; line-height: 1.6;
        }
        .legend-dot {
            width: 12px; height: 12px; border-radius: 50%; flex-shrink: 0;
        }
        .legend-section-title {
            font-family: 'Quicksand', sans-serif;
            font-size: 0.68rem; font-weight: 700;
            letter-spacing: 2px; text-transform: uppercase;
            color: #aaaaaa; margin: 18px 0 10px;
        }
        @media (max-width: 640px) {
            .legend-grid {
                grid-template-columns: 1fr !important;
            }
        }
        </style>
        <div class="legend-section-title">Los anillos: mi nivel de acceso</div>
        <div class="legend-grid">
            <div class="legend-card" style="background:#f0fff4; border-color:#c8e6c9;">
                <div class="legend-card-title">
                    <div class="legend-dot" style="background:#4caf50;"></div>
                    Verde (Conexión Directa)
                </div>
                <div class="legend-card-desc">
                   Es mi círculo de confianza y acción inmediata. Son personas con las que ya tengo una relación activa y establecida; ya hemos intercambiado correos, tenido reuniones o colaborado en proyectos.
                </div>
            </div>
            <div class="legend-card" style="background:#fffde7; border-color:#fff176;">
                <div class="legend-card-title">
                    <div class="legend-dot" style="background:#fdd835;"></div>
                    Amarillo (Conexión Indirecta)
                </div>
                <div class="legend-card-desc">
                   Están a un grado de separación. Aún no tengo contacto directo con ellos, pero alguien de mi anillo verde puede hacerme de puente. Es mi zona principal de expansión.
                </div>
            </div>
            <div class="legend-card" style="background:#fff5f5; border-color:#ffcdd2;">
                <div class="legend-card-title">
                    <div class="legend-dot" style="background:#ef5350;"></div>
                    Rojo (Sin Conexión)
                </div>
                <div class="legend-card-desc">
                    No tengo acceso ni puente claro todavía. Son mi objetivo a medio o largo plazo; para llegar a ellos, primero debo nutrir y expandir mi anillo amarillo.
                </div>
            </div>
        </div>
        <div class="legend-section-title">Los Sectores: Su rol en mi red</div>
        <div class="legend-grid">
            <div class="legend-card" style="background:#f8f8f8;">
                <div class="legend-card-title">🏆 Sponsors</div>
                <div class="legend-card-desc">
                    Son personas con poder de decisión y capacidad real para abrirme puertas a oportunidades ejecutivas. Son el objetivo final de mi estrategia.
                </div>
            </div>
            <div class="legend-card" style="background:#f8f8f8;">
                <div class="legend-card-title">🧭 Mentores</div>
                <div class="legend-card-desc">
                    Me aportan experiencia, perspectiva y criterio. Me ayudan a orientar mi carrera y a validar mi propuesta de valor dentro del ecosistema vasco.
                </div>
            </div>
            <div class="legend-card" style="background:#f8f8f8;">
                <div class="legend-card-title">🔗 Conectores</div>
                <div class="legend-card-desc">
                    Son mis "multiplicadores". Profesionales muy bien relacionados cuyo principal valor es facilitarme introducciones y servir de puente hacia los Sponsors o Mentores.
                </div>
            </div>
        </div>
        <div class="legend-section-title">Los Post-its: Su dimensión profesional</div>
        <div class="legend-grid">
            <div class="legend-card" style="background:#f3e5f5; border-color:#e1bee7;">
                <div class="legend-card-title">
                    <div class="legend-dot" style="background:#9c27b0;"></div>
                    Morado (Posible Superior)
                </div>
                <div class="legend-card-desc">
                    Personas a las que podría reportar directamente en mi próximo rol. Entender sus dolores, sus metodologías y qué valoran es clave para saber cómo posicionarme ante ellos.
                </div>
            </div>            
            <div class="legend-card" style="background:#e8f0fe; border-color:#c5cae9;">
                <div class="legend-card-title">
                    <div class="legend-dot" style="background:#5c6bc0;"></div>
                    🟦 Azul (Pares / Similares)
                </div>
                <div class="legend-card-desc">
                   Profesionales que ocupan roles similares al que aspiro. Son mi termómetro de mercado y me ayudan a calibrar mi discurso y mi propuesta de valor.
                </div>
            </div>
            <div class="legend-card" style="background:#e8f5e9; border-color:#c8e6c9;">
                <div class="legend-card-title">
                    <div class="legend-dot" style="background:#43a047;"></div>
                    🟩 Verde claro (Posible Equipo)
                </div>
                <div class="legend-card-desc">
                   Personas que podrían reportarme o estar a mi cargo. Escucharlos me da una visión real de "las trincheras" y de la cultura operativa del terreno desde dentro.
                </div>
            </div>
            <div class="legend-card" style="background:#f5f5f5; border-color:#eeeeee;">
                <div class="legend-card-title">
                    <div class="legend-dot" style="background:#9e9e9e;"></div>
                    ⬜ Gris (Relación indirecta)
                </div>
                <div class="legend-card-desc">
                    No encajan en la estructura jerárquica directa de mi objetivo, pero aportan contexto, me hablan de tendencias y me dan una visión transversal del mercado.
                </div>
            </div>
        </div>
        <div style="
            background:#0d0d0d; border-radius:10px; padding:14px 18px;
            border:1px solid rgba(255,204,102,0.15); margin-top:4px;
        ">
            <p style="
                font-family:'Manrope',sans-serif; font-size:0.84rem;
                color:#aaaaaa; line-height:1.7; margin:0;
            ">
                💡 <span style="color:#ffcc66; font-weight:600;">Cómo usarlo:</span>
                Cruza las tres dimensiones. Una persona en el <b style="color:#fff;">anillo verde</b> +
                <b style="color:#9c27b0;">post-it morado</b> es alguien a quien ya conozco y que podría ser mi próximo jefe —
                es una conversación prioritaria. Una persona en el <b style="color:#fff;">anillo amarillo</b> +
                <b style="color:#5c6bc0;">post-it azul</b> es un profesional similar del sector al que aún no tengo acceso,
                pero que vale la pena activar a través del anillo verde.
            </p>
        </div>
        <div style="height: 20px;"></div>
        """, unsafe_allow_html=True)

    # ---- MIRO EMBED ----
    # Altura adaptada: más baja en móvil
    import streamlit.components.v1 as components
    st.markdown('<div class="net-miro-wrap">', unsafe_allow_html=True)
    components.iframe(
        "https://miro.com/app/live-embed/uXjVGy29RhY=/?embedMode=view_only_without_ui&moveToViewport=-6883,-2139,6378,2948&embedId=356837250172",
        height=650,
        scrolling=False
    )
    st.markdown('</div>', unsafe_allow_html=True)
    # Nota móvil
    st.markdown("""
    <p style="
        font-family:'Manrope',sans-serif; font-size:0.72rem;
        color:#cccccc; text-align:center; margin-top:10px;
    ">
        💡 En móvil puedes usar dos dedos para hacer zoom y moverte por el mapa.
    </p>
    """, unsafe_allow_html=True)
