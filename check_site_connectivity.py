from requests import get
import time
import argparse
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
		break
	time.sleep(args['interval'])