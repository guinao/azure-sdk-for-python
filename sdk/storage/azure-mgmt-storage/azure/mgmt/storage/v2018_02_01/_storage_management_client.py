# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import StorageManagementClientConfiguration
from .operations import Operations
from .operations import SkusOperations
from .operations import StorageAccountsOperations
from .operations import UsageOperations
from .operations import BlobContainersOperations
from . import models


class StorageManagementClient(SDKClient):
    """The Azure Storage Management API.

    :ivar config: Configuration for client.
    :vartype config: StorageManagementClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.storage.v2018_02_01.operations.Operations
    :ivar skus: Skus operations
    :vartype skus: azure.mgmt.storage.v2018_02_01.operations.SkusOperations
    :ivar storage_accounts: StorageAccounts operations
    :vartype storage_accounts: azure.mgmt.storage.v2018_02_01.operations.StorageAccountsOperations
    :ivar usage: Usage operations
    :vartype usage: azure.mgmt.storage.v2018_02_01.operations.UsageOperations
    :ivar blob_containers: BlobContainers operations
    :vartype blob_containers: azure.mgmt.storage.v2018_02_01.operations.BlobContainersOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = StorageManagementClientConfiguration(credentials, subscription_id, base_url)
        super(StorageManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-02-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.skus = SkusOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.storage_accounts = StorageAccountsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.usage = UsageOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.blob_containers = BlobContainersOperations(
            self._client, self.config, self._serialize, self._deserialize)