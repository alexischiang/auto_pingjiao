# 校园网自动评教脚本

<p align="left">
    <a href="">
        <img src="https://img.shields.io/badge/状态-持续更新中-brightgreen.svg">
        </a>
    <a href="https://github.com/python/cpython">
        <img src="https://img.shields.io/badge/Python-3.7-blue.svg">
        </a>
    <a href="https://github.com/alexischiang/myWeiboSpider/stargazers">
        <img src="https://img.shields.io/github/stars/alexischiang/myWeiboSpider.svg?logo=github">
        </a>
</p>

一个用python实现的自动评教程序，应该适用于所有“湖南强智科技发展有限公司”写的校园网系统，稍加修改就能使用

*（目前只能支持评教第一页，后续会修复）*

## 使用方法
### 1.所需要的库及webdriver
#### 只需要用到selenium库，安装方法如下：
```bash
pip3 install selenium
```
#### webdriver下载地址：
http://npm.taobao.org/mirrors/chromedriver/
<br>(请根据自己的chrome版本下载对应的webdriver程序)

下载完后请按教程放置在正确的文件夹：<br>
https://www.cnblogs.com/danvy/p/10131667.html

### 2.将该项目zip下载或gitclone到本地，打开auto_pj.py
#### 由于程序的不完善，在这一步需要各位重置自己的密码为一个较复杂的密码，方法如下：
打开校园网设置即可
![](https://i.loli.net/2019/06/14/5d03a9766145e91953.png)
#### 重设后，在程序最下面修改替换成自己的账号密码
![](https://i.loli.net/2019/06/14/5d03a953bfc6194185.png)

### 3.直接在ide中运行或保存并通过终端运行
```bash
python auto_pj.py
```
#### 首先根据提示输入验证码（如验证码复杂可以单击替换）
![](https://i.loli.net/2019/06/14/5d03a962d1caf34485.png)
#### 输入评教科目数
![](http://kan.027cgb.com/623423/Inkednum_LI.jpg)
#### 根据提示输入模式
模式0：<br>
![](http://kan.027cgb.com/623423/mode0.PNG)<br>
模式1：<br>
![](http://kan.027cgb.com/623423/mode1.PNG)

## Log
#### 2019/6/14
初版，仅支持单页的评教

## Contact Me
QQ:1091285927<br>
<a target="_blank" href="http://wpa.qq.com/msgrd?v=3&uin=&site=qq&menu=yes"><img border="0" src="http://wpa.qq.com/pa?p=2::52" alt="点击这里给我发消息" title="点击这里给我发消息"/></a>
