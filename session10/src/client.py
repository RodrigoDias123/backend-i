import os
import requests
from fastapi import HTTPException


OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "smollm:135m-base-v0.2-q2_K")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434")
OLLAMA_URL = f"{OLLAMA_BASE_URL.rstrip('/')}/api/generate"
OLLAMA_CONNECT_TIMEOUT = float(os.getenv("OLLAMA_CONNECT_TIMEOUT", "5"))
OLLAMA_READ_TIMEOUT = float(os.getenv("OLLAMA_READ_TIMEOUT", "180"))
OLLAMA_INPUT_MAX_CHARS = int(os.getenv("OLLAMA_INPUT_MAX_CHARS", "3000"))
OLLAMA_NUM_PREDICT = int(os.getenv("OLLAMA_NUM_PREDICT", "160"))



def summarize_with_ollama(text: str) -> str:
    safe_text = text[:OLLAMA_INPUT_MAX_CHARS]
    prompt = (
        "Resuma a seguinte meeting em portugues claro, em ate 5 linhas, "
        "destacando objetivo, decisoes e proximos passos:\n\n"
        f"{safe_text}"
    )

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {"num_predict": OLLAMA_NUM_PREDICT, "temperature": 0.2},
            },
            timeout=(OLLAMA_CONNECT_TIMEOUT, OLLAMA_READ_TIMEOUT),
        )
        response.raise_for_status()
    except requests.Timeout as exc:
        raise HTTPException(
            status_code=504,
            detail=(
                "Timeout ao gerar resumo no Ollama. "
                f"Modelo={OLLAMA_MODEL}, url={OLLAMA_URL}, "
                f"read_timeout={OLLAMA_READ_TIMEOUT}s."
            ),
        ) from exc
    except requests.HTTPError as exc:
        status = exc.response.status_code if exc.response is not None else 502
        body = ""
        if exc.response is not None:
            body = exc.response.text.strip()
            if len(body) > 300:
                body = body[:300] + "..."
        raise HTTPException(
            status_code=502,
            detail=(
                "Ollama retornou erro HTTP ao gerar resumo. "
                f"status={status}, model={OLLAMA_MODEL}, body={body or 'vazio'}"
            ),
        ) from exc
    except requests.RequestException as exc:
        raise HTTPException(
            status_code=502,
            detail=(
                "Falha de comunicacao com Ollama para gerar resumo. "
                f"url={OLLAMA_URL}, model={OLLAMA_MODEL}. "
                "Verifique se o servico ollama esta em execucao no docker compose."
            ),
        ) from exc

    chunks = []
    try:
        payload = response.json()
    except ValueError as exc:
        raise HTTPException(
            status_code=502,
            detail="Ollama retornou JSON invalido na geracao do resumo.",
        ) from exc

    if "response" in payload:
        chunks.append(payload["response"])

    summary = "".join(chunks).strip()
    if not summary:
        raise HTTPException(
            status_code=502,
            detail="Ollama retornou resposta vazia para o resumo.",
        )

    return summary
