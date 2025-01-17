
# This file was generated automatically by generate_protocols.py

from nintendo.nex import notification, rmc, common, streams

import logging
logger = logging.getLogger(__name__)


class BlacklistedPrincipal(common.Data):
	def __init__(self):
		super().__init__()
		self.principal_info = PrincipalBasicInfo()
		self.game_key = GameKey()
		self.since = None
	
	def check_required(self, settings, version):
		for field in ['since']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.principal_info = stream.extract(PrincipalBasicInfo)
		self.game_key = stream.extract(GameKey)
		self.since = stream.datetime()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.add(self.principal_info)
		stream.add(self.game_key)
		stream.datetime(self.since)
common.DataHolder.register(BlacklistedPrincipal, "BlacklistedPrincipal")


class Comment(common.Data):
	def __init__(self):
		super().__init__()
		self.unk = None
		self.text = None
		self.changed = None
	
	def check_required(self, settings, version):
		for field in ['unk', 'text', 'changed']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.unk = stream.u8()
		self.text = stream.string()
		self.changed = stream.datetime()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u8(self.unk)
		stream.string(self.text)
		stream.datetime(self.changed)
common.DataHolder.register(Comment, "Comment")


class FriendInfo(common.Data):
	def __init__(self):
		super().__init__()
		self.nna_info = NNAInfo()
		self.presence = NintendoPresenceV2()
		self.comment = Comment()
		self.befriended = None
		self.last_online = None
		self.unk = None
	
	def check_required(self, settings, version):
		for field in ['befriended', 'last_online', 'unk']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.nna_info = stream.extract(NNAInfo)
		self.presence = stream.extract(NintendoPresenceV2)
		self.comment = stream.extract(Comment)
		self.befriended = stream.datetime()
		self.last_online = stream.datetime()
		self.unk = stream.u64()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.add(self.nna_info)
		stream.add(self.presence)
		stream.add(self.comment)
		stream.datetime(self.befriended)
		stream.datetime(self.last_online)
		stream.u64(self.unk)
common.DataHolder.register(FriendInfo, "FriendInfo")


class FriendRequest(common.Data):
	def __init__(self):
		super().__init__()
		self.principal_info = PrincipalBasicInfo()
		self.message = FriendRequestMessage()
		self.sent = None
	
	def check_required(self, settings, version):
		for field in ['sent']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.principal_info = stream.extract(PrincipalBasicInfo)
		self.message = stream.extract(FriendRequestMessage)
		self.sent = stream.datetime()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.add(self.principal_info)
		stream.add(self.message)
		stream.datetime(self.sent)
common.DataHolder.register(FriendRequest, "FriendRequest")


class FriendRequestMessage(common.Data):
	def __init__(self):
		super().__init__()
		self.unk1 = None
		self.unk2 = None
		self.unk3 = None
		self.message = None
		self.unk4 = None
		self.string = None
		self.game_key = GameKey()
		self.datetime = None
		self.expires = None
	
	def check_required(self, settings, version):
		for field in ['unk1', 'unk2', 'unk3', 'message', 'unk4', 'string', 'datetime', 'expires']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.unk1 = stream.u64()
		self.unk2 = stream.u8()
		self.unk3 = stream.u8()
		self.message = stream.string()
		self.unk4 = stream.u8()
		self.string = stream.string()
		self.game_key = stream.extract(GameKey)
		self.datetime = stream.datetime()
		self.expires = stream.datetime()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.unk1)
		stream.u8(self.unk2)
		stream.u8(self.unk3)
		stream.string(self.message)
		stream.u8(self.unk4)
		stream.string(self.string)
		stream.add(self.game_key)
		stream.datetime(self.datetime)
		stream.datetime(self.expires)
common.DataHolder.register(FriendRequestMessage, "FriendRequestMessage")


class GameKey(common.Data):
	def __init__(self):
		super().__init__()
		self.title_id = 0
		self.title_version = 0
	
	def check_required(self, settings, version):
		pass
	
	def load(self, stream, version):
		self.title_id = stream.u64()
		self.title_version = stream.u16()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.title_id)
		stream.u16(self.title_version)
common.DataHolder.register(GameKey, "GameKey")


class MiiV2(common.Data):
	def __init__(self):
		super().__init__()
		self.name = None
		self.unk1 = 0
		self.unk2 = 0
		self.data = None
		self.datetime = common.DateTime(0)
	
	def check_required(self, settings, version):
		for field in ['name', 'data']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.name = stream.string()
		self.unk1 = stream.u8()
		self.unk2 = stream.u8()
		self.data = stream.buffer()
		self.datetime = stream.datetime()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.string(self.name)
		stream.u8(self.unk1)
		stream.u8(self.unk2)
		stream.buffer(self.data)
		stream.datetime(self.datetime)
common.DataHolder.register(MiiV2, "MiiV2")


class NNAInfo(common.Data):
	def __init__(self):
		super().__init__()
		self.principal_info = PrincipalBasicInfo()
		self.unk1 = 94
		self.unk2 = 11
	
	def check_required(self, settings, version):
		pass
	
	def load(self, stream, version):
		self.principal_info = stream.extract(PrincipalBasicInfo)
		self.unk1 = stream.u8()
		self.unk2 = stream.u8()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.add(self.principal_info)
		stream.u8(self.unk1)
		stream.u8(self.unk2)
common.DataHolder.register(NNAInfo, "NNAInfo")


class NintendoCreateAccountData(common.Data):
	def __init__(self):
		super().__init__()
		self.info = NNAInfo()
		self.token = None
		self.birthday = None
		self.unk = None
	
	def check_required(self, settings, version):
		for field in ['token', 'birthday', 'unk']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.info = stream.extract(NNAInfo)
		self.token = stream.string()
		self.birthday = stream.datetime()
		self.unk = stream.u64()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.add(self.info)
		stream.string(self.token)
		stream.datetime(self.birthday)
		stream.u64(self.unk)
common.DataHolder.register(NintendoCreateAccountData, "NintendoCreateAccountData")


class NintendoPresenceV2(common.Data):
	def __init__(self):
		super().__init__()
		self.flags = 0
		self.is_online = False
		self.game_key = GameKey()
		self.unk1 = 0
		self.message = ""
		self.unk2 = 0
		self.unk3 = 0
		self.game_server_id = 0
		self.unk4 = 0
		self.pid = 0
		self.gathering_id = 0
		self.application_data = b""
		self.unk5 = 3
		self.unk6 = 3
		self.unk7 = 3
	
	def check_required(self, settings, version):
		pass
	
	def load(self, stream, version):
		self.flags = stream.u32()
		self.is_online = stream.bool()
		self.game_key = stream.extract(GameKey)
		self.unk1 = stream.u8()
		self.message = stream.string()
		self.unk2 = stream.u32()
		self.unk3 = stream.u8()
		self.game_server_id = stream.u32()
		self.unk4 = stream.u32()
		self.pid = stream.u32()
		self.gathering_id = stream.u32()
		self.application_data = stream.buffer()
		self.unk5 = stream.u8()
		self.unk6 = stream.u8()
		self.unk7 = stream.u8()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u32(self.flags)
		stream.bool(self.is_online)
		stream.add(self.game_key)
		stream.u8(self.unk1)
		stream.string(self.message)
		stream.u32(self.unk2)
		stream.u8(self.unk3)
		stream.u32(self.game_server_id)
		stream.u32(self.unk4)
		stream.u32(self.pid)
		stream.u32(self.gathering_id)
		stream.buffer(self.application_data)
		stream.u8(self.unk5)
		stream.u8(self.unk6)
		stream.u8(self.unk7)
common.DataHolder.register(NintendoPresenceV2, "NintendoPresenceV2")


class PersistentNotification(common.Data):
	def __init__(self):
		super().__init__()
		self.unk1 = None
		self.unk2 = None
		self.unk3 = None
		self.unk4 = None
		self.string = None
	
	def check_required(self, settings, version):
		for field in ['unk1', 'unk2', 'unk3', 'unk4', 'string']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.unk1 = stream.u64()
		self.unk2 = stream.u32()
		self.unk3 = stream.u32()
		self.unk4 = stream.u32()
		self.string = stream.string()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.unk1)
		stream.u32(self.unk2)
		stream.u32(self.unk3)
		stream.u32(self.unk4)
		stream.string(self.string)
common.DataHolder.register(PersistentNotification, "PersistentNotification")


class PrincipalBasicInfo(common.Data):
	def __init__(self):
		super().__init__()
		self.pid = None
		self.nnid = None
		self.mii = MiiV2()
		self.unk = 2
	
	def check_required(self, settings, version):
		for field in ['pid', 'nnid']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.pid = stream.pid()
		self.nnid = stream.string()
		self.mii = stream.extract(MiiV2)
		self.unk = stream.u8()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.pid(self.pid)
		stream.string(self.nnid)
		stream.add(self.mii)
		stream.u8(self.unk)
common.DataHolder.register(PrincipalBasicInfo, "PrincipalBasicInfo")


class PrincipalPreference(common.Data):
	def __init__(self):
		super().__init__()
		self.show_online_status = None
		self.show_current_title = None
		self.block_friend_requests = None
	
	def check_required(self, settings, version):
		for field in ['show_online_status', 'show_current_title', 'block_friend_requests']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.show_online_status = stream.bool()
		self.show_current_title = stream.bool()
		self.block_friend_requests = stream.bool()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.bool(self.show_online_status)
		stream.bool(self.show_current_title)
		stream.bool(self.block_friend_requests)
common.DataHolder.register(PrincipalPreference, "PrincipalPreference")


class PrincipalRequestBlockSetting(common.Data):
	def __init__(self):
		super().__init__()
		self.unk1 = None
		self.unk2 = None
	
	def check_required(self, settings, version):
		for field in ['unk1', 'unk2']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.unk1 = stream.u32()
		self.unk2 = stream.bool()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u32(self.unk1)
		stream.bool(self.unk2)
common.DataHolder.register(PrincipalRequestBlockSetting, "PrincipalRequestBlockSetting")


class FriendsProtocolV1:
	METHOD_UPDATE_PROFILE = 1
	METHOD_UPDATE_MII = 2
	METHOD_UPDATE_MII_LIST = 3
	METHOD_UPDATE_PLAYED_GAMES = 4
	METHOD_UPDATE_PREFERENCE = 5
	METHOD_GET_FRIEND_MII = 6
	METHOD_GET_FRIEND_MII_LIST = 7
	METHOD_IS_ACTIVE_GAME = 8
	METHOD_GET_PRINCIPAL_ID_BY_LOCAL_FRIEND_CODE = 9
	METHOD_GET_FRIEND_RELATIONSHIPS = 10
	METHOD_ADD_FRIEND_BY_PRINCIPAL_ID = 11
	METHOD_ADD_FRIEND_BY_PRINCIPAL_IDS = 12
	METHOD_REMOVE_FRIEND_BY_LOCAL_FRIEND_CODE = 13
	METHOD_REMOVE_FRIEND_BY_PRINCIPAL_ID = 14
	METHOD_GET_ALL_FRIENDS = 15
	METHOD_UPDATE_BLACK_LIST = 16
	METHOD_SYNC_FRIEND = 17
	METHOD_UPDATE_PRESENCE = 18
	METHOD_UPDATE_FAVORITE_GAME_KEY = 19
	METHOD_UPDATE_COMMENT = 20
	METHOD_UPDATE_PICTURE = 21
	METHOD_GET_FRIEND_PRESENCE = 22
	METHOD_GET_FRIEND_COMMENT = 23
	METHOD_GET_FRIEND_PICTURE = 24
	METHOD_GET_FRIEND_PERSISTENT_INFO = 25
	METHOD_SEND_INVITATION = 26
	
	PROTOCOL_ID = 0x65


class FriendsProtocolV2:
	METHOD_UPDATE_AND_GET_ALL_INFORMATION = 1
	METHOD_ADD_FRIEND = 2
	METHOD_ADD_FRIEND_BY_NAME = 3
	METHOD_REMOVE_FRIEND = 4
	METHOD_ADD_FRIEND_REQUEST = 5
	METHOD_CANCEL_FRIEND_REQUEST = 6
	METHOD_ACCEPT_FRIEND_REQUEST = 7
	METHOD_DELETE_FRIEND_REQUEST = 8
	METHOD_DENY_FRIEND_REQUEST = 9
	METHOD_MARK_FRIEND_REQUESTS_AS_RECEIVED = 10
	METHOD_ADD_BLACK_LIST = 11
	METHOD_REMOVE_BLACK_LIST = 12
	METHOD_UPDATE_PRESENCE = 13
	METHOD_UPDATE_MII = 14
	METHOD_UPDATE_COMMENT = 15
	METHOD_UPDATE_PREFERENCE = 16
	METHOD_GET_BASIC_INFO = 17
	METHOD_DELETE_PERSISTENT_NOTIFICATION = 18
	METHOD_CHECK_SETTING_STATUS = 19
	METHOD_GET_REQUEST_BLOCK_SETTINGS = 20
	
	PROTOCOL_ID = 0x66


class FriendsClientV1(FriendsProtocolV1):
	def __init__(self, client):
		self.settings = client.settings
		self.client = client
	


class FriendsClientV2(FriendsProtocolV2):
	def __init__(self, client):
		self.settings = client.settings
		self.client = client
	
	async def update_and_get_all_information(self, nna_info, presence, birthday):
		logger.info("FriendsClientV2.update_and_get_all_information()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(nna_info)
		stream.add(presence)
		stream.datetime(birthday)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_UPDATE_AND_GET_ALL_INFORMATION, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		obj = rmc.RMCResponse()
		obj.principal_preference = stream.extract(PrincipalPreference)
		obj.comment = stream.extract(Comment)
		obj.friends = stream.list(FriendInfo)
		obj.sent_requests = stream.list(FriendRequest)
		obj.received_requests = stream.list(FriendRequest)
		obj.blacklist = stream.list(BlacklistedPrincipal)
		obj.unk1 = stream.bool()
		obj.notifications = stream.list(PersistentNotification)
		obj.unk2 = stream.bool()
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("FriendsClientV2.update_and_get_all_information -> done")
		return obj
	
	async def add_friend(self, pid):
		logger.info("FriendsClientV2.add_friend()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.pid(pid)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_ADD_FRIEND, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		obj = rmc.RMCResponse()
		obj.request = stream.extract(FriendRequest)
		obj.info = stream.extract(FriendInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("FriendsClientV2.add_friend -> done")
		return obj
	
	async def add_friend_by_name(self, name):
		logger.info("FriendsClientV2.add_friend_by_name()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.string(name)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_ADD_FRIEND_BY_NAME, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		obj = rmc.RMCResponse()
		obj.request = stream.extract(FriendRequest)
		obj.info = stream.extract(FriendInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("FriendsClientV2.add_friend_by_name -> done")
		return obj
	
	async def remove_friend(self, pid):
		logger.info("FriendsClientV2.remove_friend()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.pid(pid)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_REMOVE_FRIEND, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("FriendsClientV2.remove_friend -> done")
	
	async def add_friend_request(self, unk1, unk2, unk3, unk4, unk5, game_key, unk6):
		logger.info("FriendsClientV2.add_friend_request()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u32(unk1)
		stream.u8(unk2)
		stream.string(unk3)
		stream.u8(unk4)
		stream.string(unk5)
		stream.add(game_key)
		stream.datetime(unk6)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_ADD_FRIEND_REQUEST, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		obj = rmc.RMCResponse()
		obj.request = stream.extract(FriendRequest)
		obj.info = stream.extract(FriendInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("FriendsClientV2.add_friend_request -> done")
		return obj
	
	async def cancel_friend_request(self, id):
		logger.info("FriendsClientV2.cancel_friend_request()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u64(id)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_CANCEL_FRIEND_REQUEST, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("FriendsClientV2.cancel_friend_request -> done")
	
	async def accept_friend_request(self, id):
		logger.info("FriendsClientV2.accept_friend_request()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u64(id)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_ACCEPT_FRIEND_REQUEST, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		info = stream.extract(FriendInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("FriendsClientV2.accept_friend_request -> done")
		return info
	
	async def delete_friend_request(self, id):
		logger.info("FriendsClientV2.delete_friend_request()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u64(id)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_DELETE_FRIEND_REQUEST, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("FriendsClientV2.delete_friend_request -> done")
	
	async def deny_friend_request(self, id):
		logger.info("FriendsClientV2.deny_friend_request()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u64(id)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_DENY_FRIEND_REQUEST, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		blacklist = stream.extract(BlacklistedPrincipal)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("FriendsClientV2.deny_friend_request -> done")
		return blacklist
	
	async def mark_friend_requests_as_received(self, ids):
		logger.info("FriendsClientV2.mark_friend_requests_as_received()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(ids, stream.u64)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_MARK_FRIEND_REQUESTS_AS_RECEIVED, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("FriendsClientV2.mark_friend_requests_as_received -> done")
	
	async def add_black_list(self, principal):
		logger.info("FriendsClientV2.add_black_list()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(principal)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_ADD_BLACK_LIST, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		principal = stream.extract(BlacklistedPrincipal)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("FriendsClientV2.add_black_list -> done")
		return principal
	
	async def remove_black_list(self, pid):
		logger.info("FriendsClientV2.remove_black_list()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.pid(pid)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_REMOVE_BLACK_LIST, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("FriendsClientV2.remove_black_list -> done")
	
	async def update_presence(self, presence):
		logger.info("FriendsClientV2.update_presence()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(presence)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_UPDATE_PRESENCE, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("FriendsClientV2.update_presence -> done")
	
	async def update_mii(self, mii):
		logger.info("FriendsClientV2.update_mii()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(mii)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_UPDATE_MII, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		unk = stream.datetime()
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("FriendsClientV2.update_mii -> done")
		return unk
	
	async def update_comment(self, comment):
		logger.info("FriendsClientV2.update_comment()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(comment)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_UPDATE_COMMENT, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		unk = stream.datetime()
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("FriendsClientV2.update_comment -> done")
		return unk
	
	async def update_preference(self, preference):
		logger.info("FriendsClientV2.update_preference()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(preference)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_UPDATE_PREFERENCE, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("FriendsClientV2.update_preference -> done")
	
	async def get_basic_info(self, pids):
		logger.info("FriendsClientV2.get_basic_info()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(pids, stream.pid)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_BASIC_INFO, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		info = stream.list(PrincipalBasicInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("FriendsClientV2.get_basic_info -> done")
		return info
	
	async def delete_persistent_notification(self, notifications):
		logger.info("FriendsClientV2.delete_persistent_notification()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(notifications, stream.add)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_DELETE_PERSISTENT_NOTIFICATION, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("FriendsClientV2.delete_persistent_notification -> done")
	
	async def check_setting_status(self):
		logger.info("FriendsClientV2.check_setting_status()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_CHECK_SETTING_STATUS, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		unk = stream.u8()
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("FriendsClientV2.check_setting_status -> done")
		return unk
	
	async def get_request_block_settings(self, unk):
		logger.info("FriendsClientV2.get_request_block_settings()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(unk, stream.u32)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_REQUEST_BLOCK_SETTINGS, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		settings = stream.list(PrincipalRequestBlockSetting)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("FriendsClientV2.get_request_block_settings -> done")
		return settings


class FriendsServerV1(FriendsProtocolV1):
	def __init__(self):
		self.methods = {
			self.METHOD_UPDATE_PROFILE: self.handle_update_profile,
			self.METHOD_UPDATE_MII: self.handle_update_mii,
			self.METHOD_UPDATE_MII_LIST: self.handle_update_mii_list,
			self.METHOD_UPDATE_PLAYED_GAMES: self.handle_update_played_games,
			self.METHOD_UPDATE_PREFERENCE: self.handle_update_preference,
			self.METHOD_GET_FRIEND_MII: self.handle_get_friend_mii,
			self.METHOD_GET_FRIEND_MII_LIST: self.handle_get_friend_mii_list,
			self.METHOD_IS_ACTIVE_GAME: self.handle_is_active_game,
			self.METHOD_GET_PRINCIPAL_ID_BY_LOCAL_FRIEND_CODE: self.handle_get_principal_id_by_local_friend_code,
			self.METHOD_GET_FRIEND_RELATIONSHIPS: self.handle_get_friend_relationships,
			self.METHOD_ADD_FRIEND_BY_PRINCIPAL_ID: self.handle_add_friend_by_principal_id,
			self.METHOD_ADD_FRIEND_BY_PRINCIPAL_IDS: self.handle_add_friend_by_principal_ids,
			self.METHOD_REMOVE_FRIEND_BY_LOCAL_FRIEND_CODE: self.handle_remove_friend_by_local_friend_code,
			self.METHOD_REMOVE_FRIEND_BY_PRINCIPAL_ID: self.handle_remove_friend_by_principal_id,
			self.METHOD_GET_ALL_FRIENDS: self.handle_get_all_friends,
			self.METHOD_UPDATE_BLACK_LIST: self.handle_update_black_list,
			self.METHOD_SYNC_FRIEND: self.handle_sync_friend,
			self.METHOD_UPDATE_PRESENCE: self.handle_update_presence,
			self.METHOD_UPDATE_FAVORITE_GAME_KEY: self.handle_update_favorite_game_key,
			self.METHOD_UPDATE_COMMENT: self.handle_update_comment,
			self.METHOD_UPDATE_PICTURE: self.handle_update_picture,
			self.METHOD_GET_FRIEND_PRESENCE: self.handle_get_friend_presence,
			self.METHOD_GET_FRIEND_COMMENT: self.handle_get_friend_comment,
			self.METHOD_GET_FRIEND_PICTURE: self.handle_get_friend_picture,
			self.METHOD_GET_FRIEND_PERSISTENT_INFO: self.handle_get_friend_persistent_info,
			self.METHOD_SEND_INVITATION: self.handle_send_invitation,
		}
	
	async def logout(self, client):
		pass
	
	async def handle(self, client, method_id, input, output):
		if method_id in self.methods:
			await self.methods[method_id](client, input, output)
		else:
			logger.warning("Unknown method called on FriendsServerV1: %i", method_id)
			raise common.RMCError("Core::NotImplemented")
	
	async def handle_update_profile(self, client, input, output):
		logger.warning("FriendsServerV1.update_profile is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_update_mii(self, client, input, output):
		logger.warning("FriendsServerV1.update_mii is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_update_mii_list(self, client, input, output):
		logger.warning("FriendsServerV1.update_mii_list is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_update_played_games(self, client, input, output):
		logger.warning("FriendsServerV1.update_played_games is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_update_preference(self, client, input, output):
		logger.warning("FriendsServerV1.update_preference is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_get_friend_mii(self, client, input, output):
		logger.warning("FriendsServerV1.get_friend_mii is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_get_friend_mii_list(self, client, input, output):
		logger.warning("FriendsServerV1.get_friend_mii_list is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_is_active_game(self, client, input, output):
		logger.warning("FriendsServerV1.is_active_game is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_get_principal_id_by_local_friend_code(self, client, input, output):
		logger.warning("FriendsServerV1.get_principal_id_by_local_friend_code is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_get_friend_relationships(self, client, input, output):
		logger.warning("FriendsServerV1.get_friend_relationships is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_add_friend_by_principal_id(self, client, input, output):
		logger.warning("FriendsServerV1.add_friend_by_principal_id is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_add_friend_by_principal_ids(self, client, input, output):
		logger.warning("FriendsServerV1.add_friend_by_principal_ids is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_remove_friend_by_local_friend_code(self, client, input, output):
		logger.warning("FriendsServerV1.remove_friend_by_local_friend_code is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_remove_friend_by_principal_id(self, client, input, output):
		logger.warning("FriendsServerV1.remove_friend_by_principal_id is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_get_all_friends(self, client, input, output):
		logger.warning("FriendsServerV1.get_all_friends is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_update_black_list(self, client, input, output):
		logger.warning("FriendsServerV1.update_black_list is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_sync_friend(self, client, input, output):
		logger.warning("FriendsServerV1.sync_friend is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_update_presence(self, client, input, output):
		logger.warning("FriendsServerV1.update_presence is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_update_favorite_game_key(self, client, input, output):
		logger.warning("FriendsServerV1.update_favorite_game_key is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_update_comment(self, client, input, output):
		logger.warning("FriendsServerV1.update_comment is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_update_picture(self, client, input, output):
		logger.warning("FriendsServerV1.update_picture is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_get_friend_presence(self, client, input, output):
		logger.warning("FriendsServerV1.get_friend_presence is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_get_friend_comment(self, client, input, output):
		logger.warning("FriendsServerV1.get_friend_comment is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_get_friend_picture(self, client, input, output):
		logger.warning("FriendsServerV1.get_friend_picture is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_get_friend_persistent_info(self, client, input, output):
		logger.warning("FriendsServerV1.get_friend_persistent_info is not supported")
		raise common.RMCError("Core::NotImplemented")
	
	async def handle_send_invitation(self, client, input, output):
		logger.warning("FriendsServerV1.send_invitation is not supported")
		raise common.RMCError("Core::NotImplemented")


class FriendsServerV2(FriendsProtocolV2):
	def __init__(self):
		self.methods = {
			self.METHOD_UPDATE_AND_GET_ALL_INFORMATION: self.handle_update_and_get_all_information,
			self.METHOD_ADD_FRIEND: self.handle_add_friend,
			self.METHOD_ADD_FRIEND_BY_NAME: self.handle_add_friend_by_name,
			self.METHOD_REMOVE_FRIEND: self.handle_remove_friend,
			self.METHOD_ADD_FRIEND_REQUEST: self.handle_add_friend_request,
			self.METHOD_CANCEL_FRIEND_REQUEST: self.handle_cancel_friend_request,
			self.METHOD_ACCEPT_FRIEND_REQUEST: self.handle_accept_friend_request,
			self.METHOD_DELETE_FRIEND_REQUEST: self.handle_delete_friend_request,
			self.METHOD_DENY_FRIEND_REQUEST: self.handle_deny_friend_request,
			self.METHOD_MARK_FRIEND_REQUESTS_AS_RECEIVED: self.handle_mark_friend_requests_as_received,
			self.METHOD_ADD_BLACK_LIST: self.handle_add_black_list,
			self.METHOD_REMOVE_BLACK_LIST: self.handle_remove_black_list,
			self.METHOD_UPDATE_PRESENCE: self.handle_update_presence,
			self.METHOD_UPDATE_MII: self.handle_update_mii,
			self.METHOD_UPDATE_COMMENT: self.handle_update_comment,
			self.METHOD_UPDATE_PREFERENCE: self.handle_update_preference,
			self.METHOD_GET_BASIC_INFO: self.handle_get_basic_info,
			self.METHOD_DELETE_PERSISTENT_NOTIFICATION: self.handle_delete_persistent_notification,
			self.METHOD_CHECK_SETTING_STATUS: self.handle_check_setting_status,
			self.METHOD_GET_REQUEST_BLOCK_SETTINGS: self.handle_get_request_block_settings,
		}
	
	async def logout(self, client):
		pass
	
	async def handle(self, client, method_id, input, output):
		if method_id in self.methods:
			await self.methods[method_id](client, input, output)
		else:
			logger.warning("Unknown method called on FriendsServerV2: %i", method_id)
			raise common.RMCError("Core::NotImplemented")
	
	async def handle_update_and_get_all_information(self, client, input, output):
		logger.info("FriendsServerV2.update_and_get_all_information()")
		#--- request ---
		nna_info = input.extract(NNAInfo)
		presence = input.extract(NintendoPresenceV2)
		birthday = input.datetime()
		response = await self.update_and_get_all_information(client, nna_info, presence, birthday)
		
		#--- response ---
		if not isinstance(response, rmc.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['principal_preference', 'comment', 'friends', 'sent_requests', 'received_requests', 'blacklist', 'unk1', 'notifications', 'unk2']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.add(response.principal_preference)
		output.add(response.comment)
		output.list(response.friends, output.add)
		output.list(response.sent_requests, output.add)
		output.list(response.received_requests, output.add)
		output.list(response.blacklist, output.add)
		output.bool(response.unk1)
		output.list(response.notifications, output.add)
		output.bool(response.unk2)
	
	async def handle_add_friend(self, client, input, output):
		logger.info("FriendsServerV2.add_friend()")
		#--- request ---
		pid = input.pid()
		response = await self.add_friend(client, pid)
		
		#--- response ---
		if not isinstance(response, rmc.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['request', 'info']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.add(response.request)
		output.add(response.info)
	
	async def handle_add_friend_by_name(self, client, input, output):
		logger.info("FriendsServerV2.add_friend_by_name()")
		#--- request ---
		name = input.string()
		response = await self.add_friend_by_name(client, name)
		
		#--- response ---
		if not isinstance(response, rmc.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['request', 'info']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.add(response.request)
		output.add(response.info)
	
	async def handle_remove_friend(self, client, input, output):
		logger.info("FriendsServerV2.remove_friend()")
		#--- request ---
		pid = input.pid()
		await self.remove_friend(client, pid)
	
	async def handle_add_friend_request(self, client, input, output):
		logger.info("FriendsServerV2.add_friend_request()")
		#--- request ---
		unk1 = input.u32()
		unk2 = input.u8()
		unk3 = input.string()
		unk4 = input.u8()
		unk5 = input.string()
		game_key = input.extract(GameKey)
		unk6 = input.datetime()
		response = await self.add_friend_request(client, unk1, unk2, unk3, unk4, unk5, game_key, unk6)
		
		#--- response ---
		if not isinstance(response, rmc.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['request', 'info']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.add(response.request)
		output.add(response.info)
	
	async def handle_cancel_friend_request(self, client, input, output):
		logger.info("FriendsServerV2.cancel_friend_request()")
		#--- request ---
		id = input.u64()
		await self.cancel_friend_request(client, id)
	
	async def handle_accept_friend_request(self, client, input, output):
		logger.info("FriendsServerV2.accept_friend_request()")
		#--- request ---
		id = input.u64()
		response = await self.accept_friend_request(client, id)
		
		#--- response ---
		if not isinstance(response, FriendInfo):
			raise RuntimeError("Expected FriendInfo, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_delete_friend_request(self, client, input, output):
		logger.info("FriendsServerV2.delete_friend_request()")
		#--- request ---
		id = input.u64()
		await self.delete_friend_request(client, id)
	
	async def handle_deny_friend_request(self, client, input, output):
		logger.info("FriendsServerV2.deny_friend_request()")
		#--- request ---
		id = input.u64()
		response = await self.deny_friend_request(client, id)
		
		#--- response ---
		if not isinstance(response, BlacklistedPrincipal):
			raise RuntimeError("Expected BlacklistedPrincipal, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_mark_friend_requests_as_received(self, client, input, output):
		logger.info("FriendsServerV2.mark_friend_requests_as_received()")
		#--- request ---
		ids = input.list(input.u64)
		await self.mark_friend_requests_as_received(client, ids)
	
	async def handle_add_black_list(self, client, input, output):
		logger.info("FriendsServerV2.add_black_list()")
		#--- request ---
		principal = input.extract(BlacklistedPrincipal)
		response = await self.add_black_list(client, principal)
		
		#--- response ---
		if not isinstance(response, BlacklistedPrincipal):
			raise RuntimeError("Expected BlacklistedPrincipal, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_remove_black_list(self, client, input, output):
		logger.info("FriendsServerV2.remove_black_list()")
		#--- request ---
		pid = input.pid()
		await self.remove_black_list(client, pid)
	
	async def handle_update_presence(self, client, input, output):
		logger.info("FriendsServerV2.update_presence()")
		#--- request ---
		presence = input.extract(NintendoPresenceV2)
		await self.update_presence(client, presence)
	
	async def handle_update_mii(self, client, input, output):
		logger.info("FriendsServerV2.update_mii()")
		#--- request ---
		mii = input.extract(MiiV2)
		response = await self.update_mii(client, mii)
		
		#--- response ---
		if not isinstance(response, common.DateTime):
			raise RuntimeError("Expected common.DateTime, got %s" %response.__class__.__name__)
		output.datetime(response)
	
	async def handle_update_comment(self, client, input, output):
		logger.info("FriendsServerV2.update_comment()")
		#--- request ---
		comment = input.extract(Comment)
		response = await self.update_comment(client, comment)
		
		#--- response ---
		if not isinstance(response, common.DateTime):
			raise RuntimeError("Expected common.DateTime, got %s" %response.__class__.__name__)
		output.datetime(response)
	
	async def handle_update_preference(self, client, input, output):
		logger.info("FriendsServerV2.update_preference()")
		#--- request ---
		preference = input.extract(PrincipalPreference)
		await self.update_preference(client, preference)
	
	async def handle_get_basic_info(self, client, input, output):
		logger.info("FriendsServerV2.get_basic_info()")
		#--- request ---
		pids = input.list(input.pid)
		response = await self.get_basic_info(client, pids)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.add)
	
	async def handle_delete_persistent_notification(self, client, input, output):
		logger.info("FriendsServerV2.delete_persistent_notification()")
		#--- request ---
		notifications = input.list(PersistentNotification)
		await self.delete_persistent_notification(client, notifications)
	
	async def handle_check_setting_status(self, client, input, output):
		logger.info("FriendsServerV2.check_setting_status()")
		#--- request ---
		response = await self.check_setting_status(client)
		
		#--- response ---
		if not isinstance(response, int):
			raise RuntimeError("Expected int, got %s" %response.__class__.__name__)
		output.u8(response)
	
	async def handle_get_request_block_settings(self, client, input, output):
		logger.info("FriendsServerV2.get_request_block_settings()")
		#--- request ---
		unk = input.list(input.u32)
		response = await self.get_request_block_settings(client, unk)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.add)
	
	async def update_and_get_all_information(self, *args):
		logger.warning("FriendsServerV2.update_and_get_all_information not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def add_friend(self, *args):
		logger.warning("FriendsServerV2.add_friend not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def add_friend_by_name(self, *args):
		logger.warning("FriendsServerV2.add_friend_by_name not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def remove_friend(self, *args):
		logger.warning("FriendsServerV2.remove_friend not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def add_friend_request(self, *args):
		logger.warning("FriendsServerV2.add_friend_request not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def cancel_friend_request(self, *args):
		logger.warning("FriendsServerV2.cancel_friend_request not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def accept_friend_request(self, *args):
		logger.warning("FriendsServerV2.accept_friend_request not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def delete_friend_request(self, *args):
		logger.warning("FriendsServerV2.delete_friend_request not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def deny_friend_request(self, *args):
		logger.warning("FriendsServerV2.deny_friend_request not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def mark_friend_requests_as_received(self, *args):
		logger.warning("FriendsServerV2.mark_friend_requests_as_received not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def add_black_list(self, *args):
		logger.warning("FriendsServerV2.add_black_list not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def remove_black_list(self, *args):
		logger.warning("FriendsServerV2.remove_black_list not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def update_presence(self, *args):
		logger.warning("FriendsServerV2.update_presence not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def update_mii(self, *args):
		logger.warning("FriendsServerV2.update_mii not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def update_comment(self, *args):
		logger.warning("FriendsServerV2.update_comment not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def update_preference(self, *args):
		logger.warning("FriendsServerV2.update_preference not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_basic_info(self, *args):
		logger.warning("FriendsServerV2.get_basic_info not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def delete_persistent_notification(self, *args):
		logger.warning("FriendsServerV2.delete_persistent_notification not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def check_setting_status(self, *args):
		logger.warning("FriendsServerV2.check_setting_status not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_request_block_settings(self, *args):
		logger.warning("FriendsServerV2.get_request_block_settings not implemented")
		raise common.RMCError("Core::NotImplemented")

