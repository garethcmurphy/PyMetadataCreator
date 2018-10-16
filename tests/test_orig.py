import metadatacreator.origdatablocks


def test_dataset():
    my_dataset = metadatacreator.origdatablocks.OrigDatablocks()
    d = my_dataset.size
    assert d == 20
