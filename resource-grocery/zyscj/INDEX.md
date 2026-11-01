# 资源收藏夹 zyscj.com — 全站索引

> 用途：你说「我要找 X 资源 / 我要做 X，用哪个网站」，我先在这份索引里定位到页面，再从页面清单里给你具体的站名 + 链接。
> 来源：<https://zyscj.com/zy/office/png.html> 全站抓取（sitemap 97 页 + 首页，共 98 页）
> 抓取时间：2026-11-01 · 共 **84 个资源页、3324 条外链**
> 站点性质：个人资源收藏夹（VuePress 搭建的导航站），本站内容按原样镜像，未做筛选。

## 目录结构

```
resource-grocery/zyscj/
├── INDEX.md        ← 本文件：需求速查 + 分类树
├── LINKS.md        ← 全部 3323 条外链总表（按页面分组，可 grep）
├── docs/           ← 97 个页面正文（markdown，保留原表格与链接）
└── scripts/        ← crawl.py（抓取）/ build_index.py（生成索引）/ urls.txt / _manifest.json
```

## 怎么用

- 找某个用途的站：先看下面**一、需求速查**，命中后打开对应页面，页面里按小节列出了全部站点链接。
- 只记得关键词：直接搜全文总表
  ```bash
  cd resource-grocery/zyscj
  grep -in "PNG" LINKS.md          # 搜站名/URL
  grep -rn "免费 素材" docs/       # 搜页面正文
  ```
- 索引只记录「有什么站」，是否能访问、是否需要科学上网、是否有版权风险，需自己判断。

---

## 一、需求速查（我要找什么 → 看哪页）

### 图片 / 设计素材
| 我要找 | 页面 | 外链 | 本地文件 |
| --- | --- | --- | --- |
| 免抠 PNG、透明底图、纹理图案 | 🔗png+纹理图案等素材 | 83 | [docs/zy/office/png.md](docs/zy/office/png.md) |
| 无版权图库、矢量素材、免费照片 | 🔗无版权图库+矢量素材 | 60 | [docs/zy/office/picture.md](docs/zy/office/picture.md) |
| 图标 / logo / 图标库 | 🔗图标logo素材资源 | 104 | [docs/zy/office/icon.md](docs/zy/office/icon.md) |
| 字体下载、字体识别 | 🔗字体素材资源 | 54 | [docs/zy/office/font.md](docs/zy/office/font.md) |
| 配色方案、色卡、渐变 | 🔗配色方案资源索引 | 51 | [docs/zy/office/color.md](docs/zy/office/color.md) |
| 壁纸、桌面美化 | 🔗壁纸网站与桌面美化 | 65 | [docs/zy/office/wallpaper.md](docs/zy/office/wallpaper.md) |
| PPT 模板、简历模板 | 🔗PPT与简历制作 | 48 | [docs/zy/office/ppt.md](docs/zy/office/ppt.md) |
| 视频素材、音效、BGM | 🔗视频与音效素材网站 | 35 | [docs/zy/office/video-audio.md](docs/zy/office/video-audio.md) |
| CAD 规范、制图软件 | 🔗规范查询下载及CAD常用软件 | 25 | [docs/zy/office/CAD-standard.md](docs/zy/office/CAD-standard.md) |

### 图片处理小工具
| 我要找 | 页面 | 外链 | 本地文件 |
| --- | --- | --- | --- |
| 在线 PS、抠图、去背景 | 🔗PS在线编辑+抠图 | 29 | [docs/zy/tool/imagetool/PS.md](docs/zy/tool/imagetool/PS.md) |
| 图片压缩（含软件） | 🔗图片压缩+软件 | 18 | [docs/zy/tool/imagetool/piccompress.md](docs/zy/tool/imagetool/piccompress.md) |
| 图片编辑、裁剪、加水印 | 🔗图片编辑处理 | 29 | [docs/zy/tool/imagetool/picedit.md](docs/zy/tool/imagetool/picedit.md) |
| 以图搜图、识图 | 🔗以图搜图(识图) | 21 | [docs/zy/tool/imagetool/imagesearch.md](docs/zy/tool/imagetool/imagesearch.md) |
| 免费图床 | 🔗免费图床网站 | 8 | [docs/zy/tool/imagetool/picupload.md](docs/zy/tool/imagetool/picupload.md) |
| 头像生成器 | 🔗在线头像生成器 | 16 | [docs/zy/tool/imagetool/avatar.md](docs/zy/tool/imagetool/avatar.md) |
| favicon 图标下载/生成 | 🔗网站favicon图标下载 | 5 | [docs/zy/tool/imagetool/favicon.md](docs/zy/tool/imagetool/favicon.md) |
| 表情包、GIF 制作 | 🔗表情包与GIF | 34 | [docs/zy/tool/imagetool/gif.md](docs/zy/tool/imagetool/gif.md) |
| 词云 | 🔗词云制作 | 11 | [docs/zy/tool/imagetool/wordcloud.md](docs/zy/tool/imagetool/wordcloud.md) |

### 阅读 / 书籍
| 我要找 | 页面 | 外链 | 本地文件 |
| --- | --- | --- | --- |
| 电子书 / 杂志下载站 | 🔗电子书杂志网站 | 71 | [docs/zy/book/ebook.md](docs/zy/book/ebook.md) |
| 网络小说 | 🔗免费网络小说 | 106 | [docs/zy/book/fiction.md](docs/zy/book/fiction.md) |
| 古籍、汉籍 | 🔗汉古籍资源 | 149 | [docs/zy/book/ancient.md](docs/zy/book/ancient.md) |
| 漫画 | 🔗免费漫画资源 | 15 | [docs/zy/book/comic.md](docs/zy/book/comic.md) |
| 英文电子书 | 🔗英文电子书 | 16 | [docs/zy/book/enbook.md](docs/zy/book/enbook.md) |
| Z-Library 镜像 | 🔗Z-Library书籍资源 | 14 | [docs/zy/book/zlibrary.md](docs/zy/book/zlibrary.md) |
| pixiv 插画 | 🔗pixiv插画资源 | 19 | [docs/zy/book/pixiv.md](docs/zy/book/pixiv.md) |
| 阅读器 / 小说软件 | 🔗小说书籍软件 | 30 | [docs/zy/book/ebooksoft.md](docs/zy/book/ebooksoft.md) |

### 音乐 / 音频
| 我要找 | 页面 | 外链 | 本地文件 |
| --- | --- | --- | --- |
| 在线听歌网站 | 🔗免费在线音乐网站 | 35 | [docs/zy/music/musicwebsite.md](docs/zy/music/musicwebsite.md) |
| 音乐下载/播放软件 | 🔗音乐软件下载 | 42 | [docs/zy/music/musicsoftware.md](docs/zy/music/musicsoftware.md) |
| 有声书、电台 | 🔗有声书与电台 | 38 | [docs/zy/music/audiobook.md](docs/zy/music/audiobook.md) |
| 白噪音、MV | 🔗白噪音与MV | 29 | [docs/zy/music/whitenoise.md](docs/zy/music/whitenoise.md) |

### 软件 / 系统
| 我要找 | 页面 | 外链 | 本地文件 |
| --- | --- | --- | --- |
| 常用 Windows 软件 | 🔗常用Windows软件 | 50 | [docs/zy/soft/winsoft.md](docs/zy/soft/winsoft.md) |
| Windows 效率工具 | 🔗Windows效率工具 | 56 | [docs/zy/soft/winefficiency.md](docs/zy/soft/winefficiency.md) |
| Mac 软件 | 🔗苹果MAC软件 | 77 | [docs/zy/soft/iosmac.md](docs/zy/soft/iosmac.md) |
| 安卓 App | 🔗安卓软件与PO解 | 29 | [docs/zy/soft/android.md](docs/zy/soft/android.md) |
| 软件下载站聚合 | 🔗发现网站与应用 | 89 | [docs/zy/soft/findsoft.md](docs/zy/soft/findsoft.md) |
| 软件博客 / 论坛 | 🔗软件博客与论坛 | 64 | [docs/zy/soft/blogforum.md](docs/zy/soft/blogforum.md) |
| 浏览器与油猴脚本 | 🔗浏览器及插件脚本 | 43 | [docs/zy/soft/browser.md](docs/zy/soft/browser.md) |
| 系统安装、激活 | 🔗Win系统安装与激活 | 33 | [docs/zy/soft/winsystem.md](docs/zy/soft/winsystem.md) |
| 蓝奏云 / 安装包合集 | 🔗蓝奏云与软件安装大全 | 45 | [docs/zy/soft/lanzou.md](docs/zy/soft/lanzou.md) |
| 网页小游戏 | 🔗在线网页游戏 | 47 | [docs/zy/soft/onlinegame.md](docs/zy/soft/onlinegame.md) |
| 国外破解站 | 🔒国外PO解站 | 53 | [docs/zy/soft/crackabroad.md](docs/zy/soft/crackabroad.md) |
| 破解游戏 | 🔗PO解游戏网站 | 65 | [docs/zy/soft/crackgame.md](docs/zy/soft/crackgame.md) |
| Telegram 客户端 | 🔒TG电报软件 | 47 | [docs/zy/soft/tgsoft.md](docs/zy/soft/tgsoft.md) |

### 影视 / 视频
| 我要找 | 页面 | 外链 | 本地文件 |
| --- | --- | --- | --- |
| B站/各站视频下载 | 🔗各种视频下载 | 54 | [docs/zy/video/bilidownload.md](docs/zy/video/bilidownload.md) |
| 字幕下载、字幕组 | 🔗字幕组翻译 | 27 | [docs/zy/video/subtitle.md](docs/zy/video/subtitle.md) |
| 纪录片 | 🔗纪录片合集 | 34 | [docs/zy/video/documentary.md](docs/zy/video/documentary.md) |
| 动漫 | 🔗动漫网站与下载 | 19 | [docs/zy/video/anime.md](docs/zy/video/anime.md) |
| TV 盒子 / 电视直播 | 🔗TV盒子与直播 | 58 | [docs/zy/video/tv.md](docs/zy/video/tv.md) |
| 影视 App | 🔗免费影视软件 | 15 | [docs/zy/video/videosoft.md](docs/zy/video/videosoft.md) |
| 高清影视下载 | 🔗高清4K影视下载 | 44 | [docs/zy/video/HDvideo.md](docs/zy/video/HDvideo.md) |
| 在线影视 | 🔒在线影视精选 | 10 | [docs/zy/video/onlinevideo.md](docs/zy/video/onlinevideo.md) |
| 视频解析 | 🔗视频解析 | 26 | [docs/zy/video/videoparse.md](docs/zy/video/videoparse.md) |

### 搜索 / 网盘
| 我要找 | 页面 | 外链 | 本地文件 |
| --- | --- | --- | --- |
| 网盘资源搜索 | 🔗网盘资源合集 | 116 | [docs/zy/search/diskresource.md](docs/zy/search/diskresource.md) |
| 网盘不限速 | 🔗网盘不限速 | 12 | [docs/zy/search/spnetdisk.md](docs/zy/search/spnetdisk.md) |
| BT 磁力搜索 | 🔒BT磁LI下载 | 44 | [docs/zy/search/btcilidl.md](docs/zy/search/btcilidl.md) |
| BT 站点合集 | 🔒BT种Z磁L网站合集 | 55 | [docs/zy/search/btciliweb.md](docs/zy/search/btciliweb.md) |
| TG 群组 / 频道 | 🔒TG群组频道资源 | 36 | [docs/zy/search/tgchannel.md](docs/zy/search/tgchannel.md) |
| 图片站 | 🔒看妹子 | 76 | [docs/zy/search/girl.md](docs/zy/search/girl.md) |

### 学习 / 办公文档
| 我要找 | 页面 | 外链 | 本地文件 |
| --- | --- | --- | --- |
| 编程学习 | 🔗编程学习网站 | 79 | [docs/zy/study/code.md](docs/zy/study/code.md) |
| 英语学习 | 🔗英语学习资源 | 148 | [docs/zy/study/English.md](docs/zy/study/English.md) |
| 论文 / 查重 / 降重 | 🔗论文+查重降重 | 51 | [docs/zy/study/paper.md](docs/zy/study/paper.md) |
| 电子课本 | 🔗电子课本下载 | 23 | [docs/zy/study/textbook.md](docs/zy/study/textbook.md) |
| 百度文库下载 | 🔗百度文库下载 | 11 | [docs/zy/study/wenku.md](docs/zy/study/wenku.md) |
| 思维导图 / 笔记 | 🔗思维导图与笔记 | 66 | [docs/zy/study/mindmap.md](docs/zy/study/mindmap.md) |
| 数据可视化 / 图表 | 🔗信息可视化 | 15 | [docs/zy/study/chart.md](docs/zy/study/chart.md) |
| 在线课程 / 刷课 | 🔗在线课堂与刷课 | 21 | [docs/zy/study/onlinecourse.md](docs/zy/study/onlinecourse.md) |
| 考试考证 | 🔗考试考证资源 | 12 | [docs/zy/study/certificate.md](docs/zy/study/certificate.md) |
| 知识科普 | 🔗知识科普站 | 73 | [docs/zy/study/knowledge.md](docs/zy/study/knowledge.md) |
| 心理测试 | 🔗各类心理等测试 | 29 | [docs/zy/study/psychology.md](docs/zy/study/psychology.md) |
| 国内镜像站（下载加速） | 🔗各种学习镜像站 | 30 | [docs/zy/study/mirror.md](docs/zy/study/mirror.md) |

### 通用工具
| 我要找 | 页面 | 外链 | 本地文件 |
| --- | --- | --- | --- |
| OCR 文字识别 | 🔗OCR文字图片识别 | 19 | [docs/zy/tool/ocr.md](docs/zy/tool/ocr.md) |
| PDF 处理 / 转换 | 🔗PDF转换相关资源 | 22 | [docs/zy/tool/pdf.md](docs/zy/tool/pdf.md) |
| 文件格式转换、传文件 | 🔗文件格式转换与传输 | 28 | [docs/zy/tool/fileconvert.md](docs/zy/tool/fileconvert.md) |
| 临时邮箱 | 🔗临时邮箱 | 8 | [docs/zy/tool/email.md](docs/zy/tool/email.md) |
| 短信接码 | 🔗短信接码 | 14 | [docs/zy/tool/sms.md](docs/zy/tool/sms.md) |
| 地图 / 地图资源下载 | 🔗地图资源下载 | 12 | [docs/zy/tool/map.md](docs/zy/tool/map.md) |
| 在线查毒 | 🔗在线查毒 | 11 | [docs/zy/tool/virus.md](docs/zy/tool/virus.md) |
| 电影台词搜索 | 🔗电影台词搜索+拼接 | 11 | [docs/zy/tool/actorline.md](docs/zy/tool/actorline.md) |
| 综合工具箱 | 🔗综合工具 | 23 | [docs/zy/tool/tools.md](docs/zy/tool/tools.md) |

### AI / 指南
| 我要找 | 页面 | 外链 | 本地文件 |
| --- | --- | --- | --- |
| AI 工具导航 | 🔗AI人工智能指南 | 6 | [docs/zy/AI/AI导航.md](docs/zy/AI/AI导航.md) |
| 修改 DNS 解决打不开 | 🔗修改DNS防止网站无法访问 | 10 | [docs/zy/guide/DNS.md](docs/zy/guide/DNS.md) |
| iOS 外区账号注册 | 🔗ios外区账号注册 | 4 | [docs/zy/guide/isoabroad.md](docs/zy/guide/isoabroad.md) |
| 影视获取思路 | 🔗影视资源指南 | 12 | [docs/zy/guide/videoguide.md](docs/zy/guide/videoguide.md) |
| 站点更新记录 | 🔗资源铺更新记录 | 0 | [docs/zy/AI/zypuu.md](docs/zy/AI/zypuu.md) |

---

## 二、分类树（官方结构 + 每页小节）

### AI 人工智能（2 页 · 6 条外链）

- [🔗AI人工智能指南](docs/zy/AI/AI导航.md) · **6 条外链**
- [🔗资源铺更新记录](docs/zy/AI/zypuu.md) · **0 条外链**

### 音乐动听（4 页 · 144 条外链）

- [🔗音乐软件下载](docs/zy/music/musicsoftware.md) · **42 条外链**  
  小节：`手机APP` · `Windows` · `音乐播放器`
- [🔗有声书与电台](docs/zy/music/audiobook.md) · **38 条外链**  
  小节：`免费听书站` · `在线FM` · `有声读物` · `国外电台`
- [🔗免费在线音乐网站](docs/zy/music/musicwebsite.md) · **35 条外链**  
  小节：`在线免费音乐` · `无损音乐站`
- [🔗白噪音与MV](docs/zy/music/whitenoise.md) · **29 条外链**  
  小节：`白噪音` · `高清MV`

### 阅读漫画（8 页 · 420 条外链）

- [🔗汉古籍资源](docs/zy/book/ancient.md) · **149 条外链**  
  小节：`中国大陆` · `中国香港` · `中国台湾` · `越南` · `美国` · `英国` · `韩国` · `日本`
- [🔗免费网络小说](docs/zy/book/fiction.md) · **106 条外链**  
  小节：`网络小说搜索` · `在线网站` · `精校小说` · `轻小说` · `英文玄幻小说`
- [🔗电子书杂志网站](docs/zy/book/ebook.md) · **71 条外链**  
  小节：`出版电子书` · `电子书分享` · `论坛` · `网盘资源` · `杂志` · `收费电子书` · `专业书籍`
- [🔗小说书籍软件](docs/zy/book/ebooksoft.md) · **30 条外链**
- [🔗pixiv插画资源](docs/zy/book/pixiv.md) · **19 条外链**  
  小节：`网站` · `软件` · `辅助工具`
- [🔗英文电子书](docs/zy/book/enbook.md) · **16 条外链**
- [🔗免费漫画资源](docs/zy/book/comic.md) · **15 条外链**  
  小节：`在线网站` · `其他漫画` · `耽美漫画` · `免费漫画APP` · `kindle漫画`
- [🔗Z-Library书籍资源](docs/zy/book/zlibrary.md) · **14 条外链**  
  小节：`🍉Z-Library官方` · `Z-Lib镜像/代理站` · `🥥安娜的档案` · `IPFS工具` · `收费方法` · `电子书工具`

### 各种指南（3 页 · 26 条外链）

- [🔗影视资源指南](docs/zy/guide/videoguide.md) · **12 条外链**  
  小节：`搜索引擎` · `在线影视站` · `官方影视解析` · `网盘搜索（高质量）` · `电视TV观影` · `影视下载（高质量）` · `字幕组`
- [🔗修改DNS防止网站无法访问](docs/zy/guide/DNS.md) · **10 条外链**  
  小节：`软件修改方案` · `手动修改方案` · `DNS地址列表`
- [🔗ios外区账号注册](docs/zy/guide/isoabroad.md) · **4 条外链**

### 办公素材（9 页 · 525 条外链）

- [🔗图标logo素材资源](docs/zy/office/icon.md) · **104 条外链**  
  小节：`ICON 素材` · `LOGO 素材` · `LOGO 设计`
- [🔗png+纹理图案等素材](docs/zy/office/png.md) · **83 条外链**  
  小节：`PNG素材` · `插画素材` · `纹理素材` · `模板素材`
- [🔗壁纸网站与桌面美化](docs/zy/office/wallpaper.md) · **65 条外链**  
  小节：`壁纸网站` · `二次元壁纸` · `特色壁纸` · `桌面美化`
- [🔗无版权图库+矢量素材](docs/zy/office/picture.md) · **60 条外链**  
  小节：`图库素材` · `矢量素材` · `PSD素材`
- [🔗字体素材资源](docs/zy/office/font.md) · **54 条外链**  
  小节：`字体素材` · `字体工具`
- [🔗配色方案资源索引](docs/zy/office/color.md) · **51 条外链**
- [🔗PPT与简历制作](docs/zy/office/ppt.md) · **48 条外链**  
  小节：`PPT在线制作` · `PPT模板` · `简历制作` · `简历模板资源`
- [🔗视频与音效素材网站](docs/zy/office/video-audio.md) · **35 条外链**  
  小节：`视频` · `音效`
- [🔗规范查询下载及CAD常用软件](docs/zy/office/CAD-standard.md) · **25 条外链**  
  小节：`规范图集下载` · `软件下载`

### 软件游戏（13 页 · 698 条外链）

- [🔗发现网站与应用](docs/zy/soft/findsoft.md) · **89 条外链**
- [🔗苹果MAC软件](docs/zy/soft/iosmac.md) · **77 条外链**  
  小节：`IOS软件下载` · `Mac软件下载网站与商店`
- [🔗PO解游戏网站](docs/zy/soft/crackgame.md) · **65 条外链**  
  小节：`正版游戏平台` · `pojie版游戏下载网站` · `安卓游戏软件`
- [🔗软件博客与论坛](docs/zy/soft/blogforum.md) · **64 条外链**  
  小节：`软件搜索` · `软件博客` · `软件论坛`
- [🔗Windows效率工具](docs/zy/soft/winefficiency.md) · **56 条外链**  
  小节：`磁盘文件大小查看`
- [🔒国外PO解站](docs/zy/soft/crackabroad.md) · **53 条外链**  
  小节：`国外综合破解站` · `安卓破解`
- [🔗常用Windows软件](docs/zy/soft/winsoft.md) · **50 条外链**
- [🔗在线网页游戏](docs/zy/soft/onlinegame.md) · **47 条外链**  
  小节：`在线网页游戏` · `其他游戏相关` · `云游戏平台`
- [🔒TG电报软件](docs/zy/soft/tgsoft.md) · **47 条外链**  
  小节：`國內软件频道` · `国外软件频道` · `马克丁软件`
- [🔗蓝奏云与软件安装大全](docs/zy/soft/lanzou.md) · **45 条外链**  
  小节：`软件安装管家` · `蓝奏云破解软件`
- [🔗浏览器及插件脚本](docs/zy/soft/browser.md) · **43 条外链**  
  小节：`浏览器推荐` · `Chrome插件下载` · `Chrome插件/脚本推荐` · `常用Chrome插件`
- [🔗Win系统安装与激活](docs/zy/soft/winsystem.md) · **33 条外链**  
  小节：`Windows激活` · `系统下载` · `重装系统PE工具` · `系统安装教程`
- [🔗安卓软件与PO解](docs/zy/soft/android.md) · **29 条外链**  
  小节：`应用商店` · `Google Play下载`

### 资源搜索（6 页 · 339 条外链）

- [🔗网盘资源合集](docs/zy/search/diskresource.md) · **116 条外链**  
  小节：`综合搜索` · `博客分享` · `阿里云盘` · `论坛` · `在线文档` · `软件` · `百度网盘` · `蓝奏云`
- [🔒看妹子](docs/zy/search/girl.md) · **76 条外链**
- [🔒BT种Z磁L网站合集](docs/zy/search/btciliweb.md) · **55 条外链**  
  小节：`🌐国外磁力代理` · `🎯磁力网站` · `🚁BT工具`
- [🔒BT磁LI下载](docs/zy/search/btcilidl.md) · **44 条外链**  
  小节：`Windows` · `手机软件`
- [🔒TG群组频道资源](docs/zy/search/tgchannel.md) · **36 条外链**  
  小节：`综合搜索` · `频道索引站点` · `telegram机器人索引` · `其他汇总页面`
- [🔗网盘不限速](docs/zy/search/spnetdisk.md) · **12 条外链**

### 实用工具（9 页 · 148 条外链）

- [🔗文件格式转换与传输](docs/zy/tool/fileconvert.md) · **28 条外链**  
  小节：`文件格式转换` · `极速文件传输`
- [🔗综合工具](docs/zy/tool/tools.md) · **23 条外链**  
  小节：`综合工具` · `分类工具`
- [🔗PDF转换相关资源](docs/zy/tool/pdf.md) · **22 条外链**  
  小节：`PDF在线工具` · `PDF编辑器`
- [🔗OCR文字图片识别](docs/zy/tool/ocr.md) · **19 条外链**  
  小节：`在线识别` · `电脑端` · `手机APP` · `微信小程序`
- [🔗短信接码](docs/zy/tool/sms.md) · **14 条外链**
- [🔗地图资源下载](docs/zy/tool/map.md) · **12 条外链**  
  小节：`地图资源站` · `地图软件`
- [🔗电影台词搜索+拼接](docs/zy/tool/actorline.md) · **11 条外链**  
  小节：`电影台词搜索` · `电影台词拼接`
- [🔗在线查毒](docs/zy/tool/virus.md) · **11 条外链**
- [🔗临时邮箱](docs/zy/tool/email.md) · **8 条外链**

### 图片工具（9 页 · 171 条外链）

- [🔗表情包与GIF](docs/zy/tool/imagetool/gif.md) · **34 条外链**  
  小节：`GIF`
- [🔗图片编辑处理](docs/zy/tool/imagetool/picedit.md) · **29 条外链**  
  小节：`在线设计` · `图片编辑与查看`
- [🔗PS在线编辑+抠图](docs/zy/tool/imagetool/PS.md) · **29 条外链**  
  小节：`在线PS` · `在线抠图`
- [🔗以图搜图(识图)](docs/zy/tool/imagetool/imagesearch.md) · **21 条外链**  
  小节：`综合识图` · `二次元识图` · `其他识图`
- [🔗图片压缩+软件](docs/zy/tool/imagetool/piccompress.md) · **18 条外链**  
  小节：`在线图片压缩` · `图片压缩软件`
- [🔗在线头像生成器](docs/zy/tool/imagetool/avatar.md) · **16 条外链**
- [🔗词云制作](docs/zy/tool/imagetool/wordcloud.md) · **11 条外链**
- [🔗免费图床网站](docs/zy/tool/imagetool/picupload.md) · **8 条外链**
- [🔗网站favicon图标下载](docs/zy/tool/imagetool/favicon.md) · **5 条外链**  
  小节：`0.网页插件` · `1.网站下载` · `2.直接访问favicon地址获取ico文件` · `3.使用API获取网站favicon`

### 学习教育（12 页 · 558 条外链）

- [🔗英语学习资源](docs/zy/study/English.md) · **148 条外链**  
  小节：`英语网站` · `英语资源` · `单词词汇` · `听力口语` · `阅读理解` · `写作词典` · `写作语法`
- [🔗编程学习网站](docs/zy/study/code.md) · **79 条外链**  
  小节：`学习与教程` · `计算机书籍` · `社区` · `博客` · `趋势榜单` · `开源镜像`
- [🔗知识科普站](docs/zy/study/knowledge.md) · **73 条外链**
- [🔗思维导图与笔记](docs/zy/study/mindmap.md) · **66 条外链**  
  小节：`思维导图` · `笔记` · `写作/Markdown` · `稍后阅读`
- [🔗论文+查重降重](docs/zy/study/paper.md) · **51 条外链**  
  小节：`论文下载` · `论文查重降重`
- [🔗各种学习镜像站](docs/zy/study/mirror.md) · **30 条外链**  
  小节：`Github访问` · `Sci-Hub` · `谷歌学术/谷歌镜像`
- [🔗各类心理等测试](docs/zy/study/psychology.md) · **29 条外链**
- [🔗电子课本下载](docs/zy/study/textbook.md) · **23 条外链**  
  小节：`课程学习` · `课本下载` · `查题找答案`
- [🔗在线课堂与刷课](docs/zy/study/onlinecourse.md) · **21 条外链**  
  小节：`在线课堂`
- [🔗信息可视化](docs/zy/study/chart.md) · **15 条外链**  
  小节：`图表制作` · `信息图形` · `数据可视化`
- [🔗考试考证资源](docs/zy/study/certificate.md) · **12 条外链**
- [🔗百度文库下载](docs/zy/study/wenku.md) · **11 条外链**  
  小节：`文库下载`

### 视频直播（9 页 · 287 条外链）

- [🔗TV盒子与直播](docs/zy/video/tv.md) · **58 条外链**  
  小节：`电视盒子软件` · `电视直播网站` · `直播源` · `直播录制` · `体育直播`
- [🔗各种视频下载](docs/zy/video/bilidownload.md) · **54 条外链**  
  小节：`B站视频下载/增强` · `视频号/公众号下载` · `小红书下载` · `YouTube视频下载` · `其他国外视频下载` · `在线视频下载-M3U8软件`
- [🔗高清4K影视下载](docs/zy/video/HDvideo.md) · **44 条外链**  
  小节：`网盘下载` · `高清下载` · `4K下载`
- [🔗纪录片合集](docs/zy/video/documentary.md) · **34 条外链**  
  小节：`在线网站`
- [🔗字幕组翻译](docs/zy/video/subtitle.md) · **27 条外链**  
  小节：`国内字幕组` · `动漫字幕组` · `国外字幕组` · `字幕遮挡`
- [🔗视频解析](docs/zy/video/videoparse.md) · **26 条外链**  
  小节：`影视解析` · `短视频解析`
- [🔗动漫网站与下载](docs/zy/video/anime.md) · **19 条外链**  
  小节：`动漫站` · `BT种Z下载`
- [🔗免费影视软件](docs/zy/video/videosoft.md) · **15 条外链**  
  小节：`在线聚合类` · `安卓视频软件破解资源`
- [🔒在线影视精选](docs/zy/video/onlinevideo.md) · **10 条外链**  
  小节：`综合在线网站` · `影视搜索`
---



## 三、外链总表



全部 3323 条外链按页面分组见 [LINKS.md](LINKS.md)（也可直接 grep）。



---



## 四、维护



- 重新抓取：`python scripts/crawl.py`（读 scripts/urls.txt，需能访问 zyscj.com）

- 重建索引：`python scripts/build_index.py`

- 站点有新页面时先更新 `scripts/urls.txt`（源：https://zyscj.com/sitemap.xml）

- `scripts/head.md` 为手写部分（需求速查表），改完重跑 build 生效

