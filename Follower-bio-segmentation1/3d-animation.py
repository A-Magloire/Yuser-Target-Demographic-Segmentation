import csv
import re

#open New-results file to write results to
web3_results = open("web3-results.csv", "w")
web2_results = open("web2-results.csv", "w")

web3_writer = csv.writer(web3_results)
web2_writer = csv.writer(web2_results)
#open twitter followers csv as file tor read from
with open("/data/Follower Outreach - Twitter - Yuser Followers - Full List.csv", "r") as file:
    #iterate through file with Dictreader
    reader = csv.DictReader(file)
    for row in reader:
        data = [row["username"], row["full_name"], row["follower_count"], row["email"]]
        if "crypto" in (row["biography"]).lower() or "nft" in (row["biography"]).lower() or "decentralized" in (row["biography"]).lower() or "blockchain" in (row["biography"]).lower() or "opensea" in (row["biography"]) or "opensea" in (row["external_url"]) or "foundation" in (row["biography"]) or "foundation" in (row["external_url"]):
            web3_writer.writerow(data)
        else:
            web2_writer.writerow(data)

web3_results.close()
web2_results.close()