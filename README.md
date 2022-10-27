# wallpaper-database


微软必应首页每日一图接口: [https://cn.bing.com/](https://cn.bing.com/)

在线预览：[https://mouday.github.io/wallpaper](https://mouday.github.io/wallpaper)

> 数据缓存开始时间: 2022/10/27

## 接口

接口地址：
```
https://mouday.github.io/wallpaper-database/
```

请求方式：

```
https://mouday.github.io/wallpaper-database/<year>/<month>/<day>.json
```

参数说明

| 参数 | 类型 | 说明 | 
| - | - | - | 
| year | str | 4位年份, 例如：2022 | 
| month | str | 2位月份, 例如：02、12 | 
| day | str | 2位日期, 例如：02、25 | 

例如

[https://mouday.github.io/wallpaper-database/2022/10/27.json](https://mouday.github.io/wallpaper-database/2022/10/27.json)

返回数据

```json
{
  "date": "2022-10-27",
  "headline": "一个吻和一声叹息",
  "title": "意大利威尼斯的叹息桥",
  "description": "当船夫带着你来到威尼斯叹息桥下，你可以在这里亲吻你的爱人，传闻在叹息桥下接吻爱情会长久。然而，叹息桥名字的来源与爱情无关。这座封闭的桥于1600年完工，它将新监狱和总督府的审讯室连接起来。据说，囚犯人生中最后一次欣赏美丽的威尼斯，便是在这座桥上。由此看来，这确实足以令人叹息。",
  "image_url": "https://cn.bing.com/th?id=OHR.BridgeofSighs_ZH-CN5414607871_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
  "main_text": "在桥下的旅行十分轻松惬意，你可以坐在船上欣赏威尼斯的巴洛克式桥梁，沉浸在当地的各种传奇故事中。"
}
```
