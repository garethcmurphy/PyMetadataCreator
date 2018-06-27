from ..metadatacreator import PyMetadataCreator


def test_dataset():
    my_dataset = PyMetadataCreator.PyMetadataCreator()
    d = my_dataset.orig
    assert d["size"] == 20