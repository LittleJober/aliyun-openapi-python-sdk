# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkehpc.endpoint import endpoint_data

class MountNFSRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'MountNFS')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_MountDir(self):
		return self.get_query_params().get('MountDir')

	def set_MountDir(self,MountDir):
		self.add_query_param('MountDir',MountDir)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_RemoteDir(self):
		return self.get_query_params().get('RemoteDir')

	def set_RemoteDir(self,RemoteDir):
		self.add_query_param('RemoteDir',RemoteDir)

	def get_NfsDir(self):
		return self.get_query_params().get('NfsDir')

	def set_NfsDir(self,NfsDir):
		self.add_query_param('NfsDir',NfsDir)

	def get_ProtocolType(self):
		return self.get_query_params().get('ProtocolType')

	def set_ProtocolType(self,ProtocolType):
		self.add_query_param('ProtocolType',ProtocolType)