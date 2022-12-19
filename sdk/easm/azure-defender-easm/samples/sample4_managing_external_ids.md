# Managing external asset IDs through the api
External IDs can be a useful method of keeping track of assets in multiple systems, but it can be time consuming to manually tag each asset. In this example, we'll take a look at how you can, with a map of name/kind/external id, tag each asset in your inventory with an external id automatically using the SDK

## Creating an `EasmClient`
To create an `EasmClient`, you need your subscription ID, region, and some sort of credential. For the purposes of this demo, I've chosen the `InteractiveBrowserCredential` but any credential will work.

```python 
from azure.identity import InteractiveBrowserCredential
from azure.easm import EasmClient

sub_id = "<your subscription ID here>"
region = "<your region here>"

browser_credential = InteractiveBrowserCredential()
client = EasmClient(sub_id, browser_credential, region=region)
```

## Declare a name/external ID mapping
Assets in EASM can be uniquely distinguished by `name` and `kind`, so we can create a simple dictionary containing `name`, `kind`, and `external_id`. In a more realistic case, this could be generated using an export from the external system we're using for tagging, but for our purposes, we can manually write it out

```python
external_id_mapping = [
    {
        'name': 'example.com'
        'kind': 'host'
        'external_id': 'EXT040'
    },
    {
        'name': 'example.com'
        'kind': 'domain'
        'external_id': 'EXT041'
    },
    {
        'name': '93.184.216.34'
        'kind': 'ipAddress'
        'external_id': 'EXT042'
    },
    {
        'name': 'example.org'
        'kind': 'host'
        'external_id': 'EXT050'
    },
]
```
## Update assets 
Using the `assets` client, we can update each asset and append the tracking id of the update to our update ID list, so that we can keep track of the progress on each update later

```python
resource_group = "<your resource group here>"
workspace_name = "<your workspace name here>"

update_ids = []

for asset in external_id_mapping:
    update_request = {'external_id': asset['external_id']}
    asset_filter = f"kind = {asset['kind']} AND name = {asset['name']}"
    update = client.assets.update(resource_group, workspace_name, body=update_request, filter=asset_filter)
    update_ids.append(update['id'])
```

## View update progress
Using the `tasks` client, we can view the progress of each update using the `get` method
```python
for update_id in update_ids:
    update = client.tasks.get(update_id, resource_group, workspace_name)
    print(f'{update["id"]}: {update["state"]}')
```

looking at the responses, we can see that each update has completed
```
50448a6b-918c-42d5-b0d6-b1ee6e63ac60: complete
63bea3e7-a9d6-46b4-8c33-4f704d7a2570: complete
10b00cda-30b4-407a-aed1-5d5b6f48b36e: complete
```

## Review updates
The updates can be viewed using the `assets.list` method by creating a filter that matches on each external id using an `in` query
```python
asset_filter = f"External ID in ({', '.join([asset['external_id'] for asset in external_id_mapping])})"

for asset in client.assets.list(resource_group, workspace_name, filter=asset_filter):
    print(f'{asset["externalId"]}, {asset["name"]}')
```

