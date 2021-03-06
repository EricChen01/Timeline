'''
Timeline - An AS3 CPPS emulator, written by dote, in python. Extensively using Twisted modules and is event driven.
Constants that are used during runtime. These are supposed to not change :P
'''

TIMELINE_LOGGER = 'Timeline'

PACKET_TYPE = 'xt'
PACKET_DELIMITER = '%'

AVAILABLE_XML_PACKET_TYPES = ['sys']

LOGIN_SERVER = 'LS'
WORLD_SERVER = 'WS'

LOGIN_SERVER_ALLOWED = ['w1']

AS3_PROTOCOL, AS2_PROTOCOL, CROSS_PROTOCOL = 'AS3p', 'AS2p', 'AS3p+AS2p'

# 47 -> all lang except ru, 111 -> all lang
LANGUAGE = {'en': 1, 'pt': 2, 'fr': 4, 'es': 8, 'de': 32, 'ru': 64}
EMOTES = [1, 2, 3, 33, 4, 5, 6, 7, 8, 9, 10, 11, 13, 18, 29, 24, 26, 17, 16, 28, 30, 12, 31, 32, 33, 34, 35, 36]

MULTIPLAYER_GAMES = {}
NON_BLACK_HOLE_GAMES = [900, 909, 956, 950, 963, 121]

RAINBOW_QUEST_ITEMS = [6158, 4809, 1560, 3159]

DIGGABLES = [118, 469, 412, 184, 774, 122, 498, 374, 1159, 326, 5080, 3028, 232, 112, 105, 111, 1082, 366, 1056, 790, 4039, 14523, 11343, 4154, 4082, 4199, 6219, 3205, 1196, 3003, 3183, 5100,11456, 12076, 15149, 9061, 4990, 4261, 4370, 4883, 24083, 1160, 1304, 9094, 4420] # blame arthur
GOLD_DIGGABLES = [6209, 5386, 5385, 5384, 4994, 4993, 3187, 3186, 3185, 2139, 2138, 2137, 2136, 1735, 1734, 5434, 5382]

DIGGABLE_FURN = [507, 305, 502, 150, 616, 369, 340, 506, 149, 313, 370, 504]
GOLD_DIGGABLE_FURN = [2130, 2131, 2129, 2132]

GOLD_RUSH_DIGGABLES = range(51) + range(100, 106)
PROBS = [70] + [50 for _ in range(50)] + [1 for _ in range(6)]

FIRE_STARTER_DECK = [3, 18, 216, 222, 229, 303, 304, 314, 319]

SERVER_ONLY_STAMP_GROUP = [6]

AVATARS = [0, 29]
