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
from aliyunsdkaliyuncvc.endpoint import endpoint_data

class RegisterDeviceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'aliyuncvc', '2019-10-30', 'RegisterDevice','aliyuncvc')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_IP(self):
		return self.get_query_params().get('IP')

	def set_IP(self,IP):
		self.add_query_param('IP',IP)

	def get_Mac(self):
		return self.get_query_params().get('Mac')

	def set_Mac(self,Mac):
		self.add_query_param('Mac',Mac)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)

	def get_DeviceVersion(self):
		return self.get_query_params().get('DeviceVersion')

	def set_DeviceVersion(self,DeviceVersion):
		self.add_query_param('DeviceVersion',DeviceVersion)

	def get_SN(self):
		return self.get_query_params().get('SN')

	def set_SN(self,SN):
		self.add_query_param('SN',SN)