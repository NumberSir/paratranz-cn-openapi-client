# paratranz_cn_openapi_client.StringsApi

All URIs are relative to *https://paratranz.cn/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_operate_strings**](StringsApi.md#batch_operate_strings) | **PUT** /projects/{projectId}/strings | 批量修改/删除词条
[**create_string**](StringsApi.md#create_string) | **POST** /projects/{projectId}/strings | 创建词条
[**delete_string**](StringsApi.md#delete_string) | **DELETE** /projects/{projectId}/strings/{stringId} | 删除词条
[**get_string**](StringsApi.md#get_string) | **GET** /projects/{projectId}/strings/{stringId} | 获取词条
[**get_strings**](StringsApi.md#get_strings) | **GET** /projects/{projectId}/strings | 词条列表
[**save_string**](StringsApi.md#save_string) | **PUT** /projects/{projectId}/strings/{stringId} | 更新词条


# **batch_operate_strings**
> StringItem batch_operate_strings(project_id, batch_operate_strings_request)

批量修改/删除词条

批量修改或删除词条

### Example

* Api Key Authentication (Token):

```python
import paratranz_cn_openapi_client
from paratranz_cn_openapi_client.models.batch_operate_strings_request import BatchOperateStringsRequest
from paratranz_cn_openapi_client.models.string_item import StringItem
from paratranz_cn_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://paratranz.cn/api
# See configuration.py for a list of all supported configuration parameters.
configuration = paratranz_cn_openapi_client.Configuration(
    host = "https://paratranz.cn/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
async with paratranz_cn_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paratranz_cn_openapi_client.StringsApi(api_client)
    project_id = 867 # int | 项目ID
    batch_operate_strings_request = paratranz_cn_openapi_client.BatchOperateStringsRequest() # BatchOperateStringsRequest | 

    try:
        # 批量修改/删除词条
        api_response = await api_instance.batch_operate_strings(project_id, batch_operate_strings_request)
        print("The response of StringsApi->batch_operate_strings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StringsApi->batch_operate_strings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **batch_operate_strings_request** | [**BatchOperateStringsRequest**](BatchOperateStringsRequest.md)|  | 

### Return type

[**StringItem**](StringItem.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 返回词条信息 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_string**
> StringItem create_string(project_id, string_item)

创建词条

创建词条

### Example

* Api Key Authentication (Token):

```python
import paratranz_cn_openapi_client
from paratranz_cn_openapi_client.models.string_item import StringItem
from paratranz_cn_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://paratranz.cn/api
# See configuration.py for a list of all supported configuration parameters.
configuration = paratranz_cn_openapi_client.Configuration(
    host = "https://paratranz.cn/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
async with paratranz_cn_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paratranz_cn_openapi_client.StringsApi(api_client)
    project_id = 867 # int | 项目ID
    string_item = paratranz_cn_openapi_client.StringItem() # StringItem | 

    try:
        # 创建词条
        api_response = await api_instance.create_string(project_id, string_item)
        print("The response of StringsApi->create_string:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StringsApi->create_string: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **string_item** | [**StringItem**](StringItem.md)|  | 

### Return type

[**StringItem**](StringItem.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 返回词条信息 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_string**
> delete_string(project_id, string_id)

删除词条

通过ID删除词条，仅管理员可用

### Example

* Api Key Authentication (Token):

```python
import paratranz_cn_openapi_client
from paratranz_cn_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://paratranz.cn/api
# See configuration.py for a list of all supported configuration parameters.
configuration = paratranz_cn_openapi_client.Configuration(
    host = "https://paratranz.cn/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
async with paratranz_cn_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paratranz_cn_openapi_client.StringsApi(api_client)
    project_id = 867 # int | 项目ID
    string_id = 1066 # int | 词条ID

    try:
        # 删除词条
        await api_instance.delete_string(project_id, string_id)
    except Exception as e:
        print("Exception when calling StringsApi->delete_string: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **string_id** | **int**| 词条ID | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 删除成功 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_string**
> StringItem get_string(project_id, string_id)

获取词条

通过ID获取词条信息

### Example

* Api Key Authentication (Token):

```python
import paratranz_cn_openapi_client
from paratranz_cn_openapi_client.models.string_item import StringItem
from paratranz_cn_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://paratranz.cn/api
# See configuration.py for a list of all supported configuration parameters.
configuration = paratranz_cn_openapi_client.Configuration(
    host = "https://paratranz.cn/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
async with paratranz_cn_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paratranz_cn_openapi_client.StringsApi(api_client)
    project_id = 867 # int | 项目ID
    string_id = 1066 # int | 词条ID

    try:
        # 获取词条
        api_response = await api_instance.get_string(project_id, string_id)
        print("The response of StringsApi->get_string:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StringsApi->get_string: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **string_id** | **int**| 词条ID | 

### Return type

[**StringItem**](StringItem.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 返回词条信息 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_strings**
> GetStrings200Response get_strings(project_id, file_id, page=page, page_size=page_size, stage=stage)

词条列表

获取项目词条

### Example

* Api Key Authentication (Token):

```python
import paratranz_cn_openapi_client
from paratranz_cn_openapi_client.models.get_strings200_response import GetStrings200Response
from paratranz_cn_openapi_client.models.stage import Stage
from paratranz_cn_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://paratranz.cn/api
# See configuration.py for a list of all supported configuration parameters.
configuration = paratranz_cn_openapi_client.Configuration(
    host = "https://paratranz.cn/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
async with paratranz_cn_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paratranz_cn_openapi_client.StringsApi(api_client)
    project_id = 867 # int | 项目ID
    file_id = 1453 # int | 文件ID
    page = 1 # int | 页码 (optional) (default to 1)
    page_size = 50 # int | 每页数量 (optional) (default to 50)
    stage = 0 # Stage | 筛选词条状态 (optional) (default to 0)

    try:
        # 词条列表
        api_response = await api_instance.get_strings(project_id, file_id, page=page, page_size=page_size, stage=stage)
        print("The response of StringsApi->get_strings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StringsApi->get_strings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **file_id** | **int**| 文件ID | 
 **page** | **int**| 页码 | [optional] [default to 1]
 **page_size** | **int**| 每页数量 | [optional] [default to 50]
 **stage** | [**Stage**](.md)| 筛选词条状态 | [optional] [default to 0]

### Return type

[**GetStrings200Response**](GetStrings200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 返回词条列表 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_string**
> StringItem save_string(project_id, string_id, string_item)

更新词条

通过ID更新词条信息

### Example

* Api Key Authentication (Token):

```python
import paratranz_cn_openapi_client
from paratranz_cn_openapi_client.models.string_item import StringItem
from paratranz_cn_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://paratranz.cn/api
# See configuration.py for a list of all supported configuration parameters.
configuration = paratranz_cn_openapi_client.Configuration(
    host = "https://paratranz.cn/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
async with paratranz_cn_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paratranz_cn_openapi_client.StringsApi(api_client)
    project_id = 867 # int | 项目ID
    string_id = 1066 # int | 词条ID
    string_item = paratranz_cn_openapi_client.StringItem() # StringItem | 

    try:
        # 更新词条
        api_response = await api_instance.save_string(project_id, string_id, string_item)
        print("The response of StringsApi->save_string:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StringsApi->save_string: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **string_id** | **int**| 词条ID | 
 **string_item** | [**StringItem**](StringItem.md)|  | 

### Return type

[**StringItem**](StringItem.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 返回词条信息 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

