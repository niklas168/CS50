import sqlite3

conn = sqlite3.connect('Scouting.db')
cur=conn.cursor()

# What role is Tghe Player going to have within the Team?
age=input("Are you looking for a first Team Player(1) or a Prospect for the future (2)?\n")

if (age=="1"):
    sql="SELECT Player FROM Players WHERE Age>20 AND Min>1000 "
elif(age=="2"):
    sql="SELECT Player FROM Players WHERE Age<=20 AND Min>300 "

#What Position should the Player be in?

position=input("What Position of Player are you looking for? An Defender(1), Midfielder(2) or an Attacker(3)?\n")

#Defenders
if(position=="1"):

    sql+="AND Pos== 'DF'"
    #specific types of Defenders
    role=input("What is his specific Position going to be? Full-Back(1) or Center-back(2)?\n")
    if(role=="1"):
        if(age=="1"):
            sql+="AND crs>3 AND PasProg>5"
        else:
            sql+="AND crs>2 AND PasProg>3"
    elif(role=="2"):
        role_plus=(input("Is the Defender supposed to be involved in Build-up? Y/N?\n"))
        if(role_plus=="Y"):
            if(age==1):
                sql+="AND Tkl+Int>3.5 AND AerWon>2.5 AND PasProg>3 AND PasTotCmp>50"
            else:
                sql+="AND Tkl+Int>3 AND AerWon>2 AND PasProg>2.5 AND PasTotCmp>50"
        elif(role_plus=="N"):
            if(age=="1"):
                sql+="AND Tkl+Int>6 AND AerWon>4.5 AND Blocks>2"
            else:
                sql+="AND Tkl+Int>5 AND AerWon>3.5 AND Blocks>1"

#Midfielders
elif(position=="2"):

    sql+="AND Pos =='MF'"
    #specififc types of Midfielders
    role=input("What type of midfielder are you looking for? A Defense-Specialist(1), Box-to-Box(2), Maestro(3) or a Creator(4)?\n")
    #Defensive Specialist
    if(role=="1"):
        if(age==1):
            sql+="AND TklInt>6 AND Recov>11"
        else:
            sql+="AND TklInt>5 AND Recov>8"
    #Box-to-Box-Midfielder
    elif(role=="2"):
        if(age==1):
            sql+="AND TklInt>2 AND Carries>60 AND DriSucc>1 AND Press>18"
        else:
            sql+="AND TklInt>2 AND Carries>45 AND DriSucc>1 AND Press>18"
    #Maestro
    elif(role=="3"):
        if(age=="1"):
            sql+="AND PasTotDist>1500"
        else:
            sql+="AND PasTotDist>800"
    #Creator
    elif(role=="4"):
        if(age==1):
            sql+="AND Goals>0.1 AND Assists>0.1 AND PasProg>3 AND DriSucc>2"
        else:
            sql+="AND Assists>0.1 AND DriSucc>2"

#Attackers
elif(position=="3"):

    sql+="AND Pos Like '%FW%'"
    #specific type of attackers
    role=input("What Type of Forward do you want? A creator(1) or a finisher(2)?\n")
    if(role=="1"):
        if(age=="1"):
            sql+="AND Goals>0.1 AND Assists>0.3 AND DriSucc>2 AND GCA>0.5"
        else:
            sql+="AND Goals>0.1 AND Assists>0.2 AND DriSucc>2 AND GCA>0.5"
    elif(role=="2"):
        if(age=="1"):
            sql+="AND Goals>0.5 AND Shots>4"
        else:
            sql+="AND Goals>0.3 AND Shots>3"

print("You should check ou the following Players:")
cur.execute(sql)
erg=cur.fetchall()
for i in range (len(erg)):
    value, = erg[i]
    print(value)

cur.close()
conn.close()






