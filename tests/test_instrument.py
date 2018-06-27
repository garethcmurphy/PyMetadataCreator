from ..metadatacreator import instrument


def test_instrument():
    fac = instrument.Instrument()
    sonde = fac.factory("sonde")
    d = sonde.abbreviation
    assert d == "SON"


def test_nmx():
    fac = instrument.Instrument()
    inst = fac.factory("nmx")
    d = inst.abbreviation
    assert d == "NMX"


def test_mg():
    fac = instrument.Instrument()
    inst = fac.factory("multigrid")
    d = inst.abbreviation
    assert d == "MG"


def test_mb():
    fac = instrument.Instrument()
    inst = fac.factory("multiblade")
    d = inst.abbreviation
    assert d == "MB"
