class Document:
    def __init__(self,title,content,subject):
        self.title = title
        self.content = content
        self.subject = subject
    
    def summary(self):
        return self.content[:50]+"..."

    def word_count(self):
        return len(self.content)

    def split(self):
        sentences = self.content.split("。")
        return [s for s in sentences if s != ""]

# 测试
if __name__ == "__main__":
    D1 = Document("文档1","这是文档1的内容。11111111111111啊。222222222222啊。","文档1的科目")    
    print(D1.summary())
    print(D1.word_count())
    print(D1.split())   
