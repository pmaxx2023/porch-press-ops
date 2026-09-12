#!/usr/bin/env bash
# PP-ELEANOR-AU-001A — one-click local FIXTURE preview (unpublished).
# Opens http://127.0.0.1:8765/ — no Pages, no live storefront.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
PORT="${PORT:-8765}"
URL="http://127.0.0.1:${PORT}/"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required." >&2
  exit 1
fi

# Free the port if a prior preview is still bound (best-effort).
if command -v lsof >/dev/null 2>&1; then
  PIDS="$(lsof -tiTCP:"$PORT" -sTCP:LISTEN 2>/dev/null || true)"
  if [ -n "${PIDS:-}" ]; then
    echo "Port $PORT busy — stopping prior listener(s): $PIDS"
    # shellcheck disable=SC2086
    kill $PIDS 2>/dev/null || true
    sleep 0.4
  fi
fi

echo "FIXTURE preview — NOT live game content"
echo "Serving $ROOT"
echo "Hub:    $URL"
echo "Portal: ${URL}portal/"
echo "Stop with Ctrl-C"
echo

open_browser() {
  if command -v open >/dev/null 2>&1; then
    open "$URL" >/dev/null 2>&1 || true
  elif command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$URL" >/dev/null 2>&1 || true
  elif command -v wslview >/dev/null 2>&1; then
    wslview "$URL" >/dev/null 2>&1 || true
  fi
}

# Open after the server is listening.
(
  for _ in 1 2 3 4 5 6 7 8 9 10; do
    if python3 -c "import socket; s=socket.socket(); s.settimeout(0.2); s.connect(('127.0.0.1', int('$PORT'))); s.close()" 2>/dev/null; then
      open_browser
      exit 0
    fi
    sleep 0.2
  done
) &

exec python3 -m http.server "$PORT"
