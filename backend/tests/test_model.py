import pickle
from time import time
from pathlib import Path

import pandas
from pandas import DataFrame
from sklearn.metrics import accuracy_score

from machine_learning.helper import analyze_url


def load_model():
    output_path = Path("machine_learning/model.pkl")
    return pickle.loads(output_path.read_bytes())


def create_dataset():
    dataset = pandas.read_csv("machine_learning/dataset.csv")
    data = {
        "URLLength": [],
        "DomainLength": [],
        "IsDomainIP": [],
        "TLDLength": [],
        "NoOfSubDomain": [],
        "HasObfuscation": [],
        "NoOfObfuscatedChar": [],
        "ObfuscationRatio": [],
        "NoOfLettersInURL": [],
        "LetterRatioInURL": [],
        "NoOfDegitsInURL": [],
        "DegitRatioInURL": [],
        "NoOfEqualsInURL": [],
        "NoOfQMarkInURL": [],
        "NoOfAmpersandInURL": [],
        "NoOfOtherSpecialCharsInURL": [],
        "SpacialCharRatioInURL": [],
        "IsHTTPS": [],
        "label": [],
    }

    for value in dataset[["URL", "label"]].values:
        url = value[0]
        result = analyze_url(url)

        for k, v in result.items():
            data[k].extend(v)

        data["label"].append(value[1])

    return DataFrame(data=data, columns=list(data.keys()))


def test_loading_model_duration():
    start = time()
    _ = load_model()
    end = time()

    # 30 seconds
    assert end - start < 30


def test_creating_dataset_duration():
    start = time()
    _ = create_dataset()
    end = time()

    # 30 seconds
    assert end - start < 30


def test_model_accuracy_score():
    model = load_model()
    dataset = create_dataset()
    X = dataset.drop(columns=["label"])
    y = dataset["label"]

    assert accuracy_score(y, model.predict(X)) > 0.7


def test_model_size():
    size = Path("machine_learning/model.pkl").stat().st_size

    # 50MB
    assert size < 50_000_000
