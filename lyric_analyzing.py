def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

#lyrics should be a list(which is dumb but well)
lyrics= ["this", "is", "the", "rythm", "of","the" ,"night", "oh", "yeah", "oh", "oh"]


'''find	the	words	that	occur	at	least	X	0mes	
• 	let	user	choose	“at	least	X	Smes”,	so	allow	as	parameter	
• 	return	a	list	of	tuples,	each	tuple	is	a	(list, int)
containing	the	list	of	words	ordered	by	their	frequency	
• 	IDEA:	From	song	dicSonary,	find	most	frequent	word.	Delete	
most	common	word.	Repeat.	It	works	because	you	are	
g	dicSonary.	
6.0001	LECTURE	6	 50
mutaSng	the	son'''


def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result 

print(words_often())