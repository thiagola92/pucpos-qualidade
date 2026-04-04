import pickle
from pathlib import Path

import requests


def get_model(version: int = 1):
    assert version in [1, 2], "Only version 1 and 2 supported"

    path = Path(f"./bin/model_v{version}.pkl")

    if path.exists():
        return pickle.loads(path.read_bytes())

    print(f"Downloading model_v{version}...")

    response = requests.get(
        f"https://github.com/thiagola92/pucpos-qualidade/releases/download/1.0.0/model_v{version}.pkl"
    )

    assert response.status_code == 200, "Failed to download model from Github"

    path.write_bytes(response.content)

    return pickle.loads(path.read_bytes())
