from embedding import Embedding


class VectorStore:


    def __init__(self):

        self.documents = []
        self.embedding = Embedding()



    def add_documents(self, documents):

        self.documents.extend(documents)



    def search(self, question):

        question_vector = self.embedding.encode(question)


        best_doc = None
        best_score = 0


        for doc in self.documents:

            doc_vector = self.embedding.encode(doc)


            score = self.similarity(
                question_vector,
                doc_vector
            )


            if score > best_score:
                best_score = score
                best_doc = doc


        return best_doc



    def similarity(self,a,b):

        score = 0

        for x,y in zip(a,b):

            if x == y:
                score += 1


        return score