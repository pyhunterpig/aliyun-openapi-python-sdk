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
class AssumeRoleWithServiceIdentityRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sts', '2015-04-01', 'AssumeRoleWithServiceIdentity')
		self.set_protocol_type(self, 'https');
		self.set_method('POST')

	def get_DurationSeconds(self):
		return self.get_query_params().get('DurationSeconds')

	def set_DurationSeconds(self,DurationSeconds):
		self.add_query_param('DurationSeconds',DurationSeconds)

	def get_ExternalId(self):
		return self.get_query_params().get('ExternalId')

	def set_ExternalId(self,ExternalId):
		self.add_query_param('ExternalId',ExternalId)

	def get_Policy(self):
		return self.get_query_params().get('Policy')

	def set_Policy(self,Policy):
		self.add_query_param('Policy',Policy)

	def get_RoleArn(self):
		return self.get_query_params().get('RoleArn')

	def set_RoleArn(self,RoleArn):
		self.add_query_param('RoleArn',RoleArn)

	def get_RoleSessionName(self):
		return self.get_query_params().get('RoleSessionName')

	def set_RoleSessionName(self,RoleSessionName):
		self.add_query_param('RoleSessionName',RoleSessionName)

	def get_AssumeRoleFor(self):
		return self.get_query_params().get('AssumeRoleFor')

	def set_AssumeRoleFor(self,AssumeRoleFor):
		self.add_query_param('AssumeRoleFor',AssumeRoleFor)

	def get_SerialNumber(self):
		return self.get_query_params().get('SerialNumber')

	def set_SerialNumber(self,SerialNumber):
		self.add_query_param('SerialNumber',SerialNumber)

	def get_TokenCode(self):
		return self.get_query_params().get('TokenCode')

	def set_TokenCode(self,TokenCode):
		self.add_query_param('TokenCode',TokenCode)