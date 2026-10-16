# api/index.py — Vercel ASGI entrypoint for paypal-charger
# Vercel's @vercel/python runtime detects `app` (ASGI) and serves it.
import os
import sys

# Make repo root importable so `import main` / `import paypal_engine` resolve
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from main import app  # noqa: F401  (FastAPI instance)
