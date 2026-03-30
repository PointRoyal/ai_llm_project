# Knife4j 接口完整说明（请求方法 · 请求参数 · 请求头 · 响应）

> 由 Swagger 2.0 JSON 自动生成，**与线上一致性取决于文档是否最新**。  
> 生成命令：`python3 auto_test/scripts/export_swagger_api_doc.py <swagger.json> <输出.md>`

**Swagger**：`http://10.50.31.141:28001/v2/api-docs?group=在线文档`  
**info**：在线文档 — shuhan-admin-cloud 在线文档

## 一、全局请求头说明

Knife4j 往往不会在**每个** operation 下列出网关统一要求的头。除下表「Swagger 在各接口声明的 header 参数」外，实际调用通常还包括：

| 请求头 | 典型值 | 说明 |
|--------|--------|------|
| Authorization | `Bearer <token>` | 用户端、管理端各自 token，见 `config/api.yaml` |
| Sh-Client | `Basic ...` | 与前端一致的客户端标识 |
| Content-Type | `application/json` | POST JSON 时；文件上传为 `multipart/form-data` |
| Accept | `application/json` 等 | 按网关约定 |

### Swagger securityDefinitions

- **`令牌`**: `{"type": "apiKey", "name": "Authorization", "in": "header"}`

### 关于「杂项 Query 参数」

部分 POST 接口在 Swagger 中会出现大量与当前业务无关的 `query` 字段（形似把登录用户对象摊平）。**实现上通常只传 Body（及 path 变量）即可**；以下原文档照录 Swagger，便于对照，**请以实际抓包 / 服务端为准**。

---

## 二、投稿人

### `GET` `/api/app/appUser/getByUseCode`

**摘要**：根据用途获取协议信息  

**operationId**：`getByUseCodeUsingGET`  

#### 请求方法

- **GET** `/api/app/appUser/getByUseCode`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `code` | 可选 | `string` | code |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **object** 用户协议配置表
      - `activeTime`: *string* `date-time`
      - `createTime`: *string* `date-time`
      - `createUser`: *integer* `int64`
      - `documentName`: *string*
      - `documentUrl`: *string*
      - `id`: *string*
      - `name`: *string*
      - `purpose`:
        - **object**
          - `data`: *string*
          - `key`: *string*
      - `status`: *integer* `int32`
      - `updateTime`: *string* `date-time`
      - `updateUser`: *integer* `int64`
      - `version`: *string*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/app/appUser/login`

**摘要**：投稿人登录  

**operationId**：`loginUsingPOST_1`  

#### 请求方法

- **POST** `/api/app/appUser/login`

#### 请求参数

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `loginVm` | 必填 | - **object**<br>- `account` **必填**: *string*<br>- `code` **必填**: *string*<br>- `grantType` **必填**: *string*<br>- `key` **必填**: *string*<br>- `name` **必填**: *string*<br>- `password` **必填**: *string*<br>- `rememberMe`: *boolean*<br>- `zzdCode` **必填**: *string*<br>- `zzdId` **必填**: *string* | loginVm |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **object** 认证信息
      - `account`: *string*
      - `avatar`: *string*
      - `email`: *string*
      - `firstLoginFlag`: *boolean*
      - `mobile`: *string*
      - `name`: *string*
      - `orgId`: *integer* `int64`
      - `token`: *string*
      - `userId`: *integer* `int64`
      - `workDescribe`: *string*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/app/appUser/registerAppUser`

**摘要**：投稿人注册  

**operationId**：`registerAppUserUsingPOST_1`  

#### 请求方法

- **POST** `/api/app/appUser/registerAppUser`

#### 请求参数

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `userSaveDTO` | 必填 | - **object** 投稿人信息表<br>- `account`: *string*<br>- `name`: *string*<br>- `password`: *string*<br>- `station`: *string* | userSaveDTO |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **object** 投稿人信息VO
      - `account`: *string*
      - `firstLoginFlag`: *boolean*
      - `id`: *integer* `int64`
      - `lastLoginTime`: *string* `date-time`
      - `name`: *string*
      - `passwordErrorLastTime`: *string* `date-time`
      - `passwordErrorNum`: *integer* `int32`
      - `passwordExpireTime`: *string* `date-time`
      - `station`: *string*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/app/appUser/resetPassword`

**摘要**：投稿人密码重置  

**operationId**：`resetPasswordUsingPOST_2`  

#### 请求方法

- **POST** `/api/app/appUser/resetPassword`

#### 请求参数

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `updateDTO` | 必填 | - **object** 投稿人信息表<br>- `account`: *string*<br>- `password`: *string* | updateDTO |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *boolean*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


---

## 二、投稿人-系统管理端

### `DELETE` `/api/system/appUser/delete`

**摘要**：删除  

**operationId**：`deleteUsingDELETE_3`  

#### 请求方法

- **DELETE** `/api/system/appUser/delete`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `ids[]` | 可选 | `ref` | 主键id |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *boolean*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/system/appUser/page`

**摘要**：投稿人分页列表查询  

**operationId**：`pageUsingPOST_3`  

#### 请求方法

- **POST** `/api/system/appUser/page`

#### 请求参数

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `params` | 必填 | - **object** 分页参数<br>- `current`: *integer* `int64`<br>- `map`:<br>- **object**（空） 扩展参数<br>- `model` **必填**:<br>- **object** 投稿人信息表<br>- `account`: *string*<br>- `name`: *string*<br>- `station`: *string*<br>- `order`: *string*<br>- `size`: *integer* `int64`<br>- `sort`: *string* | params |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **object**
      - `current`: *integer* `int64`
      - `hitCount`: *boolean*
      - `pages`: *integer* `int64`
      - `records`:
        - **array**
          - **object** 投稿人信息VO
            - `account`: *string*
            - `firstLoginFlag`: *boolean*
            - `id`: *integer* `int64`
            - `lastLoginTime`: *string* `date-time`
            - `name`: *string*
            - `passwordErrorLastTime`: *string* `date-time`
            - `passwordErrorNum`: *integer* `int32`
            - `passwordExpireTime`: *string* `date-time`
            - `station`: *string*
      - `searchCount`: *boolean*
      - `size`: *integer* `int64`
      - `total`: *integer* `int64`
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/system/appUser/resetPassword`

**摘要**：投稿人密码重置  

**operationId**：`resetPasswordUsingPOST_3`  

#### 请求方法

- **POST** `/api/system/appUser/resetPassword`

#### 请求参数

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `updateDTO` | 必填 | - **object** 投稿人信息表<br>- `account`: *string*<br>- `password`: *string* | updateDTO |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *boolean*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/system/appUser/update`

**摘要**：投稿人信息更新  

**operationId**：`updateUsingPOST_2`  

#### 请求方法

- **POST** `/api/system/appUser/update`

#### 请求参数

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `updateDTO` | 必填 | - **object** 投稿人信息表<br>- `id`: *integer* `int64`<br>- `name`: *string*<br>- `station`: *string* | updateDTO |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *boolean*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


---

## 二、投稿模板

### `POST` `/api/template/deleteTemplate`

**摘要**：删除投稿模板  

**operationId**：`deleteTemplateUsingPOST`  

#### 请求方法

- **POST** `/api/template/deleteTemplate`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `account` | 可选 | `string` |  |
| `email` | 可选 | `string` |  |
| `firstLoginFlag` | 可选 | `boolean` | 是否首次登录标志，false：否；true：是 |
| `id` | 可选 | `integer` (`int64`) |  |
| `idCard` | 可选 | `string` |  |
| `loginCount` | 可选 | `integer` (`int32`) |  |
| `mobile` | 可选 | `string` |  |
| `name` | 可选 | `string` |  |
| `org.abbreviation` | 可选 | `string` |  |
| `org.describe` | 可选 | `string` |  |
| `org.id` | 可选 | `integer` (`int64`) |  |
| `org.label` | 可选 | `string` |  |
| `org.orgCode` | 可选 | `string` |  |
| `org.parentId` | 可选 | `integer` (`int64`) |  |
| `org.sortValue` | 可选 | `integer` (`int32`) |  |
| `org.status` | 可选 | `boolean` |  |
| `orgId` | 可选 | `integer` (`int64`) |  |
| `password` | 可选 | `string` |  |
| `passwordErrorLastTime` | 可选 | `string` (`date-time`) | 最后一次输错密码时间 |
| `passwordErrorNum` | 可选 | `integer` (`int32`) | 密码错误次数 |
| `passwordExpireTime` | 可选 | `string` (`date-time`) | 密码过期时间 |
| `photo` | 可选 | `string` |  |
| `resources` | 可选 | `array` |  |
| `roles[0].code` | 可选 | `string` |  |
| `roles[0].describe` | 可选 | `string` |  |
| `roles[0].dsType.code` | 可选 | `string` | 编码 |
| `roles[0].dsType.declaringClass` | 可选 | `ref` |  |
| `roles[0].dsType.desc` | 可选 | `string` | 描述 |
| `roles[0].dsType.val` | 可选 | `integer` (`int32`) | 值 |
| `roles[0].id` | 可选 | `integer` (`int64`) |  |
| `roles[0].isEnable` | 可选 | `boolean` |  |
| `roles[0].isReadonly` | 可选 | `boolean` |  |
| `roles[0].name` | 可选 | `string` |  |
| `station` | 可选 | `string` |  |
| `status` | 可选 | `boolean` | 状态 |
| `superAdmin` | 可选 | `boolean` |  |
| `token` | 可选 | `string` |  |
| `username` | 可选 | `string` |  |
| `workDescribe` | 可选 | `string` |  |

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `params` | 必填 | - **object** 投稿模板表<br>- `contentElements`: *string*<br>- `domain`:<br>- **array** 模板所属领域code<br>- *string*<br>- `iconUrl`: *string*<br>- `id`: *integer* `int64`<br>- `name`: *string*<br>- `status`: *integer* `int32`<br>- `title`: *string*<br>- `titleDesc`: *string* | params |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *boolean*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `GET` `/api/template/detailTemplate`

**摘要**：获取投稿模板详情  

**operationId**：`detailTemplateUsingGET`  

#### 请求方法

- **GET** `/api/template/detailTemplate`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `id` | 必填 | `integer` (`int64`) | id |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **object** 投稿模板表
      - `contentElements`: *string*
      - `domains`:
        - **array** 所属领域
          - **object** 模板领域关联表
            - `createTime`: *string* `date-time`
            - `createUser`: *integer* `int64`
            - `domainCode`: *string*
            - `domainName`: *string*
            - `id`: *string*
            - `templateId`: *integer* `int64`
            - `updateTime`: *string* `date-time`
            - `updateUser`: *integer* `int64`
      - `iconUrl`: *string*
      - `id`: *integer* `int64`
      - `name`: *string*
      - `status`: *integer* `int32`
      - `title`: *string*
      - `titleDesc`: *string*
      - `updateTime`: *string* `date-time`
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/template/disableTemplate`

**摘要**：禁用/启用投稿模板  

**operationId**：`disableTemplateUsingPOST`  

#### 请求方法

- **POST** `/api/template/disableTemplate`

#### 请求参数

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `params` | 必填 | - **object** 投稿模板表<br>- `contentElements`: *string*<br>- `domain`:<br>- **array** 模板所属领域code<br>- *string*<br>- `iconUrl`: *string*<br>- `id`: *integer* `int64`<br>- `name`: *string*<br>- `status`: *integer* `int32`<br>- `title`: *string*<br>- `titleDesc`: *string* | params |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *boolean*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/template/pageTemplate`

**摘要**：获取投稿模板分页列表  

**operationId**：`pageTemplateUsingPOST`  

#### 请求方法

- **POST** `/api/template/pageTemplate`

#### 请求参数

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `params` | 必填 | - **object** 分页参数<br>- `current`: *integer* `int64`<br>- `map`:<br>- **object**（空） 扩展参数<br>- `model` **必填**:<br>- **object** 投稿模板表<br>- `contentElements`: *string*<br>- `domains`:<br>- **array** 所属领域<br>- **object** 模板领域关联表<br>- `createTime`: *string* `date-time`<br>- `createUser`: *integer* `int64`<br>- `domainCode`: *string*<br>- `domainName`: *string*<br>- `id`: *string*<br>- `templateId`: *integer* `int64`<br>- `updateTime`: *string* `date-time`<br>- `updateUser`: *integer* `int64`<br>- `iconUrl`: *string*<br>- `id`: *integer* `int64`<br>- `name`: *string*<br>- `status`: *integer* `int32`<br>- `title`: *string*<br>- `titleDesc`: *string*<br>- `updateTime`: *string* `date-time`<br>- `order`: *string*<br>- `size`: *integer* `int64`<br>- `sort`: *string* | params |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **object**
      - `current`: *integer* `int64`
      - `hitCount`: *boolean*
      - `pages`: *integer* `int64`
      - `records`:
        - **array**
          - **object** 投稿模板表
            - `contentElements`: *string*
            - `domains`:
              - **array** 所属领域
                - **object** 模板领域关联表
                  - `createTime`: *string* `date-time`
                  - `createUser`: *integer* `int64`
                  - `domainCode`: *string*
                  - `domainName`: *string*
                  - `id`: *string*
                  - `templateId`: *integer* `int64`
                  - `updateTime`: *string* `date-time`
                  - `updateUser`: *integer* `int64`
            - `iconUrl`: *string*
            - `id`: *integer* `int64`
            - `name`: *string*
            - `status`: *integer* `int32`
            - `title`: *string*
            - `titleDesc`: *string*
            - `updateTime`: *string* `date-time`
      - `searchCount`: *boolean*
      - `size`: *integer* `int64`
      - `total`: *integer* `int64`
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/template/saveTemplate`

**摘要**：保存投稿模板  

**operationId**：`saveTemplateUsingPOST`  

#### 请求方法

- **POST** `/api/template/saveTemplate`

#### 请求参数

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `params` | 必填 | - **object** 投稿模板表<br>- `contentElements`: *string*<br>- `domain`:<br>- **array** 模板所属领域code<br>- *string*<br>- `iconUrl`: *string*<br>- `name`: *string*<br>- `status`: *integer* `int32`<br>- `title`: *string*<br>- `titleDesc`: *string* | params |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *boolean*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/template/updateTemplate`

**摘要**：更新投稿模板  

**operationId**：`updateTemplateUsingPOST`  

#### 请求方法

- **POST** `/api/template/updateTemplate`

#### 请求参数

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `params` | 必填 | - **object** 投稿模板表<br>- `contentElements`: *string*<br>- `domain`:<br>- **array** 模板所属领域code<br>- *string*<br>- `iconUrl`: *string*<br>- `id`: *integer* `int64`<br>- `name`: *string*<br>- `status`: *integer* `int32`<br>- `title`: *string*<br>- `titleDesc`: *string* | params |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *boolean*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


---

## 二、投稿端-稿件发布控制类

### `POST` `/api/app/submission/countMyselfSubmission`

**摘要**：获取用户投稿数量  

**operationId**：`countMyselfSubmissionUsingPOST`  

#### 请求方法

- **POST** `/api/app/submission/countMyselfSubmission`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `account` | 可选 | `string` |  |
| `email` | 可选 | `string` |  |
| `firstLoginFlag` | 可选 | `boolean` | 是否首次登录标志，false：否；true：是 |
| `id` | 可选 | `integer` (`int64`) |  |
| `idCard` | 可选 | `string` |  |
| `loginCount` | 可选 | `integer` (`int32`) |  |
| `mobile` | 可选 | `string` |  |
| `name` | 可选 | `string` |  |
| `org.abbreviation` | 可选 | `string` |  |
| `org.describe` | 可选 | `string` |  |
| `org.id` | 可选 | `integer` (`int64`) |  |
| `org.label` | 可选 | `string` |  |
| `org.orgCode` | 可选 | `string` |  |
| `org.parentId` | 可选 | `integer` (`int64`) |  |
| `org.sortValue` | 可选 | `integer` (`int32`) |  |
| `org.status` | 可选 | `boolean` |  |
| `orgId` | 可选 | `integer` (`int64`) |  |
| `password` | 可选 | `string` |  |
| `passwordErrorLastTime` | 可选 | `string` (`date-time`) | 最后一次输错密码时间 |
| `passwordErrorNum` | 可选 | `integer` (`int32`) | 密码错误次数 |
| `passwordExpireTime` | 可选 | `string` (`date-time`) | 密码过期时间 |
| `photo` | 可选 | `string` |  |
| `resources` | 可选 | `array` |  |
| `roles[0].code` | 可选 | `string` |  |
| `roles[0].describe` | 可选 | `string` |  |
| `roles[0].dsType.code` | 可选 | `string` | 编码 |
| `roles[0].dsType.declaringClass` | 可选 | `ref` |  |
| `roles[0].dsType.desc` | 可选 | `string` | 描述 |
| `roles[0].dsType.val` | 可选 | `integer` (`int32`) | 值 |
| `roles[0].id` | 可选 | `integer` (`int64`) |  |
| `roles[0].isEnable` | 可选 | `boolean` |  |
| `roles[0].isReadonly` | 可选 | `boolean` |  |
| `roles[0].name` | 可选 | `string` |  |
| `station` | 可选 | `string` |  |
| `status` | 可选 | `boolean` | 状态 |
| `superAdmin` | 可选 | `boolean` |  |
| `token` | 可选 | `string` |  |
| `username` | 可选 | `string` |  |
| `workDescribe` | 可选 | `string` |  |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **object** 用户我的投稿统计
      - `countAll`: *integer* `int32`
      - `countPassed`: *integer* `int32`
      - `countRejected`: *integer* `int32`
      - `countUnderReview`: *integer* `int32`
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/app/submission/deleteSubmission`

**摘要**：删除投稿  

**operationId**：`deleteSubmissionUsingPOST`  

#### 请求方法

- **POST** `/api/app/submission/deleteSubmission`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `account` | 可选 | `string` |  |
| `email` | 可选 | `string` |  |
| `firstLoginFlag` | 可选 | `boolean` | 是否首次登录标志，false：否；true：是 |
| `id` | 可选 | `integer` (`int64`) |  |
| `idCard` | 可选 | `string` |  |
| `loginCount` | 可选 | `integer` (`int32`) |  |
| `mobile` | 可选 | `string` |  |
| `name` | 可选 | `string` |  |
| `org.abbreviation` | 可选 | `string` |  |
| `org.describe` | 可选 | `string` |  |
| `org.id` | 可选 | `integer` (`int64`) |  |
| `org.label` | 可选 | `string` |  |
| `org.orgCode` | 可选 | `string` |  |
| `org.parentId` | 可选 | `integer` (`int64`) |  |
| `org.sortValue` | 可选 | `integer` (`int32`) |  |
| `org.status` | 可选 | `boolean` |  |
| `orgId` | 可选 | `integer` (`int64`) |  |
| `password` | 可选 | `string` |  |
| `passwordErrorLastTime` | 可选 | `string` (`date-time`) | 最后一次输错密码时间 |
| `passwordErrorNum` | 可选 | `integer` (`int32`) | 密码错误次数 |
| `passwordExpireTime` | 可选 | `string` (`date-time`) | 密码过期时间 |
| `photo` | 可选 | `string` |  |
| `resources` | 可选 | `array` |  |
| `roles[0].code` | 可选 | `string` |  |
| `roles[0].describe` | 可选 | `string` |  |
| `roles[0].dsType.code` | 可选 | `string` | 编码 |
| `roles[0].dsType.declaringClass` | 可选 | `ref` |  |
| `roles[0].dsType.desc` | 可选 | `string` | 描述 |
| `roles[0].dsType.val` | 可选 | `integer` (`int32`) | 值 |
| `roles[0].id` | 可选 | `integer` (`int64`) |  |
| `roles[0].isEnable` | 可选 | `boolean` |  |
| `roles[0].isReadonly` | 可选 | `boolean` |  |
| `roles[0].name` | 可选 | `string` |  |
| `station` | 可选 | `string` |  |
| `status` | 可选 | `boolean` | 状态 |
| `superAdmin` | 可选 | `boolean` |  |
| `token` | 可选 | `string` |  |
| `username` | 可选 | `string` |  |
| `workDescribe` | 可选 | `string` |  |

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `params` | 必填 | - **object** 查询稿件下的重复稿件分页列表入参<br>- `submissionId`: *integer* `int64` | params |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *boolean*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `GET` `/api/app/submission/detailSubmission/{submissionId}`

**摘要**：获取投稿详情  

**operationId**：`detailSubmissionUsingGET`  

#### 请求方法

- **GET** `/api/app/submission/detailSubmission/{submissionId}`

#### 请求参数

**路径参数（Path）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `submissionId` | 必填 | `integer` (`int64`) | submissionId |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **object** 稿件详情VO
      - `anonymous`: *integer* `int32`
      - `assigneeName`: *string*
      - `assigneeRemark`: *string*
      - `attachments`:
        - **array** 附件
          - **object** 附件表
            - `businessType`: *string*
            - `createTime`: *string* `date-time`
            - `createUser`: *integer* `int64`
            - `fileName`: *string*
            - `fileSize`: *integer* `int64`
            - `fileUrl`: *string*
            - `id`: *string*
            - `mimeType`: *string*
            - `sortNo`: *integer* `int32`
            - `updateTime`: *string* `date-time`
            - `updateUser`: *integer* `int64`
      - `businessFlag`: *integer* `int32`
      - `citationText`: *string*
      - `contentElements`: *string*
      - `createTime`: *string* `date-time`
      - `createUser`: *integer* `int64`
      - `currentReviewerId`: *integer* `int64`
      - `currentTaskId`: *integer* `int64`
      - `domainCode`: *string*
      - `domainName`: *string*
      - `id`: *string*
      - `lastActionTime`: *string* `date-time`
      - `remark`: *string*
      - `repetitionRate`: *number*
      - `status`: *integer* `int32`
      - `submissionNo`: *string*
      - `submitTime`: *string* `date-time`
      - `submitType`: *integer* `int32`
      - `submitter`: *string*
      - `submitterId`: *integer* `int64`
      - `templateId`: *integer* `int64`
      - `title`: *string*
      - `updateTime`: *string* `date-time`
      - `updateUser`: *integer* `int64`
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `GET` `/api/app/submission/listTemplate`

**摘要**：获取所有模板列表  

**operationId**：`listTemplateUsingGET`  

#### 请求方法

- **GET** `/api/app/submission/listTemplate`

#### 请求参数

*Swagger 未声明 parameters。*

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **array** 响应数据
      - **object** 投稿模板表
        - `contentElements`: *string*
        - `domains`:
          - **array** 所属领域
            - **object** 模板领域关联表
              - `createTime`: *string* `date-time`
              - `createUser`: *integer* `int64`
              - `domainCode`: *string*
              - `domainName`: *string*
              - `id`: *string*
              - `templateId`: *integer* `int64`
              - `updateTime`: *string* `date-time`
              - `updateUser`: *integer* `int64`
        - `iconUrl`: *string*
        - `id`: *integer* `int64`
        - `name`: *string*
        - `status`: *integer* `int32`
        - `title`: *string*
        - `titleDesc`: *string*
        - `updateTime`: *string* `date-time`
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/app/submission/pageMyselfSubmission`

**摘要**：分页获取用户投稿列表/草稿箱列表  

**operationId**：`pageMyselfSubmissionUsingPOST`  

#### 请求方法

- **POST** `/api/app/submission/pageMyselfSubmission`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `account` | 可选 | `string` |  |
| `email` | 可选 | `string` |  |
| `firstLoginFlag` | 可选 | `boolean` | 是否首次登录标志，false：否；true：是 |
| `id` | 可选 | `integer` (`int64`) |  |
| `idCard` | 可选 | `string` |  |
| `loginCount` | 可选 | `integer` (`int32`) |  |
| `mobile` | 可选 | `string` |  |
| `name` | 可选 | `string` |  |
| `org.abbreviation` | 可选 | `string` |  |
| `org.describe` | 可选 | `string` |  |
| `org.id` | 可选 | `integer` (`int64`) |  |
| `org.label` | 可选 | `string` |  |
| `org.orgCode` | 可选 | `string` |  |
| `org.parentId` | 可选 | `integer` (`int64`) |  |
| `org.sortValue` | 可选 | `integer` (`int32`) |  |
| `org.status` | 可选 | `boolean` |  |
| `orgId` | 可选 | `integer` (`int64`) |  |
| `password` | 可选 | `string` |  |
| `passwordErrorLastTime` | 可选 | `string` (`date-time`) | 最后一次输错密码时间 |
| `passwordErrorNum` | 可选 | `integer` (`int32`) | 密码错误次数 |
| `passwordExpireTime` | 可选 | `string` (`date-time`) | 密码过期时间 |
| `photo` | 可选 | `string` |  |
| `resources` | 可选 | `array` |  |
| `roles[0].code` | 可选 | `string` |  |
| `roles[0].describe` | 可选 | `string` |  |
| `roles[0].dsType.code` | 可选 | `string` | 编码 |
| `roles[0].dsType.declaringClass` | 可选 | `ref` |  |
| `roles[0].dsType.desc` | 可选 | `string` | 描述 |
| `roles[0].dsType.val` | 可选 | `integer` (`int32`) | 值 |
| `roles[0].id` | 可选 | `integer` (`int64`) |  |
| `roles[0].isEnable` | 可选 | `boolean` |  |
| `roles[0].isReadonly` | 可选 | `boolean` |  |
| `roles[0].name` | 可选 | `string` |  |
| `station` | 可选 | `string` |  |
| `status` | 可选 | `boolean` | 状态 |
| `superAdmin` | 可选 | `boolean` |  |
| `token` | 可选 | `string` |  |
| `username` | 可选 | `string` |  |
| `workDescribe` | 可选 | `string` |  |

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `params` | 必填 | - **object** 分页参数<br>- `current`: *integer* `int64`<br>- `map`:<br>- **object**（空） 扩展参数<br>- `model` **必填**:<br>- **object** 用户投稿列表<br>- `domainCode`: *string*<br>- `domainName`: *string*<br>- `id`: *integer* `int64`<br>- `repetitionRate`: *number*<br>- `status`: *string*<br>- `submitTime`: *string* `date-time`<br>- `submitType`: *integer* `int32`<br>- `title`: *string*<br>- `urgeTime`: *string* `date-time`<br>- `urgencyStatus`: *string*<br>- `order`: *string*<br>- `size`: *integer* `int64`<br>- `sort`: *string* | params |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **object**
      - `current`: *integer* `int64`
      - `hitCount`: *boolean*
      - `pages`: *integer* `int64`
      - `records`:
        - **array**
          - **object** 用户投稿列表
            - `domainCode`: *string*
            - `domainName`: *string*
            - `id`: *integer* `int64`
            - `repetitionRate`: *number*
            - `status`: *string*
            - `submitTime`: *string* `date-time`
            - `submitType`: *integer* `int32`
            - `title`: *string*
            - `urgeTime`: *string* `date-time`
            - `urgencyStatus`: *string*
      - `searchCount`: *boolean*
      - `size`: *integer* `int64`
      - `total`: *integer* `int64`
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/app/submission/saveSubmission`

**摘要**：保存投稿  

**operationId**：`saveSubmissionUsingPOST`  

#### 请求方法

- **POST** `/api/app/submission/saveSubmission`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `account` | 可选 | `string` |  |
| `email` | 可选 | `string` |  |
| `firstLoginFlag` | 可选 | `boolean` | 是否首次登录标志，false：否；true：是 |
| `id` | 可选 | `integer` (`int64`) |  |
| `idCard` | 可选 | `string` |  |
| `loginCount` | 可选 | `integer` (`int32`) |  |
| `mobile` | 可选 | `string` |  |
| `name` | 可选 | `string` |  |
| `org.abbreviation` | 可选 | `string` |  |
| `org.describe` | 可选 | `string` |  |
| `org.id` | 可选 | `integer` (`int64`) |  |
| `org.label` | 可选 | `string` |  |
| `org.orgCode` | 可选 | `string` |  |
| `org.parentId` | 可选 | `integer` (`int64`) |  |
| `org.sortValue` | 可选 | `integer` (`int32`) |  |
| `org.status` | 可选 | `boolean` |  |
| `orgId` | 可选 | `integer` (`int64`) |  |
| `password` | 可选 | `string` |  |
| `passwordErrorLastTime` | 可选 | `string` (`date-time`) | 最后一次输错密码时间 |
| `passwordErrorNum` | 可选 | `integer` (`int32`) | 密码错误次数 |
| `passwordExpireTime` | 可选 | `string` (`date-time`) | 密码过期时间 |
| `photo` | 可选 | `string` |  |
| `resources` | 可选 | `array` |  |
| `roles[0].code` | 可选 | `string` |  |
| `roles[0].describe` | 可选 | `string` |  |
| `roles[0].dsType.code` | 可选 | `string` | 编码 |
| `roles[0].dsType.declaringClass` | 可选 | `ref` |  |
| `roles[0].dsType.desc` | 可选 | `string` | 描述 |
| `roles[0].dsType.val` | 可选 | `integer` (`int32`) | 值 |
| `roles[0].id` | 可选 | `integer` (`int64`) |  |
| `roles[0].isEnable` | 可选 | `boolean` |  |
| `roles[0].isReadonly` | 可选 | `boolean` |  |
| `roles[0].name` | 可选 | `string` |  |
| `station` | 可选 | `string` |  |
| `status` | 可选 | `boolean` | 状态 |
| `superAdmin` | 可选 | `boolean` |  |
| `token` | 可选 | `string` |  |
| `username` | 可选 | `string` |  |
| `workDescribe` | 可选 | `string` |  |

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `submission` | 必填 | - **object** 稿件主表<br>- `anonymous`: *integer* `int32`<br>- `attachments`:<br>- **array** 附件<br>- **object** 附件表<br>- `businessType`: *string*<br>- `createTime`: *string* `date-time`<br>- `createUser`: *integer* `int64`<br>- `fileName`: *string*<br>- `fileSize`: *integer* `int64`<br>- `fileUrl`: *string*<br>- `id`: *string*<br>- `mimeType`: *string*<br>- `sortNo`: *integer* `int32`<br>- `updateTime`: *string* `date-time`<br>- `updateUser`: *integer* `int64`<br>- `businessFlag`: *integer* `int32`<br>- `citationText`: *string*<br>- `contentElements`: *string*<br>- `domainCode`: *string*<br>- `id`: *integer* `int64`<br>- `remark`: *string*<br>- `submitType`: *integer* `int32`<br>- `submitterId`: *integer* `int64`<br>- `templateId`: *integer* `int64`<br>- `title`: *string* | submission |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *boolean*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `GET` `/api/app/submission/submissionLog/{submissionId}`

**摘要**：获取投稿端审核流程  

**operationId**：`submissionLogUsingGET`  

#### 请求方法

- **GET** `/api/app/submission/submissionLog/{submissionId}`

#### 请求参数

**路径参数（Path）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `submissionId` | 必填 | `integer` (`int64`) | submissionId |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **array** 响应数据
      - **object** 稿件流转日志
        - `actionTime`: *string* `date-time`
        - `actionType`: *string*
        - `actorId`: *integer* `int64`
        - `actorName`: *string*
        - `createTime`: *string* `date-time`
        - `createUser`: *integer* `int64`
        - `extra`: *string*
        - `id`: *string*
        - `remark`: *string*
        - `submissionId`: *integer* `int64`
        - `targetUserId`: *integer* `int64`
        - `targetUserName`: *string*
        - `taskId`: *integer* `int64`
        - `updateTime`: *string* `date-time`
        - `updateUser`: *integer* `int64`
        - `waitSeconds`: *integer* `int32`
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/app/submission/updateSubmission`

**摘要**：更新投稿  

**operationId**：`updateSubmissionUsingPOST`  

#### 请求方法

- **POST** `/api/app/submission/updateSubmission`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `account` | 可选 | `string` |  |
| `email` | 可选 | `string` |  |
| `firstLoginFlag` | 可选 | `boolean` | 是否首次登录标志，false：否；true：是 |
| `id` | 可选 | `integer` (`int64`) |  |
| `idCard` | 可选 | `string` |  |
| `loginCount` | 可选 | `integer` (`int32`) |  |
| `mobile` | 可选 | `string` |  |
| `name` | 可选 | `string` |  |
| `org.abbreviation` | 可选 | `string` |  |
| `org.describe` | 可选 | `string` |  |
| `org.id` | 可选 | `integer` (`int64`) |  |
| `org.label` | 可选 | `string` |  |
| `org.orgCode` | 可选 | `string` |  |
| `org.parentId` | 可选 | `integer` (`int64`) |  |
| `org.sortValue` | 可选 | `integer` (`int32`) |  |
| `org.status` | 可选 | `boolean` |  |
| `orgId` | 可选 | `integer` (`int64`) |  |
| `password` | 可选 | `string` |  |
| `passwordErrorLastTime` | 可选 | `string` (`date-time`) | 最后一次输错密码时间 |
| `passwordErrorNum` | 可选 | `integer` (`int32`) | 密码错误次数 |
| `passwordExpireTime` | 可选 | `string` (`date-time`) | 密码过期时间 |
| `photo` | 可选 | `string` |  |
| `resources` | 可选 | `array` |  |
| `roles[0].code` | 可选 | `string` |  |
| `roles[0].describe` | 可选 | `string` |  |
| `roles[0].dsType.code` | 可选 | `string` | 编码 |
| `roles[0].dsType.declaringClass` | 可选 | `ref` |  |
| `roles[0].dsType.desc` | 可选 | `string` | 描述 |
| `roles[0].dsType.val` | 可选 | `integer` (`int32`) | 值 |
| `roles[0].id` | 可选 | `integer` (`int64`) |  |
| `roles[0].isEnable` | 可选 | `boolean` |  |
| `roles[0].isReadonly` | 可选 | `boolean` |  |
| `roles[0].name` | 可选 | `string` |  |
| `station` | 可选 | `string` |  |
| `status` | 可选 | `boolean` | 状态 |
| `superAdmin` | 可选 | `boolean` |  |
| `token` | 可选 | `string` |  |
| `username` | 可选 | `string` |  |
| `workDescribe` | 可选 | `string` |  |

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `submission` | 必填 | - **object** 稿件主表<br>- `anonymous`: *integer* `int32`<br>- `attachments`:<br>- **array** 附件<br>- **object** 附件表<br>- `businessType`: *string*<br>- `createTime`: *string* `date-time`<br>- `createUser`: *integer* `int64`<br>- `fileName`: *string*<br>- `fileSize`: *integer* `int64`<br>- `fileUrl`: *string*<br>- `id`: *string*<br>- `mimeType`: *string*<br>- `sortNo`: *integer* `int32`<br>- `updateTime`: *string* `date-time`<br>- `updateUser`: *integer* `int64`<br>- `businessFlag`: *integer* `int32`<br>- `citationText`: *string*<br>- `contentElements`: *string*<br>- `domainCode`: *string*<br>- `id`: *integer* `int64`<br>- `remark`: *string*<br>- `submitType`: *integer* `int32`<br>- `submitterId`: *integer* `int64`<br>- `templateId`: *integer* `int64`<br>- `title`: *string* | submission |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *boolean*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/app/submission/urgeSubmission`

**摘要**：催办  

**operationId**：`urgeSubmissionUsingPOST`  

#### 请求方法

- **POST** `/api/app/submission/urgeSubmission`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `account` | 可选 | `string` |  |
| `email` | 可选 | `string` |  |
| `firstLoginFlag` | 可选 | `boolean` | 是否首次登录标志，false：否；true：是 |
| `id` | 可选 | `integer` (`int64`) |  |
| `idCard` | 可选 | `string` |  |
| `loginCount` | 可选 | `integer` (`int32`) |  |
| `mobile` | 可选 | `string` |  |
| `name` | 可选 | `string` |  |
| `org.abbreviation` | 可选 | `string` |  |
| `org.describe` | 可选 | `string` |  |
| `org.id` | 可选 | `integer` (`int64`) |  |
| `org.label` | 可选 | `string` |  |
| `org.orgCode` | 可选 | `string` |  |
| `org.parentId` | 可选 | `integer` (`int64`) |  |
| `org.sortValue` | 可选 | `integer` (`int32`) |  |
| `org.status` | 可选 | `boolean` |  |
| `orgId` | 可选 | `integer` (`int64`) |  |
| `password` | 可选 | `string` |  |
| `passwordErrorLastTime` | 可选 | `string` (`date-time`) | 最后一次输错密码时间 |
| `passwordErrorNum` | 可选 | `integer` (`int32`) | 密码错误次数 |
| `passwordExpireTime` | 可选 | `string` (`date-time`) | 密码过期时间 |
| `photo` | 可选 | `string` |  |
| `resources` | 可选 | `array` |  |
| `roles[0].code` | 可选 | `string` |  |
| `roles[0].describe` | 可选 | `string` |  |
| `roles[0].dsType.code` | 可选 | `string` | 编码 |
| `roles[0].dsType.declaringClass` | 可选 | `ref` |  |
| `roles[0].dsType.desc` | 可选 | `string` | 描述 |
| `roles[0].dsType.val` | 可选 | `integer` (`int32`) | 值 |
| `roles[0].id` | 可选 | `integer` (`int64`) |  |
| `roles[0].isEnable` | 可选 | `boolean` |  |
| `roles[0].isReadonly` | 可选 | `boolean` |  |
| `roles[0].name` | 可选 | `string` |  |
| `station` | 可选 | `string` |  |
| `status` | 可选 | `boolean` | 状态 |
| `superAdmin` | 可选 | `boolean` |  |
| `token` | 可选 | `string` |  |
| `username` | 可选 | `string` |  |
| `workDescribe` | 可选 | `string` |  |

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `urgeSubmission` | 必填 | - **object** 稿件主表<br>- `anonymous`: *integer* `int32`<br>- `attachments`:<br>- **array** 附件<br>- **object** 附件表<br>- `businessType`: *string*<br>- `createTime`: *string* `date-time`<br>- `createUser`: *integer* `int64`<br>- `fileName`: *string*<br>- `fileSize`: *integer* `int64`<br>- `fileUrl`: *string*<br>- `id`: *string*<br>- `mimeType`: *string*<br>- `sortNo`: *integer* `int32`<br>- `updateTime`: *string* `date-time`<br>- `updateUser`: *integer* `int64`<br>- `businessFlag`: *integer* `int32`<br>- `citationText`: *string*<br>- `contentElements`: *string*<br>- `domainCode`: *string*<br>- `id`: *integer* `int64`<br>- `remark`: *string*<br>- `submitType`: *integer* `int32`<br>- `submitterId`: *integer* `int64`<br>- `templateId`: *integer* `int64`<br>- `title`: *string* | urgeSubmission |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *boolean*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


---

## 二、稿件查重控制类

### `POST` `/api/submissionRepetition/getSubmissionRepetition`

**摘要**：获取稿件查重结果  

**operationId**：`getSubmissionRepetitionUsingPOST`  

#### 请求方法

- **POST** `/api/submissionRepetition/getSubmissionRepetition`

#### 请求参数

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `params` | 必填 | - **object** 稿件主表<br>- `anonymous`: *integer* `int32`<br>- `attachments`:<br>- **array** 附件<br>- **object** 附件表<br>- `businessType`: *string*<br>- `createTime`: *string* `date-time`<br>- `createUser`: *integer* `int64`<br>- `fileName`: *string*<br>- `fileSize`: *integer* `int64`<br>- `fileUrl`: *string*<br>- `id`: *string*<br>- `mimeType`: *string*<br>- `sortNo`: *integer* `int32`<br>- `updateTime`: *string* `date-time`<br>- `updateUser`: *integer* `int64`<br>- `businessFlag`: *integer* `int32`<br>- `citationText`: *string*<br>- `contentElements`: *string*<br>- `domainCode`: *string*<br>- `id`: *integer* `int64`<br>- `remark`: *string*<br>- `submitType`: *integer* `int32`<br>- `submitterId`: *integer* `int64`<br>- `templateId`: *integer* `int64`<br>- `title`: *string* | params |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *number*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/submissionRepetition/pageSubmissionRepetition`

**摘要**：获取稿件查重结果  

**operationId**：`pageSubmissionRepetitionUsingPOST`  

#### 请求方法

- **POST** `/api/submissionRepetition/pageSubmissionRepetition`

#### 请求参数

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `params` | 必填 | - **object** 分页参数<br>- `current`: *integer* `int64`<br>- `map`:<br>- **object**（空） 扩展参数<br>- `model` **必填**:<br>- **object** 查询稿件下的重复稿件分页列表入参<br>- `submissionId`: *integer* `int64`<br>- `order`: *string*<br>- `size`: *integer* `int64`<br>- `sort`: *string* | params |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **object**
      - `current`: *integer* `int64`
      - `hitCount`: *boolean*
      - `pages`: *integer* `int64`
      - `records`:
        - **array**
          - **object** 与当前稿件重复的存档稿件
            - `repetitionRate`: *number*
            - `submissionId`: *integer* `int64`
            - `submitTime`: *string* `date-time`
            - `title`: *string*
      - `searchCount`: *boolean*
      - `size`: *integer* `int64`
      - `total`: *integer* `int64`
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


---

## 二、管理端-审核稿件控制类

### `POST` `/api/submission/allocateSubmission`

**摘要**：任务分配  

**operationId**：`allocateSubmissionUsingPOST`  

#### 请求方法

- **POST** `/api/submission/allocateSubmission`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `account` | 可选 | `string` |  |
| `email` | 可选 | `string` |  |
| `firstLoginFlag` | 可选 | `boolean` | 是否首次登录标志，false：否；true：是 |
| `id` | 可选 | `integer` (`int64`) |  |
| `idCard` | 可选 | `string` |  |
| `loginCount` | 可选 | `integer` (`int32`) |  |
| `mobile` | 可选 | `string` |  |
| `name` | 可选 | `string` |  |
| `org.abbreviation` | 可选 | `string` |  |
| `org.describe` | 可选 | `string` |  |
| `org.id` | 可选 | `integer` (`int64`) |  |
| `org.label` | 可选 | `string` |  |
| `org.orgCode` | 可选 | `string` |  |
| `org.parentId` | 可选 | `integer` (`int64`) |  |
| `org.sortValue` | 可选 | `integer` (`int32`) |  |
| `org.status` | 可选 | `boolean` |  |
| `orgId` | 可选 | `integer` (`int64`) |  |
| `password` | 可选 | `string` |  |
| `passwordErrorLastTime` | 可选 | `string` (`date-time`) | 最后一次输错密码时间 |
| `passwordErrorNum` | 可选 | `integer` (`int32`) | 密码错误次数 |
| `passwordExpireTime` | 可选 | `string` (`date-time`) | 密码过期时间 |
| `photo` | 可选 | `string` |  |
| `resources` | 可选 | `array` |  |
| `roles[0].code` | 可选 | `string` |  |
| `roles[0].describe` | 可选 | `string` |  |
| `roles[0].dsType.code` | 可选 | `string` | 编码 |
| `roles[0].dsType.declaringClass` | 可选 | `ref` |  |
| `roles[0].dsType.desc` | 可选 | `string` | 描述 |
| `roles[0].dsType.val` | 可选 | `integer` (`int32`) | 值 |
| `roles[0].id` | 可选 | `integer` (`int64`) |  |
| `roles[0].isEnable` | 可选 | `boolean` |  |
| `roles[0].isReadonly` | 可选 | `boolean` |  |
| `roles[0].name` | 可选 | `string` |  |
| `station` | 可选 | `string` |  |
| `status` | 可选 | `boolean` | 状态 |
| `superAdmin` | 可选 | `boolean` |  |
| `token` | 可选 | `string` |  |
| `username` | 可选 | `string` |  |
| `workDescribe` | 可选 | `string` |  |

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `params` | 必填 | - **object** 稿件分配审核人员DTO<br>- `reviewerId`: *integer* `int64`<br>- `reviewerName`: *string*<br>- `submissionId`: *string* | params |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *boolean*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `GET` `/api/submission/countAdminSubmission`

**摘要**：管理员-任务审核列表统计  

**operationId**：`countAdminSubmissionUsingGET`  

#### 请求方法

- **GET** `/api/submission/countAdminSubmission`

#### 请求参数

*Swagger 未声明 parameters。*

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **object** 分页页面统计
      - `countAllocation`: *integer* `int32`
      - `countAudit`: *integer* `int32`
      - `countAuditing`: *integer* `int32`
      - `countPass`: *integer* `int32`
      - `countProcessing`: *integer* `int32`
      - `countReceive`: *integer* `int32`
      - `countReject`: *integer* `int32`
      - `countTransfer`: *integer* `int32`
      - `total`: *integer* `int32`
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `GET` `/api/submission/countReviewSubmission`

**摘要**：审核人-任务审核列表统计  

**operationId**：`countReviewSubmissionUsingGET`  

#### 请求方法

- **GET** `/api/submission/countReviewSubmission`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `account` | 可选 | `string` |  |
| `email` | 可选 | `string` |  |
| `firstLoginFlag` | 可选 | `boolean` | 是否首次登录标志，false：否；true：是 |
| `id` | 可选 | `integer` (`int64`) |  |
| `idCard` | 可选 | `string` |  |
| `loginCount` | 可选 | `integer` (`int32`) |  |
| `mobile` | 可选 | `string` |  |
| `name` | 可选 | `string` |  |
| `org.abbreviation` | 可选 | `string` |  |
| `org.describe` | 可选 | `string` |  |
| `org.id` | 可选 | `integer` (`int64`) |  |
| `org.label` | 可选 | `string` |  |
| `org.orgCode` | 可选 | `string` |  |
| `org.parentId` | 可选 | `integer` (`int64`) |  |
| `org.sortValue` | 可选 | `integer` (`int32`) |  |
| `org.status` | 可选 | `boolean` |  |
| `orgId` | 可选 | `integer` (`int64`) |  |
| `password` | 可选 | `string` |  |
| `passwordErrorLastTime` | 可选 | `string` (`date-time`) | 最后一次输错密码时间 |
| `passwordErrorNum` | 可选 | `integer` (`int32`) | 密码错误次数 |
| `passwordExpireTime` | 可选 | `string` (`date-time`) | 密码过期时间 |
| `photo` | 可选 | `string` |  |
| `resources` | 可选 | `array` |  |
| `roles[0].code` | 可选 | `string` |  |
| `roles[0].describe` | 可选 | `string` |  |
| `roles[0].dsType.code` | 可选 | `string` | 编码 |
| `roles[0].dsType.declaringClass` | 可选 | `ref` |  |
| `roles[0].dsType.desc` | 可选 | `string` | 描述 |
| `roles[0].dsType.val` | 可选 | `integer` (`int32`) | 值 |
| `roles[0].id` | 可选 | `integer` (`int64`) |  |
| `roles[0].isEnable` | 可选 | `boolean` |  |
| `roles[0].isReadonly` | 可选 | `boolean` |  |
| `roles[0].name` | 可选 | `string` |  |
| `station` | 可选 | `string` |  |
| `status` | 可选 | `boolean` | 状态 |
| `superAdmin` | 可选 | `boolean` |  |
| `token` | 可选 | `string` |  |
| `username` | 可选 | `string` |  |
| `workDescribe` | 可选 | `string` |  |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **object** 分页页面统计
      - `countAllocation`: *integer* `int32`
      - `countAudit`: *integer* `int32`
      - `countAuditing`: *integer* `int32`
      - `countPass`: *integer* `int32`
      - `countProcessing`: *integer* `int32`
      - `countReceive`: *integer* `int32`
      - `countReject`: *integer* `int32`
      - `countTransfer`: *integer* `int32`
      - `total`: *integer* `int32`
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/submission/dealSubmission`

**摘要**：审核人-开始处理任务（点击开始处理按钮调用)  

**operationId**：`dealSubmissionUsingPOST`  

#### 请求方法

- **POST** `/api/submission/dealSubmission`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `account` | 可选 | `string` |  |
| `email` | 可选 | `string` |  |
| `firstLoginFlag` | 可选 | `boolean` | 是否首次登录标志，false：否；true：是 |
| `id` | 可选 | `integer` (`int64`) |  |
| `idCard` | 可选 | `string` |  |
| `loginCount` | 可选 | `integer` (`int32`) |  |
| `mobile` | 可选 | `string` |  |
| `name` | 可选 | `string` |  |
| `org.abbreviation` | 可选 | `string` |  |
| `org.describe` | 可选 | `string` |  |
| `org.id` | 可选 | `integer` (`int64`) |  |
| `org.label` | 可选 | `string` |  |
| `org.orgCode` | 可选 | `string` |  |
| `org.parentId` | 可选 | `integer` (`int64`) |  |
| `org.sortValue` | 可选 | `integer` (`int32`) |  |
| `org.status` | 可选 | `boolean` |  |
| `orgId` | 可选 | `integer` (`int64`) |  |
| `password` | 可选 | `string` |  |
| `passwordErrorLastTime` | 可选 | `string` (`date-time`) | 最后一次输错密码时间 |
| `passwordErrorNum` | 可选 | `integer` (`int32`) | 密码错误次数 |
| `passwordExpireTime` | 可选 | `string` (`date-time`) | 密码过期时间 |
| `photo` | 可选 | `string` |  |
| `resources` | 可选 | `array` |  |
| `roles[0].code` | 可选 | `string` |  |
| `roles[0].describe` | 可选 | `string` |  |
| `roles[0].dsType.code` | 可选 | `string` | 编码 |
| `roles[0].dsType.declaringClass` | 可选 | `ref` |  |
| `roles[0].dsType.desc` | 可选 | `string` | 描述 |
| `roles[0].dsType.val` | 可选 | `integer` (`int32`) | 值 |
| `roles[0].id` | 可选 | `integer` (`int64`) |  |
| `roles[0].isEnable` | 可选 | `boolean` |  |
| `roles[0].isReadonly` | 可选 | `boolean` |  |
| `roles[0].name` | 可选 | `string` |  |
| `station` | 可选 | `string` |  |
| `status` | 可选 | `boolean` | 状态 |
| `superAdmin` | 可选 | `boolean` |  |
| `token` | 可选 | `string` |  |
| `username` | 可选 | `string` |  |
| `workDescribe` | 可选 | `string` |  |

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `params` | 必填 | - **object** 稿件审核处理入参DTO<br>- `assigneeId`: *integer* `int64`<br>- `assigneeName`: *string*<br>- `assigneeRemark`: *string*<br>- `remark`: *string*<br>- `status`: *integer* `int32`<br>- `submissionId`: *integer* `int64`<br>- `taskId`: *integer* `int64` | params |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *boolean*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `GET` `/api/submission/detailSubmission/{submissionId}`

**摘要**：获取投稿详情  

**operationId**：`detailSubmissionUsingGET_1`  

#### 请求方法

- **GET** `/api/submission/detailSubmission/{submissionId}`

#### 请求参数

**路径参数（Path）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `submissionId` | 必填 | `integer` (`int64`) | submissionId |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **object** 稿件详情VO
      - `anonymous`: *integer* `int32`
      - `assigneeName`: *string*
      - `assigneeRemark`: *string*
      - `attachments`:
        - **array** 附件
          - **object** 附件表
            - `businessType`: *string*
            - `createTime`: *string* `date-time`
            - `createUser`: *integer* `int64`
            - `fileName`: *string*
            - `fileSize`: *integer* `int64`
            - `fileUrl`: *string*
            - `id`: *string*
            - `mimeType`: *string*
            - `sortNo`: *integer* `int32`
            - `updateTime`: *string* `date-time`
            - `updateUser`: *integer* `int64`
      - `businessFlag`: *integer* `int32`
      - `citationText`: *string*
      - `contentElements`: *string*
      - `createTime`: *string* `date-time`
      - `createUser`: *integer* `int64`
      - `currentReviewerId`: *integer* `int64`
      - `currentTaskId`: *integer* `int64`
      - `domainCode`: *string*
      - `domainName`: *string*
      - `id`: *string*
      - `lastActionTime`: *string* `date-time`
      - `remark`: *string*
      - `repetitionRate`: *number*
      - `status`: *integer* `int32`
      - `submissionNo`: *string*
      - `submitTime`: *string* `date-time`
      - `submitType`: *integer* `int32`
      - `submitter`: *string*
      - `submitterId`: *integer* `int64`
      - `templateId`: *integer* `int64`
      - `title`: *string*
      - `updateTime`: *string* `date-time`
      - `updateUser`: *integer* `int64`
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/submission/listCheckUser`

**摘要**：审核人员列表查询  

**operationId**：`listCheckUserUsingPOST`  

#### 请求方法

- **POST** `/api/submission/listCheckUser`

#### 请求参数

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `queryDTO` | 必填 | - **object** 审核人员查询参数<br>- `name`: *string* | queryDTO |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **array** 响应数据
      - **object** 审核人员VO
        - `id`: *integer* `int64`
        - `name`: *string*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/submission/pageAdminSubmission`

**摘要**：管理员-任务审核列表  

**operationId**：`pageAdminSubmissionUsingPOST`  

#### 请求方法

- **POST** `/api/submission/pageAdminSubmission`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `account` | 可选 | `string` |  |
| `email` | 可选 | `string` |  |
| `firstLoginFlag` | 可选 | `boolean` | 是否首次登录标志，false：否；true：是 |
| `id` | 可选 | `integer` (`int64`) |  |
| `idCard` | 可选 | `string` |  |
| `loginCount` | 可选 | `integer` (`int32`) |  |
| `mobile` | 可选 | `string` |  |
| `name` | 可选 | `string` |  |
| `org.abbreviation` | 可选 | `string` |  |
| `org.describe` | 可选 | `string` |  |
| `org.id` | 可选 | `integer` (`int64`) |  |
| `org.label` | 可选 | `string` |  |
| `org.orgCode` | 可选 | `string` |  |
| `org.parentId` | 可选 | `integer` (`int64`) |  |
| `org.sortValue` | 可选 | `integer` (`int32`) |  |
| `org.status` | 可选 | `boolean` |  |
| `orgId` | 可选 | `integer` (`int64`) |  |
| `password` | 可选 | `string` |  |
| `passwordErrorLastTime` | 可选 | `string` (`date-time`) | 最后一次输错密码时间 |
| `passwordErrorNum` | 可选 | `integer` (`int32`) | 密码错误次数 |
| `passwordExpireTime` | 可选 | `string` (`date-time`) | 密码过期时间 |
| `photo` | 可选 | `string` |  |
| `resources` | 可选 | `array` |  |
| `roles[0].code` | 可选 | `string` |  |
| `roles[0].describe` | 可选 | `string` |  |
| `roles[0].dsType.code` | 可选 | `string` | 编码 |
| `roles[0].dsType.declaringClass` | 可选 | `ref` |  |
| `roles[0].dsType.desc` | 可选 | `string` | 描述 |
| `roles[0].dsType.val` | 可选 | `integer` (`int32`) | 值 |
| `roles[0].id` | 可选 | `integer` (`int64`) |  |
| `roles[0].isEnable` | 可选 | `boolean` |  |
| `roles[0].isReadonly` | 可选 | `boolean` |  |
| `roles[0].name` | 可选 | `string` |  |
| `station` | 可选 | `string` |  |
| `status` | 可选 | `boolean` | 状态 |
| `superAdmin` | 可选 | `boolean` |  |
| `token` | 可选 | `string` |  |
| `username` | 可选 | `string` |  |
| `workDescribe` | 可选 | `string` |  |

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `params` | 必填 | - **object** 分页参数<br>- `current`: *integer* `int64`<br>- `map`:<br>- **object**（空） 扩展参数<br>- `model` **必填**:<br>- **object** 审核稿件列表查询条件<br>- `domainCode`: *string*<br>- `keyword`: *string*<br>- `status`: *string*<br>- `submitEndDate`: *string*<br>- `submitStartDate`: *string*<br>- `urgencyStatus`: *string*<br>- `order`: *string*<br>- `size`: *integer* `int64`<br>- `sort`: *string* | params |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **object**
      - `current`: *integer* `int64`
      - `hitCount`: *boolean*
      - `pages`: *integer* `int64`
      - `records`:
        - **array**
          - **object** 审核稿件列表
            - `anonymous`: *integer* `int32`
            - `businessFlag`: *integer* `int32`
            - `citationText`: *string*
            - `contentElements`: *string*
            - `currentReviewer`: *string*
            - `currentTaskId`: *string*
            - `domainCode`: *string*
            - `domainName`: *string*
            - `remark`: *string*
            - `status`: *integer* `int32`
            - `statusName`: *string*
            - `submissionId`: *integer* `int64`
            - `submissionNo`: *string*
            - `submitTime`: *string* `date-time`
            - `submitter`: *string*
            - `submitterId`: *integer* `int64`
            - `templateId`: *integer* `int64`
            - `title`: *string*
            - `urgencyStatus`: *string*
      - `searchCount`: *boolean*
      - `size`: *integer* `int64`
      - `total`: *integer* `int64`
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/submission/pageAllocationSubmission`

**摘要**：任务分配列表  

**operationId**：`pageAllocationSubmissionUsingPOST`  

#### 请求方法

- **POST** `/api/submission/pageAllocationSubmission`

#### 请求参数

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `params` | 必填 | - **object** 分页参数<br>- `current`: *integer* `int64`<br>- `map`:<br>- **object**（空） 扩展参数<br>- `model` **必填**:<br>- **object** 审核稿件列表查询条件<br>- `domainCode`: *string*<br>- `keyword`: *string*<br>- `status`: *string*<br>- `submitEndDate`: *string*<br>- `submitStartDate`: *string*<br>- `urgencyStatus`: *string*<br>- `order`: *string*<br>- `size`: *integer* `int64`<br>- `sort`: *string* | params |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **object**
      - `current`: *integer* `int64`
      - `hitCount`: *boolean*
      - `pages`: *integer* `int64`
      - `records`:
        - **array**
          - **object** 审核稿件列表
            - `anonymous`: *integer* `int32`
            - `businessFlag`: *integer* `int32`
            - `citationText`: *string*
            - `contentElements`: *string*
            - `currentReviewer`: *string*
            - `currentTaskId`: *string*
            - `domainCode`: *string*
            - `domainName`: *string*
            - `remark`: *string*
            - `status`: *integer* `int32`
            - `statusName`: *string*
            - `submissionId`: *integer* `int64`
            - `submissionNo`: *string*
            - `submitTime`: *string* `date-time`
            - `submitter`: *string*
            - `submitterId`: *integer* `int64`
            - `templateId`: *integer* `int64`
            - `title`: *string*
            - `urgencyStatus`: *string*
      - `searchCount`: *boolean*
      - `size`: *integer* `int64`
      - `total`: *integer* `int64`
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/submission/pageReviewSubmission`

**摘要**：审核人-任务审核列表  

**operationId**：`pageReviewSubmissionUsingPOST`  

#### 请求方法

- **POST** `/api/submission/pageReviewSubmission`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `account` | 可选 | `string` |  |
| `email` | 可选 | `string` |  |
| `firstLoginFlag` | 可选 | `boolean` | 是否首次登录标志，false：否；true：是 |
| `id` | 可选 | `integer` (`int64`) |  |
| `idCard` | 可选 | `string` |  |
| `loginCount` | 可选 | `integer` (`int32`) |  |
| `mobile` | 可选 | `string` |  |
| `name` | 可选 | `string` |  |
| `org.abbreviation` | 可选 | `string` |  |
| `org.describe` | 可选 | `string` |  |
| `org.id` | 可选 | `integer` (`int64`) |  |
| `org.label` | 可选 | `string` |  |
| `org.orgCode` | 可选 | `string` |  |
| `org.parentId` | 可选 | `integer` (`int64`) |  |
| `org.sortValue` | 可选 | `integer` (`int32`) |  |
| `org.status` | 可选 | `boolean` |  |
| `orgId` | 可选 | `integer` (`int64`) |  |
| `password` | 可选 | `string` |  |
| `passwordErrorLastTime` | 可选 | `string` (`date-time`) | 最后一次输错密码时间 |
| `passwordErrorNum` | 可选 | `integer` (`int32`) | 密码错误次数 |
| `passwordExpireTime` | 可选 | `string` (`date-time`) | 密码过期时间 |
| `photo` | 可选 | `string` |  |
| `resources` | 可选 | `array` |  |
| `roles[0].code` | 可选 | `string` |  |
| `roles[0].describe` | 可选 | `string` |  |
| `roles[0].dsType.code` | 可选 | `string` | 编码 |
| `roles[0].dsType.declaringClass` | 可选 | `ref` |  |
| `roles[0].dsType.desc` | 可选 | `string` | 描述 |
| `roles[0].dsType.val` | 可选 | `integer` (`int32`) | 值 |
| `roles[0].id` | 可选 | `integer` (`int64`) |  |
| `roles[0].isEnable` | 可选 | `boolean` |  |
| `roles[0].isReadonly` | 可选 | `boolean` |  |
| `roles[0].name` | 可选 | `string` |  |
| `station` | 可选 | `string` |  |
| `status` | 可选 | `boolean` | 状态 |
| `superAdmin` | 可选 | `boolean` |  |
| `token` | 可选 | `string` |  |
| `username` | 可选 | `string` |  |
| `workDescribe` | 可选 | `string` |  |

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `params` | 必填 | - **object** 分页参数<br>- `current`: *integer* `int64`<br>- `map`:<br>- **object**（空） 扩展参数<br>- `model` **必填**:<br>- **object** 审核稿件列表查询条件<br>- `domainCode`: *string*<br>- `keyword`: *string*<br>- `status`: *string*<br>- `submitEndDate`: *string*<br>- `submitStartDate`: *string*<br>- `urgencyStatus`: *string*<br>- `order`: *string*<br>- `size`: *integer* `int64`<br>- `sort`: *string* | params |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **object**
      - `current`: *integer* `int64`
      - `hitCount`: *boolean*
      - `pages`: *integer* `int64`
      - `records`:
        - **array**
          - **object** 审核稿件列表
            - `anonymous`: *integer* `int32`
            - `businessFlag`: *integer* `int32`
            - `citationText`: *string*
            - `contentElements`: *string*
            - `currentReviewer`: *string*
            - `currentTaskId`: *string*
            - `domainCode`: *string*
            - `domainName`: *string*
            - `remark`: *string*
            - `status`: *integer* `int32`
            - `statusName`: *string*
            - `submissionId`: *integer* `int64`
            - `submissionNo`: *string*
            - `submitTime`: *string* `date-time`
            - `submitter`: *string*
            - `submitterId`: *integer* `int64`
            - `templateId`: *integer* `int64`
            - `title`: *string*
            - `urgencyStatus`: *string*
      - `searchCount`: *boolean*
      - `size`: *integer* `int64`
      - `total`: *integer* `int64`
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/submission/receiveSubmission`

**摘要**：审核人-接收任务（点击接收任务按钮调用)  

**operationId**：`receiveSubmissionUsingPOST`  

#### 请求方法

- **POST** `/api/submission/receiveSubmission`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `account` | 可选 | `string` |  |
| `email` | 可选 | `string` |  |
| `firstLoginFlag` | 可选 | `boolean` | 是否首次登录标志，false：否；true：是 |
| `id` | 可选 | `integer` (`int64`) |  |
| `idCard` | 可选 | `string` |  |
| `loginCount` | 可选 | `integer` (`int32`) |  |
| `mobile` | 可选 | `string` |  |
| `name` | 可选 | `string` |  |
| `org.abbreviation` | 可选 | `string` |  |
| `org.describe` | 可选 | `string` |  |
| `org.id` | 可选 | `integer` (`int64`) |  |
| `org.label` | 可选 | `string` |  |
| `org.orgCode` | 可选 | `string` |  |
| `org.parentId` | 可选 | `integer` (`int64`) |  |
| `org.sortValue` | 可选 | `integer` (`int32`) |  |
| `org.status` | 可选 | `boolean` |  |
| `orgId` | 可选 | `integer` (`int64`) |  |
| `password` | 可选 | `string` |  |
| `passwordErrorLastTime` | 可选 | `string` (`date-time`) | 最后一次输错密码时间 |
| `passwordErrorNum` | 可选 | `integer` (`int32`) | 密码错误次数 |
| `passwordExpireTime` | 可选 | `string` (`date-time`) | 密码过期时间 |
| `photo` | 可选 | `string` |  |
| `resources` | 可选 | `array` |  |
| `roles[0].code` | 可选 | `string` |  |
| `roles[0].describe` | 可选 | `string` |  |
| `roles[0].dsType.code` | 可选 | `string` | 编码 |
| `roles[0].dsType.declaringClass` | 可选 | `ref` |  |
| `roles[0].dsType.desc` | 可选 | `string` | 描述 |
| `roles[0].dsType.val` | 可选 | `integer` (`int32`) | 值 |
| `roles[0].id` | 可选 | `integer` (`int64`) |  |
| `roles[0].isEnable` | 可选 | `boolean` |  |
| `roles[0].isReadonly` | 可选 | `boolean` |  |
| `roles[0].name` | 可选 | `string` |  |
| `station` | 可选 | `string` |  |
| `status` | 可选 | `boolean` | 状态 |
| `superAdmin` | 可选 | `boolean` |  |
| `token` | 可选 | `string` |  |
| `username` | 可选 | `string` |  |
| `workDescribe` | 可选 | `string` |  |

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `params` | 必填 | - **object** 稿件审核处理入参DTO<br>- `assigneeId`: *integer* `int64`<br>- `assigneeName`: *string*<br>- `assigneeRemark`: *string*<br>- `remark`: *string*<br>- `status`: *integer* `int32`<br>- `submissionId`: *integer* `int64`<br>- `taskId`: *integer* `int64` | params |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *boolean*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/submission/reviewSubmission`

**摘要**：审核人-提交审核结果  

**operationId**：`reviewSubmissionUsingPOST`  

#### 请求方法

- **POST** `/api/submission/reviewSubmission`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `account` | 可选 | `string` |  |
| `email` | 可选 | `string` |  |
| `firstLoginFlag` | 可选 | `boolean` | 是否首次登录标志，false：否；true：是 |
| `id` | 可选 | `integer` (`int64`) |  |
| `idCard` | 可选 | `string` |  |
| `loginCount` | 可选 | `integer` (`int32`) |  |
| `mobile` | 可选 | `string` |  |
| `name` | 可选 | `string` |  |
| `org.abbreviation` | 可选 | `string` |  |
| `org.describe` | 可选 | `string` |  |
| `org.id` | 可选 | `integer` (`int64`) |  |
| `org.label` | 可选 | `string` |  |
| `org.orgCode` | 可选 | `string` |  |
| `org.parentId` | 可选 | `integer` (`int64`) |  |
| `org.sortValue` | 可选 | `integer` (`int32`) |  |
| `org.status` | 可选 | `boolean` |  |
| `orgId` | 可选 | `integer` (`int64`) |  |
| `password` | 可选 | `string` |  |
| `passwordErrorLastTime` | 可选 | `string` (`date-time`) | 最后一次输错密码时间 |
| `passwordErrorNum` | 可选 | `integer` (`int32`) | 密码错误次数 |
| `passwordExpireTime` | 可选 | `string` (`date-time`) | 密码过期时间 |
| `photo` | 可选 | `string` |  |
| `resources` | 可选 | `array` |  |
| `roles[0].code` | 可选 | `string` |  |
| `roles[0].describe` | 可选 | `string` |  |
| `roles[0].dsType.code` | 可选 | `string` | 编码 |
| `roles[0].dsType.declaringClass` | 可选 | `ref` |  |
| `roles[0].dsType.desc` | 可选 | `string` | 描述 |
| `roles[0].dsType.val` | 可选 | `integer` (`int32`) | 值 |
| `roles[0].id` | 可选 | `integer` (`int64`) |  |
| `roles[0].isEnable` | 可选 | `boolean` |  |
| `roles[0].isReadonly` | 可选 | `boolean` |  |
| `roles[0].name` | 可选 | `string` |  |
| `station` | 可选 | `string` |  |
| `status` | 可选 | `boolean` | 状态 |
| `superAdmin` | 可选 | `boolean` |  |
| `token` | 可选 | `string` |  |
| `username` | 可选 | `string` |  |
| `workDescribe` | 可选 | `string` |  |

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `params` | 必填 | - **object** 稿件审核处理入参DTO<br>- `assigneeId`: *integer* `int64`<br>- `assigneeName`: *string*<br>- `assigneeRemark`: *string*<br>- `remark`: *string*<br>- `status`: *integer* `int32`<br>- `submissionId`: *integer* `int64`<br>- `taskId`: *integer* `int64` | params |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *boolean*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `GET` `/api/submission/submissionLog/{submissionId}`

**摘要**：获取投稿追踪-稿件生命周期  

**operationId**：`submissionLogUsingGET_1`  

#### 请求方法

- **GET** `/api/submission/submissionLog/{submissionId}`

#### 请求参数

**路径参数（Path）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `submissionId` | 必填 | `integer` (`int64`) | submissionId |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **array** 响应数据
      - **object** 稿件流转日志
        - `actionTime`: *string* `date-time`
        - `actionType`: *string*
        - `actorId`: *integer* `int64`
        - `actorName`: *string*
        - `createTime`: *string* `date-time`
        - `createUser`: *integer* `int64`
        - `extra`: *string*
        - `id`: *string*
        - `remark`: *string*
        - `submissionId`: *integer* `int64`
        - `targetUserId`: *integer* `int64`
        - `targetUserName`: *string*
        - `taskId`: *integer* `int64`
        - `updateTime`: *string* `date-time`
        - `updateUser`: *integer* `int64`
        - `waitSeconds`: *integer* `int32`
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/submission/transferSubmission`

**摘要**：审核人-转办任务  

**operationId**：`transferSubmissionUsingPOST`  

#### 请求方法

- **POST** `/api/submission/transferSubmission`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `account` | 可选 | `string` |  |
| `email` | 可选 | `string` |  |
| `firstLoginFlag` | 可选 | `boolean` | 是否首次登录标志，false：否；true：是 |
| `id` | 可选 | `integer` (`int64`) |  |
| `idCard` | 可选 | `string` |  |
| `loginCount` | 可选 | `integer` (`int32`) |  |
| `mobile` | 可选 | `string` |  |
| `name` | 可选 | `string` |  |
| `org.abbreviation` | 可选 | `string` |  |
| `org.describe` | 可选 | `string` |  |
| `org.id` | 可选 | `integer` (`int64`) |  |
| `org.label` | 可选 | `string` |  |
| `org.orgCode` | 可选 | `string` |  |
| `org.parentId` | 可选 | `integer` (`int64`) |  |
| `org.sortValue` | 可选 | `integer` (`int32`) |  |
| `org.status` | 可选 | `boolean` |  |
| `orgId` | 可选 | `integer` (`int64`) |  |
| `password` | 可选 | `string` |  |
| `passwordErrorLastTime` | 可选 | `string` (`date-time`) | 最后一次输错密码时间 |
| `passwordErrorNum` | 可选 | `integer` (`int32`) | 密码错误次数 |
| `passwordExpireTime` | 可选 | `string` (`date-time`) | 密码过期时间 |
| `photo` | 可选 | `string` |  |
| `resources` | 可选 | `array` |  |
| `roles[0].code` | 可选 | `string` |  |
| `roles[0].describe` | 可选 | `string` |  |
| `roles[0].dsType.code` | 可选 | `string` | 编码 |
| `roles[0].dsType.declaringClass` | 可选 | `ref` |  |
| `roles[0].dsType.desc` | 可选 | `string` | 描述 |
| `roles[0].dsType.val` | 可选 | `integer` (`int32`) | 值 |
| `roles[0].id` | 可选 | `integer` (`int64`) |  |
| `roles[0].isEnable` | 可选 | `boolean` |  |
| `roles[0].isReadonly` | 可选 | `boolean` |  |
| `roles[0].name` | 可选 | `string` |  |
| `station` | 可选 | `string` |  |
| `status` | 可选 | `boolean` | 状态 |
| `superAdmin` | 可选 | `boolean` |  |
| `token` | 可选 | `string` |  |
| `username` | 可选 | `string` |  |
| `workDescribe` | 可选 | `string` |  |

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `params` | 必填 | - **object** 稿件审核处理入参DTO<br>- `assigneeId`: *integer* `int64`<br>- `assigneeName`: *string*<br>- `assigneeRemark`: *string*<br>- `remark`: *string*<br>- `status`: *integer* `int32`<br>- `submissionId`: *integer* `int64`<br>- `taskId`: *integer* `int64` | params |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *boolean*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


---

## 二、文件-大文件上传接口

### `POST` `/api/pub/uploadFile/checkChunk`

**摘要**：校验分块是否存在  

**operationId**：`checkChunkUsingPOST`  

#### 请求方法

- **POST** `/api/pub/uploadFile/checkChunk`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `chunk` | 可选 | `integer` (`int32`) | 当前分块数，从0开始计算 |
| `fileMd5` | 可选 | `string` | 文件md5值 |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int64`
  - `data`:
    - **object**（空）
  - `msg`: *string*


### `POST` `/api/pub/uploadFile/checkFileMd5`

**摘要**：文件校验，秒传判断，断点判断  

**operationId**：`checkFileMd5UsingPOST`  

#### 请求方法

- **POST** `/api/pub/uploadFile/checkFileMd5`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `chunks` | 可选 | `integer` (`int32`) | 文件分片后的总数量 |
| `filename` | 可选 | `string` | 文件名称 |
| `md5` | 可选 | `string` | 文件md5值 |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int64`
  - `data`:
    - **object**（空）
  - `msg`: *string*


### `GET` `/api/pub/uploadFile/cleanEmptyBucketName`

**摘要**：清除无效的bucketName, 针对分片上传出现失败时的bucketName碎片进行清理  

**operationId**：`cleanEmptyBucketNameUsingGET`  

#### 请求方法

- **GET** `/api/pub/uploadFile/cleanEmptyBucketName`

#### 请求参数

*Swagger 未声明 parameters。*

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int64`
  - `data`: *boolean*
  - `msg`: *string*


### `POST` `/api/pub/uploadFile/delBucket`

**摘要**：删除bucket  

**operationId**：`delBucketUsingPOST`  

#### 请求方法

- **POST** `/api/pub/uploadFile/delBucket`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `bucketName` | 可选 | `string` | bucketName名称 |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int64`
  - `data`:
    - **object**（空）
  - `msg`: *string*


### `POST` `/api/pub/uploadFile/fileUpload`

**摘要**：分片上传文件  

**operationId**：`fileUploadUsingPOST`  

#### 请求方法

- **POST** `/api/pub/uploadFile/fileUpload`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `chunk` | 必填 | `integer` (`int32`) | 当前为第几块分片 |
| `chunks` | 必填 | `integer` (`int32`) | 总分片数量 |
| `file` | 必填 | `file` | 文件分片对象 |
| `fileType` | 可选 | `string` | 文件类型 空：不限制，1：图片 2：视频  3：音频 |
| `id` | 必填 | `string` | 任务ID |
| `md5` | 必填 | `string` | 文件MD5 |
| `name` | 必填 | `string` | 文件名 |
| `size` | 必填 | `integer` (`int64`) | 当前分片大小 |
| `uid` | 必填 | `string` | 用户id |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int64`
  - `data`:
    - **object**（空）
  - `msg`: *string*


### `POST` `/api/pub/uploadFile/fileUploadVideo`

**摘要**：分片上传文件  

**operationId**：`fileUploadVideoUsingPOST`  

#### 请求方法

- **POST** `/api/pub/uploadFile/fileUploadVideo`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `chunk` | 必填 | `integer` (`int32`) | 当前为第几块分片 |
| `chunks` | 必填 | `integer` (`int32`) | 总分片数量 |
| `file` | 必填 | `file` | 文件分片对象 |
| `fileType` | 可选 | `string` | 文件类型 空：不限制，1：图片 2：视频  3：音频 |
| `id` | 必填 | `string` | 任务ID |
| `md5` | 必填 | `string` | 文件MD5 |
| `name` | 必填 | `string` | 文件名 |
| `size` | 必填 | `integer` (`int64`) | 当前分片大小 |
| `uid` | 必填 | `string` | 用户id |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int64`
  - `data`:
    - **object**（空）
  - `msg`: *string*


### `POST` `/api/pub/uploadFile/mergeChunks`

**摘要**：合并分块  

**operationId**：`mergeChunksUsingPOST`  

#### 请求方法

- **POST** `/api/pub/uploadFile/mergeChunks`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `fileMd5` | 可选 | `string` | 文件md5值 |
| `filename` | 可选 | `string` | 文件名称 |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int64`
  - `data`:
    - **object**（空）
  - `msg`: *string*


### `POST` `/api/pub/uploadFile/minio/delete`

**摘要**：删除bucket下的指定文件  

**operationId**：`deleteUsingPOST`  

#### 请求方法

- **POST** `/api/pub/uploadFile/minio/delete`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `bucketName` | 可选 | `string` | bucketName名称 |
| `filename` | 可选 | `string` | 文件名称 |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int64`
  - `data`: *boolean*
  - `msg`: *string*


### `GET` `/api/pub/uploadFile/minio/preview`

**摘要**：预览  

**operationId**：`previewUsingGET`  

#### 请求方法

- **GET** `/api/pub/uploadFile/minio/preview`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `bucketName` | 可选 | `string` | bucketName名称 |
| `filename` | 可选 | `string` | 文件名称 |

#### 响应（Response body schema）


**HTTP 200** — OK

*（无响应 body schema 声明）*


---

## 二、文件-通用调用接口

### `POST` `/api/pub/convertFile`

**摘要**：文件转换存储  

**operationId**：`convertFileUsingPOST`  

#### 请求方法

- **POST** `/api/pub/convertFile`

#### 请求参数

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `convertFileVm` | 必填 | - **object**<br>- `filenames`:<br>- **array** 文件全称集合，可以是a.txt也可以是b/c/d/a.txt的方式，最多一次不超过30条<br>- *string*<br>- `keepFullPath`: *boolean*<br>- `sourceStoreVm`:<br>- **object**<br>- `accessKeyId`: *string*<br>- `accessKeySecret`: *string*<br>- `bucketName`: *string*<br>- `endpoint`: *string*<br>- `sourceStoreType`: *string*<br>- `targetStoreVm`:<br>- **object**<br>- `accessKeyId`: *string*<br>- `accessKeySecret`: *string*<br>- `bucketName`: *string*<br>- `endpoint`: *string*<br>- `targetStoreType`: *string* | convertFileVm |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **array** 响应数据
      - *string*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `GET` `/api/pub/remote/getFileAuthUrl`

**摘要**：获取文件的可访问全路径  

**operationId**：`getFileAuthUrlUsingGET`  

#### 请求方法

- **GET** `/api/pub/remote/getFileAuthUrl`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `filepath` | 必填 | `string` | filepath |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *string*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `GET` `/api/pub/remote/getFileUrl`

**摘要**：获取文件的可访问全路径  

**operationId**：`getFileUrlUsingGET`  

#### 请求方法

- **GET** `/api/pub/remote/getFileUrl`

#### 请求参数

**查询参数（Query）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `filepath` | 必填 | `string` | filepath |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *string*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/pub/remote/uploadFile`

**摘要**：remote上传文件  

**operationId**：`uploadFileUsingPOST`  

#### 请求方法

- **POST** `/api/pub/remote/uploadFile`

#### 请求参数

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `remoteFileVm` | 必填 | - **object**<br>- `bytes`: *string* `byte`<br>- `content`: *string*<br>- `filename`: *string*<br>- `inputStream`:<br>- **object**（空）<br>- `keepFullPath`: *boolean*<br>- `keepOriginName`: *boolean* | remoteFileVm |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *string*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/pub/remote/uploadFileWithFullPath`

**摘要**：remote上传文件,返回文件可访问的全路径  

**operationId**：`uploadFileWithFullPathUsingPOST`  

#### 请求方法

- **POST** `/api/pub/remote/uploadFileWithFullPath`

#### 请求参数

**请求体（Body / application/json）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `remoteFileVm` | 必填 | - **object**<br>- `bytes`: *string* `byte`<br>- `content`: *string*<br>- `filename`: *string*<br>- `inputStream`:<br>- **object**（空）<br>- `keepFullPath`: *boolean*<br>- `keepOriginName`: *boolean* | remoteFileVm |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *string*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/pub/uploadFile`

**摘要**：小文件上传  

**operationId**：`uploadFileUsingPOST_1`  

#### 请求方法

- **POST** `/api/pub/uploadFile`

#### 请求参数

**表单 / 文件（formData）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `file` | 必填 | `file` | file |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`: *string*
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/pub/uploadImage`

**摘要**：上传图片文件  

**operationId**：`uploadImageUsingPOST`  

#### 请求方法

- **POST** `/api/pub/uploadImage`

#### 请求参数

**表单 / 文件（formData）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `file` | 必填 | `file` | file |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **object**（空） 响应数据
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


### `POST` `/api/pub/uploadImageWithCompress`

**摘要**：上传图片后压缩  

**operationId**：`uploadImageWithCompressUsingPOST`  

#### 请求方法

- **POST** `/api/pub/uploadImageWithCompress`

#### 请求参数

**表单 / 文件（formData）**

| 名称 | 必填 | 类型 / 结构 | 说明 |
|------|------|---------------|------|
| `file` | 必填 | `file` | file |

#### 响应（Response body schema）


**HTTP 200** — OK

**响应 Body（结构）**

- **object**
  - `code`: *integer* `int32`
  - `data`:
    - **object**（空） 响应数据
  - `extra`:
    - **object**（空） 附加数据
  - `isFail`: *boolean*
  - `isSuccess`: *boolean*
  - `msg`: *string*
  - `path`: *string*
  - `success`: *boolean*
  - `timestamp`: *integer* `int64`


