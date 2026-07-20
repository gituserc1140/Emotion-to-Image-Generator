import replicate
import streamlit as st

_CSS = """
<style>
/* ── Page background ───────────────────────────────────────────── */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    min-height: 100vh;
}
[data-testid="stHeader"] { background: transparent; }

/* ── Hero banner ───────────────────────────────────────────────── */
.hero {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
}
.hero h1 {
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(90deg, #f9a8d4, #fbbf24, #60a5fa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.3rem;
}
.hero p {
    color: #cbd5e1;
    font-size: 1.05rem;
    margin-top: 0;
}

/* ── Compliment card ───────────────────────────────────────────── */
.compliment-card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(251,191,36,0.4);
    border-radius: 14px;
    padding: 1.4rem 1.6rem;
    color: #fef9c3;
    font-size: 1.1rem;
    line-height: 1.8;
    margin-top: 1rem;
    margin-bottom: 1rem;
}
.section-label {
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #fbbf24;
    margin-bottom: 0.4rem;
}

/* ── Error card ────────────────────────────────────────────────── */
.error-card {
    background: rgba(239,68,68,0.12);
    border: 1px solid rgba(239,68,68,0.45);
    border-radius: 14px;
    padding: 1.2rem 1.6rem;
    color: #fca5a5;
    font-size: 0.97rem;
    margin-top: 1rem;
}

/* ── Buttons ───────────────────────────────────────────────────── */
[data-testid="stButton"] button {
    background: linear-gradient(135deg, #d97706, #2563eb) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.45rem 1.4rem !important;
    font-weight: 600 !important;
    transition: opacity 0.2s !important;
}
[data-testid="stButton"] button:hover { opacity: 0.85 !important; }

/* ── Sidebar ───────────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background: rgba(15,12,41,0.85);
    border-right: 1px solid rgba(251,191,36,0.2);
}
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] div { color: #cbd5e1 !important; }
[data-testid="stSidebar"] h2 {
    color: #fbbf24 !important;
    font-size: 1.1rem;
}

/* ── GitHub buttons ────────────────────────────────────────────── */
.gh-buttons {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    margin-top: 1rem;
}
.gh-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    padding: 0.4rem 0.9rem;
    border-radius: 6px;
    font-size: 0.85rem;
    font-weight: 600;
    text-decoration: none !important;
    transition: opacity 0.2s;
}
.gh-btn:hover { opacity: 0.82; }
.gh-btn-github {
    background: #24292f;
    color: #ffffff !important;
    border: 1px solid #444c56;
}
.gh-btn-sponsor {
    background: #bf3989;
    color: #ffffff !important;
    border: 1px solid #9e2d6f;
}

/* ── Warning / spinner ─────────────────────────────────────────── */
[data-testid="stAlert"] p { color: #ffffff !important; }
[data-testid="stSpinner"] p { color: #fbbf24 !important; }

/* ── Text inputs ───────────────────────────────────────────────── */
[data-testid="stTextInput"] input {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(251,191,36,0.3) !important;
    color: #f1f5f9 !important;
    border-radius: 8px !important;
}
</style>
"""

_GITHUB_URL = "https://github.com/gituserc1140/Emotion-to-Image-Generator"
_SPONSOR_URL = "https://github.com/sponsors/gituserc1140"
_SDXL_MODEL = "stability-ai/sdxl:7762fd07cf82c948538e41f63f77d685e02b063e37e496e96eefd46c929f9bdc"


def generate_image(replicate_token: str, emotion: str) -> str:
    client = replicate.Client(api_token=replicate_token)
    output = client.run(
        _SDXL_MODEL,
        input={
            "prompt": (
                f"An artistic, vibrant, and uplifting illustration representing the emotion of '{emotion}'. "
                "Evocative, colourful, painterly style."
            ),
            "width": 1024,
            "height": 1024,
        },
    )
    # output is a list of image URLs
    return output[0]


def main():
    st.set_page_config(
        page_title="Emotion to Image Generator",
        page_icon="🎨",
        layout="centered",
    )
    st.markdown(_CSS, unsafe_allow_html=True)

    # ── Hero header ────────────────────────────────────────────────
    st.markdown(
        """
        <div class="hero">
            <h1>🎨 Emotion to Image Generator</h1>
            <p>Enter your emotion and instantly receive a unique AI-generated image.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Sidebar ────────────────────────────────────────────────────
    st.sidebar.header("Settings")
    replicate_token_input = st.sidebar.text_input(
        "Replicate API Token",
        type="password",
        help="Enter your Replicate API token. Get one at https://replicate.com/account/api-tokens",
    )

    st.sidebar.markdown(
        f"""
        <div class="gh-buttons">
            <a class="gh-btn gh-btn-github" href="{_GITHUB_URL}" target="_blank">
                ⭐ View on GitHub
            </a>
            <a class="gh-btn gh-btn-sponsor" href="{_SPONSOR_URL}" target="_blank">
                💖 Sponsor on GitHub
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    replicate_token = replicate_token_input.strip()
    if not replicate_token:
        st.warning("Please enter your Replicate API token in the sidebar to continue.")
        st.stop()

    # ── Inputs ─────────────────────────────────────────────────────
    emotion = st.text_input(
        "How are you feeling?",
        placeholder="e.g. happy, anxious, excited, melancholy…",
    )

    if st.button("✨ Generate"):
        if not emotion.strip():
            st.warning("Please enter an emotion first.")
            st.stop()

        try:
            with st.spinner("Painting your image… 🎨"):
                image_url = generate_image(replicate_token, emotion.strip())

            st.markdown('<div class="section-label">🖼️ Your Image</div>', unsafe_allow_html=True)
            st.image(image_url, caption=f'Emotion: {emotion.strip().capitalize()}', use_container_width=True)

        except Exception as exc:
            err_msg = str(exc)
            # Redact the token from any error message before displaying
            if replicate_token:
                err_msg = err_msg.replace(replicate_token, "***")
            st.markdown(
                f'<div class="error-card">⚠️ Something went wrong: {err_msg}</div>',
                unsafe_allow_html=True,
            )


if __name__ == "__main__":
    main()

