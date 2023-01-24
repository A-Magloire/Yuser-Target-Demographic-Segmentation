import csv

#open empty results file to write to; w
result_csv = open("results.csv", "w")
writer = csv.writer(result_csv)

#init empty array
bounced = []
#init empty array
total = []
#init results array
result = []

#open file of entries that should be removed; r
with open("Follower Outreach - Twitter - All Artist Followers.csv", "r") as bfile:
    #iterate through total bounced entries
    bouncedReader = csv.DictReader(bfile)
    for brow in bouncedReader:
        bounced.append(brow["Profile"])


#open file that contains total entries; r
with open("../../Follower-bio-scraping/output_data/degen-results - degen-results.csv","r") as tfile:
    #iterate through total entries
    totalReader = csv.DictReader(tfile)
    for trow in totalReader:
        total.append(trow["profileUrl"])

#check similarities, append differences to new array, write contents of new array to result csv
for i in total:
    if i not in bounced:
        result.append(i)
#remove null values
for i in result:
    if i == 'null':
        result.remove(i)

#write results to result csv
for i in result:
    writer.writerow(i.split())




print(f"total length:   {len(total)}")
print(f"bounced length: {len(bounced)}")
print(f"result length:  {len(result)}")
print(f"differece = {len(total) - len(bounced)}")

