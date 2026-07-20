# Emotion to Image Generator App

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://emotion-to-image-generator-zlwg4jpc73odhx42iucbft.streamlit.app/)
[![Sponsor me on GitHub](https://img.shields.io/badge/Sponsor%20me%20on-GitHub-EA4AAA?logo=githubsponsors&style=flat-square)](https://github.com/sponsors/gituserc1140)

A Streamlit app that takes your current emotion and instantly generates:

- **A unique AI-generated image** created with Poliinations API

No configuration files or environment variables needed — Uses an open-source API endpoint

---

## Features

- **Frontend API key entry** — your keys stay in your browser session, never stored server-side
- **Personalised compliments** — optionally enter your name for a more tailored message
- **Pollinations images** — Uses Poliinations API
- **GitHub & Sponsor buttons** — right in the sidebar
- Clean, dark gradient UI styled for a polished feel

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/gituserc1140/Emotion-to-Image-Generator.git
cd Emotion-to-Image-Generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Get a Replicate API token

Sign up or log in at [https://replicate.com/account/api-tokens](https://replicate.com/account/api-tokens) and create a new token. This is used for SDXL image generation.

### 4. Run the app

```bash
streamlit run app.py
```

---

## How to Use

1. **Open the app** — Streamlit will launch it in your browser automatically.
2. **Type how you're feeling** in the "How are you feeling?" box (e.g. *happy*, *anxious*, *excited*).
3. Optionally **enter your name** for a more personalised compliment.
4. Click **Generate** — your compliment and image will appear within seconds.

---

## Requirements

| Package | Purpose |
|---------|---------|
| `streamlit` | Web app framework |
| `pollinations.ai` | (images) |

---

## Contributing

Pull requests are welcome! For major changes please open an issue first.

## Support

If you find this project useful, consider [sponsoring on GitHub](https://github.com/sponsors/gituserc1140) 
