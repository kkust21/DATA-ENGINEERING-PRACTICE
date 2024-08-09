wc_team = ["India","Bangladesh","Austria","USA"]
wc_win=[2,1,2,4]
for team,win in zip(wc_team,wc_win):
    print("team",team,"win",win)
teams= ":".join(wc_team) # changes list into string
print("teams", teams)
print(type(wc_team),wc_team)
wc_team.append("France")
print(type(wc_team),wc_team)
wc_team[2]="finland"
print(wc_team)
wc_team.insert(1,"London")
print(wc_team)
wc_team.sort()
print("sorted",wc_team)
wc_team.extend(["UAE","Greece"])
print(wc_team)
print(wc_team.pop())# removes last element
print(wc_team.remove("Bangladesh"))# can remove from specific index
print("lenght of list",len(wc_team))
print("last team",wc_team[-1])
print("print 3rd element",wc_team[2])
lis1 =["rohit","sachin","virat","hardik"]
lis2=["warner","Pat","starc","stonic"]
squrd=[lis1,lis2]
print(squrd)
print(squrd[0][2])
print(squrd[1][1])
print(squrd[1][-4])




