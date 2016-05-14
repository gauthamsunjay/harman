import json
import sys
from bottle import route, run, response, redirect
from audio import record

if len(sys.argv) < 3:
	print "USAGE: python server.py <HOST_IP> <HOST_PORT>"
	exit(-1)

HOST_IP = sys.argv[1]
HOST_PORT = int(sys.argv[2])


@route("/test")
def test():
	return '<h1> Hello World! </h1>'


@route("/record")
def record_audio():
	"""
	Call the pyaudio recording function
	"""
	record("message_record")


run(host=HOST_IP, port=HOST_PORT, debug=True)