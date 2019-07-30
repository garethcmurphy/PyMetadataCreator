from metadatacreator.instrumentfactory import InstrumentFactory


def test_instrument():
    """test instrument"""
    fac = InstrumentFactory()
    sonde = fac.factory("sonde")
    d = sonde.abbreviation
    assert d == "SONDE"


def test_nmx():
    """test nmx"""
    fac = InstrumentFactory()
    inst = fac.factory("nmx")
    d = inst.abbreviation
    assert d == "NMX"


def test_mg():
    fac = InstrumentFactory()
    inst = fac.factory("multigrid")
    d = inst.abbreviation
    assert d == "MG"


def test_mb():
    fac = InstrumentFactory()
    inst = fac.factory("multiblade")
    d = inst.abbreviation
    assert d == "MB"
