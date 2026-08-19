with open ("data.txt","r",encoding="UTF-8") as f:
    test=f.read()


documents=test.split("\n")
print("知识库已加载")

for doc in documents:
    print(doc)

question = input("\n请输入问题：")


result_if=1

for doc in documents:

    if "Python" in question and "Python" in doc:
        print("\n找到答案：")
        print(doc)
        result_if=0

    elif "GitHub" in question and "GitHub" in doc:
        print("\n找到答案：")
        print(doc)
        result_if=0

    elif "机器学习" in question and "机器学习" in doc:
        print("\n找到答案：")
        print(doc)
        result_if=0
    
if result_if==1:print("无结果")