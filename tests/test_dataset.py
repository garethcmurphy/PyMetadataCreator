import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from metadatacreator import dataset


def test_dataset():
    my_dataset = dataset.Dataset()

    d = my_dataset
    assert d.dataFormat == "lst"
