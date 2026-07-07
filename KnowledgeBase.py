from Document import Document

class KnowledgeBase:
    def __init__(self,name,documents):
        self.name = name
        self.documents = []

    def add(self,doc):
        # 添加一个文档
        self.documents.append(doc)

    # 统计文档数量
    def count(self):
        return len(self.documents)

    # 搜索文档
    # keyword: 搜索关键词
    # return: 包含关键词的文档列表
    def search(self,keyword):
        result = []
        for doc in self.documents:
            if keyword in doc.content:
                result.append(doc)
        return result


# 测试
if __name__ == "__main__":
    print("文档类测试")
    D1 = Document("文档1","这是文档1的内容。11111111111111啊。222222222222啊。","文档1的科目")    
    print(D1.summary())
    print(D1.word_count())
    print(D1.split())

    print("-----------------")

    D2 = Document("导数","这是文档2的内容。222222222222啊。333333333333啊。","导数的科目")    
    print(D2.summary())
    print(D2.word_count())
    print(D2.split())

    print("-----------------")

    print("知识库类测试")
    K1 = KnowledgeBase("知识库1",[])
    K1.add(D1)
    print(K1.count())
    print(K1.search("11111111111111啊"))
    K1.add(D2)
    print(K1.count())
    print(K1.search("222222222222啊"))
    print(K1.search("333333333333啊"))

    print("-----------------")

    