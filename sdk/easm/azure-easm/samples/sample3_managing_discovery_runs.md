# Managing Discovery Runs

This sample shows you how to create and manage discovery runs in your workspace using the `disco_groups` module of the `EasmClient` 

# Creating an `EasmClient`

To create an `EasmClient`, you need your subscription ID, region, and some sort of credential. For the purposes of this demo, I've chosen the `InteractiveBrowserCredential` but any credential will work.

```python 
from azure.identity import InteractiveBrowserCredential
from azure.easm import EasmClient

sub_id = "<your subscription ID here>"
region = "<your region here>"

browser_credential = InteractiveBrowserCredential()
client = EasmClient(sub_id, browser_credential, region=region)
```

# Creating New Discovery Groups

in order to start discovery runs, we must first create a discovery group, which is a collection of known assets that we can pivot off of. these are created using the `disco_groups.put` method
```python
from azure.easm.models import (AssetId, DiscoGroupRequest)

name = "sample_discovery_group"
assets = [
    AssetId(kind="domain", name="xkcd.com"),
    AssetId(kind="host", name="xkcd.com")
]
request = DiscoGroupRequest(
	description="Sample discovery group", 
	seeds=assets
)
response = client.disco_groups.put(name, rg, workspace_name, request)
```

# Start a Discovery Run

Discovery groups created through the API's `put` method don't get run automatically, so we need to start the run ourselves.

```
client.disco_groups.run(name)
```

# Iterating Over Discovery Groups and Runs

We can list the disco groups using the `disco_groups.list` method, and then list the runs using the `disco_groups.list_runs` method. runs are returned as `ItemPaged`, so we can use `itertools.islice` to take the top 5 most recent runs.

Runs show up immediately after they've started, so if you don't see your run in the list, that means it hasn't been started

``` python
import itertools

for group in client.disco_groups.list(resource_group, workspace_name):
    print(group.name)
    runs = client.disco_groups.list_runs(group.name, resource_group, workspace_name)
    for run in itertools.islice(runs, 5):
        print(f' - started: {run.started_date}, finished: {run.completed_date}, assets found: {run.total_assets_found_count}')
```

