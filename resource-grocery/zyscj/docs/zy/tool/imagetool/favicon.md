# 🔗网站favicon图标下载

> 来源：<https://zyscj.com/zy/tool/imagetool/favicon.html>  ·  抓取时间：2026-11-01  ·  外链 5 个

> 由于杂货铺收集网站都需要加上网站的图标，所以收集了下列网站favicon图标下载的方法：

## [0.网页插件](#_0-网页插件)

[Get Favicon](https://chrome.google.com/webstore/detail/get-favicon/gpipahagclehninhhjkhbkliinfofnhe/related)（chrome插件，推荐）

## [1.网站下载](#_1-网站下载)

| 下载方法 | 网址 |
| --- | --- |
| Favicon Grabber | <https://favicongrabber.com/> |
| The Favicon Finder | <https://besticon-demo.herokuapp.com/> |

## [2.直接访问favicon地址获取ico文件](#_2-直接访问favicon地址获取ico文件)

对于熟悉网站开发的人来说，相信很多人都知道网站的favicon是如何设置的，就是把一个文件名为 favicon.ico 的图片上传到网站根目录，然后浏览器就会自动识别其为网站的标签页的图标

知道了这个后，我们就可以直接访问这个网址下载图标，格式为 域名/favicon.ico

比如Google的网站图标就是

```
https://www.google.com/favicon.ico
```

百度的favicon图标地址就是

```
https://www.baidu.com/favicon.ico
```

访问网址后，我们再右键 – 图片存储为就可以了

有些网站还需要F12打开开发人员工具，在地址中找到相应的图标，这是不会出错的方法。

## [3.使用API获取网站favicon](#_3-使用api获取网站favicon)

一些网站还提供专门的API给其他的开发者或者特殊用途使用，可以更快捷的获取到网站图标

**Google的API**

```
https://www.google.com/s2/favicons?domain=google.com
```

使用Google的API，你只需要把后面的域名改成自己的，就可以获取到对应的网站图标了，图片格式为PNG，大小 16\*16 像素

**The Favicon Finder 的 API**

```
https://besticon-demo.herokuapp.com/icon?url=google.com&size=80..120..200
```

The Favicon Finder 的API和它的网站一样，提供了很多专业级的参数选项，你可以在它的[Github文档](https://github.com/mat/besticon/blob/master/Readme.markdown)上查看到具体的用法

来源：[下载网站favicon图标的3种方法 – v1tx](https://www.v1tx.com/post/how-to-get-favicon/)
