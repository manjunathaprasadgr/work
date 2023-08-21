# costomer={
#     "name":"sede bro",
#     "age":"23",
#     "phone":"123456"
# }
# print(costomer["name"])


# phone=input("phone: ")
# digit_mapping={
#     "1":"one",
#     "2":"two",
#     "3":"three",
#     "4":"four",
#     "5":"five",
#     "6":"six",
#     "name":"sede"
# }
# output=""
# for ch in phone:
#      output += digit_mapping.get(ch, "!")+" "
# print(output)
# print(f'name: {digit_mapping.get("name")}')




name=input("name: ")
words=name.split(' ')
name_secret={
    "mani":"sahana💕mani😎",
    "monish":"monish💕suman😎",
    "jayanth":"jayanth jayanthi😎",
    "sachin":"sachin💕shreya😋",
    "kaif":"mia kalifff😎",
    "sudin":"sule sudin😎",
    "chinmay":"boli chinmay😎"
}
output=""
for word in words:
    output += name_secret.get(word, word)+", "
print(output)





