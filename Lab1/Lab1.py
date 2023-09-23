class Database:
    _instance = None  # Статическое поле для единственного экземпляра

    def __init__(self):
        self.storage_type = None  # Тип хранилища (локальный диск или Amazon S3)

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def set_storage_type(self, storage_type):
        self.storage_type = storage_type

    def save_file(self, filename):
        print(f"Saved to {self.storage_type}: {filename}")

    def retrieve_file(self, filename):
        print(f"Retrieved from {self.storage_type}: {filename}")


# Использование
if __name__ == "__main__":
    db = Database.get_instance()  # Получаем единственный экземпляр базы данных
    db.set_storage_type("Local Disk")  # Устанавливаем тип хранилища для базы данных

    # Пример использования
    db.save_file("file1.txt")
    db.retrieve_file("file2.txt")
