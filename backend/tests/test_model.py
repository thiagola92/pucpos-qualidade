from time import time

import pandas
from pandas import DataFrame
from sklearn.metrics import accuracy_score

from machine_learning.helper import analyze_url
from utils import get_model_path, get_model, get_csv


def create_dataset():
    dataset = pandas.read_csv(get_csv())
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
    _ = get_model()
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
    model = get_model()
    dataset = create_dataset()
    X = dataset.drop(columns=["label"])
    y = dataset["label"]

    assert accuracy_score(y, model.predict(X)) > 0.7


def test_model_size():
    size = get_model_path().stat().st_size

    # 50MB
    assert size < 50_000_000
