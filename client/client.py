import requests
import json
import sys
import time

if __name__ == '__main__':
	service_url = sys.argv[1]
	print(service_url)
	while True:
		print("1.Print diseases\n2.Something else\n3.Something else\n")
		option = sys.stdin.readline().strip('\n')
		if option == "1":
			print("From:")
			source = sys.stdin.readline().strip('\n')
			print("De printat:")
			de_printat = sys.stdin.readline().strip('\n')

			print("------", de_printat)
			request_url = service_url + "/search/" + str(de_printat)
			r = requests.get(request_url)
			print(r.status_code, r.reason)
			response = json.loads(r.text)
			
			print(response)

		else:
			print("Optiunea nu este valida")
