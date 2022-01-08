
# This file was generated automatically by generate_protocols.py

from nintendo.nex import notification, rmc, common, streams

import logging
logger = logging.getLogger(__name__)


class UniqueIdInfo(common.Structure):
	def __init__(self):
		super().__init__()
		self.unique_id = 0
		self.password = 0
	
	def check_required(self, settings, version):
		pass
	
	def load(self, stream, version):
		self.unique_id = stream.u64()
		self.password = stream.u64()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.unique_id)
		stream.u64(self.password)


class UpdateCurrentUserParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.info = UniqueIdInfo()
		self.region = None
	
	def check_required(self, settings, version):
		for field in ['region']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.info = stream.extract(UniqueIdInfo)
		self.region = stream.u8()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.add(self.info)
		stream.u8(self.region)


class UtilityProtocolS2:
	METHOD_ACQUIRE_NEX_UNIQUE_ID = 1
	METHOD_ACQUIRE_NEX_UNIQUE_ID_WITH_PASSWORD = 2
	METHOD_ASSOCIATE_NEX_UNIQUE_ID_WITH_MY_PRINCIPAL_ID = 3
	METHOD_ASSOCIATE_NEX_UNIQUE_IDS_WITH_MY_PRINCIPAL_ID = 4
	METHOD_GET_ASSOCIATED_NEX_UNIQUE_ID_WITH_MY_PRINCIPAL_ID = 5
	METHOD_GET_ASSOCIATED_NEX_UNIQUE_IDS_WITH_MY_PRINCIPAL_ID = 6
	METHOD_GET_INTEGER_SETTINGS = 7
	METHOD_GET_STRING_SETTINGS = 8
	METHOD_ACQUIRE_TAG_ID = 9
	METHOD_UPDATE_CURRENT_USER = 10
	
	PROTOCOL_ID = 0x6E


class UtilityClientS2(UtilityProtocolS2):
	def __init__(self, client):
		self.settings = client.settings
		self.client = client
	
	async def acquire_nex_unique_id(self):
		logger.info("UtilityClientS2.acquire_nex_unique_id()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_ACQUIRE_NEX_UNIQUE_ID, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		unique_id = stream.u64()
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("UtilityClientS2.acquire_nex_unique_id -> done")
		return unique_id
	
	async def acquire_nex_unique_id_with_password(self):
		logger.info("UtilityClientS2.acquire_nex_unique_id_with_password()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_ACQUIRE_NEX_UNIQUE_ID_WITH_PASSWORD, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		info = stream.extract(UniqueIdInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("UtilityClientS2.acquire_nex_unique_id_with_password -> done")
		return info
	
	async def associate_nex_unique_id_with_my_principal_id(self, info):
		logger.info("UtilityClientS2.associate_nex_unique_id_with_my_principal_id()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(info)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_ASSOCIATE_NEX_UNIQUE_ID_WITH_MY_PRINCIPAL_ID, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("UtilityClientS2.associate_nex_unique_id_with_my_principal_id -> done")
	
	async def associate_nex_unique_ids_with_my_principal_id(self, infos):
		logger.info("UtilityClientS2.associate_nex_unique_ids_with_my_principal_id()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(infos, stream.add)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_ASSOCIATE_NEX_UNIQUE_IDS_WITH_MY_PRINCIPAL_ID, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("UtilityClientS2.associate_nex_unique_ids_with_my_principal_id -> done")
	
	async def get_associated_nex_unique_id_with_my_principal_id(self):
		logger.info("UtilityClientS2.get_associated_nex_unique_id_with_my_principal_id()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_ASSOCIATED_NEX_UNIQUE_ID_WITH_MY_PRINCIPAL_ID, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		info = stream.extract(UniqueIdInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("UtilityClientS2.get_associated_nex_unique_id_with_my_principal_id -> done")
		return info
	
	async def get_associated_nex_unique_ids_with_my_principal_id(self):
		logger.info("UtilityClientS2.get_associated_nex_unique_ids_with_my_principal_id()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_ASSOCIATED_NEX_UNIQUE_IDS_WITH_MY_PRINCIPAL_ID, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		infos = stream.list(UniqueIdInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("UtilityClientS2.get_associated_nex_unique_ids_with_my_principal_id -> done")
		return infos
	
	async def get_integer_settings(self, index):
		logger.info("UtilityClientS2.get_integer_settings()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u32(index)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_INTEGER_SETTINGS, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		settings = stream.map(stream.u16, stream.s32)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("UtilityClientS2.get_integer_settings -> done")
		return settings
	
	async def get_string_settings(self, index):
		logger.info("UtilityClientS2.get_string_settings()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u32(index)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_STRING_SETTINGS, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		settings = stream.map(stream.u16, stream.string)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("UtilityClientS2.get_string_settings -> done")
		return settings
	
	async def acquire_tag_id(self, nex_unique_ids):
		logger.info("UtilityClientS2.acquire_tag_id()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(nex_unique_ids, stream.u64)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_ACQUIRE_TAG_ID, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		p_tag_id = stream.u64()
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("UtilityClientS2.acquire_tag_id -> done")
		return p_tag_id
	
	async def update_current_user(self, param):
		logger.info("UtilityClientS2.update_current_user()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_UPDATE_CURRENT_USER, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("UtilityClientS2.update_current_user -> done")


class UtilityServerS2(UtilityProtocolS2):
	def __init__(self):
		self.methods = {
			self.METHOD_ACQUIRE_NEX_UNIQUE_ID: self.handle_acquire_nex_unique_id,
			self.METHOD_ACQUIRE_NEX_UNIQUE_ID_WITH_PASSWORD: self.handle_acquire_nex_unique_id_with_password,
			self.METHOD_ASSOCIATE_NEX_UNIQUE_ID_WITH_MY_PRINCIPAL_ID: self.handle_associate_nex_unique_id_with_my_principal_id,
			self.METHOD_ASSOCIATE_NEX_UNIQUE_IDS_WITH_MY_PRINCIPAL_ID: self.handle_associate_nex_unique_ids_with_my_principal_id,
			self.METHOD_GET_ASSOCIATED_NEX_UNIQUE_ID_WITH_MY_PRINCIPAL_ID: self.handle_get_associated_nex_unique_id_with_my_principal_id,
			self.METHOD_GET_ASSOCIATED_NEX_UNIQUE_IDS_WITH_MY_PRINCIPAL_ID: self.handle_get_associated_nex_unique_ids_with_my_principal_id,
			self.METHOD_GET_INTEGER_SETTINGS: self.handle_get_integer_settings,
			self.METHOD_GET_STRING_SETTINGS: self.handle_get_string_settings,
			self.METHOD_ACQUIRE_TAG_ID: self.handle_acquire_tag_id,
			self.METHOD_UPDATE_CURRENT_USER: self.handle_update_current_user,
		}
	
	async def logout(self, client):
		pass
	
	async def handle(self, client, method_id, input, output):
		if method_id in self.methods:
			await self.methods[method_id](client, input, output)
		else:
			logger.warning("Unknown method called on UtilityServerS2: %i", method_id)
			raise common.RMCError("Core::NotImplemented")
	
	async def handle_acquire_nex_unique_id(self, client, input, output):
		logger.info("UtilityServerS2.acquire_nex_unique_id()")
		#--- request ---
		response = await self.acquire_nex_unique_id(client)
		
		#--- response ---
		if not isinstance(response, int):
			raise RuntimeError("Expected int, got %s" %response.__class__.__name__)
		output.u64(response)
	
	async def handle_acquire_nex_unique_id_with_password(self, client, input, output):
		logger.info("UtilityServerS2.acquire_nex_unique_id_with_password()")
		#--- request ---
		response = await self.acquire_nex_unique_id_with_password(client)
		
		#--- response ---
		if not isinstance(response, UniqueIdInfo):
			raise RuntimeError("Expected UniqueIdInfo, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_associate_nex_unique_id_with_my_principal_id(self, client, input, output):
		logger.info("UtilityServerS2.associate_nex_unique_id_with_my_principal_id()")
		#--- request ---
		info = input.extract(UniqueIdInfo)
		await self.associate_nex_unique_id_with_my_principal_id(client, info)
	
	async def handle_associate_nex_unique_ids_with_my_principal_id(self, client, input, output):
		logger.info("UtilityServerS2.associate_nex_unique_ids_with_my_principal_id()")
		#--- request ---
		infos = input.list(UniqueIdInfo)
		await self.associate_nex_unique_ids_with_my_principal_id(client, infos)
	
	async def handle_get_associated_nex_unique_id_with_my_principal_id(self, client, input, output):
		logger.info("UtilityServerS2.get_associated_nex_unique_id_with_my_principal_id()")
		#--- request ---
		response = await self.get_associated_nex_unique_id_with_my_principal_id(client)
		
		#--- response ---
		if not isinstance(response, UniqueIdInfo):
			raise RuntimeError("Expected UniqueIdInfo, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_get_associated_nex_unique_ids_with_my_principal_id(self, client, input, output):
		logger.info("UtilityServerS2.get_associated_nex_unique_ids_with_my_principal_id()")
		#--- request ---
		response = await self.get_associated_nex_unique_ids_with_my_principal_id(client)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.add)
	
	async def handle_get_integer_settings(self, client, input, output):
		logger.info("UtilityServerS2.get_integer_settings()")
		#--- request ---
		index = input.u32()
		response = await self.get_integer_settings(client, index)
		
		#--- response ---
		if not isinstance(response, dict):
			raise RuntimeError("Expected dict, got %s" %response.__class__.__name__)
		output.map(response, output.u16, output.s32)
	
	async def handle_get_string_settings(self, client, input, output):
		logger.info("UtilityServerS2.get_string_settings()")
		#--- request ---
		index = input.u32()
		response = await self.get_string_settings(client, index)
		
		#--- response ---
		if not isinstance(response, dict):
			raise RuntimeError("Expected dict, got %s" %response.__class__.__name__)
		output.map(response, output.u16, output.string)
	
	async def handle_acquire_tag_id(self, client, input, output):
		logger.info("UtilityServerS2.acquire_tag_id()")
		#--- request ---
		nex_unique_ids = input.list(input.u64)
		response = await self.acquire_tag_id(client, nex_unique_ids)
		
		#--- response ---
		if not isinstance(response, int):
			raise RuntimeError("Expected int, got %s" %response.__class__.__name__)
		output.u64(response)
	
	async def handle_update_current_user(self, client, input, output):
		logger.info("UtilityServerS2.update_current_user()")
		#--- request ---
		param = input.extract(UpdateCurrentUserParam)
		await self.update_current_user(client, param)
	
	async def acquire_nex_unique_id(self, *args):
		logger.warning("UtilityServerS2.acquire_nex_unique_id not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def acquire_nex_unique_id_with_password(self, *args):
		logger.warning("UtilityServerS2.acquire_nex_unique_id_with_password not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def associate_nex_unique_id_with_my_principal_id(self, *args):
		logger.warning("UtilityServerS2.associate_nex_unique_id_with_my_principal_id not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def associate_nex_unique_ids_with_my_principal_id(self, *args):
		logger.warning("UtilityServerS2.associate_nex_unique_ids_with_my_principal_id not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_associated_nex_unique_id_with_my_principal_id(self, *args):
		logger.warning("UtilityServerS2.get_associated_nex_unique_id_with_my_principal_id not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_associated_nex_unique_ids_with_my_principal_id(self, *args):
		logger.warning("UtilityServerS2.get_associated_nex_unique_ids_with_my_principal_id not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_integer_settings(self, *args):
		logger.warning("UtilityServerS2.get_integer_settings not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_string_settings(self, *args):
		logger.warning("UtilityServerS2.get_string_settings not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def acquire_tag_id(self, *args):
		logger.warning("UtilityServerS2.acquire_tag_id not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def update_current_user(self, *args):
		logger.warning("UtilityServerS2.update_current_user not implemented")
		raise common.RMCError("Core::NotImplemented")

