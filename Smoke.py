days = [
    { "day_name": "wed",
      "smoked_at": {
        '15:30': 1,
        '16:30': 1,
        '16:50': 2,
        '17:30': 1,
        '18:30': 1,
        '20:20': 1,
        '21:30': 1,
        '22:30': 1
        }
    },
    { "day_name":"thurs",
        "smoked_at": {
        '08:15': 1,
        '08:40': 1,
        '09:20': 1,
        '10:00': 1,
        '11:20': 1,       
        }
    }
]

smoke_ray = []

for i in days:
    days = i["day_name"]
    smokes = i["smoked_at"].values()
    smokes_per_day = sum(smokes)
    print(f"{days}: {smokes_per_day}")
    smoke_ray.append(smokes_per_day)

def all_smokes():
    total = 0 
    for i in smoke_ray: 
        total += i 
    nl = '\n'
    print(f"{nl}{'Total:'} {total}")
	
all_smokes()
