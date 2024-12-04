years_path="C:\\Users\\SHIBIL mv\\Desktop\\Pythonworks\\data_sets\\years.txt"

century_path="C:\\Users\\SHIBIL mv\\Desktop\\Pythonworks\\data_sets\\century_year.txt"

lear_year_path="C:\\Users\\SHIBIL mv\\Desktop\\Pythonworks\\data_sets\\leap_year.txt"

f_read=open(years_path,"r")

f_century=open(century_path,"w")

f_leapyear=open(lear_year_path,"w")


for year in f_read:

    year=int(year)

    if year%100==0:

        f_century.write(str(year)+"\n")

    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:

        f_leapyear.write(str(year)+"\n")

f_read.close()

f_century.close()

    
f_leapyear.close()
