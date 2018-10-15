import metadatacreator.orig


def test_dataset():
    my_dataset = metadatacreator.orig.Orig()
    d = my_dataset.size
    assert d == 20
