from ..metadatacreator import instrument


def test_instrument():
    my_instrument = instrument.Instrument()
    d = my_instrument.ownerEmail
    assert d == "lst"
