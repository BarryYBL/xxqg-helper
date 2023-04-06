# 学习强国助手

项目地址：https://github.com/trustyboy/xxqg-helper

本项目源自于项目 https://github.com/imkenf/XueQG ，由于该项目因为一些原因后续代码并未开放，因此自行进行相关修改，适配学习强国网页版最新版本，感谢作者的无私分享。



# 最近更新

**2023/04/07**

> 1、解决Cookie有效期判断致无法获取学习积分问题。
> 
> 2、AutoQuit问题修复。

**2023/03/30**

> 1、版本更新检查地址修改。
> 
> 2、解决滑块解锁失败问题。

**2023/03/30**

> 1、版本更新检查地址修改。
> 
> 2、解决滑块解锁失败问题。

**2023/03/23**

> 1、修复获取积分失败问题。
> 
> 2、chromium降版本。


# 使用方式

#### Windows版本

> 使用Release里面的bin版本或者直接安装Python环境，使用前请修改Config/Config.cfg配置好二维码推送方式。

#### Linux版本

> **获取docker镜像**
>
> ***x86-64架构***
> 
> `docker pull trustyboy/xxqg-helper:latest`
>
> ***arm64架构***
> 
> `docker pull trustyboy/xxqg-helper-arm64:latest`

> **参数说明**
>
> 以下参数均支持 -e 以环境变量方式传入
>
> `ModeType` 答题模式 
>
> ``````
> 1、文章 + 视频
> 2、文章 + 视频 + 每日答题（★默认）
> 3、文章 + 视频 + 每日答题 + 每周答题 + 专项答题
> 4、每日答题 + 每周答题 + 专项答题
> ``````
> `PushMode` 消息推送模式
>
> 2 表示 钉钉，3 表示 PlusPush，0表示不开启
>
> `DDtoken` 钉钉token `DDsecret` 钉钉secret
> 钉钉机器人接入方式请参考 https://developers.dingtalk.com/document/app/custom-robot-access/title-72m-8ag-pqw
> 
> `PPtoken` PlusPush token 接入方式请参考http://www.pushplus.plus/push1.html
>
> `maxtrylogin` 登录二维码发送次数
>
> `tryloginsleep` 登录二维码发送间隔，单位秒
>
> `SetUser` 是否保存用户登录信息 0 表示否 1表示是

> **钉钉消息通知示例**
> 
>```shell
> docker run -d -it --name=xxqg -e ModeType=3 -e PushMode=2 -e DDtoken=钉token -e DDsecret=钉钉secret -e maxtrylogin=3 -e tryloginsleep=60 -e SetUser=1 trustyboy/xxqg-helper:latest
> ```

> **PlusPush消息通知示例**
> 
>```shell
> docker run -d -it --name=xxqg -e ModeType=3 -e PushMode=3 -e PPtoken=PlusPushtoken -e maxtrylogin=3 -e tryloginsleep=60 -e SetUser=1 trustyboy/xxqg-helper:latest
> ```

> **定时开始学习问题**
>
> 可以使用cron来定时启动docker进行学习，例如每天上午9:30开始学习
>
>```shell
> 30 9 * * * docker start xxqg
> ```

# 免责声明

使用需严格遵守开源许可协议。本项目仅限于程序开发学习交流之用，严禁用于商业用途，禁止使用本项目进行任何盈利活动。对一切非法使用所产生的后果，我们概不负责。

# 鸣谢

参考源码项目来自https://github.com/imkenf/XueQG

[JetBrains](https://jb.gg/OpenSourceSupport) 提供的IDE支持
