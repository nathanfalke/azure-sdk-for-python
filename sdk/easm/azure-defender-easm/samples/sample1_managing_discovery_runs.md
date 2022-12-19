# Managing discovery runs

This sample shows you how to create and manage discovery runs in your workspace using the `discovery_groups` module of the `EasmClient` 

## Creating an `EasmClient`

To create an `EasmClient`, you need your subscription ID, region, and some sort of credential. For the purposes of this demo, I've chosen the `InteractiveBrowserCredential` but any credential will work.

```python 
from azure.identity import InteractiveBrowserCredential
from azure.easm import EasmClient

sub_id = '<your subscription ID here>'
region = '<your region here>'

browser_credential = InteractiveBrowserCredential()
client = EasmClient(sub_id, browser_credential, region=region)
```

## Creating new discovery groups

in order to start discovery runs, we must first create a discovery group, which is a collection of known assets that we can pivot off of. these are created using the `discovery_groups.put` method
```python
workspace_name = '<your workspace name here>'
resource_group = '<your resource group here>'

name = '<your discovery group name here>'
assets = [
    {'kind': 'domain', 'name': '<a domain you want to run discovery against>'},
    {'kind': 'host', 'name': '<a host you want to run discovery against>')
]
request = {
	'description': '<a description for your discovery group>', 
	'seeds': assets
}
response = client.discovery_groups.put(name, resource_group, workspace_name, request)
```

## Start a discovery run

Discovery groups created through the API's `put` method don't get run automatically, so we need to start the run ourselves.

```python
client.discovery_groups.run(name)
```

## Iterating over discovery groups and runs

We can list the disco groups using the `discovery_groups.list` method, and then list the runs using the `discovery_groups.list_runs` method. runs are returned as `ItemPaged`, so we can use `itertools.islice` to take the top 5 most recent runs.

Runs show up immediately after they've started, so if you don't see your run in the list, that means it hasn't been started

``` python
import itertools

for group in client.discovery_groups.list(resource_group, workspace_name):
    print(group['name'])
    runs = client.discovery_groups.list_runs(group['name'], resource_group, workspace_name)
    for run in itertools.islice(runs, 5):
        print(f" - started: {run['startedDate']}, finished: {run['completedDate']}, assets found: {run['totalAssetsFoundCount']}")
```

