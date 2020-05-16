import requests
import hashlib
import sys

def request_data(query_chars):
  url = f'https://api.pwnedpasswords.com/range/{query_chars}'
  response = requests.get(url)
  if response.status_code != 200:
    raise RuntimeError(f'Error fetching data: status {response.status_code}, please check the api and try again')
  return response

def get_leaks_count(hashes, chars_to_check):
  lines = hashes.text.splitlines()
  hashes = (line.split(':') for line in lines) # not actually a comprehension, but a generator expression
  for h, count in hashes:
    if h == chars_to_check:
      return count
  return 0

def check_pw(password):
  pw_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  query_chars, chars_to_check = pw_hash[:5], pw_hash[5:]
  response = request_data(query_chars)
  return get_leaks_count(response, chars_to_check)
  
def main(args):
  for password in args:
    count = check_pw(password)
    if count:
      print(f'{password} was found {count} times')
    else:
      print(f'{password} has not been found')

main(sys.argv[1:])

