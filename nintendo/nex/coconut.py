
# This file was generated automatically by generate_protocols.py

from nintendo.nex import notification, rmc, common, streams

import logging
logger = logging.getLogger(__name__)


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

