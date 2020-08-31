class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = [x for x in self.categories if x.id == category_id][0]
        category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = [x for x in self.topics if x.id == topic_id][0]
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = [x for x in self.documents if x.id == document_id][0]
        document.file_name = new_file_name

    def delete_category(self, category_id):
        current_category = [x for x in self.categories if x.id == category_id][0]
        self.categories.remove(current_category)

    def delete_topic(self, topic_id):
        current_topic = [x for x in self.topics if x.id == topic_id][0]
        self.topics.remove(current_topic)

    def delete_document(self, document_id):
        current_doc = [x for x in self.documents if x.id == document_id][0]
        self.documents.remove(current_doc)

    def get_document(self, document_id):
        doc = [x for x in self.documents if x.id == document_id][0]
        return doc

    def __repr__(self):
        result = "\n".join([x.__repr__() for x in self.documents])
        return result
