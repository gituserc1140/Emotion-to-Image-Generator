# 🎨 Emotion to Image Generator

[![GitHub Stars](https://img.shields.io/github/stars/gituserc1140/Emotion-to-Image-Generator?style=social)](https://github.com/gituserc1140/Emotion-to-Image-Generator)
[![GitHub Sponsors](https://img.shields.io/github/sponsors/gituserc1140?style=social)](https://github.com/sponsors/gituserc1140)

A Streamlit app that takes your current emotion and instantly generates:

- 💬 **A short, personalised compliment** powered by OpenAI GPT-4o mini
- 🖼️ **A unique AI-generated image** created with DALL-E 3

No configuration files or environment variables needed — just paste your OpenAI API key directly in the sidebar.

---

## Features

- **Frontend API key entry** — your key stays in your browser session, never stored server-side
- **Personalised compliments** — optionally enter your name for a more tailored message
- **DALL-E 3 images** — vivid, artistic images matched to your emotion
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

### 3. Get an OpenAI API key

Sign up or log in at [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys) and create a new secret key. Make sure your account has access to the `gpt-4o-mini` and `dall-e-3` models.

### 4. Run the app

```bash
streamlit run app.py
```

---

## How to Use

1. **Open the app** — Streamlit will launch it in your browser automatically.
2. **Enter your OpenAI API key** in the sidebar (it is treated as a password field).
3. **Type how you're feeling** in the "How are you feeling?" box (e.g. *happy*, *anxious*, *excited*).
4. Optionally **enter your name** for a more personalised compliment.
5. Click **✨ Generate** — your compliment and image will appear within seconds.

---

## Requirements

| Package | Purpose |
|---------|---------|
| `streamlit` | Web app framework |
| `openai` | GPT-4o mini (compliments) + DALL-E 3 (images) |

---

## Contributing

Pull requests are welcome! For major changes please open an issue first.

## Support

If you find this project useful, consider [sponsoring on GitHub](https://github.com/sponsors/gituserc1140) 💖
