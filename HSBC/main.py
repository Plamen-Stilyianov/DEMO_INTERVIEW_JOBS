def run():
    company = {}
    for c in COMPANIES:
        if len(company) > 0:
            if c["Name"] in company:
                if company[c['Name']][0] < c["Price"]:
                    company.update({c['Name']: [c["Price"], c["Date"]]})
            else:
                company[c["Name"]] = [c["Price"], c["Date"]]
        else:
            company[c["Name"]] = [c["Price"], c["Date"]]

    return company


COMPANIES = [{"Date": "15/09/2082", "Name": "Airbus", "Price": 14.1},
             {"Date": "15/09/2082", "Name": "BNP", "Price": 59.1},
             {"Date": "16/09/2082", "Name": "Airbus", "Price": 20.1},
             ]

if __name__ == '__main__':
    companies = run()
    [print(row) for row in companies.items()]
