# EditMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | [**Permission**](Permission.md) | 仅管理员及所有者可用，仅所有者可设置管理员 | [optional] 
**note** | **str** | 成员备注 | [optional] 

## Example

```python
from paratranz_cn_openapi_client.models.edit_member_request import EditMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditMemberRequest from a JSON string
edit_member_request_instance = EditMemberRequest.from_json(json)
# print the JSON string representation of the object
print(EditMemberRequest.to_json())

# convert the object into a dict
edit_member_request_dict = edit_member_request_instance.to_dict()
# create an instance of EditMemberRequest from a dict
edit_member_request_from_dict = EditMemberRequest.from_dict(edit_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


