names = [
    ["Andi", "Kolb"],
    ["Peter", "Meier"],
    ["Andreas", "Walter"],
    ["Sandra", "Schnaider"]
]
asdfsfda asdfsfda asdfsfda asdfsfdaasdfsfda asdfsfdaasdfsfda asdfsfdaasdfsfda asdfsfdaasdfsfda asdfsfdaasdfsfda asdfsfdaasdfsfda asdfsfda

names.sort()

def sort_nachname(n):
    ''' Parameter [vorname, nachname]'''
    return n[1]

# nach nachnamen sortiert lambda
names.sort(key=sort_nachname, reverse=True)
print(names)