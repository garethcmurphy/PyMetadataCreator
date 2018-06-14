class Instrument:

    def factory(instrument_type=None):
        if instrument_type == "sonde":
            return Sonde()


class Sonde(Instrument):

    def __init__(self):
        self.owner = "Ramsey Al Jebali"
        self.ownerEmail = "ramsey.aljebali@esss.se"
        self.orcidOfOwner = "0000-0000-0000-0000"
        self.contactEmail = "ramsey.aljebali@esss.se"
        self.principal_investigator = "Ramsey Al Jebali"

