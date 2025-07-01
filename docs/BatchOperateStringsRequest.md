# BatchOperateStringsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | 操作类型，update - 更新，delete - 删除 | [optional] 
**id** | **List[int]** | 需要操作的词条的id | [optional] 
**stage** | [**Stage**](Stage.md) |  | [optional] [default to Stage.NUMBER_0]
**translation** | **str** | 词条翻译 | [optional] 

## Example

```python
from paratranz_cn_openapi_client.models.batch_operate_strings_request import BatchOperateStringsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchOperateStringsRequest from a JSON string
batch_operate_strings_request_instance = BatchOperateStringsRequest.from_json(json)
# print the JSON string representation of the object
print(BatchOperateStringsRequest.to_json())

# convert the object into a dict
batch_operate_strings_request_dict = batch_operate_strings_request_instance.to_dict()
# create an instance of BatchOperateStringsRequest from a dict
batch_operate_strings_request_from_dict = BatchOperateStringsRequest.from_dict(batch_operate_strings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


