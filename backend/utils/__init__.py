import pickle
from pathlib import Path
from zipfile import ZipFile

import requests


def get_model_path(version: int = 1):
    assert version in [1, 2], "Only version 1 and 2 supported"

    return Path(f"./bin/model_v{version}.pkl")


def get_model(version: int = 1):
    assert version in [1, 2], "Only version 1 and 2 supported"

    path = get_model_path(version)

    if path.exists():
        return pickle.loads(path.read_bytes())

    print(f"Downloading model_v{version}...")

    response = requests.get(
        f"https://github.com/thiagola92/pucpos-qualidade/releases/download/1.0.0/model_v{version}.pkl"
    )

    assert response.status_code == 200, "Failed to download model from Github"

    path.write_bytes(response.content)

    return pickle.loads(path.read_bytes())


def get_csv(version: int = 1):
    assert version in [1, 2], "Only version 1 and 2 supported"

    if version == 1:
        csv_path = Path("./machine_learning/dataset.csv")
        zip_path = Path("./machine_learning/dataset.zip")
    else:
        csv_path = Path("./machine_learning_remake/dataset.csv")
        zip_path = Path("./machine_learning_remake/dataset.zip")

    if not csv_path.exists():
        ZipFile(zip_path).extract("dataset.csv", path=csv_path.parent)

    return csv_path
