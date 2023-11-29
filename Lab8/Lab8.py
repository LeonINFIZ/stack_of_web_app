import json
from abc import ABC, abstractmethod

# Шаблонный метод
class EntityUpdaterTemplate(ABC):
    # Основной метод для обновления сущности
    def update_entity(self, entity_id):
        # Шаг 1: Получение объекта для обновления
        entity = self.fetch_entity(entity_id)

        # Шаг 2: Валидация исходных данных
        if self.validate_data(entity):
            # Шаг 3: Формирование запроса на сохранение информации
            save_request = self.create_save_request(entity)

            # Шаг 4: Отправка запроса и получение ответа
            response = self.send_save_request(save_request)

            # Шаг 5: Формирование ответа - кода ответа и статуса
            status_code = self.extract_status_code(response)
            status_message = self.extract_status_message(response)
            json_response = self.create_json_response(entity, status_code, status_message)

            # Шаг 6: Отличия для каждой конкретной сущности
            self.apply_entity_specific_hooks(entity, status_code, status_message)

            # Шаг 7: Вывод результата или уведомление администратора
            self.display_result(json_response)
        else:
            self.notify_admin("Validation failed for entity with ID: " + entity_id)

    @abstractmethod
    def apply_entity_specific_hooks(self, entity, status_code, status_message):
        pass

    @abstractmethod
    def fetch_entity(self, entity_id):
        pass

    @abstractmethod
    def validate_data(self, entity):
        pass

    @abstractmethod
    def create_save_request(self, entity):
        pass

    @abstractmethod
    def send_save_request(self, request):
        pass

    @abstractmethod
    def extract_status_code(self, response):
        pass

    @abstractmethod
    def extract_status_message(self, response):
        pass

    @abstractmethod
    def display_result(self, json_response):
        pass

    @abstractmethod
    def notify_admin(self, message):
        pass

    def create_json_response(self, entity, status_code, status_message):
        return json.dumps({
            "entityId": entity.get_id(),
            "statusCode": status_code,
            "statusMessage": status_message
        })

# Конкретный класс для обновления Товара
class ProductUpdater(EntityUpdaterTemplate):
    def apply_entity_specific_hooks(self, entity, status_code, status_message):
        # Запрет изменения значений в поле email для пользователя
        pass

    def fetch_entity(self, entity_id):
        # Получение объекта для обновления
        pass

    def validate_data(self, entity):
        # Валидация исходных данных
        pass

    def create_save_request(self, entity):
        # Формирование запроса на сохранение информации
        pass

    def send_save_request(self, request):
        # Отправка запроса и получение ответа
        pass

    def extract_status_code(self, response):
        # Формирование ответа - кода ответа
        pass

    def extract_status_message(self, response):
        # Формирование ответа - статуса
        pass

    def display_result(self, json_response):
        # Вывод результата
        pass

    def notify_admin(self, message):
        # Уведомление администратора
        pass
