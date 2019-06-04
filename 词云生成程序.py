import pandas as pd  
from wordcloud import WordCloud  
import jieba  

#读取数据
data=pd.read_excel('【原始】拉勾网-数据分析师岗位数据.xlsx')

#数据类型转换为str
data['职位诱惑']=data['职位诱惑'].astype("str")
data['职位描述']=data['职位描述'].astype("str")
data['岗位关键词']=data['岗位关键词'].astype("str")

# 绘制词云,将职位福利中的字符串汇总  
text =''

for line in data['岗位关键词']:  
    text += line

stop_words =['数据分析','数据挖掘','移动互联网','数据处理','数据运营']
for stop_word in stop_words:
    text = text.replace(stop_word, '')
# 使用jieba模块将字符串分割为单词列表      
cut_text = ' '.join(jieba.cut(text)) 

cloud = WordCloud(  
    font_path = 'SimHei.ttf',   
    background_color = 'white',  
    max_words = 200,  
    max_font_size = 100,
    
       )  

word_cloud = cloud.generate(cut_text)  
# 保存词云图片  
word_cloud.to_file('word_cloud.jpg')  
plt.imshow(word_cloud)  
plt.axis('off')  
plt.show()  
