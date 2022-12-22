# Creating a Sentinel data connection
Data connections can be used to get data from EASM into the other standard security tools, which can be used to achieve the intended outcomes. In this sample, we'll go over how to create a data connection to get data from EASM to Sentinel.

## Creating an `EasmClient`
To create an `EasmClient`, you need your subscription ID, region, and some sort of credential. For the purposes of this demo, I've chosen the `InteractiveBrowserCredential` but any credential will work.

```python 
from azure.identity import InteractiveBrowserCredential
from azure.defender.easm import EasmClient

sub_id = '<your subscription ID here>'
workspace_name = '<your workspace name here>'
resource_group = '<your resource group here>'
region = '<your region here>'

endpoint = f'{region}.easm.defender.microsoft.com'

browser_credential = InteractiveBrowserCredential()
client = EasmClient(endpoint, resource_group, sub_id, workspace_name, browser_credential)
```

## Creating a data connection request
To create a data connection, we need to build the request body for one to be created. For this, we'll need the Sentinel workspace ID, as well as the Sentinel API key, both of which are available from the azure portal, in the "Agents management" section of the Sentinel Workspace

```python
sentinel_ws_id='<your Sentinel workspace ID here>'
sentinel_api_key='<your Sentinel API key here>'

request = {
    'connectionString': f'WorkspaceId={sentinel_ws_id};ApiKey={sentinel_api_key}',
    'kind': 'sentinel',
    'content': 'assets'
}
```

## Validate the data connection request
Using the `data_connections.validate` method, we can ensure we're making a valid data connection request, and receive a readable error if we aren't.

```python
data_connection_name = '<your data connection name here>'

client.data_connections.validate(data_connection_name, request)
```

## Create the data connection
Once the request has been validated, it can be used in the `data_connections.put` method to create the requested data connection

```python
client.data_connections.put(data_connection_name, request)
```
## View the data connection
A single data connection can be viewed using the `data_connections.get` endpoint
```python
client.data_connections.get(data_connection_name)
```

alternatively, all of the data connections in a workspace can be listed out with the `data_connections.list` method
```python
client.data_connections.list()
```
