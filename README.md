# Flask ItsLit Demo

Sample Python web app using Flask and additional libraries:

- Flask
- flask-cors
- python-dotenv
- requests
- gunicorn
- `itslitlib` from: https://github.com/NiMouh/itslitlib

## Features

- Web UI on `/`
- Health endpoint on `/health`
- Quote API endpoint on `/api/quote`
- Colored terminal logs through `itslitlib.cprint()`

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
```

## Run (Development)

```bash
python app.py
```

Open: http://127.0.0.1:5000

## Run (Production style)

```bash
gunicorn -w 2 -b 0.0.0.0:5000 app:app
```

## Publish to GitHub

```bash
git init
git add .
git commit -m "Initial Flask sample app with itslitlib"
git branch -M main
git remote add origin https://github.com/NiMouh/flask-itslit-demo.git
git push -u origin main
```
