class RouteStatus:
    OPEN = 'Open'
    SCHEDULED = 'Scheduled'
    ON_ROUTE = 'On route'
    ARRIVED = 'Arrived'
    CANCELLED = 'Cancelled'

    order_route = (OPEN, SCHEDULED, ON_ROUTE, ARRIVED, CANCELLED)

    @classmethod
    def next_route_status(cls, current):
        idx = cls.order_route.index(current)
        if idx < len(cls.order_route) - 1:
            return cls.order_route[idx + 1]
        else:
            return current
        
class PackageStatus:
    ASSIGNED  = 'Assigned'
    UNASSIGNED = 'Unassigned'
    INPROGRESS = 'In progress'
    DELIVERED = 'Delivered'

class TruckStatus:
    FREE = 'Free'
    BUSY = 'Busy'