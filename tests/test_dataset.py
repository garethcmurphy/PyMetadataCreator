from ..metadatacreator import dataset


def test_dataset():
    my_dataset = dataset.Dataset()
    d = my_dataset.dataset
    assert d["dataFormat"] == "lst"
