rating_alice=[]
rating_bob=[]
point=[0, 0]

for i in range (3):
     rating_a=int(input("enter rating for Alice"))
     rating_alice.append(rating_a)

for i in range (3):
    rating_b=int(input("enter rating for Bob"))
    rating_bob.append(rating_b)



print(rating_alice, rating_bob)


for i in range (len(rating_alice)):
    if(rating_alice[i]>rating_bob[i]):
        point[0]+=1


for i in range (len(rating_bob)):
    if(rating_bob[i]>rating_alice[i]):
        point[1]+=1

for i in range (len(rating_alice)):
    if(rating_alice[i]==rating_bob[i]):
        pass
print(point)