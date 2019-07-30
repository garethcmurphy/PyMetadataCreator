"""instrument unit tests"""
from metadatacreator.instrumentfactory import InstrumentFactory


def test_instrument():
    """test instrument"""
    fac = InstrumentFactory()
    sonde = fac.factory("sonde")
    abbrev = sonde.abbreviation
    assert abbrev == "SONDE"


def test_nmx():
    """test nmx"""
    fac = InstrumentFactory()
    inst = fac.factory("nmx")
    abbreviation = inst.abbreviation
    assert abbreviation == "NMX"


def test_mg():
    """test mg"""
    fac = InstrumentFactory()
    inst = fac.factory("multigrid")
    abbreviation = inst.abbreviation
    assert abbreviation == "MG"


def test_mb():
    """test mb"""
    fac = InstrumentFactory()
    inst = fac.factory("multiblade")
    abbreviation = inst.abbreviation
    assert abbreviation == "MB"
