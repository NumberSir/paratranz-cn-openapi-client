# GetProjects200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** | 页码 | [optional] [default to 1]
**page_size** | **float** | 每页数量 | [optional] [default to 50]
**row_count** | **float** | 总条数 | [optional] [default to 0]
**page_count** | **float** | 总页数，通过总条数与每页数量计算得出 | [optional] [default to 0]
**results** | [**List[Project]**](Project.md) |  | [optional] 

## Example

```python
from paratranz_cn_openapi_client.models.get_projects200_response_inner import GetProjects200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjects200ResponseInner from a JSON string
get_projects200_response_inner_instance = GetProjects200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetProjects200ResponseInner.to_json())

# convert the object into a dict
get_projects200_response_inner_dict = get_projects200_response_inner_instance.to_dict()
# create an instance of GetProjects200ResponseInner from a dict
get_projects200_response_inner_from_dict = GetProjects200ResponseInner.from_dict(get_projects200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


