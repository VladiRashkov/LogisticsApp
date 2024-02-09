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

    hubs_time = {
        'SYD-MEL': 10, 'SYD-ADL': 15, 'SYD-ASP': 31, 'SYD-BRI': 10, 'SYD-DAR': 45, 'SYD-PER': 46, 
        'MEL-SYD': 10, 'MEL-ADL': 8, 'MEL-ASP': 25, 'MEL-BRI': 20, 'MEL-DAR': 43, 'MEL-PER': 40, 
        'ADL-SYD': 15, 'ADL-MEL': 8, 'ADL-ASP': 17, 'ADL-BRI': 22, 'ADL-DAR': 34, 'ADL-PER': 32, 
        'ASP-SYD': 31, 'ASP-MEL': 25, 'ASP-ADL': 17, 'ASP-BRI': 34, 'ASP-DAR': 17, 'ASP-PER': 28, 
        'BRI-SYD': 10, 'BRI-MEL': 20, 'BRI-ADL': 22, 'BRI-ASP': 34, 'BRI-DAR': 39, 'BRI-PER': 49, 
        'DAR-SYD': 45, 'DAR-MEL': 43, 'DAR-ADL': 34, 'DAR-ASP': 17, 'DAR-BRI': 20, 'DAR-PER': 46, 
        'PER-SYD': 46, 'PER-MEL': 40, 'PER-ADL': 32, 'PER-ASP': 28, 'PER-BRI': 49, 'PER-DAR': 46
    }
                    
    average_velocity = 87

    locations = ['Sydney', 'SYD', 'Melbourne','MEL', 'Adelaide', 'ADL', 'Alice Springs', 'ASP', 'Bristbane', 'BRI', 'Darwin', 'DAR', 'Perth', 'PER']

    routes_schedule_east1 = ['Alice Springs-Adelaide', 'Adelaide-Melbourne', 'Melbourne-Sydney', 'Sydney-Bristbane', 'Bristbane-Alice Springs']
    routes_schedule_east2 = ['Adelaide-Melbourne', 'Melbourne-Sydney', 'Sydney-Bristbane', 'Bristbane-Alice Springs', 'Alice Springs-Adelaide']
    routes_schedule_east3 = ['Melbourne-Sydney', 'Sydney-Bristbane', 'Bristbane-Alice Springs', 'Alice Springs-Adelaide', 'Adelaide-Melbourne']
    routes_schedule_east4 = ['Sydney-Bristbane', 'Bristbane-Alice Springs', 'Alice Springs-Adelaide', 'Adelaide-Melbourne', 'Melbourne-Sydney']
    routes_schedule_east5 = ['Bristbane-Alice Springs', 'Alice Springs-Adelaide', 'Adelaide-Melbourne', 'Melbourne-Sydney', 'Sydney-Bristbane']
    routes_schedule_east6 = ['Alice Springs-Darwin', 'Darwin-Perth', 'Perth-Alice Springs']
    routes_schedule_east7 = ['Darwin-Perth', 'Perth-Alice Springs', 'Alice Springs-Darwin']
    routes_schedule_east8 = ['Perth-Alice Springs', 'Alice Springs-Darwin', 'Darwin-Perth']

    def date_generator():
        start_date = datetime.today()
        current = start_date.strftime('%d/%m %A @ %H:%M')
        modified_start_hour = start_date.replace(hour=6)
        current = modified_start_hour.strftime('%d/%m %A @ %H:%M')
        modified_start_minute = modified_start_hour.replace(minute=00)
        current = modified_start_minute.strftime('%d/%m %A @ %H:%M')
        return current
    
    schedule_lst1 = []
    start_schedule = date_generator()
    for r in range(len(routes_schedule_east1)):
        hub = routes_schedule_east1[r].split('-')
        point = ''
        point += hub[0] + ' ' + start_schedule
        schedule_lst1.append(point)
        schedule_lst1.append('->')
        time = ''

    # print(*schedule_lst1[:-1])


    
