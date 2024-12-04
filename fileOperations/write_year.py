f=open("C:\\Users\\SHIBIL mv\\Desktop\\Pythonworks\\data_sets\\years.txt","w")

for years in range(1800,2025):

    f.write(str(years)+"\n")

f.close()