from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def find_topic(self, topic_id):
        topic = [x for x in self.topics if x.id == topic_id][0]
        return topic

    def find_document(self, document_id):
        document = [x for x in self.documents if x.id == document_id][0]
        return document

    def find_category(self, category_id):
        category = [x for x in self.categories if category_id == x.id][0]
        return category

    def edit_category(self, category_id: int, new_name: str):
        category = self.find_category(category_id)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.find_topic(topic_id)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.find_document(document_id)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.find_category(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.find_topic(topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.find_document(document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        return self.find_document(document_id)

    def __repr__(self):
        result = ""
        for d in self.documents:
            result += d.__repr__()
        return result
