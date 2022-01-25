
# This file was generated automatically by generate_protocols.py

from nintendo.nex import notification, rmc, common, streams

import logging
logger = logging.getLogger(__name__)


class RankingOrderCalc:
	STANDARD = 0
	ORDINAL = 1


class RankingMode:
	GLOBAL = 0
	GLOBAL_AROUND_SELF = 1
	SELF = 4


class RankingStatFlags:
	RANKING_COUNT = 1
	TOTAL_SCORE = 2
	LOWEST_SCORE = 4
	HIGHEST_SCORE = 8
	AVERAGE_SCORE = 16
	ALL = 31


class RankingOrderParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.order_calc = 0
		self.group_index = 255
		self.group_num = 0
		self.time_scope = 2
		self.offset = None
		self.count = None
	
	def check_required(self, settings, version):
		for field in ['offset', 'count']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.order_calc = stream.u8()
		self.group_index = stream.u8()
		self.group_num = stream.u8()
		self.time_scope = stream.u8()
		self.offset = stream.u32()
		self.count = stream.u8()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u8(self.order_calc)
		stream.u8(self.group_index)
		stream.u8(self.group_num)
		stream.u8(self.time_scope)
		stream.u32(self.offset)
		stream.u8(self.count)


class RankingRankData(common.Structure):
	def __init__(self):
		super().__init__()
		self.pid = None
		self.unique_id = None
		self.rank = None
		self.category = None
		self.score = None
		self.groups = None
		self.param = None
		self.common_data = None
		self.update_time = None
	
	def check_required(self, settings, version):
		for field in ['pid', 'unique_id', 'rank', 'category', 'score', 'groups', 'param', 'common_data']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
		if settings["nex.version"] >= 40000:
			for field in ['update_time']:
				if getattr(self, field) is None:
					raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.pid = stream.pid()
		self.unique_id = stream.u64()
		self.rank = stream.u32()
		self.category = stream.u32()
		self.score = stream.u32()
		self.groups = stream.list(stream.u8)
		self.param = stream.u64()
		self.common_data = stream.buffer()
		if stream.settings["nex.version"] >= 40000:
			self.update_time = stream.datetime()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.pid(self.pid)
		stream.u64(self.unique_id)
		stream.u32(self.rank)
		stream.u32(self.category)
		stream.u32(self.score)
		stream.list(self.groups, stream.u8)
		stream.u64(self.param)
		stream.buffer(self.common_data)
		if stream.settings["nex.version"] >= 40000:
			stream.datetime(self.update_time)


class RankingResult(common.Structure):
	def __init__(self):
		super().__init__()
		self.data = None
		self.total = None
		self.since_time = None
	
	def check_required(self, settings, version):
		for field in ['data', 'total', 'since_time']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.data = stream.list(RankingRankData)
		self.total = stream.u32()
		self.since_time = stream.datetime()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.list(self.data, stream.add)
		stream.u32(self.total)
		stream.datetime(self.since_time)


class RankingCachedResult(RankingResult):
	def __init__(self):
		super().__init__()
		self.created_time = None
		self.expired_time = None
		self.max_length = None
	
	def check_required(self, settings, version):
		for field in ['created_time', 'expired_time', 'max_length']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.created_time = stream.datetime()
		self.expired_time = stream.datetime()
		self.max_length = stream.u8()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.datetime(self.created_time)
		stream.datetime(self.expired_time)
		stream.u8(self.max_length)
common.DataHolder.register(RankingCachedResult, "RankingCachedResult")


class RankingStats(common.Structure):
	def __init__(self):
		super().__init__()
		self.stats = None
	
	def check_required(self, settings, version):
		for field in ['stats']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.stats = stream.list(stream.double)
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.list(self.stats, stream.double)


class RankingScoreData(common.Structure):
	def __init__(self):
		super().__init__()
		self.category = None
		self.score = None
		self.order = None
		self.update_mode = None
		self.groups = None
		self.param = None
	
	def check_required(self, settings, version):
		for field in ['category', 'score', 'order', 'update_mode', 'groups', 'param']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.category = stream.u32()
		self.score = stream.u32()
		self.order = stream.u8()
		self.update_mode = stream.u8()
		self.groups = stream.list(stream.u8)
		self.param = stream.u64()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u32(self.category)
		stream.u32(self.score)
		stream.u8(self.order)
		stream.u8(self.update_mode)
		stream.list(self.groups, stream.u8)
		stream.u64(self.param)


class RankingChangeAttributesParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.flags = None
		self.groups = None
		self.param = None
	
	def check_required(self, settings, version):
		for field in ['flags', 'groups', 'param']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.flags = stream.u8()
		self.groups = stream.list(stream.u8)
		self.param = stream.u64()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u8(self.flags)
		stream.list(self.groups, stream.u8)
		stream.u64(self.param)


class FestivalUploadVoteParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.festival_id = None
		self.theme_id = None
	
	def check_required(self, settings, version):
		for field in ['festival_id', 'theme_id']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.festival_id = stream.u32()
		self.theme_id = stream.u8()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u32(self.festival_id)
		stream.u8(self.theme_id)


class FestivalUploadScoreParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.unique_id = None
		self.region = None
		self.festival_id = None
		self.team_id = None
		self.score = None
		self.battle_gathering_id = None
		self.battle_result = None
		self.application_buffer = None
	
	def check_required(self, settings, version):
		for field in ['unique_id', 'region', 'festival_id', 'team_id', 'score', 'battle_gathering_id', 'battle_result', 'application_buffer']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.unique_id = stream.u64()
		self.region = stream.u8()
		self.festival_id = stream.u32()
		self.team_id = stream.u8()
		self.score = stream.u32()
		self.battle_gathering_id = stream.u32()
		self.battle_result = stream.u32()
		self.application_buffer = stream.qbuffer()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.unique_id)
		stream.u8(self.region)
		stream.u32(self.festival_id)
		stream.u8(self.team_id)
		stream.u32(self.score)
		stream.u32(self.battle_gathering_id)
		stream.u32(self.battle_result)
		stream.qbuffer(self.application_buffer)


class FestivalResult(common.Structure):
	def __init__(self):
		super().__init__()
		self.festival_id = None
		self.num_participants = None
		self.team_participants = None
		self.team_scores = None
		self.updated_time = None
	
	def check_required(self, settings, version):
		for field in ['festival_id', 'num_participants', 'team_participants', 'team_scores', 'updated_time']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.festival_id = stream.u32()
		self.num_participants = stream.u32()
		self.team_participants = stream.list(stream.u32)
		self.team_scores = stream.list(stream.u32)
		self.updated_time = stream.datetime()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u32(self.festival_id)
		stream.u32(self.num_participants)
		stream.list(self.team_participants, stream.u32)
		stream.list(self.team_scores, stream.u32)
		stream.datetime(self.updated_time)


class LeaguePlayerDetail(common.Structure):
	def __init__(self):
		super().__init__()
		self.principal_id = None
		self.weapon_id = None
	
	def check_required(self, settings, version):
		for field in ['principal_id', 'weapon_id']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.principal_id = stream.u64()
		self.weapon_id = stream.s32()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.principal_id)
		stream.s32(self.weapon_id)


class LeaguePointInfo(common.Structure):
	def __init__(self):
		super().__init__()
		self.tag_id = None
		self.region_flag = None
		self.league_id = None
		self.point = None
		self.tag_members = None
		self.application_buffer = None
	
	def check_required(self, settings, version):
		for field in ['tag_id', 'region_flag', 'league_id', 'point', 'tag_members', 'application_buffer']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.tag_id = stream.u64()
		self.region_flag = stream.u8()
		self.league_id = stream.string()
		self.point = stream.u32()
		self.tag_members = stream.map(stream.u64, LeaguePlayerDetail)
		self.application_buffer = stream.qbuffer()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.tag_id)
		stream.u8(self.region_flag)
		stream.string(self.league_id)
		stream.u32(self.point)
		stream.map(self.tag_members, stream.u64, stream.add)
		stream.qbuffer(self.application_buffer)


class LeagueResult(common.Structure):
	def __init__(self):
		super().__init__()
		self.league_point_info = LeaguePointInfo()
		self.status = None
		self.specific_rank = None
		self.rank_ratio = None
		self.tag_num = None
		self.match_count = None
	
	def check_required(self, settings, version):
		for field in ['status', 'specific_rank', 'rank_ratio', 'tag_num', 'match_count']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.league_point_info = stream.extract(LeaguePointInfo)
		self.status = stream.u8()
		self.specific_rank = stream.u32()
		self.rank_ratio = stream.u8()
		self.tag_num = stream.u32()
		self.match_count = stream.u32()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.add(self.league_point_info)
		stream.u8(self.status)
		stream.u32(self.specific_rank)
		stream.u8(self.rank_ratio)
		stream.u32(self.tag_num)
		stream.u32(self.match_count)


class XPowerUploadParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.season_id = None
		self.name = None
		self.region = None
		self.x_power = None
		self.x_power_max = None
		self.weapon_id = None
		self.application_buffer = None
	
	def check_required(self, settings, version):
		for field in ['season_id', 'name', 'region', 'x_power', 'x_power_max', 'weapon_id', 'application_buffer']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.season_id = stream.string()
		self.name = stream.string()
		self.region = stream.u8()
		self.x_power = stream.s32()
		self.x_power_max = stream.s32()
		self.weapon_id = stream.s32()
		self.application_buffer = stream.qbuffer()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.string(self.season_id)
		stream.string(self.name)
		stream.u8(self.region)
		stream.s32(self.x_power)
		stream.s32(self.x_power_max)
		stream.s32(self.weapon_id)
		stream.qbuffer(self.application_buffer)


class XPowerGetRankingParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.season_id = None
		self.flag = None
		self.top_ranking_offset = None
		self.top_ranking_limit = None
	
	def check_required(self, settings, version):
		for field in ['season_id', 'flag', 'top_ranking_offset', 'top_ranking_limit']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.season_id = stream.string()
		self.flag = stream.u8()
		self.top_ranking_offset = stream.u32()
		self.top_ranking_limit = stream.u32()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.string(self.season_id)
		stream.u8(self.flag)
		stream.u32(self.top_ranking_offset)
		stream.u32(self.top_ranking_limit)


class XPowerRankingDetail(common.Structure):
	def __init__(self):
		super().__init__()
		self.principal_id = None
		self.unique_id = None
		self.rank = None
		self.last_rank = None
		self.name = None
		self.region = None
		self.x_power = None
		self.x_power_max = None
		self.weapon_id = None
		self.application_buffer = None
		self.cheater = None
	
	def check_required(self, settings, version):
		for field in ['principal_id', 'unique_id', 'rank', 'last_rank', 'name', 'region', 'x_power', 'x_power_max', 'weapon_id', 'application_buffer', 'cheater']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.principal_id = stream.u64()
		self.unique_id = stream.u64()
		self.rank = stream.s32()
		self.last_rank = stream.s32()
		self.name = stream.string()
		self.region = stream.u8()
		self.x_power = stream.s32()
		self.x_power_max = stream.s32()
		self.weapon_id = stream.s32()
		self.application_buffer = stream.qbuffer()
		self.cheater = stream.u32()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.principal_id)
		stream.u64(self.unique_id)
		stream.s32(self.rank)
		stream.s32(self.last_rank)
		stream.string(self.name)
		stream.u8(self.region)
		stream.s32(self.x_power)
		stream.s32(self.x_power_max)
		stream.s32(self.weapon_id)
		stream.qbuffer(self.application_buffer)
		stream.u32(self.cheater)


class XPowerRanking(common.Structure):
	def __init__(self):
		super().__init__()
		self.param = XPowerGetRankingParam()
		self.status = None
		self.player_num = None
		self.top_rankings = None
		self.weapon_ranking = XPowerRankingDetail()
		self.my_ranking = XPowerRankingDetail()
	
	def check_required(self, settings, version):
		for field in ['status', 'player_num', 'top_rankings']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.param = stream.extract(XPowerGetRankingParam)
		self.status = stream.u8()
		self.player_num = stream.s32()
		self.top_rankings = stream.list(XPowerRankingDetail)
		self.weapon_ranking = stream.extract(XPowerRankingDetail)
		self.my_ranking = stream.extract(XPowerRankingDetail)
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.add(self.param)
		stream.u8(self.status)
		stream.s32(self.player_num)
		stream.list(self.top_rankings, stream.add)
		stream.add(self.weapon_ranking)
		stream.add(self.my_ranking)


class RankingProtocolS2:
	METHOD_UPLOAD_SCORE = 1
	METHOD_DELETE_SCORE = 2
	METHOD_DELETE_ALL_SCORES = 3
	METHOD_UPLOAD_COMMON_DATA = 4
	METHOD_DELETE_COMMON_DATA = 5
	METHOD_GET_COMMON_DATA = 6
	METHOD_CHANGE_ATTRIBUTES = 7
	METHOD_CHANGE_ALL_ATTRIBUTES = 8
	METHOD_GET_RANKING = 9
	METHOD_GET_APPROX_ORDER = 10
	METHOD_GET_STATS = 11
	METHOD_GET_RANKING_BY_PID_LIST = 12
	METHOD_GET_RANKING_BY_UNIQUE_ID_LIST = 13
	METHOD_GET_CACHED_TOPX_RANKING = 14
	METHOD_GET_CACHED_TOPX_RANKINGS = 15
	METHOD_UPLOAD_LEAGUE_POINT = 16
	METHOD_GET_LEAGUE_RESULT = 17
	METHOD_GET_FESTIVAL_RESULT = 18
	METHOD_UPLOAD_FESTIVAL_VOTE = 19
	METHOD_UPLOAD_FESTIVAL_SCORE = 20
	METHOD_DELETE_FESTIVAL = 21
	METHOD_UPLOAD_X_POWER = 22
	METHOD_GET_X_POWER_RANKING = 23
	
	PROTOCOL_ID = 0x70


class RankingClientS2(RankingProtocolS2):
	def __init__(self, client):
		self.settings = client.settings
		self.client = client
	
	async def upload_score(self, score_data, unique_id):
		logger.info("RankingClientS2.upload_score()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(score_data)
		stream.u64(unique_id)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_UPLOAD_SCORE, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.upload_score -> done")
	
	async def delete_score(self, category, unique_id):
		logger.info("RankingClientS2.delete_score()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u32(category)
		stream.u64(unique_id)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_DELETE_SCORE, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.delete_score -> done")
	
	async def delete_all_scores(self, unique_id):
		logger.info("RankingClientS2.delete_all_scores()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u64(unique_id)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_DELETE_ALL_SCORES, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.delete_all_scores -> done")
	
	async def upload_common_data(self, common_data, unique_id):
		logger.info("RankingClientS2.upload_common_data()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.buffer(common_data)
		stream.u64(unique_id)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_UPLOAD_COMMON_DATA, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.upload_common_data -> done")
	
	async def delete_common_data(self, unique_id):
		logger.info("RankingClientS2.delete_common_data()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u64(unique_id)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_DELETE_COMMON_DATA, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.delete_common_data -> done")
	
	async def get_common_data(self, unique_id):
		logger.info("RankingClientS2.get_common_data()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u64(unique_id)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_COMMON_DATA, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		data = stream.buffer()
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.get_common_data -> done")
		return data
	
	async def change_attributes(self, category, param, unique_id):
		logger.info("RankingClientS2.change_attributes()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u32(category)
		stream.add(param)
		stream.u64(unique_id)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_CHANGE_ATTRIBUTES, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.change_attributes -> done")
	
	async def change_all_attributes(self, param, unique_id):
		logger.info("RankingClientS2.change_all_attributes()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		stream.u64(unique_id)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_CHANGE_ALL_ATTRIBUTES, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.change_all_attributes -> done")
	
	async def get_ranking(self, mode, category, order, unique_id, pid):
		logger.info("RankingClientS2.get_ranking()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u8(mode)
		stream.u32(category)
		stream.add(order)
		stream.u64(unique_id)
		stream.pid(pid)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_RANKING, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		result = stream.extract(RankingResult)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.get_ranking -> done")
		return result
	
	async def get_approx_order(self, category, order, score, unique_id, pid):
		logger.info("RankingClientS2.get_approx_order()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u32(category)
		stream.add(order)
		stream.u32(score)
		stream.u64(unique_id)
		stream.pid(pid)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_APPROX_ORDER, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		order = stream.u32()
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.get_approx_order -> done")
		return order
	
	async def get_stats(self, category, order, flags):
		logger.info("RankingClientS2.get_stats()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u32(category)
		stream.add(order)
		stream.u32(flags)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_STATS, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		stats = stream.extract(RankingStats)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.get_stats -> done")
		return stats
	
	async def get_ranking_by_pid_list(self, pids, mode, category, order, unique_id):
		logger.info("RankingClientS2.get_ranking_by_pid_list()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(pids, stream.pid)
		stream.u8(mode)
		stream.u32(category)
		stream.add(order)
		stream.u64(unique_id)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_RANKING_BY_PID_LIST, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		result = stream.extract(RankingResult)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.get_ranking_by_pid_list -> done")
		return result
	
	async def get_ranking_by_unique_id_list(self, ids, mode, category, order, unique_id):
		logger.info("RankingClientS2.get_ranking_by_unique_id_list()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(ids, stream.u64)
		stream.u8(mode)
		stream.u32(category)
		stream.add(order)
		stream.u64(unique_id)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_RANKING_BY_UNIQUE_ID_LIST, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		result = stream.extract(RankingResult)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.get_ranking_by_unique_id_list -> done")
		return result
	
	async def get_cached_topx_ranking(self, category, order):
		logger.info("RankingClientS2.get_cached_topx_ranking()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u32(category)
		stream.add(order)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_CACHED_TOPX_RANKING, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		result = stream.extract(RankingCachedResult)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.get_cached_topx_ranking -> done")
		return result
	
	async def get_cached_topx_rankings(self, categories, order):
		logger.info("RankingClientS2.get_cached_topx_rankings()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(categories, stream.u32)
		stream.list(order, stream.add)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_CACHED_TOPX_RANKINGS, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		results = stream.list(RankingCachedResult)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.get_cached_topx_rankings -> done")
		return results
	
	async def upload_league_point(self, info):
		logger.info("RankingClientS2.upload_league_point()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(info)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_UPLOAD_LEAGUE_POINT, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.upload_league_point -> done")
	
	async def get_league_result(self, league_id, tag_id):
		logger.info("RankingClientS2.get_league_result()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.string(league_id)
		stream.u64(tag_id)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_LEAGUE_RESULT, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		result = stream.extract(LeagueResult)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.get_league_result -> done")
		return result
	
	async def get_festival_result(self, festival_id):
		logger.info("RankingClientS2.get_festival_result()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u32(festival_id)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_FESTIVAL_RESULT, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		result = stream.extract(FestivalResult)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.get_festival_result -> done")
		return result
	
	async def upload_festival_vote(self, upload_param):
		logger.info("RankingClientS2.upload_festival_vote()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(upload_param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_UPLOAD_FESTIVAL_VOTE, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.upload_festival_vote -> done")
	
	async def upload_festival_score(self, upload_param):
		logger.info("RankingClientS2.upload_festival_score()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(upload_param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_UPLOAD_FESTIVAL_SCORE, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.upload_festival_score -> done")
	
	async def delete_festival(self, festival_id):
		logger.info("RankingClientS2.delete_festival()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u32(festival_id)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_DELETE_FESTIVAL, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.delete_festival -> done")
	
	async def upload_x_power(self, param):
		logger.info("RankingClientS2.upload_x_power()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_UPLOAD_X_POWER, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		result = stream.extract(XPowerRankingDetail)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.upload_x_power -> done")
		return result
	
	async def get_x_power_ranking(self, params):
		logger.info("RankingClientS2.get_x_power_ranking()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(params, stream.add)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_X_POWER_RANKING, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		results = stream.list(XPowerRanking)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("RankingClientS2.get_x_power_ranking -> done")
		return results


class RankingServerS2(RankingProtocolS2):
	def __init__(self):
		self.methods = {
			self.METHOD_UPLOAD_SCORE: self.handle_upload_score,
			self.METHOD_DELETE_SCORE: self.handle_delete_score,
			self.METHOD_DELETE_ALL_SCORES: self.handle_delete_all_scores,
			self.METHOD_UPLOAD_COMMON_DATA: self.handle_upload_common_data,
			self.METHOD_DELETE_COMMON_DATA: self.handle_delete_common_data,
			self.METHOD_GET_COMMON_DATA: self.handle_get_common_data,
			self.METHOD_CHANGE_ATTRIBUTES: self.handle_change_attributes,
			self.METHOD_CHANGE_ALL_ATTRIBUTES: self.handle_change_all_attributes,
			self.METHOD_GET_RANKING: self.handle_get_ranking,
			self.METHOD_GET_APPROX_ORDER: self.handle_get_approx_order,
			self.METHOD_GET_STATS: self.handle_get_stats,
			self.METHOD_GET_RANKING_BY_PID_LIST: self.handle_get_ranking_by_pid_list,
			self.METHOD_GET_RANKING_BY_UNIQUE_ID_LIST: self.handle_get_ranking_by_unique_id_list,
			self.METHOD_GET_CACHED_TOPX_RANKING: self.handle_get_cached_topx_ranking,
			self.METHOD_GET_CACHED_TOPX_RANKINGS: self.handle_get_cached_topx_rankings,
			self.METHOD_UPLOAD_LEAGUE_POINT: self.handle_upload_league_point,
			self.METHOD_GET_LEAGUE_RESULT: self.handle_get_league_result,
			self.METHOD_GET_FESTIVAL_RESULT: self.handle_get_festival_result,
			self.METHOD_UPLOAD_FESTIVAL_VOTE: self.handle_upload_festival_vote,
			self.METHOD_UPLOAD_FESTIVAL_SCORE: self.handle_upload_festival_score,
			self.METHOD_DELETE_FESTIVAL: self.handle_delete_festival,
			self.METHOD_UPLOAD_X_POWER: self.handle_upload_x_power,
			self.METHOD_GET_X_POWER_RANKING: self.handle_get_x_power_ranking,
		}
	
	async def logout(self, client):
		pass
	
	async def handle(self, client, method_id, input, output):
		if method_id in self.methods:
			await self.methods[method_id](client, input, output)
		else:
			logger.warning("Unknown method called on RankingServerS2: %i", method_id)
			raise common.RMCError("Core::NotImplemented")
	
	async def handle_upload_score(self, client, input, output):
		logger.info("RankingServerS2.upload_score()")
		#--- request ---
		score_data = input.extract(RankingScoreData)
		unique_id = input.u64()
		await self.upload_score(client, score_data, unique_id)
	
	async def handle_delete_score(self, client, input, output):
		logger.info("RankingServerS2.delete_score()")
		#--- request ---
		category = input.u32()
		unique_id = input.u64()
		await self.delete_score(client, category, unique_id)
	
	async def handle_delete_all_scores(self, client, input, output):
		logger.info("RankingServerS2.delete_all_scores()")
		#--- request ---
		unique_id = input.u64()
		await self.delete_all_scores(client, unique_id)
	
	async def handle_upload_common_data(self, client, input, output):
		logger.info("RankingServerS2.upload_common_data()")
		#--- request ---
		common_data = input.buffer()
		unique_id = input.u64()
		await self.upload_common_data(client, common_data, unique_id)
	
	async def handle_delete_common_data(self, client, input, output):
		logger.info("RankingServerS2.delete_common_data()")
		#--- request ---
		unique_id = input.u64()
		await self.delete_common_data(client, unique_id)
	
	async def handle_get_common_data(self, client, input, output):
		logger.info("RankingServerS2.get_common_data()")
		#--- request ---
		unique_id = input.u64()
		response = await self.get_common_data(client, unique_id)
		
		#--- response ---
		if not isinstance(response, bytes):
			raise RuntimeError("Expected bytes, got %s" %response.__class__.__name__)
		output.buffer(response)
	
	async def handle_change_attributes(self, client, input, output):
		logger.info("RankingServerS2.change_attributes()")
		#--- request ---
		category = input.u32()
		param = input.extract(RankingChangeAttributesParam)
		unique_id = input.u64()
		await self.change_attributes(client, category, param, unique_id)
	
	async def handle_change_all_attributes(self, client, input, output):
		logger.info("RankingServerS2.change_all_attributes()")
		#--- request ---
		param = input.extract(RankingChangeAttributesParam)
		unique_id = input.u64()
		await self.change_all_attributes(client, param, unique_id)
	
	async def handle_get_ranking(self, client, input, output):
		logger.info("RankingServerS2.get_ranking()")
		#--- request ---
		mode = input.u8()
		category = input.u32()
		order = input.extract(RankingOrderParam)
		unique_id = input.u64()
		pid = input.pid()
		response = await self.get_ranking(client, mode, category, order, unique_id, pid)
		
		#--- response ---
		if not isinstance(response, RankingResult):
			raise RuntimeError("Expected RankingResult, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_get_approx_order(self, client, input, output):
		logger.info("RankingServerS2.get_approx_order()")
		#--- request ---
		category = input.u32()
		order = input.extract(RankingOrderParam)
		score = input.u32()
		unique_id = input.u64()
		pid = input.pid()
		response = await self.get_approx_order(client, category, order, score, unique_id, pid)
		
		#--- response ---
		if not isinstance(response, int):
			raise RuntimeError("Expected int, got %s" %response.__class__.__name__)
		output.u32(response)
	
	async def handle_get_stats(self, client, input, output):
		logger.info("RankingServerS2.get_stats()")
		#--- request ---
		category = input.u32()
		order = input.extract(RankingOrderParam)
		flags = input.u32()
		response = await self.get_stats(client, category, order, flags)
		
		#--- response ---
		if not isinstance(response, RankingStats):
			raise RuntimeError("Expected RankingStats, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_get_ranking_by_pid_list(self, client, input, output):
		logger.info("RankingServerS2.get_ranking_by_pid_list()")
		#--- request ---
		pids = input.list(input.pid)
		mode = input.u8()
		category = input.u32()
		order = input.extract(RankingOrderParam)
		unique_id = input.u64()
		response = await self.get_ranking_by_pid_list(client, pids, mode, category, order, unique_id)
		
		#--- response ---
		if not isinstance(response, RankingResult):
			raise RuntimeError("Expected RankingResult, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_get_ranking_by_unique_id_list(self, client, input, output):
		logger.info("RankingServerS2.get_ranking_by_unique_id_list()")
		#--- request ---
		ids = input.list(input.u64)
		mode = input.u8()
		category = input.u32()
		order = input.extract(RankingOrderParam)
		unique_id = input.u64()
		response = await self.get_ranking_by_unique_id_list(client, ids, mode, category, order, unique_id)
		
		#--- response ---
		if not isinstance(response, RankingResult):
			raise RuntimeError("Expected RankingResult, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_get_cached_topx_ranking(self, client, input, output):
		logger.info("RankingServerS2.get_cached_topx_ranking()")
		#--- request ---
		category = input.u32()
		order = input.extract(RankingOrderParam)
		response = await self.get_cached_topx_ranking(client, category, order)
		
		#--- response ---
		if not isinstance(response, RankingCachedResult):
			raise RuntimeError("Expected RankingCachedResult, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_get_cached_topx_rankings(self, client, input, output):
		logger.info("RankingServerS2.get_cached_topx_rankings()")
		#--- request ---
		categories = input.list(input.u32)
		order = input.list(RankingOrderParam)
		response = await self.get_cached_topx_rankings(client, categories, order)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.add)
	
	async def handle_upload_league_point(self, client, input, output):
		logger.info("RankingServerS2.upload_league_point()")
		#--- request ---
		info = input.extract(LeaguePointInfo)
		await self.upload_league_point(client, info)
	
	async def handle_get_league_result(self, client, input, output):
		logger.info("RankingServerS2.get_league_result()")
		#--- request ---
		league_id = input.string()
		tag_id = input.u64()
		response = await self.get_league_result(client, league_id, tag_id)
		
		#--- response ---
		if not isinstance(response, LeagueResult):
			raise RuntimeError("Expected LeagueResult, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_get_festival_result(self, client, input, output):
		logger.info("RankingServerS2.get_festival_result()")
		#--- request ---
		festival_id = input.u32()
		response = await self.get_festival_result(client, festival_id)
		
		#--- response ---
		if not isinstance(response, FestivalResult):
			raise RuntimeError("Expected FestivalResult, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_upload_festival_vote(self, client, input, output):
		logger.info("RankingServerS2.upload_festival_vote()")
		#--- request ---
		upload_param = input.extract(FestivalUploadVoteParam)
		await self.upload_festival_vote(client, upload_param)
	
	async def handle_upload_festival_score(self, client, input, output):
		logger.info("RankingServerS2.upload_festival_score()")
		#--- request ---
		upload_param = input.extract(FestivalUploadScoreParam)
		await self.upload_festival_score(client, upload_param)
	
	async def handle_delete_festival(self, client, input, output):
		logger.info("RankingServerS2.delete_festival()")
		#--- request ---
		festival_id = input.u32()
		await self.delete_festival(client, festival_id)
	
	async def handle_upload_x_power(self, client, input, output):
		logger.info("RankingServerS2.upload_x_power()")
		#--- request ---
		param = input.extract(XPowerUploadParam)
		response = await self.upload_x_power(client, param)
		
		#--- response ---
		if not isinstance(response, XPowerRankingDetail):
			raise RuntimeError("Expected XPowerRankingDetail, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_get_x_power_ranking(self, client, input, output):
		logger.info("RankingServerS2.get_x_power_ranking()")
		#--- request ---
		params = input.list(XPowerGetRankingParam)
		response = await self.get_x_power_ranking(client, params)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.add)
	
	async def upload_score(self, *args):
		logger.warning("RankingServerS2.upload_score not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def delete_score(self, *args):
		logger.warning("RankingServerS2.delete_score not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def delete_all_scores(self, *args):
		logger.warning("RankingServerS2.delete_all_scores not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def upload_common_data(self, *args):
		logger.warning("RankingServerS2.upload_common_data not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def delete_common_data(self, *args):
		logger.warning("RankingServerS2.delete_common_data not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_common_data(self, *args):
		logger.warning("RankingServerS2.get_common_data not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def change_attributes(self, *args):
		logger.warning("RankingServerS2.change_attributes not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def change_all_attributes(self, *args):
		logger.warning("RankingServerS2.change_all_attributes not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_ranking(self, *args):
		logger.warning("RankingServerS2.get_ranking not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_approx_order(self, *args):
		logger.warning("RankingServerS2.get_approx_order not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_stats(self, *args):
		logger.warning("RankingServerS2.get_stats not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_ranking_by_pid_list(self, *args):
		logger.warning("RankingServerS2.get_ranking_by_pid_list not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_ranking_by_unique_id_list(self, *args):
		logger.warning("RankingServerS2.get_ranking_by_unique_id_list not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_cached_topx_ranking(self, *args):
		logger.warning("RankingServerS2.get_cached_topx_ranking not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_cached_topx_rankings(self, *args):
		logger.warning("RankingServerS2.get_cached_topx_rankings not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def upload_league_point(self, *args):
		logger.warning("RankingServerS2.upload_league_point not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_league_result(self, *args):
		logger.warning("RankingServerS2.get_league_result not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_festival_result(self, *args):
		logger.warning("RankingServerS2.get_festival_result not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def upload_festival_vote(self, *args):
		logger.warning("RankingServerS2.upload_festival_vote not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def upload_festival_score(self, *args):
		logger.warning("RankingServerS2.upload_festival_score not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def delete_festival(self, *args):
		logger.warning("RankingServerS2.delete_festival not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def upload_x_power(self, *args):
		logger.warning("RankingServerS2.upload_x_power not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_x_power_ranking(self, *args):
		logger.warning("RankingServerS2.get_x_power_ranking not implemented")
		raise common.RMCError("Core::NotImplemented")

