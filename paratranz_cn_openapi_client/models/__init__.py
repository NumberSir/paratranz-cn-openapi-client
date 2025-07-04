# coding: utf-8

# flake8: noqa
"""
    ParaTranz OpenAPI 文档

    本文档介绍 ParaTranz.cn 平台的 API ## 获取 Token 首先需要获取API Token，可以在个人资料页面中的设置选项卡获取API Token， 调用 API 时将 Token 直接放在请求头的 Authorization 中即可。  cURL 使用示例:       $ curl --header \"Authorization: Bearer {TOKEN}\" https://paratranz.cn/api/projects  ## 错误处理 API 返回的错误格式如下       {       \"message\": \"ERROR MESSAGE\", // 错误消息       \"code\": 10000 // 5位错误代码，注意与下面的HTTP状态码区分，部分接口不返回     }  HTTP状态码有以下几种类型    * 400 - 调用参数错误   * 401 - Token 错误或过期   * 403 - 没有相关权限   * 404 - 资源不存在   * 405 - 没有相关HTTP方法，一般为调用方法错误   * 429 - 调用过于频繁，具体频率限制请看上一节   * 500 - 服务器错误，一般会提供具体出错的位置，请发送给站长方便定位问题   * 502 - 服务器无响应，部分用户被墙时可能会遇到   * 503 - 服务不可用   * 504 - 服务超时，访问量大时会出现  ## SDK 及 JSON 格式的 API 文档 本文档遵循 OpenAPI 规范，您可以 [获取 JSON 格式](/api-docs?format=json) 或 [YML 格式](/api-docs?format=yml) 的文档，并使用 [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) 生成各种语言的 SDK ## 更新历史    * v0.4.0 - 2025.04.02 增加批量操作词条接口说明   * v0.3.7 - 2025.03.29 补充更新文件接口说明   * v0.3.6 - 2024.07.12 修复获取 Token 说明   * v0.3.5 - 2023.12.25 修复部分 schema 问题   * v0.3.4 - 2023.12.23 增加API调用频率限制说明   * v0.3.3 - 2023.08.11 增加项目成员相关接口说明   * v0.3.2 - 2022.11.04 增加文件翻译相关接口说明   * v0.3.1 - 2022.10.16 修改 tag 及 schema 以便生成 sdk   * v0.3.0 - 2022.10.16 增加术语历史记录接口说明，调整历史记录接口字段; 增加文档中 operationId 定义;                         修复项目信息相关接口格式定义; 增加 JSON 格式文档入口   * v0.2.1 - 2022.07.23 增加成员贡献接口文档; 完善列表接口数据结构   * v0.2.0 - 2022.06.15 增加讨论及私信相关接口文档   * v0.1.3 - 2022.03.10 增加历史记录相关接口文档   * v0.1.2 - 2022.02.07 完善词条搜索接口 query 参数说明   * v0.1.1 - 2022.01.17 增加文件历史相关接口文档   * v0.1.0 - 2022.01.12 初次发布 

    The version of the OpenAPI document: 0.4.0
    Contact: master@mail.paratranz.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from paratranz_cn_openapi_client.models.artifact import Artifact
from paratranz_cn_openapi_client.models.batch_operate_strings_request import BatchOperateStringsRequest
from paratranz_cn_openapi_client.models.comment import Comment
from paratranz_cn_openapi_client.models.create_file200_response import CreateFile200Response
from paratranz_cn_openapi_client.models.create_issue_request import CreateIssueRequest
from paratranz_cn_openapi_client.models.edit_member_request import EditMemberRequest
from paratranz_cn_openapi_client.models.file import File
from paratranz_cn_openapi_client.models.get_file_revisions200_response import GetFileRevisions200Response
from paratranz_cn_openapi_client.models.get_history200_response import GetHistory200Response
from paratranz_cn_openapi_client.models.get_issue200_response import GetIssue200Response
from paratranz_cn_openapi_client.models.get_issues200_response import GetIssues200Response
from paratranz_cn_openapi_client.models.get_issues200_response_results_inner import GetIssues200ResponseResultsInner
from paratranz_cn_openapi_client.models.get_mails200_response import GetMails200Response
from paratranz_cn_openapi_client.models.get_projects200_response_inner import GetProjects200ResponseInner
from paratranz_cn_openapi_client.models.get_scores200_response import GetScores200Response
from paratranz_cn_openapi_client.models.get_strings200_response import GetStrings200Response
from paratranz_cn_openapi_client.models.get_term_history200_response import GetTermHistory200Response
from paratranz_cn_openapi_client.models.get_terms200_response import GetTerms200Response
from paratranz_cn_openapi_client.models.history import History
from paratranz_cn_openapi_client.models.history_target import HistoryTarget
from paratranz_cn_openapi_client.models.import_terms200_response import ImportTerms200Response
from paratranz_cn_openapi_client.models.issue import Issue
from paratranz_cn_openapi_client.models.job import Job
from paratranz_cn_openapi_client.models.mail import Mail
from paratranz_cn_openapi_client.models.member import Member
from paratranz_cn_openapi_client.models.operate_issue_request import OperateIssueRequest
from paratranz_cn_openapi_client.models.permission import Permission
from paratranz_cn_openapi_client.models.project import Project
from paratranz_cn_openapi_client.models.reply import Reply
from paratranz_cn_openapi_client.models.revision import Revision
from paratranz_cn_openapi_client.models.save_file_request import SaveFileRequest
from paratranz_cn_openapi_client.models.save_user_request import SaveUserRequest
from paratranz_cn_openapi_client.models.score import Score
from paratranz_cn_openapi_client.models.stage import Stage
from paratranz_cn_openapi_client.models.string_item import StringItem
from paratranz_cn_openapi_client.models.term import Term
from paratranz_cn_openapi_client.models.term_history import TermHistory
from paratranz_cn_openapi_client.models.term_history_target import TermHistoryTarget
from paratranz_cn_openapi_client.models.user import User
