import metadatacreator.instrument


def test_instrument():
    fac = metadatacreator.instrument.Instrument()
    sonde = fac.factory("sonde")
    d = sonde.abbreviation
    assert d == "SONDE"


def test_nmx():
    fac = metadatacreator.instrument.Instrument()
    inst = fac.factory("nmx")
    d = inst.abbreviation
    assert d == "NMX"


def test_mg():
    fac = metadatacreator.instrument.Instrument()
    inst = fac.factory("multigrid")
    d = inst.abbreviation
    assert d == "MG"


def test_mb():
    fac = metadatacreator.instrument.Instrument()
    inst = fac.factory("multiblade")
    d = inst.abbreviation
    assert d == "MB"
