from requests import get
from win10toast import ToastNotifier
import time
import argparse

toaster = ToastNotifier()
url_pool = []
parser = argparse.ArgumentParser()

parser.add_argument('--check',help='Start Checking')
parser.add_argument('--interval',help='Set intervals',type=int)
args = vars(parser.parse_args())

url_pool.append(args['check'])


while True:
	try:

		response = get(url_pool[0])
		response.raise_for_status()
	except Exception as err:
		print('Error occured :(')
	else:
		print('Success :)')
		toaster.show_toast("Notification","your website is available")
		break
	time.sleep(args['interval'])