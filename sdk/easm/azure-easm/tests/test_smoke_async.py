# coding: utf-8
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -------------------------------------------------------------------------
from testcase import EasmPowerShellPreparer
from testcase_async import EasmAsyncTest


class EasmSmokeAsyncTest(EasmAsyncTest):

    @EasmPowerShellPreparer()
    async def test_smoke_async(self, easm_endpoint):
        client = self.create_client(endpoint=easm_endpoint)
        # test your code here, for example:
        # result = await client.xxx.xx(...)
        # assert result is not None
