#!/usr/bin/env python3

from jinja2 import Template

"""
Take the data from the csv files in ../csv and turn them into an HTML webpage
"""

def chart_data_montreal(montreal):
    """
    Generate info to be used in the HTML page chart
    """
    rgb_color = [
        '198,40,40',
        '173,20,87',
        '106,27,154',
        '69,39,160',
        '40,53,147',
        '21,101,192',
        '2,119,189',
        '0,131,143',
        '0,105,92',
        '46,125,50',
        '85,139,47',
        '158,157,36',
        '158,157,36',
        '249,168,37',
        '255,143,0',
        '239,108,0',
        '216,67,21',
        '78,52,46',
        '100,30,22',
        '120,40,31',
        '81,46,95',
        '74,35,90',
        '21,67,96',
        '27,79,114',
        '14,98,81',
        '11,83,69',
        '20,90,50',
        '24,106,59',
        '125,102,8',
        '126,81,9',
        '120,66,18',
        '110,44,0',
        '123,125,125'
    ]

    chart_data = {'dates': [], 'borough': {}}
    for borough, date, total_case in montreal:
        # Add date to dates
        if date not in chart_data['dates']:
            chart_data['dates'].append(date)

        if borough != 'Territory to be confirmed':
            # Add borough data for this date
            if borough not in chart_data['borough']:
                chart_data['borough'][borough] = {'label': borough, 'data': [], 'color': rgb_color.pop(0)}

            if total_case == '?':
                total_case = chart_data['borough'][borough]['data'][-1]

            chart_data['borough'][borough]['data'].append(total_case)

    return chart_data


def chart_data_regions(regions):
    """
    Generate info to be used in the HTML page chart
    """
    rgb_color = [
        '198,40,40',
        '173,20,87',
        '106,27,154',
        '69,39,160',
        '40,53,147',
        '21,101,192',
        '2,119,189',
        '0,131,143',
        '0,105,92',
        '46,125,50',
        '85,139,47',
        '158,157,36',
        '158,157,36',
        '249,168,37',
        '255,143,0',
        '239,108,0',
        '216,67,21',
        '78,52,46'
    ]

    chart_data = {'dates': [], 'regions': {}}
    for region, date, new_case, total_case in regions:
        # Add date to dates
        if date not in chart_data['dates']:
            chart_data['dates'].append(date)

        # Add region data for this date
        if region not in chart_data['regions']:
            chart_data['regions'][region] = {'label': region, 'data': [], 'color': rgb_color.pop(0)}

        chart_data['regions'][region]['data'].append(total_case)

    return chart_data


def chart_data_total(total):
    """
    Generate info to be used in the HTML page chart
    """

    chart_data = {'dates': [], 'deaths': [], 'recoveries': [], 'total_cases': [], 'hospitalisations': [], 'icu': []}
    for date, total_cases, deaths, recoveries, hosp, icu in total:

        # Use last day recoveries number if we don't have data for today
        if recoveries == '?':
            recoveries = chart_data['recoveries'][-1]

        if hosp == '?':
            hosp = chart_data['hospitalisations'][-1]

        if icu == '?':
            icu = chart_data['icu'][-1]

        chart_data['dates'].append(date)
        chart_data['total_cases'].append(total_cases)
        chart_data['deaths'].append(deaths)
        chart_data['recoveries'].append(recoveries)
        chart_data['hospitalisations'].append(hosp)
        chart_data['icu'].append(icu)

    return chart_data


def main():
    # Get regions data
    with open('../csv/region.csv') as f:
        regions = [x.strip().split(',') for x in f.readlines()]

    # Get total data
    with open('../csv/total.csv') as f:
        total = [x.strip().split(',') for x in f.readlines()]

    # Get total data
    with open('../csv/montreal.csv') as f:
        montreal = [x.strip().split(',') for x in f.readlines()]

    # Remove headers
    regions.pop(0)
    total.pop(0)
    montreal.pop(0)

    # Generate HTML with jinja2
    html_template = Template(open('template.html').read())
    rendered = html_template.render(
        datasets_region = chart_data_regions(regions),
        datasets_total = chart_data_total(total),
        datasets_montreal = chart_data_montreal(montreal)
    )

    with open('../data.html', 'w') as f:
        f.write(rendered)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
