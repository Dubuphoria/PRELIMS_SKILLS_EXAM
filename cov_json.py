import json # importing json
import csv # importing csv

# opens the json file for READING
with open('covid_cases.json','r') as json_file:
    covid_json = json.load(json_file)

# Creating a separate csv for the parsed covid_cases.json

# opens the parsed file for WRITING
# needed to retrieve "dateRep" "countriesAndTerritories" "cases" "deaths"
with open('parsed_covid_cases.csv', 'w') as covid_write:
    file = csv.writer(covid_write)
    file.writerow(["dateRep","countriesAndTerritories","cases","deaths"]) # initializes the titles of the first row

    for parsing in covid_json['records']:
        file.writerow([parsing['dateRep'],parsing['countriesAndTerritories'],parsing['cases'],parsing['deaths']])


# opens the csv file for CHECKING
# with open('parsed_covid_cases.csv','r') as csv_file:
    # covid_csv = csv.loads(csv_file)


# print(covid_json) for checking of json if it reads
