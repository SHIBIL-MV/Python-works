orders=["tea","coffee","tea","coffee","gheeroast","plainroast","porotta","tea"]

summery_dictinory={}

for item in orders:

    if item in summery_dictinory:

        summery_dictinory[item]+=1

    else:

        summery_dictinory[item]=1

print(summery_dictinory)