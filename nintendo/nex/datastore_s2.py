
# This file was generated automatically by generate_protocols.py

from nintendo.nex import notification, rmc, common, streams

import logging
logger = logging.getLogger(__name__)


class DataStoreChangeMetaCompareParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.comparison_flag = None
		self.name = None
		self.permission = DataStorePermission()
		self.delete_permission = DataStorePermission()
		self.period = None
		self.meta_binary = None
		self.tags = None
		self.referred_count = None
		self.data_type = None
		self.status = None
	
	def check_required(self, settings, version):
		for field in ['comparison_flag', 'name', 'period', 'meta_binary', 'tags', 'referred_count', 'data_type', 'status']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.comparison_flag = stream.u32()
		self.name = stream.string()
		self.permission = stream.extract(DataStorePermission)
		self.delete_permission = stream.extract(DataStorePermission)
		self.period = stream.u16()
		self.meta_binary = stream.qbuffer()
		self.tags = stream.list(stream.string)
		self.referred_count = stream.u32()
		self.data_type = stream.u16()
		self.status = stream.u8()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u32(self.comparison_flag)
		stream.string(self.name)
		stream.add(self.permission)
		stream.add(self.delete_permission)
		stream.u16(self.period)
		stream.qbuffer(self.meta_binary)
		stream.list(self.tags, stream.string)
		stream.u32(self.referred_count)
		stream.u16(self.data_type)
		stream.u8(self.status)


class DataStoreChangeMetaParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.modifies_flag = None
		self.name = None
		self.permission = DataStorePermission()
		self.delete_permission = DataStorePermission()
		self.period = None
		self.meta_binary = None
		self.tags = None
		self.update_password = None
		self.referred_count = None
		self.data_type = None
		self.status = None
		self.compare_param = DataStoreChangeMetaCompareParam()
		self.persistence_target = DataStorePersistenceTarget()
	
	def check_required(self, settings, version):
		for field in ['data_id', 'modifies_flag', 'name', 'period', 'meta_binary', 'tags', 'update_password', 'referred_count', 'data_type', 'status']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.data_id = stream.u64()
		self.modifies_flag = stream.u32()
		self.name = stream.string()
		self.permission = stream.extract(DataStorePermission)
		self.delete_permission = stream.extract(DataStorePermission)
		self.period = stream.u16()
		self.meta_binary = stream.qbuffer()
		self.tags = stream.list(stream.string)
		self.update_password = stream.u64()
		self.referred_count = stream.u32()
		self.data_type = stream.u16()
		self.status = stream.u8()
		self.compare_param = stream.extract(DataStoreChangeMetaCompareParam)
		self.persistence_target = stream.extract(DataStorePersistenceTarget)
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.data_id)
		stream.u32(self.modifies_flag)
		stream.string(self.name)
		stream.add(self.permission)
		stream.add(self.delete_permission)
		stream.u16(self.period)
		stream.qbuffer(self.meta_binary)
		stream.list(self.tags, stream.string)
		stream.u64(self.update_password)
		stream.u32(self.referred_count)
		stream.u16(self.data_type)
		stream.u8(self.status)
		stream.add(self.compare_param)
		stream.add(self.persistence_target)


class DataStoreChangeMetaParamV1(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.modifies_flag = None
		self.name = None
		self.permission = DataStorePermission()
		self.delete_permission = DataStorePermission()
		self.period = None
		self.meta_binary = None
		self.tags = None
		self.update_password = None
	
	def check_required(self, settings, version):
		for field in ['data_id', 'modifies_flag', 'name', 'period', 'meta_binary', 'tags', 'update_password']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.data_id = stream.u64()
		self.modifies_flag = stream.u32()
		self.name = stream.string()
		self.permission = stream.extract(DataStorePermission)
		self.delete_permission = stream.extract(DataStorePermission)
		self.period = stream.u16()
		self.meta_binary = stream.qbuffer()
		self.tags = stream.list(stream.string)
		self.update_password = stream.u64()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.data_id)
		stream.u32(self.modifies_flag)
		stream.string(self.name)
		stream.add(self.permission)
		stream.add(self.delete_permission)
		stream.u16(self.period)
		stream.qbuffer(self.meta_binary)
		stream.list(self.tags, stream.string)
		stream.u64(self.update_password)


class DataStoreCompletePostParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.success = None
	
	def check_required(self, settings, version):
		for field in ['data_id', 'success']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.data_id = stream.u64()
		self.success = stream.bool()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.data_id)
		stream.bool(self.success)


class DataStoreCompletePostParamV1(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.success = None
	
	def check_required(self, settings, version):
		for field in ['data_id', 'success']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.data_id = stream.u32()
		self.success = stream.bool()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u32(self.data_id)
		stream.bool(self.success)


class DataStoreCompleteUpdateParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.version = None
		self.success = None
	
	def check_required(self, settings, version):
		for field in ['data_id', 'version', 'success']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.data_id = stream.u64()
		self.version = stream.u32()
		self.success = stream.bool()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.data_id)
		stream.u32(self.version)
		stream.bool(self.success)


class DataStoreDeleteParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.update_password = None
	
	def check_required(self, settings, version):
		for field in ['data_id', 'update_password']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.data_id = stream.u64()
		self.update_password = stream.u64()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.data_id)
		stream.u64(self.update_password)


class DataStoreGetMetaParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = 0
		self.persistence_target = DataStorePersistenceTarget()
		self.result_option = 0
		self.access_password = 0
	
	def check_required(self, settings, version):
		pass
	
	def load(self, stream, version):
		self.data_id = stream.u64()
		self.persistence_target = stream.extract(DataStorePersistenceTarget)
		self.result_option = stream.u8()
		self.access_password = stream.u64()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.data_id)
		stream.add(self.persistence_target)
		stream.u8(self.result_option)
		stream.u64(self.access_password)


class DataStoreGetNewArrivedNotificationsParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.last_notification_id = None
		self.limit = None
	
	def check_required(self, settings, version):
		for field in ['last_notification_id', 'limit']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.last_notification_id = stream.u64()
		self.limit = stream.u16()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.last_notification_id)
		stream.u16(self.limit)


class DataStoreGetNotificationUrlParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.previous_url = None
	
	def check_required(self, settings, version):
		for field in ['previous_url']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.previous_url = stream.string()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.string(self.previous_url)


class DataStoreGetSpecificMetaParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_ids = None
	
	def check_required(self, settings, version):
		for field in ['data_ids']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.data_ids = stream.list(stream.u64)
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.list(self.data_ids, stream.u64)


class DataStoreGetSpecificMetaParamV1(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_ids = None
	
	def check_required(self, settings, version):
		for field in ['data_ids']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.data_ids = stream.list(stream.u32)
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.list(self.data_ids, stream.u32)


class DataStoreKeyValue(common.Structure):
	def __init__(self):
		super().__init__()
		self.key = None
		self.value = None
	
	def check_required(self, settings, version):
		for field in ['key', 'value']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.key = stream.string()
		self.value = stream.string()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.string(self.key)
		stream.string(self.value)


class DataStoreMetaInfo(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.owner_id = None
		self.size = None
		self.name = None
		self.data_type = None
		self.meta_binary = None
		self.permission = DataStorePermission()
		self.delete_permission = DataStorePermission()
		self.create_time = None
		self.update_time = None
		self.period = None
		self.status = None
		self.referred_count = None
		self.refer_data_id = None
		self.flag = None
		self.referred_time = None
		self.expire_time = None
		self.tags = None
		self.ratings = None
	
	def check_required(self, settings, version):
		for field in ['data_id', 'owner_id', 'size', 'name', 'data_type', 'meta_binary', 'create_time', 'update_time', 'period', 'status', 'referred_count', 'refer_data_id', 'flag', 'referred_time', 'expire_time', 'tags', 'ratings']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.data_id = stream.u64()
		self.owner_id = stream.pid()
		self.size = stream.u32()
		self.name = stream.string()
		self.data_type = stream.u16()
		self.meta_binary = stream.qbuffer()
		self.permission = stream.extract(DataStorePermission)
		self.delete_permission = stream.extract(DataStorePermission)
		self.create_time = stream.datetime()
		self.update_time = stream.datetime()
		self.period = stream.u16()
		self.status = stream.u8()
		self.referred_count = stream.u32()
		self.refer_data_id = stream.u32()
		self.flag = stream.u32()
		self.referred_time = stream.datetime()
		self.expire_time = stream.datetime()
		self.tags = stream.list(stream.string)
		self.ratings = stream.list(DataStoreRatingInfoWithSlot)
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.data_id)
		stream.pid(self.owner_id)
		stream.u32(self.size)
		stream.string(self.name)
		stream.u16(self.data_type)
		stream.qbuffer(self.meta_binary)
		stream.add(self.permission)
		stream.add(self.delete_permission)
		stream.datetime(self.create_time)
		stream.datetime(self.update_time)
		stream.u16(self.period)
		stream.u8(self.status)
		stream.u32(self.referred_count)
		stream.u32(self.refer_data_id)
		stream.u32(self.flag)
		stream.datetime(self.referred_time)
		stream.datetime(self.expire_time)
		stream.list(self.tags, stream.string)
		stream.list(self.ratings, stream.add)


class DataStoreNotification(common.Structure):
	def __init__(self):
		super().__init__()
		self.notification_id = None
		self.data_id = None
	
	def check_required(self, settings, version):
		for field in ['notification_id', 'data_id']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.notification_id = stream.u64()
		self.data_id = stream.u64()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.notification_id)
		stream.u64(self.data_id)


class DataStoreNotificationV1(common.Structure):
	def __init__(self):
		super().__init__()
		self.notification_id = None
		self.data_id = None
	
	def check_required(self, settings, version):
		for field in ['notification_id', 'data_id']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.notification_id = stream.u64()
		self.data_id = stream.u32()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.notification_id)
		stream.u32(self.data_id)


class DataStorePasswordInfo(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.access_password = None
		self.update_password = None
	
	def check_required(self, settings, version):
		for field in ['data_id', 'access_password', 'update_password']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.data_id = stream.u64()
		self.access_password = stream.u64()
		self.update_password = stream.u64()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.data_id)
		stream.u64(self.access_password)
		stream.u64(self.update_password)


class DataStorePermission(common.Structure):
	def __init__(self):
		super().__init__()
		self.permission = 3
		self.recipients = []
	
	def check_required(self, settings, version):
		pass
	
	def load(self, stream, version):
		self.permission = stream.u8()
		self.recipients = stream.list(stream.pid)
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u8(self.permission)
		stream.list(self.recipients, stream.pid)


class DataStorePersistenceInfo(common.Structure):
	def __init__(self):
		super().__init__()
		self.owner_id = None
		self.slot_id = None
		self.data_id = None
	
	def check_required(self, settings, version):
		for field in ['owner_id', 'slot_id', 'data_id']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.owner_id = stream.pid()
		self.slot_id = stream.u16()
		self.data_id = stream.u64()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.pid(self.owner_id)
		stream.u16(self.slot_id)
		stream.u64(self.data_id)


class DataStorePersistenceInitParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.persistence_id = 65535
		self.delete_last_object = True
	
	def check_required(self, settings, version):
		pass
	
	def load(self, stream, version):
		self.persistence_id = stream.u16()
		self.delete_last_object = stream.bool()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u16(self.persistence_id)
		stream.bool(self.delete_last_object)


class DataStorePersistenceTarget(common.Structure):
	def __init__(self):
		super().__init__()
		self.owner_id = 0
		self.persistence_id = 65535
	
	def check_required(self, settings, version):
		pass
	
	def load(self, stream, version):
		self.owner_id = stream.pid()
		self.persistence_id = stream.u16()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.pid(self.owner_id)
		stream.u16(self.persistence_id)


class DataStorePrepareGetParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = 0
		self.lock_id = 0
		self.persistence_target = DataStorePersistenceTarget()
		self.access_password = 0
		self.extra_data = []
	
	def check_required(self, settings, version):
		if settings["nex.version"] >= 30500:
			pass
	
	def load(self, stream, version):
		self.data_id = stream.u64()
		self.lock_id = stream.u32()
		self.persistence_target = stream.extract(DataStorePersistenceTarget)
		self.access_password = stream.u64()
		if stream.settings["nex.version"] >= 30500:
			self.extra_data = stream.list(stream.string)
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.data_id)
		stream.u32(self.lock_id)
		stream.add(self.persistence_target)
		stream.u64(self.access_password)
		if stream.settings["nex.version"] >= 30500:
			stream.list(self.extra_data, stream.string)


class DataStorePrepareGetParamV1(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.lock_id = 0
	
	def check_required(self, settings, version):
		for field in ['data_id']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.data_id = stream.u32()
		self.lock_id = stream.u32()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u32(self.data_id)
		stream.u32(self.lock_id)


class DataStorePreparePostParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.size = None
		self.name = None
		self.data_type = None
		self.meta_binary = None
		self.permission = DataStorePermission()
		self.delete_permission = DataStorePermission()
		self.flag = None
		self.period = None
		self.refer_data_id = 0
		self.tags = []
		self.rating_init_param = []
		self.persistence_init_param = DataStorePersistenceInitParam()
		self.extra_data = None
	
	def check_required(self, settings, version):
		for field in ['size', 'name', 'data_type', 'meta_binary', 'flag', 'period']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
		if settings["nex.version"] >= 30500:
			for field in ['extra_data']:
				if getattr(self, field) is None:
					raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.size = stream.u32()
		self.name = stream.string()
		self.data_type = stream.u16()
		self.meta_binary = stream.qbuffer()
		self.permission = stream.extract(DataStorePermission)
		self.delete_permission = stream.extract(DataStorePermission)
		self.flag = stream.u32()
		self.period = stream.u16()
		self.refer_data_id = stream.u32()
		self.tags = stream.list(stream.string)
		self.rating_init_param = stream.list(DataStoreRatingInitParamWithSlot)
		self.persistence_init_param = stream.extract(DataStorePersistenceInitParam)
		if stream.settings["nex.version"] >= 30500:
			self.extra_data = stream.list(stream.string)
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u32(self.size)
		stream.string(self.name)
		stream.u16(self.data_type)
		stream.qbuffer(self.meta_binary)
		stream.add(self.permission)
		stream.add(self.delete_permission)
		stream.u32(self.flag)
		stream.u16(self.period)
		stream.u32(self.refer_data_id)
		stream.list(self.tags, stream.string)
		stream.list(self.rating_init_param, stream.add)
		stream.add(self.persistence_init_param)
		if stream.settings["nex.version"] >= 30500:
			stream.list(self.extra_data, stream.string)


class DataStorePreparePostParamV1(common.Structure):
	def __init__(self):
		super().__init__()
		self.size = None
		self.name = None
		self.data_type = 0
		self.meta_binary = b""
		self.permission = DataStorePermission()
		self.delete_permission = DataStorePermission()
		self.flag = None
		self.period = None
		self.refer_data_id = 0
		self.tags = None
		self.rating_init_param = None
	
	def check_required(self, settings, version):
		for field in ['size', 'name', 'flag', 'period', 'tags', 'rating_init_param']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.size = stream.u32()
		self.name = stream.string()
		self.data_type = stream.u16()
		self.meta_binary = stream.qbuffer()
		self.permission = stream.extract(DataStorePermission)
		self.delete_permission = stream.extract(DataStorePermission)
		self.flag = stream.u32()
		self.period = stream.u16()
		self.refer_data_id = stream.u32()
		self.tags = stream.list(stream.string)
		self.rating_init_param = stream.list(DataStoreRatingInitParamWithSlot)
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u32(self.size)
		stream.string(self.name)
		stream.u16(self.data_type)
		stream.qbuffer(self.meta_binary)
		stream.add(self.permission)
		stream.add(self.delete_permission)
		stream.u32(self.flag)
		stream.u16(self.period)
		stream.u32(self.refer_data_id)
		stream.list(self.tags, stream.string)
		stream.list(self.rating_init_param, stream.add)


class DataStorePrepareUpdateParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.size = None
		self.update_password = None
		self.extra_data = None
	
	def check_required(self, settings, version):
		for field in ['data_id', 'size', 'update_password', 'extra_data']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.data_id = stream.u64()
		self.size = stream.u32()
		self.update_password = stream.u64()
		self.extra_data = stream.list(stream.string)
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.data_id)
		stream.u32(self.size)
		stream.u64(self.update_password)
		stream.list(self.extra_data, stream.string)


class DataStoreRateObjectParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.rating_value = None
		self.access_password = None
	
	def check_required(self, settings, version):
		for field in ['rating_value', 'access_password']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.rating_value = stream.s32()
		self.access_password = stream.u64()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.s32(self.rating_value)
		stream.u64(self.access_password)


class DataStoreRatingInfo(common.Structure):
	def __init__(self):
		super().__init__()
		self.total_value = None
		self.count = None
		self.initial_value = None
	
	def check_required(self, settings, version):
		for field in ['total_value', 'count', 'initial_value']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.total_value = stream.s64()
		self.count = stream.u32()
		self.initial_value = stream.s64()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.s64(self.total_value)
		stream.u32(self.count)
		stream.s64(self.initial_value)


class DataStoreRatingInfoWithSlot(common.Structure):
	def __init__(self):
		super().__init__()
		self.slot = None
		self.info = DataStoreRatingInfo()
	
	def check_required(self, settings, version):
		for field in ['slot']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.slot = stream.u8()
		self.info = stream.extract(DataStoreRatingInfo)
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u8(self.slot)
		stream.add(self.info)


class DataStoreRatingInitParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.flag = None
		self.internal_flag = None
		self.lock_type = None
		self.initial_value = None
		self.range_min = None
		self.range_max = None
		self.period_hour = None
		self.period_duration = None
	
	def check_required(self, settings, version):
		for field in ['flag', 'internal_flag', 'lock_type', 'initial_value', 'range_min', 'range_max', 'period_hour', 'period_duration']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.flag = stream.u8()
		self.internal_flag = stream.u8()
		self.lock_type = stream.u8()
		self.initial_value = stream.s64()
		self.range_min = stream.s32()
		self.range_max = stream.s32()
		self.period_hour = stream.s8()
		self.period_duration = stream.s16()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u8(self.flag)
		stream.u8(self.internal_flag)
		stream.u8(self.lock_type)
		stream.s64(self.initial_value)
		stream.s32(self.range_min)
		stream.s32(self.range_max)
		stream.s8(self.period_hour)
		stream.s16(self.period_duration)


class DataStoreRatingInitParamWithSlot(common.Structure):
	def __init__(self):
		super().__init__()
		self.slot = None
		self.param = DataStoreRatingInitParam()
	
	def check_required(self, settings, version):
		for field in ['slot']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.slot = stream.s8()
		self.param = stream.extract(DataStoreRatingInitParam)
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.s8(self.slot)
		stream.add(self.param)


class DataStoreRatingLog(common.Structure):
	def __init__(self):
		super().__init__()
		self.is_rated = None
		self.pid = None
		self.rating_value = None
		self.lock_expiration_time = None
	
	def check_required(self, settings, version):
		for field in ['is_rated', 'pid', 'rating_value', 'lock_expiration_time']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.is_rated = stream.bool()
		self.pid = stream.pid()
		self.rating_value = stream.s32()
		self.lock_expiration_time = stream.datetime()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.bool(self.is_rated)
		stream.pid(self.pid)
		stream.s32(self.rating_value)
		stream.datetime(self.lock_expiration_time)


class DataStoreRatingTarget(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.slot = None
	
	def check_required(self, settings, version):
		for field in ['data_id', 'slot']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.data_id = stream.u64()
		self.slot = stream.s8()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.data_id)
		stream.s8(self.slot)


class DataStoreReqGetAdditionalMeta(common.Structure):
	def __init__(self):
		super().__init__()
		self.owner_id = None
		self.data_type = None
		self.version = None
		self.meta_binary = None
	
	def check_required(self, settings, version):
		for field in ['owner_id', 'data_type', 'version', 'meta_binary']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.owner_id = stream.pid()
		self.data_type = stream.u16()
		self.version = stream.u16()
		self.meta_binary = stream.qbuffer()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.pid(self.owner_id)
		stream.u16(self.data_type)
		stream.u16(self.version)
		stream.qbuffer(self.meta_binary)


class DataStoreReqGetInfo(common.Structure):
	def __init__(self):
		super().__init__()
		self.url = None
		self.headers = None
		self.size = None
		self.root_ca_cert = None
		self.data_id = None
	
	def check_required(self, settings, version):
		for field in ['url', 'headers', 'size', 'root_ca_cert']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
		if settings["nex.version"] >= 30500:
			for field in ['data_id']:
				if getattr(self, field) is None:
					raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.url = stream.string()
		self.headers = stream.list(DataStoreKeyValue)
		self.size = stream.u32()
		self.root_ca_cert = stream.buffer()
		if stream.settings["nex.version"] >= 30500:
			self.data_id = stream.u64()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.string(self.url)
		stream.list(self.headers, stream.add)
		stream.u32(self.size)
		stream.buffer(self.root_ca_cert)
		if stream.settings["nex.version"] >= 30500:
			stream.u64(self.data_id)


class DataStoreReqGetInfoV1(common.Structure):
	def __init__(self):
		super().__init__()
		self.url = None
		self.headers = None
		self.size = None
		self.root_ca_cert = None
	
	def check_required(self, settings, version):
		for field in ['url', 'headers', 'size', 'root_ca_cert']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.url = stream.string()
		self.headers = stream.list(DataStoreKeyValue)
		self.size = stream.u32()
		self.root_ca_cert = stream.buffer()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.string(self.url)
		stream.list(self.headers, stream.add)
		stream.u32(self.size)
		stream.buffer(self.root_ca_cert)


class DataStoreReqGetNotificationUrlInfo(common.Structure):
	def __init__(self):
		super().__init__()
		self.url = None
		self.key = None
		self.query = None
		self.root_ca_cert = None
	
	def check_required(self, settings, version):
		for field in ['url', 'key', 'query', 'root_ca_cert']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.url = stream.string()
		self.key = stream.string()
		self.query = stream.string()
		self.root_ca_cert = stream.buffer()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.string(self.url)
		stream.string(self.key)
		stream.string(self.query)
		stream.buffer(self.root_ca_cert)


class DataStoreReqPostInfo(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.url = None
		self.headers = None
		self.form = None
		self.root_ca_cert = None
	
	def check_required(self, settings, version):
		for field in ['data_id', 'url', 'headers', 'form', 'root_ca_cert']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.data_id = stream.u64()
		self.url = stream.string()
		self.headers = stream.list(DataStoreKeyValue)
		self.form = stream.list(DataStoreKeyValue)
		self.root_ca_cert = stream.buffer()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.data_id)
		stream.string(self.url)
		stream.list(self.headers, stream.add)
		stream.list(self.form, stream.add)
		stream.buffer(self.root_ca_cert)


class DataStoreReqPostInfoV1(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.url = None
		self.headers = None
		self.form = None
		self.root_ca_cert = None
	
	def check_required(self, settings, version):
		for field in ['data_id', 'url', 'headers', 'form', 'root_ca_cert']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.data_id = stream.u32()
		self.url = stream.string()
		self.headers = stream.list(DataStoreKeyValue)
		self.form = stream.list(DataStoreKeyValue)
		self.root_ca_cert = stream.buffer()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u32(self.data_id)
		stream.string(self.url)
		stream.list(self.headers, stream.add)
		stream.list(self.form, stream.add)
		stream.buffer(self.root_ca_cert)


class DataStoreReqUpdateInfo(common.Structure):
	def __init__(self):
		super().__init__()
		self.version = None
		self.url = None
		self.headers = None
		self.form = None
		self.root_ca_cert = None
	
	def check_required(self, settings, version):
		for field in ['version', 'url', 'headers', 'form', 'root_ca_cert']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.version = stream.u32()
		self.url = stream.string()
		self.headers = stream.list(DataStoreKeyValue)
		self.form = stream.list(DataStoreKeyValue)
		self.root_ca_cert = stream.buffer()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u32(self.version)
		stream.string(self.url)
		stream.list(self.headers, stream.add)
		stream.list(self.form, stream.add)
		stream.buffer(self.root_ca_cert)


class DataStoreSearchParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.search_target = 1
		self.owner_ids = []
		self.owner_type = 0
		self.destination_ids = []
		self.data_type = 65535
		self.created_after = common.DateTime(671076024059)
		self.created_before = common.DateTime(671076024059)
		self.updated_after = common.DateTime(671076024059)
		self.updated_before = common.DateTime(671076024059)
		self.refer_data_id = 0
		self.tags = []
		self.result_order_column = 0
		self.result_order = 0
		self.result_range = common.ResultRange()
		self.result_option = 0
		self.minimal_rating_frequency = 0
		self.use_cache = False
		self.total_count_enabled = True
		self.data_types = []
	
	def check_required(self, settings, version):
		pass
	
	def load(self, stream, version):
		self.search_target = stream.u8()
		self.owner_ids = stream.list(stream.pid)
		self.owner_type = stream.u8()
		self.destination_ids = stream.list(stream.u64)
		self.data_type = stream.u16()
		self.created_after = stream.datetime()
		self.created_before = stream.datetime()
		self.updated_after = stream.datetime()
		self.updated_before = stream.datetime()
		self.refer_data_id = stream.u32()
		self.tags = stream.list(stream.string)
		self.result_order_column = stream.u8()
		self.result_order = stream.u8()
		self.result_range = stream.extract(common.ResultRange)
		self.result_option = stream.u8()
		self.minimal_rating_frequency = stream.u32()
		self.use_cache = stream.bool()
		self.total_count_enabled = stream.bool()
		self.data_types = stream.list(stream.u16)
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u8(self.search_target)
		stream.list(self.owner_ids, stream.pid)
		stream.u8(self.owner_type)
		stream.list(self.destination_ids, stream.u64)
		stream.u16(self.data_type)
		stream.datetime(self.created_after)
		stream.datetime(self.created_before)
		stream.datetime(self.updated_after)
		stream.datetime(self.updated_before)
		stream.u32(self.refer_data_id)
		stream.list(self.tags, stream.string)
		stream.u8(self.result_order_column)
		stream.u8(self.result_order)
		stream.add(self.result_range)
		stream.u8(self.result_option)
		stream.u32(self.minimal_rating_frequency)
		stream.bool(self.use_cache)
		stream.bool(self.total_count_enabled)
		stream.list(self.data_types, stream.u16)


class DataStoreSearchResult(common.Structure):
	def __init__(self):
		super().__init__()
		self.total_count = None
		self.result = None
		self.total_count_type = None
	
	def check_required(self, settings, version):
		for field in ['total_count', 'result', 'total_count_type']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.total_count = stream.u32()
		self.result = stream.list(DataStoreMetaInfo)
		self.total_count_type = stream.u8()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u32(self.total_count)
		stream.list(self.result, stream.add)
		stream.u8(self.total_count_type)


class DataStoreSpecificMetaInfo(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.owner_id = None
		self.size = None
		self.data_type = None
		self.version = None
	
	def check_required(self, settings, version):
		for field in ['data_id', 'owner_id', 'size', 'data_type', 'version']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.data_id = stream.u64()
		self.owner_id = stream.pid()
		self.size = stream.u32()
		self.data_type = stream.u16()
		self.version = stream.u32()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.data_id)
		stream.pid(self.owner_id)
		stream.u32(self.size)
		stream.u16(self.data_type)
		stream.u32(self.version)


class DataStoreSpecificMetaInfoV1(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.owner_id = None
		self.size = None
		self.data_type = None
		self.version = None
	
	def check_required(self, settings, version):
		for field in ['data_id', 'owner_id', 'size', 'data_type', 'version']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.data_id = stream.u32()
		self.owner_id = stream.pid()
		self.size = stream.u32()
		self.data_type = stream.u16()
		self.version = stream.u16()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u32(self.data_id)
		stream.pid(self.owner_id)
		stream.u32(self.size)
		stream.u16(self.data_type)
		stream.u16(self.version)


class DataStoreTouchObjectParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.lock_id = None
		self.access_password = None
	
	def check_required(self, settings, version):
		for field in ['data_id', 'lock_id', 'access_password']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.data_id = stream.u64()
		self.lock_id = stream.u32()
		self.access_password = stream.u64()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.data_id)
		stream.u32(self.lock_id)
		stream.u64(self.access_password)


class CoconutMeta(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.tweet_id = None
		self.region = None
		self.post_type = None
		self.theme_id = None
		self.festival_id = None
		self.language = None
		self.binary_data = None
	
	def check_required(self, settings, version):
		for field in ['data_id', 'tweet_id', 'region', 'post_type', 'theme_id', 'festival_id', 'language', 'binary_data']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.data_id = stream.u64()
		self.tweet_id = stream.u64()
		self.region = stream.u8()
		self.post_type = stream.u8()
		self.theme_id = stream.u8()
		self.festival_id = stream.u32()
		self.language = stream.string()
		self.binary_data = stream.qbuffer()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.data_id)
		stream.u64(self.tweet_id)
		stream.u8(self.region)
		stream.u8(self.post_type)
		stream.u8(self.theme_id)
		stream.u32(self.festival_id)
		stream.string(self.language)
		stream.qbuffer(self.binary_data)


class CoconutGetInfo(common.Structure):
	def __init__(self):
		super().__init__()
		self.info = DataStoreReqGetInfo()
		self.meta = CoconutMeta()
	
	def check_required(self, settings, version):
		pass
	
	def load(self, stream, version):
		self.info = stream.extract(DataStoreReqGetInfo)
		self.meta = stream.extract(CoconutMeta)
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.add(self.info)
		stream.add(self.meta)


class CoconutGetParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.unique_ids = None
		self.get_type = None
		self.region = None
		self.festival_id = None
	
	def check_required(self, settings, version):
		for field in ['unique_ids', 'get_type', 'region', 'festival_id']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.unique_ids = stream.list(stream.u64)
		self.get_type = stream.u8()
		self.region = stream.u8()
		self.festival_id = stream.u32()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.list(self.unique_ids, stream.u64)
		stream.u8(self.get_type)
		stream.u8(self.region)
		stream.u32(self.festival_id)


class CoconutViolation(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.category_code = None
		self.reason = None
	
	def check_required(self, settings, version):
		for field in ['data_id', 'category_code', 'reason']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.data_id = stream.u64()
		self.category_code = stream.string()
		self.reason = stream.string()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.data_id)
		stream.string(self.category_code)
		stream.string(self.reason)


class OrderedInfo(common.Structure):
	def __init__(self):
		super().__init__()
		self.gear_kind = None
		self.gear_id = None
		self.skill_id = None
		self.price = None
	
	def check_required(self, settings, version):
		for field in ['gear_kind', 'gear_id', 'skill_id', 'price']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.gear_kind = stream.s32()
		self.gear_id = stream.s32()
		self.skill_id = stream.s32()
		self.price = stream.s32()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.s32(self.gear_kind)
		stream.s32(self.gear_id)
		stream.s32(self.skill_id)
		stream.s32(self.price)


class PlayLogEntry(common.Structure):
	def __init__(self):
		super().__init__()
		self.user_id = None
		self.player_name = None
		self.unknown = None
		self.properties = None
	
	def check_required(self, settings, version):
		for field in ['user_id', 'player_name', 'unknown', 'properties']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.user_id = stream.pid()
		self.player_name = stream.string()
		self.unknown = stream.u64()
		self.properties = stream.map(stream.string, stream.variant)
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.pid(self.user_id)
		stream.string(self.player_name)
		stream.u64(self.unknown)
		stream.map(self.properties, stream.string, stream.variant)


class PlayLogPrepareGetParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.unknown0 = None
		self.unknown1 = None
		self.unknown2 = None
	
	def check_required(self, settings, version):
		for field in ['unknown0', 'unknown1', 'unknown2']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.unknown0 = stream.u64()
		self.unknown1 = stream.datetime()
		self.unknown2 = stream.u32()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u64(self.unknown0)
		stream.datetime(self.unknown1)
		stream.u32(self.unknown2)


class PlayLogPreparePostParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.entries = None
		self.play_time = None
		self.stage_id = None
		self.unknown0 = None
		self.properties = None
	
	def check_required(self, settings, version):
		for field in ['entries', 'play_time', 'stage_id', 'unknown0', 'properties']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.entries = stream.list(PlayLogEntry)
		self.play_time = stream.datetime()
		self.stage_id = stream.u32()
		self.unknown0 = stream.u32()
		self.properties = stream.map(stream.string, stream.variant)
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.list(self.entries, stream.add)
		stream.datetime(self.play_time)
		stream.u32(self.stage_id)
		stream.u32(self.unknown0)
		stream.map(self.properties, stream.string, stream.variant)


class StageTimeAttackInfo(common.Structure):
	def __init__(self):
		super().__init__()
		self.clear_weapons = None
	
	def check_required(self, settings, version):
		for field in ['clear_weapons']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.clear_weapons = stream.map(stream.s32, StageTimeAttackWeapon)
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.map(self.clear_weapons, stream.s32, stream.add)


class StageTimeAttackWeapon(common.Structure):
	def __init__(self):
		super().__init__()
		self.weapon_level = None
		self.clear_time = None
	
	def check_required(self, settings, version):
		for field in ['weapon_level', 'clear_time']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.weapon_level = stream.s32()
		self.clear_time = stream.s32()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.s32(self.weapon_level)
		stream.s32(self.clear_time)


class TimeAttackInfo(common.Structure):
	def __init__(self):
		super().__init__()
		self.stage_infos = None
	
	def check_required(self, settings, version):
		for field in ['stage_infos']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.stage_infos = stream.map(stream.s32, StageTimeAttackInfo)
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.map(self.stage_infos, stream.s32, stream.add)


class CalicoPlayerResult(common.Structure):
	def __init__(self):
		super().__init__()
		self.player_simple = CalicoPlayerSimple()
		self.kill_count = None
		self.assist_count = None
		self.death_count = None
		self.special_count = None
		self.game_paint_point = None
		self.sort_score = None
	
	def check_required(self, settings, version):
		for field in ['kill_count', 'assist_count', 'death_count', 'special_count', 'game_paint_point', 'sort_score']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.player_simple = stream.extract(CalicoPlayerSimple)
		self.kill_count = stream.s32()
		self.assist_count = stream.s32()
		self.death_count = stream.s32()
		self.special_count = stream.s32()
		self.game_paint_point = stream.s32()
		self.sort_score = stream.s32()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.add(self.player_simple)
		stream.s32(self.kill_count)
		stream.s32(self.assist_count)
		stream.s32(self.death_count)
		stream.s32(self.special_count)
		stream.s32(self.game_paint_point)
		stream.s32(self.sort_score)


class CalicoPlayerSimple(common.Structure):
	def __init__(self):
		super().__init__()
		self.pid = None
		self.name = None
		self.player_type = None
		self.udemae = None
		self.player_rank = None
		self.star_rank = None
		self.fes_grade = None
		self.weapon_id = None
		self.head_id = None
		self.head_skill_ids = None
		self.clothes_ids = None
		self.clothes_skill_ids = None
		self.shoes_id = None
		self.shoes_skill_ids = None
	
	def check_required(self, settings, version):
		for field in ['pid', 'name', 'player_type', 'udemae', 'player_rank', 'star_rank', 'fes_grade', 'weapon_id', 'head_id', 'head_skill_ids', 'clothes_ids', 'clothes_skill_ids', 'shoes_id', 'shoes_skill_ids']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.pid = stream.pid()
		self.name = stream.string()
		self.player_type = stream.u8()
		self.udemae = stream.s32()
		self.player_rank = stream.s32()
		self.star_rank = stream.s32()
		self.fes_grade = stream.s32()
		self.weapon_id = stream.s32()
		self.head_id = stream.s32()
		self.head_skill_ids = stream.list(stream.s32)
		self.clothes_ids = stream.s32()
		self.clothes_skill_ids = stream.list(stream.s32)
		self.shoes_id = stream.s32()
		self.shoes_skill_ids = stream.list(stream.s32)
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.pid(self.pid)
		stream.string(self.name)
		stream.u8(self.player_type)
		stream.s32(self.udemae)
		stream.s32(self.player_rank)
		stream.s32(self.star_rank)
		stream.s32(self.fes_grade)
		stream.s32(self.weapon_id)
		stream.s32(self.head_id)
		stream.list(self.head_skill_ids, stream.s32)
		stream.s32(self.clothes_ids)
		stream.list(self.clothes_skill_ids, stream.s32)
		stream.s32(self.shoes_id)
		stream.list(self.shoes_skill_ids, stream.s32)


class CalicoStatsBase(common.Structure):
	def __init__(self):
		super().__init__()
		self.game_mode = None
		self.rule = None
		self.result = None
		self.stage = None
		self.player_result = CalicoPlayerResult()
		self.my_team_members = None
		self.other_team_members = None
		self.weapon_paint_point = None
		self.start_time = None
		self.battle_num = None
		self.player_rank = None
		self.star_rank = None
	
	def check_required(self, settings, version):
		for field in ['game_mode', 'rule', 'result', 'stage', 'my_team_members', 'other_team_members', 'weapon_paint_point', 'start_time', 'battle_num', 'player_rank', 'star_rank']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.game_mode = stream.u32()
		self.rule = stream.s32()
		self.result = stream.u8()
		self.stage = stream.s32()
		self.player_result = stream.extract(CalicoPlayerResult)
		self.my_team_members = stream.list(CalicoPlayerResult)
		self.other_team_members = stream.list(CalicoPlayerResult)
		self.weapon_paint_point = stream.s32()
		self.start_time = stream.datetime()
		self.battle_num = stream.u64()
		self.player_rank = stream.s32()
		self.star_rank = stream.s32()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u32(self.game_mode)
		stream.s32(self.rule)
		stream.u8(self.result)
		stream.s32(self.stage)
		stream.add(self.player_result)
		stream.list(self.my_team_members, stream.add)
		stream.list(self.other_team_members, stream.add)
		stream.s32(self.weapon_paint_point)
		stream.datetime(self.start_time)
		stream.u64(self.battle_num)
		stream.s32(self.player_rank)
		stream.s32(self.star_rank)


class CalicoRegularStats(CalicoStatsBase):
	def __init__(self):
		super().__init__()
		self.my_team_percentage = None
		self.other_team_percentage = None
		self.win_meter = None
	
	def check_required(self, settings, version):
		for field in ['my_team_percentage', 'other_team_percentage', 'win_meter']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.my_team_percentage = stream.s32()
		self.other_team_percentage = stream.s32()
		self.win_meter = stream.s32()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.s32(self.my_team_percentage)
		stream.s32(self.other_team_percentage)
		stream.s32(self.win_meter)
common.DataHolder.register(CalicoRegularStats, "CalicoRegularStats")


class CalicoGachiStats(CalicoStatsBase):
	def __init__(self):
		super().__init__()
		self.elapsed_time = None
		self.my_team_count = None
		self.other_team_count = None
		self.udemae = None
		self.estimate_gachi_power = None
	
	def check_required(self, settings, version):
		for field in ['elapsed_time', 'my_team_count', 'other_team_count', 'udemae', 'estimate_gachi_power']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.elapsed_time = stream.s32()
		self.my_team_count = stream.s8()
		self.other_team_count = stream.s8()
		self.udemae = stream.s32()
		self.estimate_gachi_power = stream.s32()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.s32(self.elapsed_time)
		stream.s8(self.my_team_count)
		stream.s8(self.other_team_count)
		stream.s32(self.udemae)
		stream.s32(self.estimate_gachi_power)
common.DataHolder.register(CalicoGachiStats, "CalicoGachiStats")


class CalicoLeagueStats(CalicoGachiStats):
	def __init__(self):
		super().__init__()
		self.league_id = None
		self.tag_id = None
		self.league_point = None
		self.max_league_point = None
		self.my_estimate_league_point = None
		self.other_estimate_league_point = None
	
	def check_required(self, settings, version):
		for field in ['league_id', 'tag_id', 'league_point', 'max_league_point', 'my_estimate_league_point', 'other_estimate_league_point']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.league_id = stream.string()
		self.tag_id = stream.u64()
		self.league_point = stream.s32()
		self.max_league_point = stream.s32()
		self.my_estimate_league_point = stream.s32()
		self.other_estimate_league_point = stream.s32()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.string(self.league_id)
		stream.u64(self.tag_id)
		stream.s32(self.league_point)
		stream.s32(self.max_league_point)
		stream.s32(self.my_estimate_league_point)
		stream.s32(self.other_estimate_league_point)
common.DataHolder.register(CalicoLeagueStats, "CalicoLeagueStats")


class CalicoFesStats(CalicoRegularStats):
	def __init__(self):
		super().__init__()
		self.fes_id = None
		self.theme_id = None
		self.fes_grade = None
		self.fes_point = None
		self.fes_power = None
		self.max_fes_power = None
		self.my_estimate_fes_power = None
		self.other_estimate_fes_power = None
	
	def check_required(self, settings, version):
		for field in ['fes_id', 'theme_id', 'fes_grade', 'fes_point', 'fes_power', 'max_fes_power', 'my_estimate_fes_power', 'other_estimate_fes_power']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.fes_id = stream.u32()
		self.theme_id = stream.u8()
		self.fes_grade = stream.s32()
		self.fes_point = stream.s32()
		self.fes_power = stream.u32()
		self.max_fes_power = stream.u32()
		self.my_estimate_fes_power = stream.s32()
		self.other_estimate_fes_power = stream.s32()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u32(self.fes_id)
		stream.u8(self.theme_id)
		stream.s32(self.fes_grade)
		stream.s32(self.fes_point)
		stream.u32(self.fes_power)
		stream.u32(self.max_fes_power)
		stream.s32(self.my_estimate_fes_power)
		stream.s32(self.other_estimate_fes_power)
common.DataHolder.register(CalicoFesStats, "CalicoFesStats")


class CalicoFesStatsV2(CalicoFesStats):
	def __init__(self):
		super().__init__()
		self.other_theme_id = None
	
	def check_required(self, settings, version):
		for field in ['other_theme_id']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.other_theme_id = stream.u8()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.u8(self.other_theme_id)
common.DataHolder.register(CalicoFesStatsV2, "CalicoFesStatsV2")


class CalicoXStats(CalicoGachiStats):
	def __init__(self):
		super().__init__()
		self.crown_players = None
		self.estimate_x_power = None
		self.x_power = None
		self.rank = None
	
	def check_required(self, settings, version):
		for field in ['crown_players', 'estimate_x_power', 'x_power', 'rank']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream, version):
		self.crown_players = stream.list(stream.u64)
		self.estimate_x_power = stream.s32()
		self.x_power = stream.s32()
		self.rank = stream.s32()
	
	def save(self, stream, version):
		self.check_required(stream.settings, version)
		stream.list(self.crown_players, stream.u64)
		stream.s32(self.estimate_x_power)
		stream.s32(self.x_power)
		stream.s32(self.rank)
common.DataHolder.register(CalicoXStats, "CalicoXStats")


class DataStoreProtocolS2:
	METHOD_PREPARE_GET_OBJECT_V1 = 1
	METHOD_PREPARE_POST_OBJECT_V1 = 2
	METHOD_COMPLETE_POST_OBJECT_V1 = 3
	METHOD_DELETE_OBJECT = 4
	METHOD_DELETE_OBJECTS = 5
	METHOD_CHANGE_META_V1 = 6
	METHOD_CHANGE_METAS_V1 = 7
	METHOD_GET_META = 8
	METHOD_GET_METAS = 9
	METHOD_PREPARE_UPDATE_OBJECT = 10
	METHOD_COMPLETE_UPDATE_OBJECT = 11
	METHOD_SEARCH_OBJECT = 12
	METHOD_GET_NOTIFICATION_URL = 13
	METHOD_GET_NEW_ARRIVED_NOTIFICATIONS_V1 = 14
	METHOD_RATE_OBJECT = 15
	METHOD_GET_RATING = 16
	METHOD_GET_RATINGS = 17
	METHOD_RESET_RATING = 18
	METHOD_RESET_RATINGS = 19
	METHOD_GET_SPECIFIC_META_V1 = 20
	METHOD_POST_META_BINARY = 21
	METHOD_TOUCH_OBJECT = 22
	METHOD_GET_RATING_WITH_LOG = 23
	METHOD_PREPARE_POST_OBJECT = 24
	METHOD_PREPARE_GET_OBJECT = 25
	METHOD_COMPLETE_POST_OBJECT = 26
	METHOD_GET_NEW_ARRIVED_NOTIFICATIONS = 27
	METHOD_GET_SPECIFIC_META = 28
	METHOD_GET_PERSISTENCE_INFO = 29
	METHOD_GET_PERSISTENCE_INFOS = 30
	METHOD_PERPETUATE_OBJECT = 31
	METHOD_UNPERPETUATE_OBJECT = 32
	METHOD_PREPARE_GET_OBJECT_OR_META_BINARY = 33
	METHOD_GET_PASSWORD_INFO = 34
	METHOD_GET_PASSWORD_INFOS = 35
	METHOD_GET_METAS_MULTIPLE_PARAM = 36
	METHOD_COMPLETE_POST_OBJECTS = 37
	METHOD_CHANGE_META = 38
	METHOD_CHANGE_METAS = 39
	METHOD_RATE_OBJECTS = 40
	METHOD_POST_META_BINARY_WITH_DATA_ID = 41
	METHOD_POST_META_BINARIES_WITH_DATA_ID = 42
	METHOD_RATE_OBJECT_WITH_POSTING = 43
	METHOD_RATE_OBJECTS_WITH_POSTING = 44
	METHOD_GET_OBJECT_INFOS = 45
	METHOD_SEARCH_OBJECT_LIGHT = 46
	METHOD_COCONUT_REGISTER_META = 47
	METHOD_COCONUT_RATE_POST = 48
	METHOD_COCONUT_GET_OBJECT_INFOS = 49
	METHOD_COCONUT_REPORT_VIOLATION = 50
	METHOD_UPLOAD_REGULAR_MATCH_RESULT = 51
	METHOD_UPLOAD_GACHI_MATCH_RESULT = 52
	METHOD_UPLOAD_LEAGUE_MATCH_RESULT = 53
	METHOD_UPLOAD_FES_MATCH_RESULT = 54
	METHOD_GET_ORDERED_GEAR = 55
	METHOD_PURCHASE_GEAR = 56
	METHOD_UPLOAD_TIME_ATTACK = 57
	METHOD_COCONUT_REGISTER_META_BY_PARAM = 58
	METHOD_UPLOAD_FES_MATCH_RESULT_V2 = 59
	METHOD_UPLOAD_X_MATCH_RESULT = 60
	METHOD_PREPARE_POST_PLAY_LOG = 66
	METHOD_PREPARE_GET_PLAY_LOG = 67
	
	PROTOCOL_ID = 0x73


class DataStoreClientS2(DataStoreProtocolS2):
	def __init__(self, client):
		self.settings = client.settings
		self.client = client
	
	async def prepare_get_object_v1(self, param):
		logger.info("DataStoreClientS2.prepare_get_object_v1()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_PREPARE_GET_OBJECT_V1, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		info = stream.extract(DataStoreReqGetInfoV1)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.prepare_get_object_v1 -> done")
		return info
	
	async def prepare_post_object_v1(self, param):
		logger.info("DataStoreClientS2.prepare_post_object_v1()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_PREPARE_POST_OBJECT_V1, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		info = stream.extract(DataStoreReqPostInfoV1)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.prepare_post_object_v1 -> done")
		return info
	
	async def complete_post_object_v1(self, param):
		logger.info("DataStoreClientS2.complete_post_object_v1()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_COMPLETE_POST_OBJECT_V1, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.complete_post_object_v1 -> done")
	
	async def delete_object(self, param):
		logger.info("DataStoreClientS2.delete_object()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_DELETE_OBJECT, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.delete_object -> done")
	
	async def delete_objects(self, param, transactional):
		logger.info("DataStoreClientS2.delete_objects()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(param, stream.add)
		stream.bool(transactional)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_DELETE_OBJECTS, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		results = stream.list(stream.result)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.delete_objects -> done")
		return results
	
	async def change_meta_v1(self, param):
		logger.info("DataStoreClientS2.change_meta_v1()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_CHANGE_META_V1, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.change_meta_v1 -> done")
	
	async def change_metas_v1(self, data_ids, param, transactional):
		logger.info("DataStoreClientS2.change_metas_v1()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(data_ids, stream.u64)
		stream.list(param, stream.add)
		stream.bool(transactional)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_CHANGE_METAS_V1, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		results = stream.list(stream.result)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.change_metas_v1 -> done")
		return results
	
	async def get_meta(self, param):
		logger.info("DataStoreClientS2.get_meta()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_META, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		info = stream.extract(DataStoreMetaInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.get_meta -> done")
		return info
	
	async def get_metas(self, data_ids, param):
		logger.info("DataStoreClientS2.get_metas()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(data_ids, stream.u64)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_METAS, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		obj = rmc.RMCResponse()
		obj.info = stream.list(DataStoreMetaInfo)
		obj.results = stream.list(stream.result)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.get_metas -> done")
		return obj
	
	async def prepare_update_object(self, param):
		logger.info("DataStoreClientS2.prepare_update_object()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_PREPARE_UPDATE_OBJECT, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		info = stream.extract(DataStoreReqUpdateInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.prepare_update_object -> done")
		return info
	
	async def complete_update_object(self, param):
		logger.info("DataStoreClientS2.complete_update_object()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_COMPLETE_UPDATE_OBJECT, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.complete_update_object -> done")
	
	async def search_object(self, param):
		logger.info("DataStoreClientS2.search_object()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_SEARCH_OBJECT, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		result = stream.extract(DataStoreSearchResult)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.search_object -> done")
		return result
	
	async def get_notification_url(self, param):
		logger.info("DataStoreClientS2.get_notification_url()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_NOTIFICATION_URL, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		info = stream.extract(DataStoreReqGetNotificationUrlInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.get_notification_url -> done")
		return info
	
	async def get_new_arrived_notifications_v1(self, param):
		logger.info("DataStoreClientS2.get_new_arrived_notifications_v1()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_NEW_ARRIVED_NOTIFICATIONS_V1, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		obj = rmc.RMCResponse()
		obj.result = stream.list(DataStoreNotificationV1)
		obj.has_next = stream.bool()
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.get_new_arrived_notifications_v1 -> done")
		return obj
	
	async def rate_object(self, target, param, fetch_ratings):
		logger.info("DataStoreClientS2.rate_object()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(target)
		stream.add(param)
		stream.bool(fetch_ratings)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_RATE_OBJECT, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		info = stream.extract(DataStoreRatingInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.rate_object -> done")
		return info
	
	async def get_rating(self, target, access_password):
		logger.info("DataStoreClientS2.get_rating()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(target)
		stream.u64(access_password)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_RATING, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		rating = stream.extract(DataStoreRatingInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.get_rating -> done")
		return rating
	
	async def get_ratings(self, data_ids, access_password):
		logger.info("DataStoreClientS2.get_ratings()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(data_ids, stream.u64)
		stream.u64(access_password)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_RATINGS, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		obj = rmc.RMCResponse()
		obj.ratings = stream.list(lambda: stream.list(DataStoreRatingInfoWithSlot))
		obj.results = stream.list(stream.result)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.get_ratings -> done")
		return obj
	
	async def reset_rating(self, target, update_password):
		logger.info("DataStoreClientS2.reset_rating()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(target)
		stream.u64(update_password)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_RESET_RATING, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.reset_rating -> done")
	
	async def reset_ratings(self, data_ids, transactional):
		logger.info("DataStoreClientS2.reset_ratings()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(data_ids, stream.u64)
		stream.bool(transactional)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_RESET_RATINGS, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		results = stream.list(stream.result)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.reset_ratings -> done")
		return results
	
	async def get_specific_meta_v1(self, param):
		logger.info("DataStoreClientS2.get_specific_meta_v1()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_SPECIFIC_META_V1, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		infos = stream.list(DataStoreSpecificMetaInfoV1)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.get_specific_meta_v1 -> done")
		return infos
	
	async def post_meta_binary(self, param):
		logger.info("DataStoreClientS2.post_meta_binary()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_POST_META_BINARY, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		data_id = stream.u64()
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.post_meta_binary -> done")
		return data_id
	
	async def touch_object(self, param):
		logger.info("DataStoreClientS2.touch_object()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_TOUCH_OBJECT, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.touch_object -> done")
	
	async def get_rating_with_log(self, target, access_password):
		logger.info("DataStoreClientS2.get_rating_with_log()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(target)
		stream.u64(access_password)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_RATING_WITH_LOG, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		obj = rmc.RMCResponse()
		obj.rating = stream.extract(DataStoreRatingInfo)
		obj.log = stream.extract(DataStoreRatingLog)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.get_rating_with_log -> done")
		return obj
	
	async def prepare_post_object(self, param):
		logger.info("DataStoreClientS2.prepare_post_object()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_PREPARE_POST_OBJECT, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		info = stream.extract(DataStoreReqPostInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.prepare_post_object -> done")
		return info
	
	async def prepare_get_object(self, param):
		logger.info("DataStoreClientS2.prepare_get_object()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_PREPARE_GET_OBJECT, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		info = stream.extract(DataStoreReqGetInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.prepare_get_object -> done")
		return info
	
	async def complete_post_object(self, param):
		logger.info("DataStoreClientS2.complete_post_object()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_COMPLETE_POST_OBJECT, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.complete_post_object -> done")
	
	async def get_new_arrived_notifications(self, param):
		logger.info("DataStoreClientS2.get_new_arrived_notifications()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_NEW_ARRIVED_NOTIFICATIONS, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		obj = rmc.RMCResponse()
		obj.result = stream.list(DataStoreNotification)
		obj.has_next = stream.bool()
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.get_new_arrived_notifications -> done")
		return obj
	
	async def get_specific_meta(self, param):
		logger.info("DataStoreClientS2.get_specific_meta()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_SPECIFIC_META, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		infos = stream.list(DataStoreSpecificMetaInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.get_specific_meta -> done")
		return infos
	
	async def get_persistence_info(self, owner_id, slot_id):
		logger.info("DataStoreClientS2.get_persistence_info()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.pid(owner_id)
		stream.u16(slot_id)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_PERSISTENCE_INFO, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		info = stream.extract(DataStorePersistenceInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.get_persistence_info -> done")
		return info
	
	async def get_persistence_infos(self, owner_id, slot_ids):
		logger.info("DataStoreClientS2.get_persistence_infos()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.pid(owner_id)
		stream.list(slot_ids, stream.u16)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_PERSISTENCE_INFOS, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		obj = rmc.RMCResponse()
		obj.infos = stream.list(DataStorePersistenceInfo)
		obj.results = stream.list(stream.result)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.get_persistence_infos -> done")
		return obj
	
	async def perpetuate_object(self, persistence_slot_id, data_id, delete_last_object):
		logger.info("DataStoreClientS2.perpetuate_object()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u16(persistence_slot_id)
		stream.u64(data_id)
		stream.bool(delete_last_object)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_PERPETUATE_OBJECT, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.perpetuate_object -> done")
	
	async def unperpetuate_object(self, persistence_slot_id, delete_last_object):
		logger.info("DataStoreClientS2.unperpetuate_object()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u16(persistence_slot_id)
		stream.bool(delete_last_object)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_UNPERPETUATE_OBJECT, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.unperpetuate_object -> done")
	
	async def prepare_get_object_or_meta_binary(self, param):
		logger.info("DataStoreClientS2.prepare_get_object_or_meta_binary()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_PREPARE_GET_OBJECT_OR_META_BINARY, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		obj = rmc.RMCResponse()
		obj.get_info = stream.extract(DataStoreReqGetInfo)
		obj.additional_meta = stream.extract(DataStoreReqGetAdditionalMeta)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.prepare_get_object_or_meta_binary -> done")
		return obj
	
	async def get_password_info(self, data_id):
		logger.info("DataStoreClientS2.get_password_info()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u64(data_id)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_PASSWORD_INFO, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		info = stream.extract(DataStorePasswordInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.get_password_info -> done")
		return info
	
	async def get_password_infos(self, data_ids):
		logger.info("DataStoreClientS2.get_password_infos()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(data_ids, stream.u64)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_PASSWORD_INFOS, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		obj = rmc.RMCResponse()
		obj.infos = stream.list(DataStorePasswordInfo)
		obj.results = stream.list(stream.result)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.get_password_infos -> done")
		return obj
	
	async def get_metas_multiple_param(self, params):
		logger.info("DataStoreClientS2.get_metas_multiple_param()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(params, stream.add)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_METAS_MULTIPLE_PARAM, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		obj = rmc.RMCResponse()
		obj.infos = stream.list(DataStoreMetaInfo)
		obj.results = stream.list(stream.result)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.get_metas_multiple_param -> done")
		return obj
	
	async def complete_post_objects(self, data_ids):
		logger.info("DataStoreClientS2.complete_post_objects()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(data_ids, stream.u64)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_COMPLETE_POST_OBJECTS, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.complete_post_objects -> done")
	
	async def change_meta(self, param):
		logger.info("DataStoreClientS2.change_meta()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_CHANGE_META, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.change_meta -> done")
	
	async def change_metas(self, data_ids, param, transactional):
		logger.info("DataStoreClientS2.change_metas()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(data_ids, stream.u64)
		stream.list(param, stream.add)
		stream.bool(transactional)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_CHANGE_METAS, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		results = stream.list(stream.result)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.change_metas -> done")
		return results
	
	async def rate_objects(self, targets, param, transactional, fetch_ratings):
		logger.info("DataStoreClientS2.rate_objects()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(targets, stream.add)
		stream.list(param, stream.add)
		stream.bool(transactional)
		stream.bool(fetch_ratings)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_RATE_OBJECTS, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		obj = rmc.RMCResponse()
		obj.infos = stream.list(DataStoreRatingInfo)
		obj.results = stream.list(stream.result)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.rate_objects -> done")
		return obj
	
	async def post_meta_binary_with_data_id(self, data_id, param):
		logger.info("DataStoreClientS2.post_meta_binary_with_data_id()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u64(data_id)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_POST_META_BINARY_WITH_DATA_ID, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.post_meta_binary_with_data_id -> done")
	
	async def post_meta_binaries_with_data_id(self, data_ids, param, transactional):
		logger.info("DataStoreClientS2.post_meta_binaries_with_data_id()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(data_ids, stream.u64)
		stream.list(param, stream.add)
		stream.bool(transactional)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_POST_META_BINARIES_WITH_DATA_ID, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		results = stream.list(stream.result)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.post_meta_binaries_with_data_id -> done")
		return results
	
	async def rate_object_with_posting(self, target, rate_param, post_param, fetch_ratings):
		logger.info("DataStoreClientS2.rate_object_with_posting()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(target)
		stream.add(rate_param)
		stream.add(post_param)
		stream.bool(fetch_ratings)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_RATE_OBJECT_WITH_POSTING, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		info = stream.extract(DataStoreRatingInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.rate_object_with_posting -> done")
		return info
	
	async def rate_objects_with_posting(self, targets, rate_param, post_param, transactional, fetch_ratings):
		logger.info("DataStoreClientS2.rate_objects_with_posting()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(targets, stream.add)
		stream.list(rate_param, stream.add)
		stream.list(post_param, stream.add)
		stream.bool(transactional)
		stream.bool(fetch_ratings)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_RATE_OBJECTS_WITH_POSTING, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		obj = rmc.RMCResponse()
		obj.ratings = stream.list(DataStoreRatingInfo)
		obj.results = stream.list(stream.result)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.rate_objects_with_posting -> done")
		return obj
	
	async def get_object_infos(self, data_ids):
		logger.info("DataStoreClientS2.get_object_infos()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.list(data_ids, stream.u64)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_OBJECT_INFOS, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		obj = rmc.RMCResponse()
		obj.infos = stream.list(DataStoreReqGetInfo)
		obj.results = stream.list(stream.result)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.get_object_infos -> done")
		return obj
	
	async def search_object_light(self, param):
		logger.info("DataStoreClientS2.search_object_light()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_SEARCH_OBJECT_LIGHT, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		result = stream.extract(DataStoreSearchResult)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.search_object_light -> done")
		return result
	
	async def coconut_register_meta(self, meta, url):
		logger.info("DataStoreClientS2.coconut_register_meta()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(meta)
		stream.string(url)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_COCONUT_REGISTER_META, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.coconut_register_meta -> done")
	
	async def coconut_rate_post(self, data_id):
		logger.info("DataStoreClientS2.coconut_rate_post()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.u64(data_id)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_COCONUT_RATE_POST, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.coconut_rate_post -> done")
	
	async def coconut_get_object_infos(self, param):
		logger.info("DataStoreClientS2.coconut_get_object_infos()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_COCONUT_GET_OBJECT_INFOS, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		obj = rmc.RMCResponse()
		obj.p_infos = stream.list(CoconutGetInfo)
		obj.p_results = stream.list(stream.result)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.coconut_get_object_infos -> done")
		return obj
	
	async def coconut_report_violation(self, violation):
		logger.info("DataStoreClientS2.coconut_report_violation()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(violation)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_COCONUT_REPORT_VIOLATION, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.coconut_report_violation -> done")
	
	async def upload_regular_match_result(self, stats):
		logger.info("DataStoreClientS2.upload_regular_match_result()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(stats)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_UPLOAD_REGULAR_MATCH_RESULT, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.upload_regular_match_result -> done")
	
	async def upload_gachi_match_result(self, stats):
		logger.info("DataStoreClientS2.upload_gachi_match_result()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(stats)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_UPLOAD_GACHI_MATCH_RESULT, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.upload_gachi_match_result -> done")
	
	async def upload_league_match_result(self, stats):
		logger.info("DataStoreClientS2.upload_league_match_result()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(stats)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_UPLOAD_LEAGUE_MATCH_RESULT, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.upload_league_match_result -> done")
	
	async def upload_fes_match_result(self, stats):
		logger.info("DataStoreClientS2.upload_fes_match_result()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(stats)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_UPLOAD_FES_MATCH_RESULT, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.upload_fes_match_result -> done")
	
	async def get_ordered_gear(self):
		logger.info("DataStoreClientS2.get_ordered_gear()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_GET_ORDERED_GEAR, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		info = stream.extract(OrderedInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.get_ordered_gear -> done")
		return info
	
	async def purchase_gear(self, info):
		logger.info("DataStoreClientS2.purchase_gear()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(info)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_PURCHASE_GEAR, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.purchase_gear -> done")
	
	async def upload_time_attack(self, info):
		logger.info("DataStoreClientS2.upload_time_attack()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(info)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_UPLOAD_TIME_ATTACK, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.upload_time_attack -> done")
	
	async def coconut_register_meta_by_param(self, meta, sns_name, post_id):
		logger.info("DataStoreClientS2.coconut_register_meta_by_param()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(meta)
		stream.string(sns_name)
		stream.string(post_id)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_COCONUT_REGISTER_META_BY_PARAM, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.coconut_register_meta_by_param -> done")
	
	async def upload_fes_match_result_v2(self, stats):
		logger.info("DataStoreClientS2.upload_fes_match_result_v2()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(stats)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_UPLOAD_FES_MATCH_RESULT_V2, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.upload_fes_match_result_v2 -> done")
	
	async def upload_x_match_result(self, stats):
		logger.info("DataStoreClientS2.upload_x_match_result()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(stats)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_UPLOAD_X_MATCH_RESULT, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.upload_x_match_result -> done")
	
	async def prepare_post_play_log(self, param):
		logger.info("DataStoreClientS2.prepare_post_play_log()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_PREPARE_POST_PLAY_LOG, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		post_request_info = stream.extract(DataStoreReqPostInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.prepare_post_play_log -> done")
		return post_request_info
	
	async def prepare_get_play_log(self, param):
		logger.info("DataStoreClientS2.prepare_get_play_log()")
		#--- request ---
		stream = streams.StreamOut(self.settings)
		stream.add(param)
		data = await self.client.request(self.PROTOCOL_ID, self.METHOD_PREPARE_GET_PLAY_LOG, stream.get())
		
		#--- response ---
		stream = streams.StreamIn(data, self.settings)
		get_request_info = stream.extract(DataStoreReqGetInfo)
		if not stream.eof():
			raise ValueError("Response is bigger than expected (got %i bytes, but only %i were read)" %(stream.size(), stream.tell()))
		logger.info("DataStoreClientS2.prepare_get_play_log -> done")
		return get_request_info


class DataStoreServerS2(DataStoreProtocolS2):
	def __init__(self):
		self.methods = {
			self.METHOD_PREPARE_GET_OBJECT_V1: self.handle_prepare_get_object_v1,
			self.METHOD_PREPARE_POST_OBJECT_V1: self.handle_prepare_post_object_v1,
			self.METHOD_COMPLETE_POST_OBJECT_V1: self.handle_complete_post_object_v1,
			self.METHOD_DELETE_OBJECT: self.handle_delete_object,
			self.METHOD_DELETE_OBJECTS: self.handle_delete_objects,
			self.METHOD_CHANGE_META_V1: self.handle_change_meta_v1,
			self.METHOD_CHANGE_METAS_V1: self.handle_change_metas_v1,
			self.METHOD_GET_META: self.handle_get_meta,
			self.METHOD_GET_METAS: self.handle_get_metas,
			self.METHOD_PREPARE_UPDATE_OBJECT: self.handle_prepare_update_object,
			self.METHOD_COMPLETE_UPDATE_OBJECT: self.handle_complete_update_object,
			self.METHOD_SEARCH_OBJECT: self.handle_search_object,
			self.METHOD_GET_NOTIFICATION_URL: self.handle_get_notification_url,
			self.METHOD_GET_NEW_ARRIVED_NOTIFICATIONS_V1: self.handle_get_new_arrived_notifications_v1,
			self.METHOD_RATE_OBJECT: self.handle_rate_object,
			self.METHOD_GET_RATING: self.handle_get_rating,
			self.METHOD_GET_RATINGS: self.handle_get_ratings,
			self.METHOD_RESET_RATING: self.handle_reset_rating,
			self.METHOD_RESET_RATINGS: self.handle_reset_ratings,
			self.METHOD_GET_SPECIFIC_META_V1: self.handle_get_specific_meta_v1,
			self.METHOD_POST_META_BINARY: self.handle_post_meta_binary,
			self.METHOD_TOUCH_OBJECT: self.handle_touch_object,
			self.METHOD_GET_RATING_WITH_LOG: self.handle_get_rating_with_log,
			self.METHOD_PREPARE_POST_OBJECT: self.handle_prepare_post_object,
			self.METHOD_PREPARE_GET_OBJECT: self.handle_prepare_get_object,
			self.METHOD_COMPLETE_POST_OBJECT: self.handle_complete_post_object,
			self.METHOD_GET_NEW_ARRIVED_NOTIFICATIONS: self.handle_get_new_arrived_notifications,
			self.METHOD_GET_SPECIFIC_META: self.handle_get_specific_meta,
			self.METHOD_GET_PERSISTENCE_INFO: self.handle_get_persistence_info,
			self.METHOD_GET_PERSISTENCE_INFOS: self.handle_get_persistence_infos,
			self.METHOD_PERPETUATE_OBJECT: self.handle_perpetuate_object,
			self.METHOD_UNPERPETUATE_OBJECT: self.handle_unperpetuate_object,
			self.METHOD_PREPARE_GET_OBJECT_OR_META_BINARY: self.handle_prepare_get_object_or_meta_binary,
			self.METHOD_GET_PASSWORD_INFO: self.handle_get_password_info,
			self.METHOD_GET_PASSWORD_INFOS: self.handle_get_password_infos,
			self.METHOD_GET_METAS_MULTIPLE_PARAM: self.handle_get_metas_multiple_param,
			self.METHOD_COMPLETE_POST_OBJECTS: self.handle_complete_post_objects,
			self.METHOD_CHANGE_META: self.handle_change_meta,
			self.METHOD_CHANGE_METAS: self.handle_change_metas,
			self.METHOD_RATE_OBJECTS: self.handle_rate_objects,
			self.METHOD_POST_META_BINARY_WITH_DATA_ID: self.handle_post_meta_binary_with_data_id,
			self.METHOD_POST_META_BINARIES_WITH_DATA_ID: self.handle_post_meta_binaries_with_data_id,
			self.METHOD_RATE_OBJECT_WITH_POSTING: self.handle_rate_object_with_posting,
			self.METHOD_RATE_OBJECTS_WITH_POSTING: self.handle_rate_objects_with_posting,
			self.METHOD_GET_OBJECT_INFOS: self.handle_get_object_infos,
			self.METHOD_SEARCH_OBJECT_LIGHT: self.handle_search_object_light,
			self.METHOD_COCONUT_REGISTER_META: self.handle_coconut_register_meta,
			self.METHOD_COCONUT_RATE_POST: self.handle_coconut_rate_post,
			self.METHOD_COCONUT_GET_OBJECT_INFOS: self.handle_coconut_get_object_infos,
			self.METHOD_COCONUT_REPORT_VIOLATION: self.handle_coconut_report_violation,
			self.METHOD_UPLOAD_REGULAR_MATCH_RESULT: self.handle_upload_regular_match_result,
			self.METHOD_UPLOAD_GACHI_MATCH_RESULT: self.handle_upload_gachi_match_result,
			self.METHOD_UPLOAD_LEAGUE_MATCH_RESULT: self.handle_upload_league_match_result,
			self.METHOD_UPLOAD_FES_MATCH_RESULT: self.handle_upload_fes_match_result,
			self.METHOD_GET_ORDERED_GEAR: self.handle_get_ordered_gear,
			self.METHOD_PURCHASE_GEAR: self.handle_purchase_gear,
			self.METHOD_UPLOAD_TIME_ATTACK: self.handle_upload_time_attack,
			self.METHOD_COCONUT_REGISTER_META_BY_PARAM: self.handle_coconut_register_meta_by_param,
			self.METHOD_UPLOAD_FES_MATCH_RESULT_V2: self.handle_upload_fes_match_result_v2,
			self.METHOD_UPLOAD_X_MATCH_RESULT: self.handle_upload_x_match_result,
			self.METHOD_PREPARE_POST_PLAY_LOG: self.handle_prepare_post_play_log,
			self.METHOD_PREPARE_GET_PLAY_LOG: self.handle_prepare_get_play_log,
		}
	
	async def logout(self, client):
		pass
	
	async def handle(self, client, method_id, input, output):
		if method_id in self.methods:
			await self.methods[method_id](client, input, output)
		else:
			logger.warning("Unknown method called on DataStoreServerS2: %i", method_id)
			raise common.RMCError("Core::NotImplemented")
	
	async def handle_prepare_get_object_v1(self, client, input, output):
		logger.info("DataStoreServerS2.prepare_get_object_v1()")
		#--- request ---
		param = input.extract(DataStorePrepareGetParamV1)
		response = await self.prepare_get_object_v1(client, param)
		
		#--- response ---
		if not isinstance(response, DataStoreReqGetInfoV1):
			raise RuntimeError("Expected DataStoreReqGetInfoV1, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_prepare_post_object_v1(self, client, input, output):
		logger.info("DataStoreServerS2.prepare_post_object_v1()")
		#--- request ---
		param = input.extract(DataStorePreparePostParamV1)
		response = await self.prepare_post_object_v1(client, param)
		
		#--- response ---
		if not isinstance(response, DataStoreReqPostInfoV1):
			raise RuntimeError("Expected DataStoreReqPostInfoV1, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_complete_post_object_v1(self, client, input, output):
		logger.info("DataStoreServerS2.complete_post_object_v1()")
		#--- request ---
		param = input.extract(DataStoreCompletePostParamV1)
		await self.complete_post_object_v1(client, param)
	
	async def handle_delete_object(self, client, input, output):
		logger.info("DataStoreServerS2.delete_object()")
		#--- request ---
		param = input.extract(DataStoreDeleteParam)
		await self.delete_object(client, param)
	
	async def handle_delete_objects(self, client, input, output):
		logger.info("DataStoreServerS2.delete_objects()")
		#--- request ---
		param = input.list(DataStoreDeleteParam)
		transactional = input.bool()
		response = await self.delete_objects(client, param, transactional)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.result)
	
	async def handle_change_meta_v1(self, client, input, output):
		logger.info("DataStoreServerS2.change_meta_v1()")
		#--- request ---
		param = input.extract(DataStoreChangeMetaParamV1)
		await self.change_meta_v1(client, param)
	
	async def handle_change_metas_v1(self, client, input, output):
		logger.info("DataStoreServerS2.change_metas_v1()")
		#--- request ---
		data_ids = input.list(input.u64)
		param = input.list(DataStoreChangeMetaParamV1)
		transactional = input.bool()
		response = await self.change_metas_v1(client, data_ids, param, transactional)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.result)
	
	async def handle_get_meta(self, client, input, output):
		logger.info("DataStoreServerS2.get_meta()")
		#--- request ---
		param = input.extract(DataStoreGetMetaParam)
		response = await self.get_meta(client, param)
		
		#--- response ---
		if not isinstance(response, DataStoreMetaInfo):
			raise RuntimeError("Expected DataStoreMetaInfo, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_get_metas(self, client, input, output):
		logger.info("DataStoreServerS2.get_metas()")
		#--- request ---
		data_ids = input.list(input.u64)
		param = input.extract(DataStoreGetMetaParam)
		response = await self.get_metas(client, data_ids, param)
		
		#--- response ---
		if not isinstance(response, rmc.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['info', 'results']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.list(response.info, output.add)
		output.list(response.results, output.result)
	
	async def handle_prepare_update_object(self, client, input, output):
		logger.info("DataStoreServerS2.prepare_update_object()")
		#--- request ---
		param = input.extract(DataStorePrepareUpdateParam)
		response = await self.prepare_update_object(client, param)
		
		#--- response ---
		if not isinstance(response, DataStoreReqUpdateInfo):
			raise RuntimeError("Expected DataStoreReqUpdateInfo, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_complete_update_object(self, client, input, output):
		logger.info("DataStoreServerS2.complete_update_object()")
		#--- request ---
		param = input.extract(DataStoreCompleteUpdateParam)
		await self.complete_update_object(client, param)
	
	async def handle_search_object(self, client, input, output):
		logger.info("DataStoreServerS2.search_object()")
		#--- request ---
		param = input.extract(DataStoreSearchParam)
		response = await self.search_object(client, param)
		
		#--- response ---
		if not isinstance(response, DataStoreSearchResult):
			raise RuntimeError("Expected DataStoreSearchResult, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_get_notification_url(self, client, input, output):
		logger.info("DataStoreServerS2.get_notification_url()")
		#--- request ---
		param = input.extract(DataStoreGetNotificationUrlParam)
		response = await self.get_notification_url(client, param)
		
		#--- response ---
		if not isinstance(response, DataStoreReqGetNotificationUrlInfo):
			raise RuntimeError("Expected DataStoreReqGetNotificationUrlInfo, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_get_new_arrived_notifications_v1(self, client, input, output):
		logger.info("DataStoreServerS2.get_new_arrived_notifications_v1()")
		#--- request ---
		param = input.extract(DataStoreGetNewArrivedNotificationsParam)
		response = await self.get_new_arrived_notifications_v1(client, param)
		
		#--- response ---
		if not isinstance(response, rmc.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['result', 'has_next']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.list(response.result, output.add)
		output.bool(response.has_next)
	
	async def handle_rate_object(self, client, input, output):
		logger.info("DataStoreServerS2.rate_object()")
		#--- request ---
		target = input.extract(DataStoreRatingTarget)
		param = input.extract(DataStoreRateObjectParam)
		fetch_ratings = input.bool()
		response = await self.rate_object(client, target, param, fetch_ratings)
		
		#--- response ---
		if not isinstance(response, DataStoreRatingInfo):
			raise RuntimeError("Expected DataStoreRatingInfo, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_get_rating(self, client, input, output):
		logger.info("DataStoreServerS2.get_rating()")
		#--- request ---
		target = input.extract(DataStoreRatingTarget)
		access_password = input.u64()
		response = await self.get_rating(client, target, access_password)
		
		#--- response ---
		if not isinstance(response, DataStoreRatingInfo):
			raise RuntimeError("Expected DataStoreRatingInfo, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_get_ratings(self, client, input, output):
		logger.info("DataStoreServerS2.get_ratings()")
		#--- request ---
		data_ids = input.list(input.u64)
		access_password = input.u64()
		response = await self.get_ratings(client, data_ids, access_password)
		
		#--- response ---
		if not isinstance(response, rmc.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['ratings', 'results']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.list(response.ratings, lambda x: output.list(x, output.add))
		output.list(response.results, output.result)
	
	async def handle_reset_rating(self, client, input, output):
		logger.info("DataStoreServerS2.reset_rating()")
		#--- request ---
		target = input.extract(DataStoreRatingTarget)
		update_password = input.u64()
		await self.reset_rating(client, target, update_password)
	
	async def handle_reset_ratings(self, client, input, output):
		logger.info("DataStoreServerS2.reset_ratings()")
		#--- request ---
		data_ids = input.list(input.u64)
		transactional = input.bool()
		response = await self.reset_ratings(client, data_ids, transactional)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.result)
	
	async def handle_get_specific_meta_v1(self, client, input, output):
		logger.info("DataStoreServerS2.get_specific_meta_v1()")
		#--- request ---
		param = input.extract(DataStoreGetSpecificMetaParamV1)
		response = await self.get_specific_meta_v1(client, param)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.add)
	
	async def handle_post_meta_binary(self, client, input, output):
		logger.info("DataStoreServerS2.post_meta_binary()")
		#--- request ---
		param = input.extract(DataStorePreparePostParam)
		response = await self.post_meta_binary(client, param)
		
		#--- response ---
		if not isinstance(response, int):
			raise RuntimeError("Expected int, got %s" %response.__class__.__name__)
		output.u64(response)
	
	async def handle_touch_object(self, client, input, output):
		logger.info("DataStoreServerS2.touch_object()")
		#--- request ---
		param = input.extract(DataStoreTouchObjectParam)
		await self.touch_object(client, param)
	
	async def handle_get_rating_with_log(self, client, input, output):
		logger.info("DataStoreServerS2.get_rating_with_log()")
		#--- request ---
		target = input.extract(DataStoreRatingTarget)
		access_password = input.u64()
		response = await self.get_rating_with_log(client, target, access_password)
		
		#--- response ---
		if not isinstance(response, rmc.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['rating', 'log']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.add(response.rating)
		output.add(response.log)
	
	async def handle_prepare_post_object(self, client, input, output):
		logger.info("DataStoreServerS2.prepare_post_object()")
		#--- request ---
		param = input.extract(DataStorePreparePostParam)
		response = await self.prepare_post_object(client, param)
		
		#--- response ---
		if not isinstance(response, DataStoreReqPostInfo):
			raise RuntimeError("Expected DataStoreReqPostInfo, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_prepare_get_object(self, client, input, output):
		logger.info("DataStoreServerS2.prepare_get_object()")
		#--- request ---
		param = input.extract(DataStorePrepareGetParam)
		response = await self.prepare_get_object(client, param)
		
		#--- response ---
		if not isinstance(response, DataStoreReqGetInfo):
			raise RuntimeError("Expected DataStoreReqGetInfo, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_complete_post_object(self, client, input, output):
		logger.info("DataStoreServerS2.complete_post_object()")
		#--- request ---
		param = input.extract(DataStoreCompletePostParam)
		await self.complete_post_object(client, param)
	
	async def handle_get_new_arrived_notifications(self, client, input, output):
		logger.info("DataStoreServerS2.get_new_arrived_notifications()")
		#--- request ---
		param = input.extract(DataStoreGetNewArrivedNotificationsParam)
		response = await self.get_new_arrived_notifications(client, param)
		
		#--- response ---
		if not isinstance(response, rmc.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['result', 'has_next']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.list(response.result, output.add)
		output.bool(response.has_next)
	
	async def handle_get_specific_meta(self, client, input, output):
		logger.info("DataStoreServerS2.get_specific_meta()")
		#--- request ---
		param = input.extract(DataStoreGetSpecificMetaParam)
		response = await self.get_specific_meta(client, param)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.add)
	
	async def handle_get_persistence_info(self, client, input, output):
		logger.info("DataStoreServerS2.get_persistence_info()")
		#--- request ---
		owner_id = input.pid()
		slot_id = input.u16()
		response = await self.get_persistence_info(client, owner_id, slot_id)
		
		#--- response ---
		if not isinstance(response, DataStorePersistenceInfo):
			raise RuntimeError("Expected DataStorePersistenceInfo, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_get_persistence_infos(self, client, input, output):
		logger.info("DataStoreServerS2.get_persistence_infos()")
		#--- request ---
		owner_id = input.pid()
		slot_ids = input.list(input.u16)
		response = await self.get_persistence_infos(client, owner_id, slot_ids)
		
		#--- response ---
		if not isinstance(response, rmc.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['infos', 'results']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.list(response.infos, output.add)
		output.list(response.results, output.result)
	
	async def handle_perpetuate_object(self, client, input, output):
		logger.info("DataStoreServerS2.perpetuate_object()")
		#--- request ---
		persistence_slot_id = input.u16()
		data_id = input.u64()
		delete_last_object = input.bool()
		await self.perpetuate_object(client, persistence_slot_id, data_id, delete_last_object)
	
	async def handle_unperpetuate_object(self, client, input, output):
		logger.info("DataStoreServerS2.unperpetuate_object()")
		#--- request ---
		persistence_slot_id = input.u16()
		delete_last_object = input.bool()
		await self.unperpetuate_object(client, persistence_slot_id, delete_last_object)
	
	async def handle_prepare_get_object_or_meta_binary(self, client, input, output):
		logger.info("DataStoreServerS2.prepare_get_object_or_meta_binary()")
		#--- request ---
		param = input.extract(DataStorePrepareGetParam)
		response = await self.prepare_get_object_or_meta_binary(client, param)
		
		#--- response ---
		if not isinstance(response, rmc.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['get_info', 'additional_meta']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.add(response.get_info)
		output.add(response.additional_meta)
	
	async def handle_get_password_info(self, client, input, output):
		logger.info("DataStoreServerS2.get_password_info()")
		#--- request ---
		data_id = input.u64()
		response = await self.get_password_info(client, data_id)
		
		#--- response ---
		if not isinstance(response, DataStorePasswordInfo):
			raise RuntimeError("Expected DataStorePasswordInfo, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_get_password_infos(self, client, input, output):
		logger.info("DataStoreServerS2.get_password_infos()")
		#--- request ---
		data_ids = input.list(input.u64)
		response = await self.get_password_infos(client, data_ids)
		
		#--- response ---
		if not isinstance(response, rmc.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['infos', 'results']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.list(response.infos, output.add)
		output.list(response.results, output.result)
	
	async def handle_get_metas_multiple_param(self, client, input, output):
		logger.info("DataStoreServerS2.get_metas_multiple_param()")
		#--- request ---
		params = input.list(DataStoreGetMetaParam)
		response = await self.get_metas_multiple_param(client, params)
		
		#--- response ---
		if not isinstance(response, rmc.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['infos', 'results']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.list(response.infos, output.add)
		output.list(response.results, output.result)
	
	async def handle_complete_post_objects(self, client, input, output):
		logger.info("DataStoreServerS2.complete_post_objects()")
		#--- request ---
		data_ids = input.list(input.u64)
		await self.complete_post_objects(client, data_ids)
	
	async def handle_change_meta(self, client, input, output):
		logger.info("DataStoreServerS2.change_meta()")
		#--- request ---
		param = input.extract(DataStoreChangeMetaParam)
		await self.change_meta(client, param)
	
	async def handle_change_metas(self, client, input, output):
		logger.info("DataStoreServerS2.change_metas()")
		#--- request ---
		data_ids = input.list(input.u64)
		param = input.list(DataStoreChangeMetaParam)
		transactional = input.bool()
		response = await self.change_metas(client, data_ids, param, transactional)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.result)
	
	async def handle_rate_objects(self, client, input, output):
		logger.info("DataStoreServerS2.rate_objects()")
		#--- request ---
		targets = input.list(DataStoreRatingTarget)
		param = input.list(DataStoreRateObjectParam)
		transactional = input.bool()
		fetch_ratings = input.bool()
		response = await self.rate_objects(client, targets, param, transactional, fetch_ratings)
		
		#--- response ---
		if not isinstance(response, rmc.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['infos', 'results']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.list(response.infos, output.add)
		output.list(response.results, output.result)
	
	async def handle_post_meta_binary_with_data_id(self, client, input, output):
		logger.info("DataStoreServerS2.post_meta_binary_with_data_id()")
		#--- request ---
		data_id = input.u64()
		param = input.extract(DataStorePreparePostParam)
		await self.post_meta_binary_with_data_id(client, data_id, param)
	
	async def handle_post_meta_binaries_with_data_id(self, client, input, output):
		logger.info("DataStoreServerS2.post_meta_binaries_with_data_id()")
		#--- request ---
		data_ids = input.list(input.u64)
		param = input.list(DataStorePreparePostParam)
		transactional = input.bool()
		response = await self.post_meta_binaries_with_data_id(client, data_ids, param, transactional)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.result)
	
	async def handle_rate_object_with_posting(self, client, input, output):
		logger.info("DataStoreServerS2.rate_object_with_posting()")
		#--- request ---
		target = input.extract(DataStoreRatingTarget)
		rate_param = input.extract(DataStoreRateObjectParam)
		post_param = input.extract(DataStorePreparePostParam)
		fetch_ratings = input.bool()
		response = await self.rate_object_with_posting(client, target, rate_param, post_param, fetch_ratings)
		
		#--- response ---
		if not isinstance(response, DataStoreRatingInfo):
			raise RuntimeError("Expected DataStoreRatingInfo, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_rate_objects_with_posting(self, client, input, output):
		logger.info("DataStoreServerS2.rate_objects_with_posting()")
		#--- request ---
		targets = input.list(DataStoreRatingTarget)
		rate_param = input.list(DataStoreRateObjectParam)
		post_param = input.list(DataStorePreparePostParam)
		transactional = input.bool()
		fetch_ratings = input.bool()
		response = await self.rate_objects_with_posting(client, targets, rate_param, post_param, transactional, fetch_ratings)
		
		#--- response ---
		if not isinstance(response, rmc.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['ratings', 'results']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.list(response.ratings, output.add)
		output.list(response.results, output.result)
	
	async def handle_get_object_infos(self, client, input, output):
		logger.info("DataStoreServerS2.get_object_infos()")
		#--- request ---
		data_ids = input.list(input.u64)
		response = await self.get_object_infos(client, data_ids)
		
		#--- response ---
		if not isinstance(response, rmc.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['infos', 'results']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.list(response.infos, output.add)
		output.list(response.results, output.result)
	
	async def handle_search_object_light(self, client, input, output):
		logger.info("DataStoreServerS2.search_object_light()")
		#--- request ---
		param = input.extract(DataStoreSearchParam)
		response = await self.search_object_light(client, param)
		
		#--- response ---
		if not isinstance(response, DataStoreSearchResult):
			raise RuntimeError("Expected DataStoreSearchResult, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_coconut_register_meta(self, client, input, output):
		logger.info("DataStoreServerS2.coconut_register_meta()")
		#--- request ---
		meta = input.extract(CoconutMeta)
		url = input.string()
		await self.coconut_register_meta(client, meta, url)
	
	async def handle_coconut_rate_post(self, client, input, output):
		logger.info("DataStoreServerS2.coconut_rate_post()")
		#--- request ---
		data_id = input.u64()
		await self.coconut_rate_post(client, data_id)
	
	async def handle_coconut_get_object_infos(self, client, input, output):
		logger.info("DataStoreServerS2.coconut_get_object_infos()")
		#--- request ---
		param = input.extract(CoconutGetParam)
		response = await self.coconut_get_object_infos(client, param)
		
		#--- response ---
		if not isinstance(response, rmc.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['p_infos', 'p_results']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.list(response.p_infos, output.add)
		output.list(response.p_results, output.result)
	
	async def handle_coconut_report_violation(self, client, input, output):
		logger.info("DataStoreServerS2.coconut_report_violation()")
		#--- request ---
		violation = input.extract(CoconutViolation)
		await self.coconut_report_violation(client, violation)
	
	async def handle_upload_regular_match_result(self, client, input, output):
		logger.info("DataStoreServerS2.upload_regular_match_result()")
		#--- request ---
		stats = input.extract(CalicoRegularStats)
		await self.upload_regular_match_result(client, stats)
	
	async def handle_upload_gachi_match_result(self, client, input, output):
		logger.info("DataStoreServerS2.upload_gachi_match_result()")
		#--- request ---
		stats = input.extract(CalicoGachiStats)
		await self.upload_gachi_match_result(client, stats)
	
	async def handle_upload_league_match_result(self, client, input, output):
		logger.info("DataStoreServerS2.upload_league_match_result()")
		#--- request ---
		stats = input.extract(CalicoLeagueStats)
		await self.upload_league_match_result(client, stats)
	
	async def handle_upload_fes_match_result(self, client, input, output):
		logger.info("DataStoreServerS2.upload_fes_match_result()")
		#--- request ---
		stats = input.extract(CalicoFesStats)
		await self.upload_fes_match_result(client, stats)
	
	async def handle_get_ordered_gear(self, client, input, output):
		logger.info("DataStoreServerS2.get_ordered_gear()")
		#--- request ---
		response = await self.get_ordered_gear(client)
		
		#--- response ---
		if not isinstance(response, OrderedInfo):
			raise RuntimeError("Expected OrderedInfo, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_purchase_gear(self, client, input, output):
		logger.info("DataStoreServerS2.purchase_gear()")
		#--- request ---
		info = input.extract(OrderedInfo)
		await self.purchase_gear(client, info)
	
	async def handle_upload_time_attack(self, client, input, output):
		logger.info("DataStoreServerS2.upload_time_attack()")
		#--- request ---
		info = input.extract(TimeAttackInfo)
		await self.upload_time_attack(client, info)
	
	async def handle_coconut_register_meta_by_param(self, client, input, output):
		logger.info("DataStoreServerS2.coconut_register_meta_by_param()")
		#--- request ---
		meta = input.extract(CoconutMeta)
		sns_name = input.string()
		post_id = input.string()
		await self.coconut_register_meta_by_param(client, meta, sns_name, post_id)
	
	async def handle_upload_fes_match_result_v2(self, client, input, output):
		logger.info("DataStoreServerS2.upload_fes_match_result_v2()")
		#--- request ---
		stats = input.extract(CalicoFesStatsV2)
		await self.upload_fes_match_result_v2(client, stats)
	
	async def handle_upload_x_match_result(self, client, input, output):
		logger.info("DataStoreServerS2.upload_x_match_result()")
		#--- request ---
		stats = input.extract(CalicoXStats)
		await self.upload_x_match_result(client, stats)
	
	async def handle_prepare_post_play_log(self, client, input, output):
		logger.info("DataStoreServerS2.prepare_post_play_log()")
		#--- request ---
		param = input.extract(PlayLogPreparePostParam)
		response = await self.prepare_post_play_log(client, param)
		
		#--- response ---
		if not isinstance(response, DataStoreReqPostInfo):
			raise RuntimeError("Expected DataStoreReqPostInfo, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def handle_prepare_get_play_log(self, client, input, output):
		logger.info("DataStoreServerS2.prepare_get_play_log()")
		#--- request ---
		param = input.extract(PlayLogPrepareGetParam)
		response = await self.prepare_get_play_log(client, param)
		
		#--- response ---
		if not isinstance(response, DataStoreReqGetInfo):
			raise RuntimeError("Expected DataStoreReqGetInfo, got %s" %response.__class__.__name__)
		output.add(response)
	
	async def prepare_get_object_v1(self, *args):
		logger.warning("DataStoreServerS2.prepare_get_object_v1 not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def prepare_post_object_v1(self, *args):
		logger.warning("DataStoreServerS2.prepare_post_object_v1 not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def complete_post_object_v1(self, *args):
		logger.warning("DataStoreServerS2.complete_post_object_v1 not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def delete_object(self, *args):
		logger.warning("DataStoreServerS2.delete_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def delete_objects(self, *args):
		logger.warning("DataStoreServerS2.delete_objects not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def change_meta_v1(self, *args):
		logger.warning("DataStoreServerS2.change_meta_v1 not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def change_metas_v1(self, *args):
		logger.warning("DataStoreServerS2.change_metas_v1 not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_meta(self, *args):
		logger.warning("DataStoreServerS2.get_meta not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_metas(self, *args):
		logger.warning("DataStoreServerS2.get_metas not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def prepare_update_object(self, *args):
		logger.warning("DataStoreServerS2.prepare_update_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def complete_update_object(self, *args):
		logger.warning("DataStoreServerS2.complete_update_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def search_object(self, *args):
		logger.warning("DataStoreServerS2.search_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_notification_url(self, *args):
		logger.warning("DataStoreServerS2.get_notification_url not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_new_arrived_notifications_v1(self, *args):
		logger.warning("DataStoreServerS2.get_new_arrived_notifications_v1 not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def rate_object(self, *args):
		logger.warning("DataStoreServerS2.rate_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_rating(self, *args):
		logger.warning("DataStoreServerS2.get_rating not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_ratings(self, *args):
		logger.warning("DataStoreServerS2.get_ratings not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def reset_rating(self, *args):
		logger.warning("DataStoreServerS2.reset_rating not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def reset_ratings(self, *args):
		logger.warning("DataStoreServerS2.reset_ratings not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_specific_meta_v1(self, *args):
		logger.warning("DataStoreServerS2.get_specific_meta_v1 not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def post_meta_binary(self, *args):
		logger.warning("DataStoreServerS2.post_meta_binary not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def touch_object(self, *args):
		logger.warning("DataStoreServerS2.touch_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_rating_with_log(self, *args):
		logger.warning("DataStoreServerS2.get_rating_with_log not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def prepare_post_object(self, *args):
		logger.warning("DataStoreServerS2.prepare_post_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def prepare_get_object(self, *args):
		logger.warning("DataStoreServerS2.prepare_get_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def complete_post_object(self, *args):
		logger.warning("DataStoreServerS2.complete_post_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_new_arrived_notifications(self, *args):
		logger.warning("DataStoreServerS2.get_new_arrived_notifications not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_specific_meta(self, *args):
		logger.warning("DataStoreServerS2.get_specific_meta not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_persistence_info(self, *args):
		logger.warning("DataStoreServerS2.get_persistence_info not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_persistence_infos(self, *args):
		logger.warning("DataStoreServerS2.get_persistence_infos not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def perpetuate_object(self, *args):
		logger.warning("DataStoreServerS2.perpetuate_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def unperpetuate_object(self, *args):
		logger.warning("DataStoreServerS2.unperpetuate_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def prepare_get_object_or_meta_binary(self, *args):
		logger.warning("DataStoreServerS2.prepare_get_object_or_meta_binary not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_password_info(self, *args):
		logger.warning("DataStoreServerS2.get_password_info not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_password_infos(self, *args):
		logger.warning("DataStoreServerS2.get_password_infos not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_metas_multiple_param(self, *args):
		logger.warning("DataStoreServerS2.get_metas_multiple_param not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def complete_post_objects(self, *args):
		logger.warning("DataStoreServerS2.complete_post_objects not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def change_meta(self, *args):
		logger.warning("DataStoreServerS2.change_meta not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def change_metas(self, *args):
		logger.warning("DataStoreServerS2.change_metas not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def rate_objects(self, *args):
		logger.warning("DataStoreServerS2.rate_objects not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def post_meta_binary_with_data_id(self, *args):
		logger.warning("DataStoreServerS2.post_meta_binary_with_data_id not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def post_meta_binaries_with_data_id(self, *args):
		logger.warning("DataStoreServerS2.post_meta_binaries_with_data_id not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def rate_object_with_posting(self, *args):
		logger.warning("DataStoreServerS2.rate_object_with_posting not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def rate_objects_with_posting(self, *args):
		logger.warning("DataStoreServerS2.rate_objects_with_posting not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_object_infos(self, *args):
		logger.warning("DataStoreServerS2.get_object_infos not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def search_object_light(self, *args):
		logger.warning("DataStoreServerS2.search_object_light not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def coconut_register_meta(self, *args):
		logger.warning("DataStoreServerS2.coconut_register_meta not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def coconut_rate_post(self, *args):
		logger.warning("DataStoreServerS2.coconut_rate_post not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def coconut_get_object_infos(self, *args):
		logger.warning("DataStoreServerS2.coconut_get_object_infos not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def coconut_report_violation(self, *args):
		logger.warning("DataStoreServerS2.coconut_report_violation not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def upload_regular_match_result(self, *args):
		logger.warning("DataStoreServerS2.upload_regular_match_result not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def upload_gachi_match_result(self, *args):
		logger.warning("DataStoreServerS2.upload_gachi_match_result not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def upload_league_match_result(self, *args):
		logger.warning("DataStoreServerS2.upload_league_match_result not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def upload_fes_match_result(self, *args):
		logger.warning("DataStoreServerS2.upload_fes_match_result not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def get_ordered_gear(self, *args):
		logger.warning("DataStoreServerS2.get_ordered_gear not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def purchase_gear(self, *args):
		logger.warning("DataStoreServerS2.purchase_gear not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def upload_time_attack(self, *args):
		logger.warning("DataStoreServerS2.upload_time_attack not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def coconut_register_meta_by_param(self, *args):
		logger.warning("DataStoreServerS2.coconut_register_meta_by_param not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def upload_fes_match_result_v2(self, *args):
		logger.warning("DataStoreServerS2.upload_fes_match_result_v2 not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def upload_x_match_result(self, *args):
		logger.warning("DataStoreServerS2.upload_x_match_result not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def prepare_post_play_log(self, *args):
		logger.warning("DataStoreServerS2.prepare_post_play_log not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	async def prepare_get_play_log(self, *args):
		logger.warning("DataStoreServerS2.prepare_get_play_log not implemented")
		raise common.RMCError("Core::NotImplemented")

