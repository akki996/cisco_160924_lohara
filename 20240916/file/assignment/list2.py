
names_list = input("Enter student nams (seprated by spaces): ").split()
#convert the list to a set to remove any duplicate  names..
names_set = set(names_list)
#convert the set to frozen set
names_fset = frozenset(names_set)
#create a dictionary
names_dict = {name:len(name) for name in names_fset}
print(f'Original list: {names_list}')
print(f'Set (no duplicates): {names_set}')
print(f'Frozen set: {names_fset}')
print(f'Dictionary of name lengths: {names_dict}')
import json
with open('qn02_data.json','w') as names_db:
    json.dump(names_dict, names_db)
print("Dictionary written to JSON file...")
with open('qn02_data.json','r') as names_db:
    names_dict2=json.load(names_db)
    print(f"Reading from JSON file...\n{names_dict2}")