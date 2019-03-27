from requests import get
import time

url = 'https://explained.ai/matrix-calculus/index.html'

while True:
	try:

		response = get(url)
		response.raise_for_status()
	except Exception as err:
		print('Error occured :(')
	else:
		print('Success :)')
		break
	time.sleep(6)