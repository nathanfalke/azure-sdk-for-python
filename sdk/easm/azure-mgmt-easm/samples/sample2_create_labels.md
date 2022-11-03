# Manage labels
Labelling assets can be a convenient way to organize your workspace. For example, they could be used to keep track of multiple brands/organizations in your workspace. In this sample we'll go over how to create labels using the `EasmMgmtClient`

## Auth and setup
To create an `EasmMgmtClient`, you need your subscription ID, and some sort of credential. For the purposes of this demo, I've chosen the `DefaultAzureCredential` but any credential will work.

```python
import azure.identity as identity
from azure.mgmt.easm import EasmMgmtClient
from azure.mgmt.easm.models import WorkspaceResource

sub_id = "<your subscription id here>"

credential = identity.DefaultAzureCredential()
mgmt_client = EasmMgmtClient(sub_id, credential)
```
## Create labels
A new label can be created with the client's `labels.begin_create_and_update` method using your resource group, workspace name, and the name of your new label. You may also optionally specify a display name and color for your new label.

```python
from azure.mgmt.easm.models import LabelResource, LabelResourceProperties
label_name = '<your label name here>'
display_name = '<your display name here>'
color = '<your color here>'

properties = LabelResourceProperties(display_name=display_name, color=color)
label_resource = LabelResource(properties=properties)

response = mgmt_client.labels.begin_create_and_update(
	resource_group, workspace_name, label_name, label_resource)
```

## View labels
An individual label can be viewed using the `labels.get_by_workspace` method, by specifying resource group, workspace name, and label name. All labels for a workspace can be listed out using the `labels.list_by_workspace` method

```python
label = mgmt_client.labels.get_by_workspace(
	resource_group, workspace_name, label_name)
```

```python
labels = mgmt_client.labels.list_by_workspace(
	resource_group, workspace_name)
```

## Update labels
To update labels, use the `labels.update` method with the resource group, workspace name, and label name. Updatable fields include the display name and color, which can be provided in either a `LabelPatchResource` object or a `LabelResource` object

```python
from azure.mgmt.easm.models import LabelPatchResource
new_display_name = '<your new display name here>'
new_color = '<your new color here>'

new_properties = LabelResourceProperties(display_name=new_display_name, color=new_color)
patch = LabelPatchResource(properties=new_properties)

mgmt_client.labels.update(resource_group, workspace_name, label_name, patch)
```

## Delete labels
Should a label no longer be needed, it can be deleted using the client's `labels.begin_delete` method

```
mgmt_client.labels.begin_delete(resource_group, workspace_name, label_name)
```
