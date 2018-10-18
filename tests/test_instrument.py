import metadatacreator.instrumentfactory


def test_instrument():
    fac = metadatacreator.instrumentfactory.InstrumentFactory()
    sonde = fac.factory("sonde")
    d = sonde.abbreviation
    assert d == "SONDE"


def test_nmx():
    fac = metadatacreator.instrumentfactory.InstrumentFactory()
    inst = fac.factory("nmx")
    d = inst.abbreviation
    assert d == "NMX"


def test_mg():
    fac = metadatacreator.instrumentfactory.InstrumentFactory()
    inst = fac.factory("multigrid")
    d = inst.abbreviation
    assert d == "MG"


def test_mb():
    fac = metadatacreator.instrumentfactory.InstrumentFactory()
    inst = fac.factory("multiblade")
    d = inst.abbreviation
    assert d == "MB"
