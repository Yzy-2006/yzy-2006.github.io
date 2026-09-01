---
title: 配置个人信息
description: 网站环境配置完成之后如何设置
author: 阎梓瑜
date: 2026-05-10 11:03:00 +0800
categories: [个人网站, 站点配置]
tags: [jekyll,chirpy]
pin: false
math: true
mermaid: true
---

## 网站基础信息

修改`_config.yml`,目前先改这些吧，其实是我目前只会这些，将来可能加一下评论系统
```yaml
#语言，这里需要到官方仓库里下载语言配置文件，放到_data/locales/zh-CN.yml
lang: zh-CN
#时区
timezone: Asia/Shanghai
#左上角的标题以及简介
title: 你的博客名
tagline: 你的个人简介
description: >-
  这里写你的网站描述。
#网站的地址
url: "https://yzy-2006.github.io"
baseurl: ""
#github的用户名
github:
  username: yzy-2006
#社交信息
social:
  name: 你的名字
  email: 你的邮箱
  fediverse_handle:
  links:
    - https://github.com/yzy-2006
#头像
avatar: /assets/img/yzy.jpg
#是否要开启文章右侧的目录
toc: true
```

## 网站的LOGO

这个是网站在浏览器显示的时候的小logo，我的现在是伟大的派大星大王，这个我感觉官方的教程就足够用了，链接在这里[(官方教程)](https://chirpy.cotes.page/posts/customize-the-favicon/)
