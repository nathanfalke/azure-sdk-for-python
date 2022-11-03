# Create a workspace
Workspaces can be created programmatically over the API using the `EasmMgmtClient`

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

## Create workspace
To create your workspace, create a `WorkspaceResource` object, using your desired region for the location parameter, and then use the client's `workspaces.begin_create_and_update` method with your `resource_group`, `workspace_name`, and the `WorkspaceResource` to create your workspace

```python
resource_group = "<your resource group here>"
workspace_name = "<your workspace name here>"
region = "<your region here>"

resource = WorkspaceResource(location=region)
mgmt_client.workspaces.begin_create_and_update(
	resource_group, workspace_name, workspace_resource=resource)
```

## View the workspace
An individual workspace can be viewed using the `workspaces.get` method of the `EasmMgmtClient`
```python
mgmt_client.workspaces.get(resource_group, workspace_name)
```

All workspaces in a resource group, or across an entire subscription can be viewed using the provided `list_by_resource_group` and `list_by_subscription` methods
```python
mgmt_client.workspaces.list_by_resource_group(resource_group)
mgmt_client.workspaces.list_by_subscription()
```

## Delete the workspace
if a workspace is no longer needed, it can be removed with using the `workspaces.begin_delete` method
```python
mgmt_client.workspaces.begin_delete(resource_group, workspace_name)
```

