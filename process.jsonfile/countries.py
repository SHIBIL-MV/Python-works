from json import load

f=open("C:\\Users\\SHIBIL mv\\Desktop\\Pythonworks\\data_sets\\countries.json",encoding="utf-8")

data=load(f)
#all_country_names=[country.get("name") for country in data ]

#print(all_country_names)

all_regions=[country.get("region") for country in data ]

print(set(all_regions))


