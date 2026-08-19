# Simple RAG

我的第一个从零学习 RAG 的 Python 项目。

## 当前版本

v0.3 - 简单向量检索

## 功能

- 读取文本数据
- 将文本切分为多个 Document
- 使用 DataLoader 管理数据读取
- 使用 VectorStore 管理文档
- 使用 QAEngine 管理问答流程
- 将文本转换成简单数字向量
- 计算文档与问题的相似度
- 返回最相关的文档

## 项目结构

simple_Rag/
├── main.py
├── data_loader.py
├── vector_store.py
├── embedding.py
├── qa.py
├── data.txt
├── .gitignore
└── README.md

## 版本记录

### v0.1
- 文本读取
- 关键词检索

### v0.2
- 使用 class 重构
- 添加 DataLoader
- 添加 VectorStore
- 添加 QAEngine
- 模块化项目结构

### v0.3
- 添加 Embedding 类
- 文本转换成简单数字向量
- 使用相似度寻找最佳文档

## 后续计划

- [ ] 使用真正的 Embedding 模型
- [ ] 使用 FAISS 向量数据库
- [ ] 接入 Ollama
- [ ] 实现真正的 RAG 问答