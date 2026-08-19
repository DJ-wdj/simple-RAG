
class QAEngine:

    def __init__(self, vector_store):
        self.vector_store = vector_store


    def ask(self, question):

        results = self.vector_store.search(question)

        if results:
            return results

        else:
            return "没有找到答案"