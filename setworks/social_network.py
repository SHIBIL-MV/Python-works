user=["rahul","kohli","rohit","rishab","sanju","pandya","siraj"]

rahul_followers=["rohit","kohli","rishab"]

sanju_followers=["sanju","rohit","kohli"]

mutual_friends=set(rahul_followers).intersection(set(sanju_followers))

print(mutual_friends)

