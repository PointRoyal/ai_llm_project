# Knife4j 在线文档 — 请求方法与参数（摘自 Swagger 2.0）
**数据来源**：`http://10.50.31.141:28001/v2/api-docs?group=在线文档`
**说明**：`*` 表示文档中 `required: true`；`{...}` 为 body/query 内对象字段概要；Spring 生成文档里部分接口会带误混入的 query 参数，以线上实测为准。

---

## 投稿人

### `GET` `/api/app/appUser/getByUseCode`
*摘要：根据用途获取协议信息*
  - [query] `code`: string

### `POST` `/api/app/appUser/login`
*摘要：投稿人登录*
  - [body] `loginVm`*: 用户登录实体类

### `POST` `/api/app/appUser/registerAppUser`
*摘要：投稿人注册*
  - [body] `userSaveDTO`*: AppUserSaveDTO

### `POST` `/api/app/appUser/resetPassword`
*摘要：投稿人密码重置*
  - [body] `updateDTO`*: AppUserPasswordUpdateDTO

---

## 投稿人-系统管理端

### `DELETE` `/api/system/appUser/delete`
*摘要：删除*
  - [query] `ids[]`: ref

### `POST` `/api/system/appUser/page`
*摘要：投稿人分页列表查询*
  - [body] `params`*: PageParams«AppUserPageDTO»

### `POST` `/api/system/appUser/resetPassword`
*摘要：投稿人密码重置*
  - [body] `updateDTO`*: AppUserPasswordUpdateDTO

### `POST` `/api/system/appUser/update`
*摘要：投稿人信息更新*
  - [body] `updateDTO`*: AppUserUpdateDTO

---

## 投稿模板

### `POST` `/api/template/deleteTemplate`
*摘要：删除投稿模板*
  - [query] `account`: string
  - [query] `email`: string
  - [query] `firstLoginFlag`: boolean
  - [query] `id`: integer
  - [query] `idCard`: string
  - [query] `loginCount`: integer
  - [query] `mobile`: string
  - [query] `name`: string
  - [query] `org.abbreviation`: string
  - [query] `org.describe`: string
  - [query] `org.id`: integer
  - [query] `org.label`: string
  - [query] `org.orgCode`: string
  - [query] `org.parentId`: integer
  - [query] `org.sortValue`: integer
  - [query] `org.status`: boolean
  - [query] `orgId`: integer
  - [body] `params`*: TemplateUpdateDTO
  - [query] `password`: string
  - [query] `passwordErrorLastTime`: string
  - [query] `passwordErrorNum`: integer
  - [query] `passwordExpireTime`: string
  - [query] `photo`: string
  - [query] `resources`: array
  - [query] `roles[0].code`: string
  - [query] `roles[0].describe`: string
  - [query] `roles[0].dsType.code`: string
  - [query] `roles[0].dsType.declaringClass`: ref
  - [query] `roles[0].dsType.desc`: string
  - [query] `roles[0].dsType.val`: integer
  - [query] `roles[0].id`: integer
  - [query] `roles[0].isEnable`: boolean
  - [query] `roles[0].isReadonly`: boolean
  - [query] `roles[0].name`: string
  - [query] `station`: string
  - [query] `status`: boolean
  - [query] `superAdmin`: boolean
  - [query] `token`: string
  - [query] `username`: string
  - [query] `workDescribe`: string

### `GET` `/api/template/detailTemplate`
*摘要：获取投稿模板详情*
  - [query] `id`*: integer

### `POST` `/api/template/disableTemplate`
*摘要：禁用/启用投稿模板*
  - [body] `params`*: TemplateUpdateDTO

### `POST` `/api/template/pageTemplate`
*摘要：获取投稿模板分页列表*
  - [body] `params`*: PageParams«TemplatePageDTO»

### `POST` `/api/template/saveTemplate`
*摘要：保存投稿模板*
  - [body] `params`*: TemplateSaveDTO

### `POST` `/api/template/updateTemplate`
*摘要：更新投稿模板*
  - [body] `params`*: TemplateUpdateDTO

---

## 投稿端-稿件发布控制类

### `POST` `/api/app/submission/countMyselfSubmission`
*摘要：获取用户投稿数量*
  - [query] `account`: string
  - [query] `email`: string
  - [query] `firstLoginFlag`: boolean
  - [query] `id`: integer
  - [query] `idCard`: string
  - [query] `loginCount`: integer
  - [query] `mobile`: string
  - [query] `name`: string
  - [query] `org.abbreviation`: string
  - [query] `org.describe`: string
  - [query] `org.id`: integer
  - [query] `org.label`: string
  - [query] `org.orgCode`: string
  - [query] `org.parentId`: integer
  - [query] `org.sortValue`: integer
  - [query] `org.status`: boolean
  - [query] `orgId`: integer
  - [query] `password`: string
  - [query] `passwordErrorLastTime`: string
  - [query] `passwordErrorNum`: integer
  - [query] `passwordExpireTime`: string
  - [query] `photo`: string
  - [query] `resources`: array
  - [query] `roles[0].code`: string
  - [query] `roles[0].describe`: string
  - [query] `roles[0].dsType.code`: string
  - [query] `roles[0].dsType.declaringClass`: ref
  - [query] `roles[0].dsType.desc`: string
  - [query] `roles[0].dsType.val`: integer
  - [query] `roles[0].id`: integer
  - [query] `roles[0].isEnable`: boolean
  - [query] `roles[0].isReadonly`: boolean
  - [query] `roles[0].name`: string
  - [query] `station`: string
  - [query] `status`: boolean
  - [query] `superAdmin`: boolean
  - [query] `token`: string
  - [query] `username`: string
  - [query] `workDescribe`: string

### `POST` `/api/app/submission/deleteSubmission`
*摘要：删除投稿*
  - [query] `account`: string
  - [query] `email`: string
  - [query] `firstLoginFlag`: boolean
  - [query] `id`: integer
  - [query] `idCard`: string
  - [query] `loginCount`: integer
  - [query] `mobile`: string
  - [query] `name`: string
  - [query] `org.abbreviation`: string
  - [query] `org.describe`: string
  - [query] `org.id`: integer
  - [query] `org.label`: string
  - [query] `org.orgCode`: string
  - [query] `org.parentId`: integer
  - [query] `org.sortValue`: integer
  - [query] `org.status`: boolean
  - [query] `orgId`: integer
  - [body] `params`*: SubmissionRepetitionDTO
  - [query] `password`: string
  - [query] `passwordErrorLastTime`: string
  - [query] `passwordErrorNum`: integer
  - [query] `passwordExpireTime`: string
  - [query] `photo`: string
  - [query] `resources`: array
  - [query] `roles[0].code`: string
  - [query] `roles[0].describe`: string
  - [query] `roles[0].dsType.code`: string
  - [query] `roles[0].dsType.declaringClass`: ref
  - [query] `roles[0].dsType.desc`: string
  - [query] `roles[0].dsType.val`: integer
  - [query] `roles[0].id`: integer
  - [query] `roles[0].isEnable`: boolean
  - [query] `roles[0].isReadonly`: boolean
  - [query] `roles[0].name`: string
  - [query] `station`: string
  - [query] `status`: boolean
  - [query] `superAdmin`: boolean
  - [query] `token`: string
  - [query] `username`: string
  - [query] `workDescribe`: string

### `GET` `/api/app/submission/detailSubmission/{submissionId}`
*摘要：获取投稿详情*
  - [path] `submissionId`*: integer

### `GET` `/api/app/submission/listTemplate`
*摘要：获取所有模板列表*
*（无 parameters 声明，可能为无参或文档未列全）*

### `POST` `/api/app/submission/pageMyselfSubmission`
*摘要：分页获取用户投稿列表/草稿箱列表*
  - [query] `account`: string
  - [query] `email`: string
  - [query] `firstLoginFlag`: boolean
  - [query] `id`: integer
  - [query] `idCard`: string
  - [query] `loginCount`: integer
  - [query] `mobile`: string
  - [query] `name`: string
  - [query] `org.abbreviation`: string
  - [query] `org.describe`: string
  - [query] `org.id`: integer
  - [query] `org.label`: string
  - [query] `org.orgCode`: string
  - [query] `org.parentId`: integer
  - [query] `org.sortValue`: integer
  - [query] `org.status`: boolean
  - [query] `orgId`: integer
  - [body] `params`*: PageParams«AppSubmissionMyselfPageDTO»
  - [query] `password`: string
  - [query] `passwordErrorLastTime`: string
  - [query] `passwordErrorNum`: integer
  - [query] `passwordExpireTime`: string
  - [query] `photo`: string
  - [query] `resources`: array
  - [query] `roles[0].code`: string
  - [query] `roles[0].describe`: string
  - [query] `roles[0].dsType.code`: string
  - [query] `roles[0].dsType.declaringClass`: ref
  - [query] `roles[0].dsType.desc`: string
  - [query] `roles[0].dsType.val`: integer
  - [query] `roles[0].id`: integer
  - [query] `roles[0].isEnable`: boolean
  - [query] `roles[0].isReadonly`: boolean
  - [query] `roles[0].name`: string
  - [query] `station`: string
  - [query] `status`: boolean
  - [query] `superAdmin`: boolean
  - [query] `token`: string
  - [query] `username`: string
  - [query] `workDescribe`: string

### `POST` `/api/app/submission/saveSubmission`
*摘要：保存投稿*
  - [query] `account`: string
  - [query] `email`: string
  - [query] `firstLoginFlag`: boolean
  - [query] `id`: integer
  - [query] `idCard`: string
  - [query] `loginCount`: integer
  - [query] `mobile`: string
  - [query] `name`: string
  - [query] `org.abbreviation`: string
  - [query] `org.describe`: string
  - [query] `org.id`: integer
  - [query] `org.label`: string
  - [query] `org.orgCode`: string
  - [query] `org.parentId`: integer
  - [query] `org.sortValue`: integer
  - [query] `org.status`: boolean
  - [query] `orgId`: integer
  - [query] `password`: string
  - [query] `passwordErrorLastTime`: string
  - [query] `passwordErrorNum`: integer
  - [query] `passwordExpireTime`: string
  - [query] `photo`: string
  - [query] `resources`: array
  - [query] `roles[0].code`: string
  - [query] `roles[0].describe`: string
  - [query] `roles[0].dsType.code`: string
  - [query] `roles[0].dsType.declaringClass`: ref
  - [query] `roles[0].dsType.desc`: string
  - [query] `roles[0].dsType.val`: integer
  - [query] `roles[0].id`: integer
  - [query] `roles[0].isEnable`: boolean
  - [query] `roles[0].isReadonly`: boolean
  - [query] `roles[0].name`: string
  - [query] `station`: string
  - [query] `status`: boolean
  - [body] `submission`*: SubmissionSaveDTO
  - [query] `superAdmin`: boolean
  - [query] `token`: string
  - [query] `username`: string
  - [query] `workDescribe`: string

### `GET` `/api/app/submission/submissionLog/{submissionId}`
*摘要：获取投稿端审核流程*
  - [path] `submissionId`*: integer

### `POST` `/api/app/submission/updateSubmission`
*摘要：更新投稿*
  - [query] `account`: string
  - [query] `email`: string
  - [query] `firstLoginFlag`: boolean
  - [query] `id`: integer
  - [query] `idCard`: string
  - [query] `loginCount`: integer
  - [query] `mobile`: string
  - [query] `name`: string
  - [query] `org.abbreviation`: string
  - [query] `org.describe`: string
  - [query] `org.id`: integer
  - [query] `org.label`: string
  - [query] `org.orgCode`: string
  - [query] `org.parentId`: integer
  - [query] `org.sortValue`: integer
  - [query] `org.status`: boolean
  - [query] `orgId`: integer
  - [query] `password`: string
  - [query] `passwordErrorLastTime`: string
  - [query] `passwordErrorNum`: integer
  - [query] `passwordExpireTime`: string
  - [query] `photo`: string
  - [query] `resources`: array
  - [query] `roles[0].code`: string
  - [query] `roles[0].describe`: string
  - [query] `roles[0].dsType.code`: string
  - [query] `roles[0].dsType.declaringClass`: ref
  - [query] `roles[0].dsType.desc`: string
  - [query] `roles[0].dsType.val`: integer
  - [query] `roles[0].id`: integer
  - [query] `roles[0].isEnable`: boolean
  - [query] `roles[0].isReadonly`: boolean
  - [query] `roles[0].name`: string
  - [query] `station`: string
  - [query] `status`: boolean
  - [body] `submission`*: SubmissionSaveDTO
  - [query] `superAdmin`: boolean
  - [query] `token`: string
  - [query] `username`: string
  - [query] `workDescribe`: string

### `POST` `/api/app/submission/urgeSubmission`
*摘要：催办*
  - [query] `account`: string
  - [query] `email`: string
  - [query] `firstLoginFlag`: boolean
  - [query] `id`: integer
  - [query] `idCard`: string
  - [query] `loginCount`: integer
  - [query] `mobile`: string
  - [query] `name`: string
  - [query] `org.abbreviation`: string
  - [query] `org.describe`: string
  - [query] `org.id`: integer
  - [query] `org.label`: string
  - [query] `org.orgCode`: string
  - [query] `org.parentId`: integer
  - [query] `org.sortValue`: integer
  - [query] `org.status`: boolean
  - [query] `orgId`: integer
  - [query] `password`: string
  - [query] `passwordErrorLastTime`: string
  - [query] `passwordErrorNum`: integer
  - [query] `passwordExpireTime`: string
  - [query] `photo`: string
  - [query] `resources`: array
  - [query] `roles[0].code`: string
  - [query] `roles[0].describe`: string
  - [query] `roles[0].dsType.code`: string
  - [query] `roles[0].dsType.declaringClass`: ref
  - [query] `roles[0].dsType.desc`: string
  - [query] `roles[0].dsType.val`: integer
  - [query] `roles[0].id`: integer
  - [query] `roles[0].isEnable`: boolean
  - [query] `roles[0].isReadonly`: boolean
  - [query] `roles[0].name`: string
  - [query] `station`: string
  - [query] `status`: boolean
  - [query] `superAdmin`: boolean
  - [query] `token`: string
  - [body] `urgeSubmission`*: SubmissionSaveDTO
  - [query] `username`: string
  - [query] `workDescribe`: string

---

## 文件-大文件上传接口

### `POST` `/api/pub/uploadFile/checkChunk`
*摘要：校验分块是否存在*
  - [query] `chunk`: integer
  - [query] `fileMd5`: string

### `POST` `/api/pub/uploadFile/checkFileMd5`
*摘要：文件校验，秒传判断，断点判断*
  - [query] `chunks`: integer
  - [query] `filename`: string
  - [query] `md5`: string

### `GET` `/api/pub/uploadFile/cleanEmptyBucketName`
*摘要：清除无效的bucketName, 针对分片上传出现失败时的bucketName碎片进行清理*
*（无 parameters 声明，可能为无参或文档未列全）*

### `POST` `/api/pub/uploadFile/delBucket`
*摘要：删除bucket*
  - [query] `bucketName`: string

### `POST` `/api/pub/uploadFile/fileUpload`
*摘要：分片上传文件*
  - [query] `chunk`*: integer
  - [query] `chunks`*: integer
  - [query] `file`*: file
  - [query] `fileType`: string
  - [query] `id`*: string
  - [query] `md5`*: string
  - [query] `name`*: string
  - [query] `size`*: integer
  - [query] `uid`*: string

### `POST` `/api/pub/uploadFile/fileUploadVideo`
*摘要：分片上传文件*
  - [query] `chunk`*: integer
  - [query] `chunks`*: integer
  - [query] `file`*: file
  - [query] `fileType`: string
  - [query] `id`*: string
  - [query] `md5`*: string
  - [query] `name`*: string
  - [query] `size`*: integer
  - [query] `uid`*: string

### `POST` `/api/pub/uploadFile/mergeChunks`
*摘要：合并分块*
  - [query] `fileMd5`: string
  - [query] `filename`: string

### `POST` `/api/pub/uploadFile/minio/delete`
*摘要：删除bucket下的指定文件*
  - [query] `bucketName`: string
  - [query] `filename`: string

### `GET` `/api/pub/uploadFile/minio/preview`
*摘要：预览*
  - [query] `bucketName`: string
  - [query] `filename`: string

---

## 文件-通用调用接口

### `POST` `/api/pub/convertFile`
*摘要：文件转换存储*
  - [body] `convertFileVm`*: 文件转存

### `GET` `/api/pub/remote/getFileAuthUrl`
*摘要：获取文件的可访问全路径*
  - [query] `filepath`*: string

### `GET` `/api/pub/remote/getFileUrl`
*摘要：获取文件的可访问全路径*
  - [query] `filepath`*: string

### `POST` `/api/pub/remote/uploadFile`
*摘要：remote上传文件*
  - [body] `remoteFileVm`*: 远程上传文件实体类

### `POST` `/api/pub/remote/uploadFileWithFullPath`
*摘要：remote上传文件,返回文件可访问的全路径*
  - [body] `remoteFileVm`*: 远程上传文件实体类

### `POST` `/api/pub/uploadFile`
*摘要：小文件上传*
  - [formData] `file`*: file

### `POST` `/api/pub/uploadImage`
*摘要：上传图片文件*
  - [formData] `file`*: file

### `POST` `/api/pub/uploadImageWithCompress`
*摘要：上传图片后压缩*
  - [formData] `file`*: file

---

## 稿件查重控制类

### `POST` `/api/submissionRepetition/getSubmissionRepetition`
*摘要：获取稿件查重结果*
  - [body] `params`*: SubmissionSaveDTO

### `POST` `/api/submissionRepetition/pageSubmissionRepetition`
*摘要：获取稿件查重结果*
  - [body] `params`*: PageParams«SubmissionRepetitionDTO»

---

## 管理端-审核稿件控制类

### `POST` `/api/submission/allocateSubmission`
*摘要：任务分配*
  - [query] `account`: string
  - [query] `email`: string
  - [query] `firstLoginFlag`: boolean
  - [query] `id`: integer
  - [query] `idCard`: string
  - [query] `loginCount`: integer
  - [query] `mobile`: string
  - [query] `name`: string
  - [query] `org.abbreviation`: string
  - [query] `org.describe`: string
  - [query] `org.id`: integer
  - [query] `org.label`: string
  - [query] `org.orgCode`: string
  - [query] `org.parentId`: integer
  - [query] `org.sortValue`: integer
  - [query] `org.status`: boolean
  - [query] `orgId`: integer
  - [body] `params`*: AllocateSubmissionDTO
  - [query] `password`: string
  - [query] `passwordErrorLastTime`: string
  - [query] `passwordErrorNum`: integer
  - [query] `passwordExpireTime`: string
  - [query] `photo`: string
  - [query] `resources`: array
  - [query] `roles[0].code`: string
  - [query] `roles[0].describe`: string
  - [query] `roles[0].dsType.code`: string
  - [query] `roles[0].dsType.declaringClass`: ref
  - [query] `roles[0].dsType.desc`: string
  - [query] `roles[0].dsType.val`: integer
  - [query] `roles[0].id`: integer
  - [query] `roles[0].isEnable`: boolean
  - [query] `roles[0].isReadonly`: boolean
  - [query] `roles[0].name`: string
  - [query] `station`: string
  - [query] `status`: boolean
  - [query] `superAdmin`: boolean
  - [query] `token`: string
  - [query] `username`: string
  - [query] `workDescribe`: string

### `GET` `/api/submission/countAdminSubmission`
*摘要：管理员-任务审核列表统计*
*（无 parameters 声明，可能为无参或文档未列全）*

### `GET` `/api/submission/countReviewSubmission`
*摘要：审核人-任务审核列表统计*
  - [query] `account`: string
  - [query] `email`: string
  - [query] `firstLoginFlag`: boolean
  - [query] `id`: integer
  - [query] `idCard`: string
  - [query] `loginCount`: integer
  - [query] `mobile`: string
  - [query] `name`: string
  - [query] `org.abbreviation`: string
  - [query] `org.describe`: string
  - [query] `org.id`: integer
  - [query] `org.label`: string
  - [query] `org.orgCode`: string
  - [query] `org.parentId`: integer
  - [query] `org.sortValue`: integer
  - [query] `org.status`: boolean
  - [query] `orgId`: integer
  - [query] `password`: string
  - [query] `passwordErrorLastTime`: string
  - [query] `passwordErrorNum`: integer
  - [query] `passwordExpireTime`: string
  - [query] `photo`: string
  - [query] `resources`: array
  - [query] `roles[0].code`: string
  - [query] `roles[0].describe`: string
  - [query] `roles[0].dsType.code`: string
  - [query] `roles[0].dsType.declaringClass`: ref
  - [query] `roles[0].dsType.desc`: string
  - [query] `roles[0].dsType.val`: integer
  - [query] `roles[0].id`: integer
  - [query] `roles[0].isEnable`: boolean
  - [query] `roles[0].isReadonly`: boolean
  - [query] `roles[0].name`: string
  - [query] `station`: string
  - [query] `status`: boolean
  - [query] `superAdmin`: boolean
  - [query] `token`: string
  - [query] `username`: string
  - [query] `workDescribe`: string

### `POST` `/api/submission/dealSubmission`
*摘要：审核人-开始处理任务（点击开始处理按钮调用)*
  - [query] `account`: string
  - [query] `email`: string
  - [query] `firstLoginFlag`: boolean
  - [query] `id`: integer
  - [query] `idCard`: string
  - [query] `loginCount`: integer
  - [query] `mobile`: string
  - [query] `name`: string
  - [query] `org.abbreviation`: string
  - [query] `org.describe`: string
  - [query] `org.id`: integer
  - [query] `org.label`: string
  - [query] `org.orgCode`: string
  - [query] `org.parentId`: integer
  - [query] `org.sortValue`: integer
  - [query] `org.status`: boolean
  - [query] `orgId`: integer
  - [body] `params`*: DealSubmissionDTO
  - [query] `password`: string
  - [query] `passwordErrorLastTime`: string
  - [query] `passwordErrorNum`: integer
  - [query] `passwordExpireTime`: string
  - [query] `photo`: string
  - [query] `resources`: array
  - [query] `roles[0].code`: string
  - [query] `roles[0].describe`: string
  - [query] `roles[0].dsType.code`: string
  - [query] `roles[0].dsType.declaringClass`: ref
  - [query] `roles[0].dsType.desc`: string
  - [query] `roles[0].dsType.val`: integer
  - [query] `roles[0].id`: integer
  - [query] `roles[0].isEnable`: boolean
  - [query] `roles[0].isReadonly`: boolean
  - [query] `roles[0].name`: string
  - [query] `station`: string
  - [query] `status`: boolean
  - [query] `superAdmin`: boolean
  - [query] `token`: string
  - [query] `username`: string
  - [query] `workDescribe`: string

### `GET` `/api/submission/detailSubmission/{submissionId}`
*摘要：获取投稿详情*
  - [path] `submissionId`*: integer

### `POST` `/api/submission/listCheckUser`
*摘要：审核人员列表查询*
  - [body] `queryDTO`*: CheckUserQueryDTO

### `POST` `/api/submission/pageAdminSubmission`
*摘要：管理员-任务审核列表*
  - [query] `account`: string
  - [query] `email`: string
  - [query] `firstLoginFlag`: boolean
  - [query] `id`: integer
  - [query] `idCard`: string
  - [query] `loginCount`: integer
  - [query] `mobile`: string
  - [query] `name`: string
  - [query] `org.abbreviation`: string
  - [query] `org.describe`: string
  - [query] `org.id`: integer
  - [query] `org.label`: string
  - [query] `org.orgCode`: string
  - [query] `org.parentId`: integer
  - [query] `org.sortValue`: integer
  - [query] `org.status`: boolean
  - [query] `orgId`: integer
  - [body] `params`*: PageParams«SubmissionQueryDTO»
  - [query] `password`: string
  - [query] `passwordErrorLastTime`: string
  - [query] `passwordErrorNum`: integer
  - [query] `passwordExpireTime`: string
  - [query] `photo`: string
  - [query] `resources`: array
  - [query] `roles[0].code`: string
  - [query] `roles[0].describe`: string
  - [query] `roles[0].dsType.code`: string
  - [query] `roles[0].dsType.declaringClass`: ref
  - [query] `roles[0].dsType.desc`: string
  - [query] `roles[0].dsType.val`: integer
  - [query] `roles[0].id`: integer
  - [query] `roles[0].isEnable`: boolean
  - [query] `roles[0].isReadonly`: boolean
  - [query] `roles[0].name`: string
  - [query] `station`: string
  - [query] `status`: boolean
  - [query] `superAdmin`: boolean
  - [query] `token`: string
  - [query] `username`: string
  - [query] `workDescribe`: string

### `POST` `/api/submission/pageAllocationSubmission`
*摘要：任务分配列表*
  - [body] `params`*: PageParams«SubmissionQueryDTO»

### `POST` `/api/submission/pageReviewSubmission`
*摘要：审核人-任务审核列表*
  - [query] `account`: string
  - [query] `email`: string
  - [query] `firstLoginFlag`: boolean
  - [query] `id`: integer
  - [query] `idCard`: string
  - [query] `loginCount`: integer
  - [query] `mobile`: string
  - [query] `name`: string
  - [query] `org.abbreviation`: string
  - [query] `org.describe`: string
  - [query] `org.id`: integer
  - [query] `org.label`: string
  - [query] `org.orgCode`: string
  - [query] `org.parentId`: integer
  - [query] `org.sortValue`: integer
  - [query] `org.status`: boolean
  - [query] `orgId`: integer
  - [body] `params`*: PageParams«SubmissionQueryDTO»
  - [query] `password`: string
  - [query] `passwordErrorLastTime`: string
  - [query] `passwordErrorNum`: integer
  - [query] `passwordExpireTime`: string
  - [query] `photo`: string
  - [query] `resources`: array
  - [query] `roles[0].code`: string
  - [query] `roles[0].describe`: string
  - [query] `roles[0].dsType.code`: string
  - [query] `roles[0].dsType.declaringClass`: ref
  - [query] `roles[0].dsType.desc`: string
  - [query] `roles[0].dsType.val`: integer
  - [query] `roles[0].id`: integer
  - [query] `roles[0].isEnable`: boolean
  - [query] `roles[0].isReadonly`: boolean
  - [query] `roles[0].name`: string
  - [query] `station`: string
  - [query] `status`: boolean
  - [query] `superAdmin`: boolean
  - [query] `token`: string
  - [query] `username`: string
  - [query] `workDescribe`: string

### `POST` `/api/submission/receiveSubmission`
*摘要：审核人-接收任务（点击接收任务按钮调用)*
  - [query] `account`: string
  - [query] `email`: string
  - [query] `firstLoginFlag`: boolean
  - [query] `id`: integer
  - [query] `idCard`: string
  - [query] `loginCount`: integer
  - [query] `mobile`: string
  - [query] `name`: string
  - [query] `org.abbreviation`: string
  - [query] `org.describe`: string
  - [query] `org.id`: integer
  - [query] `org.label`: string
  - [query] `org.orgCode`: string
  - [query] `org.parentId`: integer
  - [query] `org.sortValue`: integer
  - [query] `org.status`: boolean
  - [query] `orgId`: integer
  - [body] `params`*: DealSubmissionDTO
  - [query] `password`: string
  - [query] `passwordErrorLastTime`: string
  - [query] `passwordErrorNum`: integer
  - [query] `passwordExpireTime`: string
  - [query] `photo`: string
  - [query] `resources`: array
  - [query] `roles[0].code`: string
  - [query] `roles[0].describe`: string
  - [query] `roles[0].dsType.code`: string
  - [query] `roles[0].dsType.declaringClass`: ref
  - [query] `roles[0].dsType.desc`: string
  - [query] `roles[0].dsType.val`: integer
  - [query] `roles[0].id`: integer
  - [query] `roles[0].isEnable`: boolean
  - [query] `roles[0].isReadonly`: boolean
  - [query] `roles[0].name`: string
  - [query] `station`: string
  - [query] `status`: boolean
  - [query] `superAdmin`: boolean
  - [query] `token`: string
  - [query] `username`: string
  - [query] `workDescribe`: string

### `POST` `/api/submission/reviewSubmission`
*摘要：审核人-提交审核结果*
  - [query] `account`: string
  - [query] `email`: string
  - [query] `firstLoginFlag`: boolean
  - [query] `id`: integer
  - [query] `idCard`: string
  - [query] `loginCount`: integer
  - [query] `mobile`: string
  - [query] `name`: string
  - [query] `org.abbreviation`: string
  - [query] `org.describe`: string
  - [query] `org.id`: integer
  - [query] `org.label`: string
  - [query] `org.orgCode`: string
  - [query] `org.parentId`: integer
  - [query] `org.sortValue`: integer
  - [query] `org.status`: boolean
  - [query] `orgId`: integer
  - [body] `params`*: DealSubmissionDTO
  - [query] `password`: string
  - [query] `passwordErrorLastTime`: string
  - [query] `passwordErrorNum`: integer
  - [query] `passwordExpireTime`: string
  - [query] `photo`: string
  - [query] `resources`: array
  - [query] `roles[0].code`: string
  - [query] `roles[0].describe`: string
  - [query] `roles[0].dsType.code`: string
  - [query] `roles[0].dsType.declaringClass`: ref
  - [query] `roles[0].dsType.desc`: string
  - [query] `roles[0].dsType.val`: integer
  - [query] `roles[0].id`: integer
  - [query] `roles[0].isEnable`: boolean
  - [query] `roles[0].isReadonly`: boolean
  - [query] `roles[0].name`: string
  - [query] `station`: string
  - [query] `status`: boolean
  - [query] `superAdmin`: boolean
  - [query] `token`: string
  - [query] `username`: string
  - [query] `workDescribe`: string

### `GET` `/api/submission/submissionLog/{submissionId}`
*摘要：获取投稿追踪-稿件生命周期*
  - [path] `submissionId`*: integer

### `POST` `/api/submission/transferSubmission`
*摘要：审核人-转办任务*
  - [query] `account`: string
  - [query] `email`: string
  - [query] `firstLoginFlag`: boolean
  - [query] `id`: integer
  - [query] `idCard`: string
  - [query] `loginCount`: integer
  - [query] `mobile`: string
  - [query] `name`: string
  - [query] `org.abbreviation`: string
  - [query] `org.describe`: string
  - [query] `org.id`: integer
  - [query] `org.label`: string
  - [query] `org.orgCode`: string
  - [query] `org.parentId`: integer
  - [query] `org.sortValue`: integer
  - [query] `org.status`: boolean
  - [query] `orgId`: integer
  - [body] `params`*: DealSubmissionDTO
  - [query] `password`: string
  - [query] `passwordErrorLastTime`: string
  - [query] `passwordErrorNum`: integer
  - [query] `passwordExpireTime`: string
  - [query] `photo`: string
  - [query] `resources`: array
  - [query] `roles[0].code`: string
  - [query] `roles[0].describe`: string
  - [query] `roles[0].dsType.code`: string
  - [query] `roles[0].dsType.declaringClass`: ref
  - [query] `roles[0].dsType.desc`: string
  - [query] `roles[0].dsType.val`: integer
  - [query] `roles[0].id`: integer
  - [query] `roles[0].isEnable`: boolean
  - [query] `roles[0].isReadonly`: boolean
  - [query] `roles[0].name`: string
  - [query] `station`: string
  - [query] `status`: boolean
  - [query] `superAdmin`: boolean
  - [query] `token`: string
  - [query] `username`: string
  - [query] `workDescribe`: string
