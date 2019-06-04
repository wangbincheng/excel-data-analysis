# excel-data-analysis

对拉勾网数据分析职位做数据分析

## 数据分析思路

![](拉勾网数据分析——职位分析.png)

## 数据采集

岗位数据来自于拉勾网，采用“后羿采集器”进行数据采集，数据导出为Excel格式 
![](原始表格数据.png)

## 数据的清洗与处理

1. 数据清洗

1）处理“工作经验”这列的数据

使用excel的替换功能将该列工作经验的“经验”去掉
![](工作经验处理.png)

2）处理“岗位描述”这列数据

找出数据缺省值，利用“=LEN(K2)<15”判断表格内容是否小于15字符，并筛选出结果为“TRUE”，并删除对应的行数据。

3）处理薪资 

从“薪资区间”数据，采集薪资上下限

薪资上限：=LEFT(RIGHT(C2,LEN(C2)-FIND("-",C2)),LEN(RIGHT(C2,LEN(C2)-FIND("-",C2)))-1)

薪资下限：=LEFT(C2,SEARCH("k",C2)-1)
![](薪资区间处理.png)




