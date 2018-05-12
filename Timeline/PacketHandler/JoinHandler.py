from Timeline.Server.Constants import TIMELINE_LOGGER, PACKET_TYPE, PACKET_DELIMITER, LOGIN_SERVER, WORLD_SERVER, LOGIN_SERVER_ALLOWED
from Timeline.Utils.Events import PacketEventHandler

from twisted.internet import threads
from twisted.internet.defer import Deferred

from collections import deque
import logging

'''
AS2 and AS3 Compatible
'''
@PacketEventHandler.XTPacketRule('s', 'j#js', WORLD_SERVER)
@PacketEventHandler.XTPacketRule_AS2('s', 'j#js', WORLD_SERVER)
def JoinServerRule(data):
	param = data[2]

	_id = int(param[0])
	pword = str(param[1])
	lang = str(param[2])

	if lang not in ['en']:
		raise Exception("[TE601] Language {} not supported!".format(lang))


	return [[_id, pword, lang], {}]

'''
AS2 and AS3 Compatible
'''
@PacketEventHandler.XTPacketRule('s', 'j#jr', WORLD_SERVER)
@PacketEventHandler.XTPacketRule_AS2('s', 'j#jr', WORLD_SERVER)
def JoinRoomRule(data):
	param = data[2]

	room = int(param[0])
	x = y = 0
	
	try:
		x = int(param[1])
		y = int(param[2])
	except:
		pass

	return [[room, x, y], {}]
'''
AS2 Join Igloo
'''
@PacketEventHandler.XTPacketRule_AS2('s', 'j#jp', WORLD_SERVER)
def JoinPlayerRuleAS2(data):
	return [[int(data[2][0]) - 1000, 'igloo'], {}]

'''
AS3 Join Igloo
'''
@PacketEventHandler.XTPacketRule('s', 'j#jp', WORLD_SERVER)
def JoinPlayerRule(data):

	return [[int(data[2][0]), str(data[2][1])], {}]