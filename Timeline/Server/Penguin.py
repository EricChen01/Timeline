'''
Timeline - An AS3 CPPS emulator, written by dote, in python. Extensively using Twisted modules and is event driven.
Penguin is a extension of LineReceiver, protocol. Implements the base of Client Object
'''
from Timeline.Server.Constants import TIMELINE_LOGGER, PACKET_TYPE, PACKET_DELIMITER
from Timeline.Utils.Events import Event

from twisted.protocols.basic import LineReceiver
from twisted.internet import threads
from twisted.internet.defer import Deferred

from repr import Repr
from collections import deque
import logging

class Penguin(LineReceiver):

	delimiter = chr(0)

	def __init__(self, engine):
		self.factory = self.engine = engine
		self.logger = logging.getLogger(TIMELINE_LOGGER)

		self.buildPenguin()

	def buildPenguin(self):
		self.penguin = PenguinObject() # POvalue should be penguin name. Sooner.
		self.penguin.name = None
		self.penguin.id = None

		self.penguin.room = None

	def getPortableName(self):
		if self["name"] == None and self["id"] == None:
			return self.client

		if self["name"] != None:
			return self["name"]

		if self["id"] != None:
			return self["id"]

		return self["name"]

	# Easy access to penguin properties
	def __getitem__(self, prop):
		return getattr(self.penguin, prop)

	def __setitem__(self, prop, val):
		self.penguin[prop] = val

	def lineReceived(self, line):
		me = self.getPortableName()
		self.engine.log("debug", "[RECV]", me, line)

	def send(self, *args):
		buffers = list(args)
		if len(buffers) < 1:
			return

		if len(buffers) == 1:
			self.engine.log("debug", "[SEND]", buffers[0])
			return self.sendLine(buffers[0])

		server_internal_id = "-1"
		if self.room != None:
			server_internal_id = self.room.internal_id

		buffering = ['', PACKET_TYPE]
		buffering.append(buffers[0])
		buffering.append(server_internal_id)

		buffering += packets[1:]
		buffering.append('')

		buffering = PACKET_DELIMITER.join(list(map(str, buffering)))
		self.engine.log("debug", "[SEND]", buffering)
		return self.sendLine(buffering)


	def disconnect(self):
		self.transport.loseConnection()
		return

	def connectionLost(self, reason):
		self.engine.log("info", self.getPortableName(), "Disconnected!")

		self.engine.disconnect(self)

	def makeConnection(self, transport):
		self.transport = self.client = transport
		self.connectionMade = True

		self.engine.log("info", "New client connection:", self.client)

class PenguinObject(dict):

	def __init__(self, value=None):
		dict.__init__(self)
		self.POvalue = value

	def __repr__(self):
		values = list()

		for i, j in dict.iteritems(self):
			values.append("{0}={1}".format(i, j))

		values = ", ".join(values)
		return "<{0}: {1}>".format(self.__class__.__name__, values)

	def __getitem__(self, key):
		try:
			value = (dict.__getitem__(self, key))
		except:
			value = PenguinObject()
			dict.__setitem__(self, key, value)
		finally:
			return value

	def __setitem__(self, key, value):
		dict.__setitem__(self, key, PenguinObject(value))

	def __setattr__(self, attr, value):
		if attr != "POvalue":
			value = PenguinObject(value)

		dict.__setitem__(self, attr, value)
		object.__setattr__(self, attr, value)

	def __getattr__(self, attr):
		try:
			value = (dict.__getitem__(self, key)).POvalue
		except:
			value = PenguinObject()
			dict.__setitem__(self, key, value)
		finally:
			return value