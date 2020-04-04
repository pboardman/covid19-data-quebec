#!/usr/bin/env python3

import os
import re
import requests
import sqlite3
import html
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

csv_region = '../csv/region.csv'
csv_total = '../csv/total.csv'

def get_data_date(soup):
    """Return the date of the data on the Quebec governement website in format YYYY-MM-DD"""

    # Date string, will return something like 'April 4'
    date_str = soup.find_all('div', {'class': 'ce-bodytext'})[1].find_all('p')[2].decode_contents().replace(u'\xa0', u' ').split(',')[1].strip().replace('on ', '')

    return datetime.strptime(date_str, '%B %d').replace(year=datetime.now().year).strftime('%Y-%m-%d')


def is_new_data(soup):
    with open(csv_total, 'r') as f:
        if get_data_date(soup) in f.read():
            return False

        return True


def update_total_csv(soup):
     # Header of the table where total case and deaths are written
    table_header = soup.find_all('div', {'class': 'ce-bodytext'})[1].find('p').decode_contents().replace(u'\xa0', u'')

    # Get total cases and deaths via regex
    nb_pattern = re.compile('\d+')
    total, _, deaths = nb_pattern.findall(table_header)

    # Get the current date of the data
    date = get_data_date(soup)

    print(f'Updating total csv with: {date},{total},{deaths},?')
    with open(csv_total, 'a') as f:
        f.write(f'{date},{total},{deaths},?\n')


def get_total_case(region, date):
    with open(csv_region, 'r') as f:
        for line in f.readlines():
            if region in line and date in line:
                return int(line.strip().split(',')[-1])


def update_region_csv(soup):
    """
    Update the region csv
    """

    # Get the current date of the data
    date = get_data_date(soup)

    regions = [
        ['Bas-Saint-Laurent', date],
        ['Saguenay-Lac-Saint-Jean', date],
        ['Capitale Nationale', date],
        ['Mauricie - Centre du Québec', date],
        ['Estrie', date],
        ['Montréal', date],
        ['Outaouais', date],
        ['Abitibi-Temiscamingue', date],
        ['Côte-Nord', date],
        ['Nord-du-Québec', date],
        ['Gaspésie-Îles-de-la-Madeleine', date],
        ['Chaudière-Appalaches', date],
        ['Laval', date],
        ['Lanaudière', date],
        ['Laurentides', date],
        ['Montérégie', date],
        ['Nunavik', date],
        ['Terres-Cries-de-la-Baie-James', date],
    ]

    # Get cases by region, it is assumed that the table stays in the same order
    cases_per_region = [x.find_all('p')[1].text.replace(u'\xa0', u'') for x in soup.find_all('div', {'class': 'ce-bodytext'})[1].find_all('tr')[2:-1]]

    # validation
    if len(cases_per_region) != 18:
        print(f'Numbers of region != 18, error!')
        exit(1)

    # Add total number of cases to regions
    for i in range(0, 18):
        regions[i].append(cases_per_region[i])

    # Compute new_case by region
    for region in regions:
        yesterday = (datetime.strptime(region[1], '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')
        region.insert(2, str(int(region[2]) - get_total_case(region[0], yesterday)))


    with open(csv_region, 'a') as f:
        for region in regions:
            print('Udpating region csv with: ' + ','.join(region))
            f.write(','.join(region) + '\n')


def main():
    ret = requests.get('https://www.quebec.ca/en/health/health-issues/a-z/2019-coronavirus/situation-coronavirus-in-quebec/')
    soup = BeautifulSoup(ret.content, 'html.parser')

    if not is_new_data(soup):
        print('No new data, exiting.')
        exit(0)

    update_total_csv(soup)
    update_region_csv(soup)





if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
