# 学习强国助手

本项目源自于项目 https://github.com/imkenf/XueQG ，由于该项目因为一些原因后续代码并未开放，因此自行进行相关修改，适配学习强国网页版最新版本，感谢作者的无私分享。



# 更新日志

**2022/12/14**

> 1、支持二维码多次推送设置
> 
> 2、部分配置支持从环境变量读取
> 
> 3、修复每周答题、专项答题翻页可能崩溃问题
> 
> 4、支持arm64 docker镜像

**2022/12/09**

> 1、适配最新版本学习强国
> 
> 2、解决每日答题滑块验证码问题

# 使用方式

> **目前只修复钉钉推送登录，其他方式暂未测试**
> 
> **x86-64架构**
> 
> `docker pull trustyboy/xxqg-helper:latest`
> `docker run -d -it --name=xxqg -e ModeType=3 -e PushMode=2 -e DDtoken=钉钉token -e DDsecret=钉钉secret -e maxtrylogin=3 -e tryloginsleep=60 trustyboy/xxqg-helper:latest`
> 
> **arm64架构**
> 
> `docker pull trustyboy/xxqg-helper-arm64:latest`
> `docker run -d -it --name=xxqg -e ModeType=3 -e PushMode=2 -e DDtoken=钉token -e DDsecret=钉钉secret -e maxtrylogin=3 -e tryloginsleep=60 trustyboy/xxqg-helper-arm64:latest`

# 免责声明

使用需严格遵守开源许可协议。本项目仅限于程序开发学习交流之用，严禁用于商业用途，禁止使用本项目进行任何盈利活动。对一切非法使用所产生的后果，我们概不负责。

# 鸣谢

参考源码项目来自https://github.com/imkenf/XueQG
