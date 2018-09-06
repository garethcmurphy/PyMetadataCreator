import metadatacreator.orig


def test_dataset():
    my_dataset = metadatacreator.orig.Orig()
    d = my_dataset.orig
    assert d["size"] == 20
