from data_loader import DataLoader
from vector_store import VectorStore
from qa import QAEngine


# 1. 加载数据
loader = DataLoader("data.txt")

documents = loader.load()
'''
测试用例
print("读取的数据:")
print(documents)
'''

# 2. 创建知识库
store = VectorStore()

store.add_documents(documents)
''' 
测试用例
print("知识库:")
print(store.documents)

test = store.search("Python")
print("搜索结果:")
print(test)
'''
# 3. 创建问答系统
qa = QAEngine(store)
#

# 4. 用户提问
while True:

    question = input("\n请输入问题：")

    if question == "退出":
        break


    answer = qa.ask(question)

    print("\n答案：")
    print(answer)