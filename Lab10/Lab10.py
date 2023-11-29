from abc import ABC, abstractmethod

# Объявление класса Посредник
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, message):
        pass

# Объявление класса Компонент
class Component:
    def __init__(self, mediator=None):
        self._mediator = mediator

    def set_mediator(self, mediator):
        self._mediator = mediator

# Объявление класса Календарь
class Calendar(Component):
    def choose_date(self, date):
        pass

    def choose_time_slot(self, time_slot):
        pass

# Объявление класса Форма Доставки
class DeliveryForm(Component):
    def toggle_recipient_info(self, is_checked):
        pass

    def provide_recipient_info(self, name, phone_number):
        pass

    def enable_delivery_info(self, is_enabled):
        pass

# Объявление класса Магазин
class FlowerShop(Component):
    def enable_self_pickup(self, is_enabled):
        pass

# Реализация класса Конкретный Посредник
class ConcreteMediator(Mediator):
    def __init__(self, calendar, delivery_form, flower_shop):
        self._calendar = calendar
        self._delivery_form = delivery_form
        self._flower_shop = flower_shop

        self._calendar.set_mediator(self)
        self._delivery_form.set_mediator(self)
        self._flower_shop.set_mediator(self)

    def notify(self, sender, message):
        pass

# Клиентский код, который использует паттерн Посредник
def main():
    # Создание объектов для календаря, формы доставки и магазина
    calendar = Calendar()
    delivery_form = DeliveryForm()
    flower_shop = FlowerShop()

    # Создание экземпляра конкретного посредника
    mediator = ConcreteMediator(calendar, delivery_form, flower_shop)

    # Использование компонентов через посредника
    # ...

if __name__ == "__main__":
    main()
