class Trainer:
    auto_incr_id = 1

    def __init__(self, name):
        self.name = name
        self.id = Trainer.auto_incr_id
        Trainer.auto_incr_id += 1

    @staticmethod
    def get_next_id():
        return Trainer.auto_incr_id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
