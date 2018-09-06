import metadatacreator.dataset


def test_dataset():
    my_dataset = metadatacreator.dataset.Dataset()

    d = my_dataset.dataset
    assert d["dataFormat"] == "lst"
