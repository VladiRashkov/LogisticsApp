from datetime import datetime, timedelta

# S = v * t; S(km); v(km/h); t(h); average_v = 87 km/h; t = S / v

class Schedule:

    hubs_distance = {
        'Sydney-Melbourne': 877, 'Sydney-Adelaide': 1376, 'Sydney-Alice Springs': 2762, 'Sydney-Bristbane': 909, 'Sydney-Darwin': 3935, 'Sydney-Perth': 4016,
            'Melbourne-Sydney': 877, 'Melbourne-Adelaide': 725, 'Melbourne-Alice Springs': 2255, 'Melbourne-Bristbane': 1765, 'Melbourne-Darwin': 3752, 'Melbourne-Perth': 3509,
            'Adelaide-Sydney': 1376, 'Adelaide-Melbourne': 725, 'Adelaide-Alice Springs': 1530, 'Adelaide-Bristbane': 1927, 'Adelaide-Darwin': 3027, 'Adelaide-Perth': 2785,
            'Alice Springs-Sydney': 2762, 'Alice Springs-Melbourne': 2255, 'Alice Springs-Adelaide': 1530, 'Alice Springs-BRI': 2993, 'Alice Springs-Darwin': 1497, 'Alice Springs-Perth': 2481,
            'Bristbane-Sydney': 909, 'Bristbane-Melbourne': 1765, 'Bristbane-Adelaide': 1927, 'Bristbane-Alice Springs': 2993, 'Bristbane-Darwin': 3426, 'Bristbane-Perth': 4311,
            'Darwin-Sydney': 3935, 'Darwin-Melbourne': 3752, 'Darwin-Adelaide': 3027, 'Darwin-Alice Springs': 1497, 'Darwin-Bristbane': 1765, 'Darwin-Perth': 4025,
            'Perth-Sydney': 4016, 'Perth-Melbourne': 3509, 'Perth-Adelaide': 2785, 'Perth-Alice Springs': 2481, 'Perth-Bristbane': 4311, 'Perth-Darwin': 4025
    }

    hubs_time = {
        'Sydney-Melbourne': 10, 'Sydney-Adelaide': 15, 'Sydney-Alice Springs': 31, 'Sydney-Bristbane': 10, 'Sydney-Darwin': 45, 'Sydney-Perth': 46, 
        'Melbourne-Sydney': 10, 'Melbourne-Adelaide': 8, 'Melbourne-Alice Springs': 25, 'Melbourne-Bristbane': 20, 'Melbourne-Darwin': 43, 'Melbourne-Perth': 40, 
        'Adelaide-Sydney': 15, 'Adelaide-Melbourne': 8, 'Adelaide-Alice Springs': 17, 'Adelaide-Bristbane': 22, 'Adelaide-Darwin': 34, 'Adelaide-Perth': 32, 
        'Alice Springs-Sydney': 31, 'Alice Springs-Melbourne': 25, 'Alice Springs-Adelaide': 17, 'Alice Springs-BRI': 34, 'Alice Springs-Darwin': 17, 'Alice Springs-Perth': 28, 
        'Bristbane-Sydney': 10, 'Bristbane-Melbourne': 20, 'Bristbane-Adelaide': 22, 'Bristbane-Alice Springs': 34, 'Bristbane-Darwin': 39, 'Bristbane-Perth': 49, 
        'Darwin-Sydney': 45, 'Darwin-Melbourne': 43, 'Darwin-Adelaide': 34, 'Darwin-Alice Springs': 17, 'Darwin-Bristbane': 20, 'Darwin-Perth': 46, 
        'Perth-Sydney': 46, 'Perth-Melbourne': 40, 'Perth-Adelaide': 32, 'Perth-Alice Springs': 28, 'Perth-Bristbane': 49, 'Perth-Darwin': 46
    }
                    
    average_velocity = 87

    locations = ['Sydney', 'Melbourne', 'Adelaide', 'Alice Springs', 'Bristbane', 'Darwin', 'Perth']


    def date_generator():
        start_date = datetime.today()
        current = start_date.strftime('%d/%m %A @ %H:%M')
        modified_start_hour = start_date.replace(hour=6)
        current = modified_start_hour.strftime('%d/%m %A @ %H:%M')
        modified_start_minute = modified_start_hour.replace(minute=00)
        # current = modified_start_minute.strftime('%d/%m %A @ %H:%M')
        current = modified_start_minute
        return current.strftime('%d/%m %A @ %H:%M')
    
    def date_current_generator():
        start_date = datetime.today()
        # current_new = start_date.strftime('%d/%m %A @ %H:%M')
        modified_start_hour = start_date.replace(hour=6)
        # current_new = modified_start_hour.strftime('%d/%m %A @ %H:%M')
        modified_start_minute = modified_start_hour.replace(minute=00)
        # current_new = modified_start_minute.strftime('%d/%m %A @ %H:%M')
        current_date = modified_start_minute + timedelta(hours=10)
        return current_date.strftime('%d/%m %A @ %H:%M')
    
    current_date = date_current_generator()
    print(current_date)
    
    # schedule_lst1 = []
    start_schedule = date_generator()
    print(start_schedule)
    # for r in range(len(routes_schedule_east1)):
    #     hub = routes_schedule_east1[r].split('-')
    #     point = ''
    #     point += hub[0] + ' ' + start_schedule
    #     schedule_lst1.append(point)
    #     schedule_lst1.append('->')
    #     time = ''

    # print(*schedule_lst1[:-1])


    
