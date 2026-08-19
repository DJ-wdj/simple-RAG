from data_loader import DataLoader
from vector_store import VectorStore
from QA import QAEngine


# 1. 加载数据
loader = DataLoader("data.txt")

documents = loader.load()


# 2. 创建知识库
store = VectorStore()

store.add_documents(documents)


# 3. 创建问答系统
qa = QAEngine(store)


# 4. 用户提问
while True:

    question = input("\n请输入问题：")

    if question == "退出":
        break


    answer = qa.ask(question)

    print("\n答案：")
    print(answer)