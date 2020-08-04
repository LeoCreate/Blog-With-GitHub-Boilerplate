---
layout: post
title: 使 Typecho 支持 emoji 表情
slug: Typecho-emoji
date: 2020-07-31 19:47
status: publish
author: Leo
categories: 
  - 建站
  - Typecho
tags: 
  - 博客
  - Typecho
excerpt: Typecho默认不支持emoji表情，是由于编码的问题，只需要将默认的数据库编码utf8修改为utf8mb4即可，不过utf8mb4编码在PHP5.5以后才支持。
---
Typecho默认不支持emoji表情，是由于编码的问题，只需要将默认的数据库编码utf8修改为utf8mb4即可，不过utf8mb4编码在PHP5.5以后才支持。

#### 1.修改数据库编码
在PhpMyadmin中选择typecho数据库，操作-->排序规则-->选择utf8mb4_unicode_ci然后执行。

#### 2.修改表编码

执行以下sql语句:

```sql
alter table typecho_comments convert to character set utf8mb4 collate utf8mb4_unicode_ci;
alter table typecho_contents convert to character set utf8mb4 collate utf8mb4_unicode_ci;
alter table typecho_fields convert to character set utf8mb4 collate utf8mb4_unicode_ci;
alter table typecho_metas convert to character set utf8mb4 collate utf8mb4_unicode_ci;
alter table typecho_options convert to character set utf8mb4 collate utf8mb4_unicode_ci;
alter table typecho_relationships convert to character set utf8mb4 collate utf8mb4_unicode_ci;
alter table typecho_users convert to character set utf8mb4 collate utf8mb4_unicode_ci;
```
#### 3.修改typecho配置文件config.inc.php

把这一行

```php
'charset'   =>  'utf8', 
```
修改为
```php
'charset'   =>  'utf8mb4', 
```
然后typecho就可以使用emoji表情了。