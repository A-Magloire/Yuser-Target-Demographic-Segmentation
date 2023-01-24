import csv
import re

#open New-results file to write results to
web3_results = open("web3-results.csv", "w")
# web2_results = open("web2-results.csv", "w")

web3_writer = csv.writer(web3_results)
# web2_writer = csv.writer(web2_results)
#open twitter followers csv as file tor read from
with open("data/Follower Outreach - Twitter - Yuser Followers - Full List.csv", "r") as file:
    #iterate through file with Dictreader
    reader = csv.DictReader(file)
    for row in reader:
        data = [row["profileUrl"], row["followersCount"]]
        if "degen" in row["bio"].lower() or "investor" in row["bio"].lower() or "collector" in row["bio"].lower() or "trader" in row["bio"].lower() or "airdrop" in row["bio"].lower():
            web3_writer.writerow(data)
        # else:
        #     web2_writer.writerow(data)

web3_results.close()
# web2_results.close()