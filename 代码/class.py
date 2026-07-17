from Document import Document
from KnowledgeBase import KnowledgeBase

class Student :
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def show(self):
      print(f"学生姓名: {self.name}, 年龄: {self.age}, 年级: {self.grade}")  

S1 = Student("张三",18,"大二")
S2 = Student("里斯",19,"大三")

print("----------------- 学生类测试")
print(f"学生姓名: {S1.name}, 年龄: {S1.age}, 年级: {S1.grade}")
print(f"学生姓名: {S2.name}, 年龄: {S2.age}, 年级: {S2.grade}")

S1.show()
S2.show()

print("----------------- 文档类测试")
D1 = Document("文档1","这是文档1的内容。11111111111111啊。222222222222啊。","文档1的科目")    
D2 = Document("导数","这是文档2的内容。222222222222啊。333333333333啊。","导数的科目")    
print(D2.summary())
print(D2.word_count())
print(D2.split())

print("----------------- 知识库类测试")
K1 = KnowledgeBase("知识库1",[])
K1.add(D1)
K1.add(D2)

print(K1.count())
print(K1.search("11111111111111啊"))
print(K1.search("222222222222啊"))
print(K1.search("333333333333啊"))  
