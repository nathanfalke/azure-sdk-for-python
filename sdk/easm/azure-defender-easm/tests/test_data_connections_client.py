# coding: utf-8
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -------------------------------------------------------------------------
from testcase import EasmTest, EasmPowerShellPreparer

class EasmDataConnectionsTest(EasmTest):
    put_data_connection_name = 'smoke_test_put_data_connection'
    delete_data_connection_name = 'smoke_test_delete_data_connection'
    time_format = '%Y-%m-%dT%H:%M:%S.%f%z'

    @EasmPowerShellPreparer()
    def test_list_data_connections(self, easm_endpoint):
        client = self.create_client(endpoint=easm_endpoint)
        response = client.data_connections.list()
        connection = response.next()
        self.check_timestamp_format(self.time_format, connection['createdDate'])
        self.check_timestamp_format(self.time_format, connection['updatedDate'])
        assert connection['id']
        assert connection['name']
        assert connection['kind']
        assert connection['displayName']

    @EasmPowerShellPreparer()
    def test_get_data_connection(self, easm_endpoint):
        client = self.create_client(endpoint=easm_endpoint)
        connection = client.data_connections.get('a')
        self.check_timestamp_format(self.time_format, connection['createdDate'])
        self.check_timestamp_format(self.time_format, connection['updatedDate'])
        assert connection['id']
        assert connection['name']
        assert connection['kind']
        assert connection['displayName']

    @EasmPowerShellPreparer()
    def test_put_data_connection(self, easm_endpoint):
        client = self.create_client(endpoint=easm_endpoint)
        sentinel_ws_id='workspaceid'
        sentinel_api_key='apikey'
        request = {
            'connectionString': f'WorkspaceId={sentinel_ws_id};ApiKey={sentinel_api_key}',
            'kind': 'sentinel',
            'content': 'assets'
        }

        connection = client.data_connections.put(self.put_data_connection_name, request)

        self.check_timestamp_format(self.time_format, connection['createdDate'])
        self.check_timestamp_format(self.time_format, connection['updatedDate'])
        assert connection['id']
        assert connection['name']
        assert connection['kind'] == request['kind']
        assert connection['displayName']
        assert connection['connectionString'] == request['connectionString']

    @EasmPowerShellPreparer()
    def test_delete_data_connection(self, easm_endpoint):
        client = self.create_client(endpoint=easm_endpoint)
        response = client.data_connections.delete(self.delete_data_connection_name)
        assert not response
