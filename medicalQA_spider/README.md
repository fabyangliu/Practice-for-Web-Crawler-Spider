# 医疗问答信息爬虫
## 描述
    基于requests和xpath爬取医疗问答网站的问题简述和详情描述，并且使用了fake-useragent伪装了请求头，最后结果保存至MongoDB数据库中。\
    详细过程是：从列表页中提取问题不完整描述的@href链接属性，然后进入详情页面爬取问题完整描述和详情描述。
## 软件环境
  * python >= 3;
  * requests;
  * xpath;
  * fake-useragent;
  * mongodb;
## 实战过程截图
  爬取过程中提示信息的显示
![index1](https://github.com/fabyangliu/yang-spider/blob/master/medicalQA_spider/1.png)
  存入数据库后查看
![index2](https://github.com/fabyangliu/yang-spider/blob/master/medicalQA_spider/2.png)
![index3](https://github.com/fabyangliu/yang-spider/blob/master/medicalQA_spider/3.png)
![index4](https://github.com/fabyangliu/yang-spider/blob/master/medicalQA_spider/4.png)
---
### 注释
  可以根据需要修改，如使用pandas存储数据等。
