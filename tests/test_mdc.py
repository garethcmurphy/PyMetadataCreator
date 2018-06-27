from ..metadatacreator import PyMetadataCreator


def test_dataset():
    my_dataset = PyMetadataCreator.PyMetadataCreator()
    d = my_dataset.mydir
    assert d == "./data"
