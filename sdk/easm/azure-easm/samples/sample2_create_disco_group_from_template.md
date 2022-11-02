# Create discovery group from a template
This sample shows you how to use the `disco_groups` module to create discovery groups using templates provided by the `disco_templates` module of the `EasmClient`

# Creating an `EasmClient`
To create an `EasmClient`, you need your subscription ID, region, and some sort of credential. For the purposes of this demo, I've chosen the `InteractiveBrowserCredential` but any credential will work.

```python 
from azure.identity import InteractiveBrowserCredential
from azure.easm import EasmClient

sub_id = '<your subscription ID here>'
region = '<your region here>'

browser_credential = InteractiveBrowserCredential()
client = EasmClient(sub_id, browser_credential, region=region)
```

## Find a disco template
The `disco_templates.list` method can be used to find a discovery template using a filter.
The endpoint will return templates based on a partial match on the `name` field.

```python
workspace_name = '<your workspace name here>'
resource_group = '<your resource group here>'

partial_name = 'taco'
templates = client.disco_templates.list(
	resource_group, workspace_name, filter=partial_name)

for template in templates:
    print(f'{template.id}: {template.display_name}')
```

## Get more details
To get more detail about a disco template, we can use the `disco_templates.get` method.
From here, we can see the names and seeds which would be used in a discovery run.

```python
template_id = '<your chosen template id>'
template = client.disco_templates.get(
	template_id, resource_group, workspace_name)

for name in template.names:
    print(name)

for seed in template.seeds:
    print(f'{seed.kind}, {seed.name}')
```

## Create a discovery group
The discovery template can be used to create a discovery group with using a `DiscoGroupRequest` and the `EasmClient`'s `disco_groups.put` method. Don't forget to run your new disco group with `disco_groups.run`

```python
group_name = '<your group name here>'
request = DiscoGroupRequest(template_id=template_id)

response = client.disco_groups.put(
	group_name, resource_group, workspace_name, body=request)

client.disco_groups.run(group_name, resource_group, workspace_name)
```
