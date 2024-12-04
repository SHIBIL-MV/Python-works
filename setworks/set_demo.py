 

st1={1,2,3}

st2={1,2,3,4,5,}

print(st1.issubset(st2))

print(st2.issuperset(st1))


st1={1,2,3,10,20}
st2={1,2,3,4,5,}

#10,20,4,5

syymetric_difference=st1.symmetric_difference(st2)

print(syymetric_difference)