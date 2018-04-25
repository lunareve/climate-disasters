# take data returned from request and process it
# basic: make a dict of states and count number of disasters in each state
# extra: count by each county

US_STATES = {
        'AK': '02',
        'AL': '01',
        'AR': '05',
        'AS': 'American Samoa',
        'AZ': '04',
        'CA': '06',
        'CO': '08',
        'CT': '09',
        'DC': '11',
        'DE': '10',
        'FL': '12',
        'GA': '13',
        'GU': 'Guam',
        'HI': '15',
        'IA': '19',
        'ID': '16',
        'IL': '17',
        'IN': '18',
        'KS': '20',
        'KY': '21',
        'LA': '22',
        'MA': '25',
        'MD': '24',
        'ME': '23',
        'MI': '26',
        'MN': '27',
        'MO': '29',
        'MP': 'Northern Mariana Islands',
        'MS': '28',
        'MT': '30',
        'NA': 'National',
        'NC': '37',
        'ND': '38',
        'NE': '31',
        'NH': '33',
        'NJ': '34',
        'NM': '35',
        'NV': '32',
        'NY': '36',
        'OH': '39',
        'OK': '40',
        'OR': '41',
        'PA': '42',
        'PR': '72',
        'RI': '44',
        'SC': '45',
        'SD': '46',
        'TN': '47',
        'TX': '48',
        'UT': '49',
        'VA': '51',
        'VI': 'Virgin Islands',
        'VT': '50',
        'WA': '53',
        'WI': '55',
        'WV': '54',
        'WY': '56'
}


def count_disasters(response):
    states = {}
    total_records = len(response['DisasterDeclarationsSummaries'])

    for record in response['DisasterDeclarationsSummaries']:
        state_abbr = record['state']
        # set key as html id
        state = US_STATES[state_abbr]
        states[state] = states.get(state, 0) + 1

    results = {}
    results['total'] = total_records
    results['counts'] = states

    return results
