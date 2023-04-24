# 学习强国助手

项目地址：https://github.com/trustyboy/xxqg-helper

本项目源自于项目 https://github.com/imkenf/XueQG ，由于该项目因为一些原因后续代码并未开放，因此自行进行相关修改，适配学习强国网页版最新版本，感谢作者的无私分享。



**注意：arm64平台已经合并amd64镜像地址，统一镜像trustyboy/xxqg-helper。
近期可能出现被官方检测问题，已进行相关优化。但不能保证一定可以避免，请谨慎使用。尽量避免在云服务器上使用，避免多账号同时运行。**

# 最近更新

**2023/04/25**

> 1、启动时增加随机等待时间（参考配置SleepSeconds）。
> 
> 2、消息内容增加时间，解决PushPlus限制相同消息问题。
> 
> 3、其他优化


**2023/04/20**

> 1、二维码未扫描增加消息通知。
> 
> 2、优化解锁滑块验证码逻辑。
> 
> 3、文章、答题模块增加重试功能。
> 
> 4、增加cookie保活机制。（由@xiaoWangSec提供）


**2023/04/18**

> 1、尝试优化被检测问题。
> 
> 2、去除随机UA。
> 
> 3、滑块验证码优化。
> 

**2023/04/12**

> 1、添加消息发送结果判断。
> 
> 2、PushPlus消息中增加二维码显示。
> 
> 3、docker镜像改成多架构模式。
> 

# 使用方式

#### Windows版本（小白用户建议使用）

> 使用Release里面的bin版本或者直接安装Python环境。

#### Linux版本

> **获取docker镜像**
>
> 
> `docker pull trustyboy/xxqg-helper:latest`
>
> **注意：arm64镜像，arm64平台已经合并**
> 


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
> 
> `SleepSeconds` 启动时随机等待时间，单位：秒

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

> **如何对登录状态进行保活**
>
> 目前cookie有效时间为12小时。每次启动程序时会执行一次保活, 仅当前Cookie有效时才会执行。
> 请设置多个时段的crontab任务以实现保活。(由@xiaoWangSec提供)
>```shell
> 30 9 * * * docker start xxqg
> 30 15 * * * docker start xxqg
> 30 21 * * * docker start xxqg
> 5 23 * * * docker start xxqg
> ```
> 此模式下可能会有很多消息，屏蔽保活的消息可以参照如下设置：
> 
> 例如：docker容器创建时候映射 /data/XueQG/User 到宿主机 /data/XueQG/User
> 
> 那么cron中7点保活时是不通知的，也不进行学习，13:00开始学习，并且有消息通知。
>```shell
> 0 7 * * * echo "" >/data/XueQG/User/UpdateCookie && docker start xxqg
> 0 13 * * * docker start xueqg
>```
# 免责声明

使用需严格遵守开源许可协议。本项目仅限于程序开发学习交流之用，严禁用于商业用途，禁止使用本项目进行任何盈利活动。对一切非法使用所产生的后果，我们概不负责。

# 鸣谢

参考源码项目来自https://github.com/imkenf/XueQG

[JetBrains](https://jb.gg/OpenSourceSupport) 提供的IDE支持
