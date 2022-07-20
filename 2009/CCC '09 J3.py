Ottawa = int(input())

Victoria = int(Ottawa-300)
Edmonton = int(Ottawa-200)
Winnipeg = int(Ottawa-100)
Toronto = int(Ottawa)
Halifax = int(Ottawa+100)
StJohn = int(Ottawa+130)

times = {"Victoria":Victoria,"Edmonton":Edmonton,"Winnipeg":Winnipeg,"Toronto":Toronto,"Halifax":Halifax,"St. John's":StJohn}


for place in times:
    if times[place]<0:
        times[place] = times[place]+2400
    if times[place] > 2359:
        times[place]  = times[place]-2400

print(str(Ottawa)+ " in Ottawa")

for key in times:
    print(str(times[key])+ " in " + key)
