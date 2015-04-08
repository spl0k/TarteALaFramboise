#! env python
# coding: utf-8

import socket
import feedparser

socket.setdefaulttimeout(10)

def gmail_unread_count(login, password):
	res = feedparser.parse("https://{}:{}@mail.google.com/gmail/feed/atom".format(login, password))
	return int(res['feed']['fullcount'])

def get_login_info(args):
	if not args:
		raise RuntimeError('No login info provided')
	if len(args) > 1:
		return tuple(args[0:2])
	args = args[0].split(':')
	if len(args) < 2:
		raise RuntimeError('Invalid login info')
	return tuple(args[0:2])

if __name__ == '__main__':
	import sys
	if len(sys.argv) < 2:
		print >>sys.stderr, 'Usage: {0} <login> <pass>\n -or- {0} <login>:<pass>'.format(sys.argv[0])
		sys.exit(1)

	try:
		login_info = get_login_info(sys.argv[1:])
	except RuntimeError, e:
		print >>sys.stderr, str(e)
		sys.exit(2)

	print gmail_unread_count(login_info[0], login_info[1])

