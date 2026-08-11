import os
import sys
from pathlib import Path

import uvicorn

BASE_DIR = Path(__file__).resolve().parent


def load_local_env() -> None:
    env_path = BASE_DIR / ".env"
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


os.chdir(BASE_DIR)
sys.path.insert(0, str(BASE_DIR))
load_local_env()

host = os.getenv("HOST", "0.0.0.0")
port = int(os.getenv("PORT", "8000"))

uvicorn.run("server:app", host=host, port=port, proxy_headers=True)
