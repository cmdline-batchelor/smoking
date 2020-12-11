days = [
    { "day_name": 'wed',
      "smoked_at": {
        '15:30': 1,
        '16:30': 1,
        '16:50': 2,
        '17:30': 1,
        '18:30': 1,
        '20:20': 1,
        '21:30': 1,
        '22:30': 1,
        '25:00': 5
        }
    },
    { "day_name": 'thurs',
      "smoked_at": {
        '08:15': 1,
        '08:40': 1,
        '09:20': 1,
        '10:00': 1,
        '11:20': 1,
        '11:38': 1, 
        '12:10': 1,
        '13:00': 1,
        '14:26': 1,
        '15:40': 1, 
        '17:08': 1,
        '18:10': 1,
        '19:30': 1,
        '20:20': 1,
        '22:00': 1,
        '23:00': 1,
        '25:00': 2
        }
    }
]

total = 0 
for i in days:
    day = (i["day_name"])
    smokes = i["smoked_at"].values()
    smokes_per_day = sum(smokes)
    print(day, smokes_per_day)
    total += smokes_per_day
    
print('total:', total)
