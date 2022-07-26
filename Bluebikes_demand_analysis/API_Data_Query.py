import pandas as pd
import sportradar.MLB

## Part III

key = ""

client = sportradar.MLB.MLB(key)
date = []
away_team=[]
status=[]
audience=[]
l = 0
for year in range(2019,2022):
    sched = client.get_league_schedule(year, "REG")
    sched = sched.json()
    for game in sched["games"]:
        if game["home"]["name"] == "Red Sox":
            month = game["scheduled"].split("T")[0].split("-")[1]
            day = game["scheduled"].split("T")[0].split("-")[2]
            daysched = client.get_daily_schedule(year, int(month), int(day))
            daysched = daysched.json()
            for i in daysched["games"]:
                if i["home"]["name"] == "Red Sox":
                    date.append(game["scheduled"].split("T")[0])
                    away_team.append(game["away"]["name"])
                    try:
                        attendance = i["attendance"]
                        audience.append(attendance)
                        status.append(i["status"])
                    except KeyError:
                        attendance = 0
                        audience.append(attendance)
                        status.append(i["status"])
                    # l+=1

dict={'Schedule': date, "Away Team": away_team,'Attendance':audience, "Status": status }
df=pd.DataFrame(dict)
print(df)
df.to_csv('Schedule.csv') 
