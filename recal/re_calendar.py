#! /usr/bin/env python3
"""
Recal
Did you know your old March 1986 calendar can be re-used to July 2017? Never wonder again!
"""

import calendar
from datetime import datetime
import itertools


today = datetime.today()


def get_similar_months(year=today.year, month=today.month, years=None):
	if not years:
		years = list(range(2018+1, 1100, -1))
	# be extra careful with December and January: (in case 3 month display is used)
	if month == 12:
		years.remove(year)
		for y, m in get_similar_months(year+1, 2, years):
			yield y-1, 12
	elif month == 1:
		years.remove(year-1)
		for y, m in get_similar_months(year, month+1, years):
			yield y, m-1
	else:
		years.remove(year)
		actual = calendar.monthrange(year, month)
		if month == 2: months = [2]
		else: months = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
		for (m, y) in itertools.product(months, years):
			if calendar.monthrange(y, m) == actual: yield y, m


def get_similar_years(year, **kwargs):
	for y, _ in get_similar_months(year, 2, **kwargs):
		yield y
