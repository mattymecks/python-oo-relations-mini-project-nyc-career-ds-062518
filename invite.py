

class Invite:

    _all = []

    def __init__(self, dinner_party, guest, rsvp_status = False):
        self._guest = guest
        self._dinner_party = dinner_party
        self._rsvp_status = rsvp_status
        Invite._all.append(self)

    #CLASSMETHODS

    @classmethod
    def all(cls):
        return cls._all

    #INSTANCEMETHODS

    @property
    def accepted(self):
        return self._rsvp_status

    @accepted.setter
    def accepted(self, bool):
        self._rsvp_status = bool
    #returns a boolean value (true or false) for whether the the guest accepted the invite or not


    #DECORATORS

    #decorators for _guest

    @property
    def guest(self):
       return self._guest

    @guest.setter
    def guest(self, guest):
       self._guest = guest


    #decorators for _dinner_party

    @property
    def dinner_party(self):
       return self._dinner_party

    @dinner_party.setter
    def dinner_party(self, dinner_party):
       self._dinner_party = dinner_party


    #decorators for _rsvp_status

    @property
    def rsvp_status(self):
       return self._rsvp_status

    @rsvp_status.setter
    def rsvp_status(self, rsvp_status):
       self._rsvp_status = rsvp_status
