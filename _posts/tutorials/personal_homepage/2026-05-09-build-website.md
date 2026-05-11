---
title: 网站环境搭建
description: 如何使用Jekyll的chirpy模板来搭建个人网站
author: 阎梓瑜
date: 2026-05-09 15:24:00 +0800
categories: [教程,个人网站]
tags: [jekyll,chirpy]
pin: false
math: true
mermaid: true
---

## 官方文档

[官方教程](https://chirpy.cotes.page/)

> 其实我就是对着官方的教程然后和AI一起搭的，不过我相信屏幕前的各位可能也懒得去看英文教程
{: .prompt-info } 

> 但是因为我是在Ubuntu系统里进行开发的，所以某些细节可能和Windows不太一样，Windows里边可能需要使用容器，这个就要自己看官方教程或者问AI了
{: .prompt-warning }
## 核心工具

- `Jekyll`：站点生成器
- `gem`：Ruby 包管理命令
- `bundle`：项目级依赖管理工具
- `Gemfile`：依赖声明文件
- `Gemfile.lock`：依赖锁定文件
- `github`： 存放网站源码并对网站进行托管服务

> 其实对这些没必要了解的太深入，大概知道用了这些东西就行，其实我也不是那么懂...
{: .prompt-info } 

## 环境准备

### 1.安装Ruby和编译依赖

```bash
sudo apt update
sudo apt install ruby-full build-essential zlib1g-dev
```

验证安装

```bash
ruby -v
gem -v
```
### 2.使用gem安装bundle和jekyll

在个人开发环境中，我们通常把gem安装到用户目录中，可以避免一些权限问题或者污染系统环境

```bash
gem install --user-install bundler jekyll
echo 'export PATH="$(ruby -r rbconfig -e '\''puts RbConfig::CONFIG["userbindir"]'\''):$PATH"' >> ~/.bashrc
source ~/.bashrc
```

验证安装

```bash
bundle -v
jekyll -v
```



## 搭建流程

### 1.创建仓库

在github上打开官方的仓库，我知道大家可能也找不到仓库在哪里，所以地址也给大家准备好了

[仓库地址](https://github.com/cotes2020/chirpy-starter)

点击：

```
Use this template → Create a new repository
```

仓库名建议用(如果用户名里面有大写字母在这里要改成小写)

```
你的GitHub用户名.github.io
```

将仓库克隆到本地

```bash
git clone <你的仓库地址>
```

### 2.安装Ruby依赖

如果你按照官方教程里的办法直接使用`bundle install`，应该不出意外会遇到权限问题，所以我们通常设置一下安装的路径

```bash
bundle config set --local path vendor/bundle
bundle install
```

### 3.运行网站

```bash
bundle exec jekyll serve --port 4001
```
如果想要在本地预览草稿的话(这个目前阶段应该还用不到)
```bash
bundle exec jekyll serve --drafts --port 4001
```
之后在本地访问[http://127.0.0.1:4001](http://127.0.0.1:4001),如果看到了自己的网站，就说明你的环境搭建成功了，没人觉得这是个很有意思的事情吗

> 默认使用的端口是4000,但是因为我的4000经常被占用，所以我一般用4001
{: .prompt-info } 

### 一些奇奇怪怪的问题

1. 我发现我的网站本地很正常但是推送到远程出问题了，一直没有更新我新写的文章

> 要把`GitHub pages`的发布方式改为`GitHub Actions`