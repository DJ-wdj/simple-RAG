class VectorStore:


    def __init__(self):

        self.documents = []


    def add_documents(self, documents):

        self.documents.extend(documents)



    def search(self, keyword):

        result = []


        for doc in self.documents:

            if keyword in doc:

                result.append(doc)


        return result