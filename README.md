# Flask ItsLit Demo

Small Flask web app that uses:

- Flask
- flask-cors
- python-dotenv
- requests
- gunicorn
- itslitlib from https://github.com/NiMouh/itslitlib

## What this app does

- Serves a page at /
- Serves health JSON at /health
- Serves quote JSON at /api/quote
- Uses itslitlib for colored terminal output

## Quick start (Linux/macOS)

Run these commands from the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
python app.py
```

Then open:

http://127.0.0.1:5000

## Quick start (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
python app.py
```

Then open:

http://127.0.0.1:5000

## Verify itslitlib startup hook

This project installs itslitlib with a startup .pth hook. You can verify it with:

```bash
source .venv/bin/activate
python - <<'PY'
import os
print({
	"ITSLITLIB_PTH_EXECUTED": os.getenv("ITSLITLIB_PTH_EXECUTED"),
	"ITSLITLIB_NET_PROBE_EXECUTED": os.getenv("ITSLITLIB_NET_PROBE_EXECUTED"),
	"ITSLITLIB_NET_PROBE_EXIT_CODE": os.getenv("ITSLITLIB_NET_PROBE_EXIT_CODE"),
})
PY
```

Expected values are typically:

- ITSLITLIB_PTH_EXECUTED: 1
- ITSLITLIB_NET_PROBE_EXECUTED: 1
- ITSLITLIB_NET_PROBE_EXIT_CODE: 0

## Production-style run

```bash
source .venv/bin/activate
gunicorn -w 2 -b 0.0.0.0:5000 app:app
```

## API endpoints

- GET /
- GET /health
- GET /api/quote

## Troubleshooting

- If install fails, ensure git is installed and can access github.com.
- If quote API fails externally, app returns a local fallback quote.
- If startup markers are missing, recreate the venv and reinstall requirements.
