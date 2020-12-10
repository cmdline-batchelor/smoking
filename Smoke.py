wed = {
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

thurs = {
    '08:15': 1, 
    '08:40': 1, 
    '09:20': 1
}

wed_vals = wed.values()
thurs_vals = thurs.values()

def add(lst):
    total = 0 
    for i in lst:
        total += i
    return total 
#----------------------------
z = lambda x, y : print(x, y)

#cant use for loop in this way to do 
# what the 2 functions below do
# doesn't work 

days = ['wed', 'thurs']

for i in days:
    z("i:", add("i"_vals))

# works 
#z('wed:', add(wed_vals))
#z('thurs:', add(thurs_vals))
