import pickle

with open('./web_size.pickle', 'rb') as handle:
    sites = pickle.load(handle)

with open('./web_size_new.pickle', 'rb') as handle:
    sites_new = pickle.load(handle)

sum = 0
empty_sites = 0
print(sites[0])
print(sites_new[0])

for index in range(0, len(sites_new)):
    sum += sites_new[index]['size']

total_size = round(sum / 1024, 2)
print(f"total size is: {total_size} Gb")

avg_size = round(total_size / len(sites_new), 2)
print(f"avg site size is: {avg_size} Gb")

for index in range(0, len(sites_new)):
    if sites[index]['size'] != sites_new[index]['size']:
        difference = sites_new[index]['size'] - sites[index]['size']
        change = round(difference / (sites_new[index]['size'] / 100), 2)
        if change > 0:
            print(f"{sites_new[index]['domain']} changed by +{change} %")
        else:
            print(f"{sites_new[index]['domain']} changed by {change} %")

for index in range(0, len(sites_new)):
    if sites_new[index]['size'] == 0:
        empty_sites += 1
print(f"there are {empty_sites} empty sites")

for index in range(0, len(sites_new)):
    if sites_new[index]['size'] > 1024 and sites_new[index]['size'] != 0:
        print(
            f"{sites_new[index]['domain']} is: {round(sites_new[index]['size']/1024,2)} Gb"
        )
    if sites_new[index]['size'] < 1024 and sites_new[index]['size'] != 0:
        print(
            f"{sites_new[index]['domain']} is: {sites_new[index]['size']} Mb")