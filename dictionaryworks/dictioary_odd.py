arr=[10,20,30,40,2,3,7,8,9]

even_sqares={num:num**2 for num in arr if num%2==0}

print(even_sqares)

odd_cubes={num:num**3 for num in arr if num%2!=0}

print(odd_cubes)