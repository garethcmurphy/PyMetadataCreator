from ..metadatacreator import orig


def test_dataset():
    my_dataset = orig.Orig()
    d = my_dataset.orig
    assert d["size"] == 20