
from datetime import datetime
import sys

#from recal.re_calendar import *
from .re_calendar import *


cli_args = sys.argv[1:]
today = datetime.today()


def get_ncal_args(*args, **kwargs):
	for y, m in get_similar_months(*args, **kwargs):
		return(("-H", "{:04d}-{:02d}-{:02d}".format(y, m, today.day),
				"-d", "{:04d}-{:02d}".format(y, m)) )


def get_command_args(*args, **kwargs):
	return ' '.join([ "ncal", *get_ncal_args(*args, **kwargs), *cli_args ])
