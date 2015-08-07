out=open("data.out","w")
print("test", file=out)
out.close()

import pickle
with open("mydata.pickle","wb") as mysavedata:
    pickle.dump([1,2,"three"], mysavedata)
with open("mydata.pickle","rb") as myrestoredata:
    a_list=pickle.load(myrestoredata)
print(a_list)

"""BF_01_A"""