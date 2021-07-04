import json
import requests


def api_call(company_domain, page=None):
    headers = {'Accept': 'application/json'}
    payload = company_domain
    search_endpoint = 'https://api.dehashed.com/search?query="{}"'.format(payload)
    company = requests.get(search_endpoint, headers=headers,  auth=("PatDiNizio@protonmail.com,eecnnwj2sp067kceijhf3fv6y6ns7xxq ")) #email,api_key
    company = json.loads(company.text)
    entries = company["entries"]
    total = company["total"]
    if int(total) > 0:
        with open(company_domain+".csv", "w") as fh:
            # to write heading of all entry keys to the csv
            csv_heading = ""
            for each_field in entries[0]:
                csv_heading += each_field+","
            csv_heading.rstrip(",")
            fh.write(csv_heading+"\n")
            # to write each entry to the csv
            for each_entry in entries:
                csv_entry_value = ""
                for each_key in each_entry:
                    csv_entry_value += each_entry[each_key]+","
                csv_entry_value.rstrip(",")
                fh.write(csv_entry_value+"\n")
        return {entries, total}
    else:
        return {"error": "no entry found"}

company_domain = input("matthey.com")
print(api_call(company_domain))
