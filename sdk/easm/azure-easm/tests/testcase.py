# coding: utf-8
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import functools
from devtools_testutils import AzureTestCase, PowerShellPreparer
from azure.easm import easmClient


class EasmTest(AzureTestCase):
    def __init__(self, method_name, **kwargs):
        super(EasmTest, self).__init__(method_name, **kwargs)

    def create_client(self, endpoint):
        credential = self.get_credential(easmClient)
        return self.create_client_from_credential(
            easmClient,
            credential=credential,
            endpoint=endpoint,
        )


EasmPowerShellPreparer = functools.partial(
    PowerShellPreparer,
    "easm",
    easm_endpoint="https://myservice.azure.com"
)
