# File

文件

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**created_at** | **datetime** | 文件创建时间 | [optional] [readonly] 
**updated_at** | **datetime** | 文件更新时间（上传文件时更新），默认为创建时间 | [optional] [readonly] 
**modified_at** | **datetime** | 文件修改时间（词条修改时更新），默认为创建时间；可利用此字段判断文件中词条是否有更新 | [optional] [readonly] 
**name** | **str** |  | [optional] 
**project** | **int** |  | [optional] [readonly] 
**format** | **str** | 文件格式，由系统自动计算 | [optional] [readonly] 
**total** | **int** | 文件总词条数 | [optional] [readonly] 
**translated** | **int** | 已翻译词条数 | [optional] [readonly] 
**disputed** | **int** | 有疑问的词条数 | [optional] [readonly] 
**checked** | **int** | 已检查的词条数 | [optional] [readonly] 
**reviewed** | **int** | 已审核的词条数 | [optional] [readonly] 
**hidden** | **int** | 已隐藏的词条数 | [optional] [readonly] 
**locked** | **int** | 已锁定的词条数 | [optional] [readonly] 
**words** | **int** | 总词数 | [optional] [readonly] 
**hash** | **str** | 上一次文件更新或创建时的原文件哈希值 | [optional] [readonly] 

## Example

```python
from paratranz_cn_openapi_client.models.file import File

# TODO update the JSON string below
json = "{}"
# create an instance of File from a JSON string
file_instance = File.from_json(json)
# print the JSON string representation of the object
print(File.to_json())

# convert the object into a dict
file_dict = file_instance.to_dict()
# create an instance of File from a dict
file_from_dict = File.from_dict(file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


