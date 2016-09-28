with open("programmers_blues.txt", "r") as myfile:
    txt = myfile.read().replace(".", "").replace("(", "").replace(")", "").replace(",", "").replace("!", "").replace("\n", " ")

counts = {}
txt = str.lower(txt)
#print txt

txt2 = txt.split()
#print txt2

for word in txt2:
    counts[word] = counts.get(word, 0) + 1

for word, count in counts.items():
    print "%s: %d" % (word, count)

new_list = counts.items()

# for word, count in counts.iteritems():
#     temp = [word, count]
#     new_list.append(temp)

def getKey(item):
    return item[1]

stuff = sorted(new_list, key=getKey, reverse=True)[:10]

print "TOP TEN WORD LIST"
for word, count in stuff:
    print "%s appears %d times" % (word, count)

# phonebook_dict = {
#     "Alice": "703-493-1834",
#     "Bob": "857-384-1234",
#     "Elizabeth": "484-584-2923"
# }
#
# print phonebook_dict["Elizabeth"]
# phonebook_dict["Kareem"] = "938-489-1234"
# del phonebook_dict["Alice"]
# phonebook_dict["Bob"] = "968-345-2345"
# print phonebook_dict
#
# ramit = {
#     "name": "Ramit",
#     "email": "ramit@gmail.com",
#     "interests": ["movies", "tennis"],
#     "friends": [
#         {
#             "name": "Jasmine",
#             "email": "jasmine@yahoo.com",
#             "interests": ["photography", "tennis"]
#         },
#         {
#             "name": "Jan",
#             "email": "jan@hotmail.com",
#             "interests": ["movies", "tv"]
#         }
#     ]
# }
#
# print ramit["email"]
# print ramit["interests"]
# print ramit["friends"][0]["email"]
# print ramit["friends"][1]["interests"][1]
