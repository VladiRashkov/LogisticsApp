# needed for route - Elena

class Status:
    OPEN = 'Open'
    SCHEDULED = 'Scheduled'
    ON_ROUTE = 'On route'
    ARRIVED = 'Arrived'
    CANCELLED = 'Cancelled'
    UNASSIGNED = 'Unassigned'
    ASSIGNED = 'Assigned'
    AVAILABLE = 'Available'
    UNAVAILABLE = 'Unavailable'
    

    order_route = (OPEN, SCHEDULED, ON_ROUTE, ARRIVED, CANCELLED)
    order_package = (UNASSIGNED, ASSIGNED)
    order_truck = (AVAILABLE, UNAVAILABLE)


    @classmethod
    def next_route_status(cls, current):
        idx = cls.order_route.index(current)
        if idx < len(cls.order_route) - 1:
            return cls.order_route[idx + 1]
        else:
            return current
