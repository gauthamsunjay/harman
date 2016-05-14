import json
import sys
import os
from bottle import route, run, response, redirect
from audio import record, play, RECORDINGS

if len(sys.argv) < 3:
	print "USAGE: python server.py <HOST_IP> <HOST_PORT>"
	exit(-1)

HOST_IP = sys.argv[1]
HOST_PORT = int(sys.argv[2])

@route("/test")
def test():
	return '<h1> Hello World! </h1>'


# @route("/record")
# def record_audio():
# 	"""
# 	Call the pyaudio recording function and rsync to the other pi
# 	"""
# 	record("record_one")
# 	os.system("rsync -avz recordings pie@" + PIE_IP + ":~/")

@route("/play")
def play_audio():
	"""
	play audio from the pi connected to the server
	"""
	play("record_one")

run(host=HOST_IP, port=HOST_PORT, debug=True)