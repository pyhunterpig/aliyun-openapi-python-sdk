# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class DescribeSnapshotsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeSnapshots')

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_DiskId(self):
		return self.get_query_params().get('DiskId')

	def set_DiskId(self,DiskId):
		self.add_query_param('DiskId',DiskId)

	def get_SnapshotIds(self):
		return self.get_query_params().get('SnapshotIds')

	def set_SnapshotIds(self,SnapshotIds):
		self.add_query_param('SnapshotIds',SnapshotIds)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_SnapshotName(self):
		return self.get_query_params().get('SnapshotName')

	def set_SnapshotName(self,SnapshotName):
		self.add_query_param('SnapshotName',SnapshotName)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)

	def get_SnapshotType(self):
		return self.get_query_params().get('SnapshotType')

	def set_SnapshotType(self,SnapshotType):
		self.add_query_param('SnapshotType',SnapshotType)

	def get_Filter1Key(self):
		return self.get_query_params().get('Filter1Key')

	def set_Filter1Key(self,Filter1Key):
		self.add_query_param('Filter1Key',Filter1Key)

	def get_Filter2Key(self):
		return self.get_query_params().get('Filter2Key')

	def set_Filter2Key(self,Filter2Key):
		self.add_query_param('Filter2Key',Filter2Key)

	def get_Filter1Value(self):
		return self.get_query_params().get('Filter1Value')

	def set_Filter1Value(self,Filter1Value):
		self.add_query_param('Filter1Value',Filter1Value)

	def get_Filter2Value(self):
		return self.get_query_params().get('Filter2Value')

	def set_Filter2Value(self,Filter2Value):
		self.add_query_param('Filter2Value',Filter2Value)

	def get_Usage(self):
		return self.get_query_params().get('Usage')

	def set_Usage(self,Usage):
		self.add_query_param('Usage',Usage)

	def get_SourceDiskType(self):
		return self.get_query_params().get('SourceDiskType')

	def set_SourceDiskType(self,SourceDiskType):
		self.add_query_param('SourceDiskType',SourceDiskType)

	def get_Tag1Key(self):
		return self.get_query_params().get('Tag1Key')

	def set_Tag1Key(self,Tag1Key):
		self.add_query_param('Tag1Key',Tag1Key)

	def get_Tag2Key(self):
		return self.get_query_params().get('Tag2Key')

	def set_Tag2Key(self,Tag2Key):
		self.add_query_param('Tag2Key',Tag2Key)

	def get_Tag3Key(self):
		return self.get_query_params().get('Tag3Key')

	def set_Tag3Key(self,Tag3Key):
		self.add_query_param('Tag3Key',Tag3Key)

	def get_Tag4Key(self):
		return self.get_query_params().get('Tag4Key')

	def set_Tag4Key(self,Tag4Key):
		self.add_query_param('Tag4Key',Tag4Key)

	def get_Tag5Key(self):
		return self.get_query_params().get('Tag5Key')

	def set_Tag5Key(self,Tag5Key):
		self.add_query_param('Tag5Key',Tag5Key)

	def get_Tag1Value(self):
		return self.get_query_params().get('Tag1Value')

	def set_Tag1Value(self,Tag1Value):
		self.add_query_param('Tag1Value',Tag1Value)

	def get_Tag2Value(self):
		return self.get_query_params().get('Tag2Value')

	def set_Tag2Value(self,Tag2Value):
		self.add_query_param('Tag2Value',Tag2Value)

	def get_Tag3Value(self):
		return self.get_query_params().get('Tag3Value')

	def set_Tag3Value(self,Tag3Value):
		self.add_query_param('Tag3Value',Tag3Value)

	def get_Tag4Value(self):
		return self.get_query_params().get('Tag4Value')

	def set_Tag4Value(self,Tag4Value):
		self.add_query_param('Tag4Value',Tag4Value)

	def get_Tag5Value(self):
		return self.get_query_params().get('Tag5Value')

	def set_Tag5Value(self,Tag5Value):
		self.add_query_param('Tag5Value',Tag5Value)