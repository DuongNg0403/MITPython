dict_studinfo = {"Ann":"A","Kyle":"C","Mike":"B+","James":"A++"}

print(dict_studinfo["Mike"])
dict_studinfo["Sylvia"] = "A#" #add an entry
print("Mike" in dict_studinfo) #test
del (dict_studinfo["Ann"]) #delete 
dict_studinfo.keys() #returns ["Kyle","Mike","James","Sylvia"]
dict_studinfo.values()#returns ["A","C","B+","A++","A#"]
