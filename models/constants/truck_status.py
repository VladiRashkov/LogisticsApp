class TruckStatus:
    FREE = 'Free'
    BUSY = 'Busy'

    @classmethod
    def from_string(cls, truck_status_string):
        if truck_status_string not in [cls.FREE, cls.BUSY]:
            raise ValueError('invalid truck status')
        
        return truck_status_string