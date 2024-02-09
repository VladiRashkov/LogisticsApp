from datetime import datetime, timedelta

# S = v * t; S(km); v(km/h); t(h); average_v = 87 km/h; t = S / v

class Schedule:
    hubs_distance = {
        'SYD-MEL': 877, 'SYD-ADL': 1376, 'SYD-ASP': 2762, 'SYD-BRI': 909, 'SYD-DAR': 3935, 'SYD-PER': 4016,
            'MEL-SYD': 877, 'MEL-ADL': 725, 'MEL-ASP': 2255, 'MEL-BRI': 1765, 'MEL-DAR': 3752, 'MEL-PER': 3509,
            'ADL-SYD': 1376, 'ADL-MEL': 725, 'ADL-ASP': 1530, 'ADL-BRI': 1927, 'ADL-DAR': 3027, 'ADL-PER': 2785,
            'ASP-SYD': 2762, 'ASP-MEL': 2255, 'ASP-ADL': 1530, 'ASP-BRI': 2993, 'ASP-DAR': 1497, 'ASP-PER': 2481,
            'BRI-SYD': 909, 'BRI-MEL': 1765, 'BRI-ADL': 1927, 'BRI-ASP': 2993, 'BRI-DAR': 3426, 'BRI-PER': 4311,
            'DAR-SYD': 3935, 'DAR-MEL': 3752, 'DAR-ADL': 3027, 'DAR-ASP': 1497, 'DAR-BRI': 1765, 'DAR-PER': 4025,
            'PER-SYD': 4016, 'PER-MEL': 3509, 'PER-ADL': 2785, 'PER-ASP': 2481, 'PER-BRI': 4311, 'PER-DAR': 4025
    }
                    
    average_velocity = 87

    locations = ['SYD', 'MEL', 'ADL', 'ASP', 'BRI', 'DAR', 'PER']

    routes_schedule_east1 = ['ASP-ADL', 'ADL-MEL', 'MEL-SYD', 'SYD-BRI', 'BRI-ASP']
    routes_schedule_east2 = ['ADL-MEL', 'MEL-SYD', 'SYD-BRI', 'BRI-ASP', 'ASP-ADL']
    routes_schedule_east3 = ['MEL-SYD', 'SYD-BRI', 'BRI-ASP', 'ASP-ADL', 'ADL-MEL']
    routes_schedule_east4 = ['SYD-BRI', 'BRI-ASP', 'ASP-ADL', 'ADL-MEL', 'MEL-SYD']
    routes_schedule_east5 = ['BRI-ASP', 'ASP-ADL', 'ADL-MEL', 'MEL-SYD', 'SYD-BRI']
    routes_schedule_east6 = ['ASP-DAR', 'DAR-PER', 'PER-ASP']
    routes_schedule_east7 = ['DAR-PER', 'PER-ASP', 'ASP-DAR']
    routes_schedule_east8 = ['PER-ASP', 'ASP-DAR', 'DAR-PER']

    travel_hours = 'hubs_distance' // average_velocity

    # calculate_distance = 0
    # for p in routes_schedule_east:
    #     for point, distance in hubs.items():
    #         hubs_point = point
    #         if p == hubs_point:
    #            dist = distance
    #            calculate_distance += dist
    #            break
    #         continue
    # print(calculate_distance)


