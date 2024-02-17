# for route needed - Elena

class Location:
    locations_distance = {
        'Sydney-Melbourne': 877, 'Sydney-Adelaide': 1376, 'Sydney-AliceSprings': 2762, 'Sydney-Bristbane': 909, 'Sydney-Darwin': 3935, 'Sydney-Perth': 4016,
            'Melbourne-Sydney': 877, 'Melbourne-Adelaide': 725, 'Melbourne-AliceSprings': 2255, 'Melbourne-Bristbane': 1765, 'Melbourne-Darwin': 3752, 'Melbourne-Perth': 3509,
            'Adelaide-Sydney': 1376, 'Adelaide-Melbourne': 725, 'Adelaide-AliceSprings': 1530, 'Adelaide-Bristbane': 1927, 'Adelaide-Darwin': 3027, 'Adelaide-Perth': 2785,
            'AliceSprings-Sydney': 2762, 'AliceSprings-Melbourne': 2255, 'AliceSprings-Adelaide': 1530, 'AliceSprings-Bristbane': 2993, 'AliceSprings-Darwin': 1497, 'AliceSprings-Perth': 2481,
            'Bristbane-Sydney': 909, 'Bristbane-Melbourne': 1765, 'Bristbane-Adelaide': 1927, 'Bristbane-AliceSprings': 2993, 'Bristbane-Darwin': 3426, 'Bristbane-Perth': 4311,
            'Darwin-Sydney': 3935, 'Darwin-Melbourne': 3752, 'Darwin-Adelaide': 3027, 'Darwin-AliceSprings': 1497, 'Darwin-Bristbane': 1765, 'Darwin-Perth': 4025,
            'Perth-Sydney': 4016, 'Perth-Melbourne': 3509, 'Perth-Adelaide': 2785, 'Perth-AliceSprings': 2481, 'Perth-Bristbane': 4311, 'Perth-Darwin': 4025
    }

    locations_time = {
        'Sydney-Melbourne': 10, 'Sydney-Adelaide': 15, 'Sydney-AliceSprings': 31, 'Sydney-Bristbane': 10, 'Sydney-Darwin': 45, 'Sydney-Perth': 46, 
        'Melbourne-Sydney': 10, 'Melbourne-Adelaide': 8, 'Melbourne-AliceSprings': 25, 'Melbourne-Bristbane': 20, 'Melbourne-Darwin': 43, 'Melbourne-Perth': 40, 
        'Adelaide-Sydney': 15, 'Adelaide-Melbourne': 8, 'Adelaide-AliceSprings': 17, 'Adelaide-Bristbane': 22, 'Adelaide-Darwin': 34, 'Adelaide-Perth': 32, 
        'AliceSprings-Sydney': 31, 'AliceSprings-Melbourne': 25, 'AliceSprings-Adelaide': 17, 'AliceSprings-Bristbane': 34, 'AliceSprings-Darwin': 17, 'AliceSprings-Perth': 28, 
        'Bristbane-Sydney': 10, 'Bristbane-Melbourne': 20, 'Bristbane-Adelaide': 22, 'Bristbane-AliceSprings': 34, 'Bristbane-Darwin': 39, 'Bristbane-Perth': 49, 
        'Darwin-Sydney': 45, 'Darwin-Melbourne': 43, 'Darwin-Adelaide': 34, 'Darwin-AliceSprings': 17, 'Darwin-Bristbane': 20, 'Darwin-Perth': 46, 
        'Perth-Sydney': 46, 'Perth-Melbourne': 40, 'Perth-Adelaide': 32, 'Perth-AliceSprings': 28, 'Perth-Bristbane': 49, 'Perth-Darwin': 46
    }
    
    locations = ['Adelaide', 'Melbourne', 'Sydney', 'Bristbane', 'AliceSprings', 'Darwin', 'Perth']