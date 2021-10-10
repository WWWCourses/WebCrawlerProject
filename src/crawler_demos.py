import requests
import os
import re

# get script path
SCRIPT_FOLDER = os.path.dirname(os.path.realpath(__file__))

def get_filename(url):
	rx = re.compile(r"^https?://(.+?)(?:/|$)")
	m = rx.search(url)
	if m:
		filename = m.group(1)
		return filename


def	save_to_file(content, filename):
	with open(SCRIPT_FOLDER+'/data/'+filename,"w") as f:
		f.write(content)

def get_request_without_SSL(url):
	r = requests.get(url,verify=False)
	r.encoding="utf-8"
	filename = get_filename(url)+'.html'

	save_to_file(r.text,filename)


def make_post_request(url, login_data):
	r = requests.post(url, data=login_data)
	filename = get_filename(url)+'.html'

	# get response status
	# print(r.status_code)
	if r.status_code=='200':
		r.encoding="utf-8"
		save_to_file(r.text,filename)

# url="https://passport.abv.bg/app/profiles/login"
# url="https://www.abv.bg"
url = "https://www.autokelly.bg"

login_data = {
	"username":"test2testtest2test",
	"password":"test1234"
}

get_request_without_SSL(url)



