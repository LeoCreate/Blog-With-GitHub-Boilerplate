# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Kepler",
    "type": "git",
    "url": "https://github.com/AlanDecode/Maverick-Theme-Kepler.git",
    "branch": "latest"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "LeoCreate/LeoWiki@gh-pages"
}

# 站点设置
site_name = "Leo's Wiki"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "Leo"
email = "1193886304@qq.com"
author_homepage = "https://www.isolitude.cn/"
description = "THIS IS MY STORY."
key_words = ['Wiki', 'Leo', '维基', '知识库']
language = 'zh-CN'
external_links = [
    {
        "name": "BLOG",
        "url": "https://www.isolitude.cn/",
        "brief": "Leo的个人博客。"
    },
    {
        "name": "GALLERY",
        "url": "https://img.isolitude.cn",
        "brief": "Leo的私人图床。"
    }
]
nav = [
    {
        "name": "HOME",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "ARCHIVES",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "ABOUT",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/AlanDecode",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/AlanDecode",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/5245109677/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="icon" type="image/ico" href="${static_prefix}wiki.png">
'''

footer_addon = ''

body_addon = ''
