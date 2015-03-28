#! env python
# coding: utf-8

import requests

def theoldreader_unread_count(token):
	r = requests.get('https://theoldreader.com/reader/api/0/unread-count',
		params = { 'output': 'json' },
		headers = { 'Authorization': 'GoogleLogin auth={}'.format(token) })
	return filter(lambda d: d['id'] == 'user/-/state/com.google/reading-list', r.json['unreadcounts'])[0]['count']

if __name__ == '__main__':
	import sys
	if len(sys.argv) < 2:
		print >>sys.stderr, 'Usage: {} <token>'.format(sys.argv[0])
		sys.exit(1)

	print theoldreader_unread_count(sys.argv[1])

