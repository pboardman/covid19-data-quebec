#!/usr/bin/env python3

from jinja2 import Template

"""
Take the data from the csv files in ../csv and turn them into an HTML webpage
"""


def main():
    # Get regions data
    with open('../csv/region.csv') as f:
        regions = [x.strip().split(',') for x in  f.readlines()]

    # Get total data
    with open('../csv/total.csv') as f:
        total = [x.strip().split(',') for x in  f.readlines()]

    # Remove headers
    regions.pop(0)
    total.pop(0)

    # Generate HTML with jinja2
    html_template = Template(open('template.html').read())
    rendered = html_template.render(
        regions = regions,
        total = total,
    )

    with open('../html/all.html', 'w') as f:
        f.write(rendered)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
