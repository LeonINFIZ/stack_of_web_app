from abc import ABC, abstractmethod

# Интерфейс стратегии для расчета стоимости доставки
class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, order_amount: float) -> float:
        pass

# Конкретная стратегия для самовывоза
class PickupStrategy(DeliveryStrategy):
    def calculate_cost(self, order_amount: float) -> float:
        # Расчет стоимости для самовывоза
        pass

# Конкретная стратегия для доставки внешней службой доставки
class ExternalDeliveryStrategy(DeliveryStrategy):
    def calculate_cost(self, order_amount: float) -> float:
        # Расчет стоимости для доставки внешней службой
        pass

# Конкретная стратегия для доставки собственной службой доставки
class OwnDeliveryStrategy(DeliveryStrategy):
    def calculate_cost(self, order_amount: float) -> float:
        # Расчет стоимости для доставки собственной службой
        pass

# Класс контекста, который использует стратегию
class DeliveryContext:
    def __init__(self, strategy: DeliveryStrategy):
        self.delivery_strategy = strategy

    def set_delivery_strategy(self, strategy: DeliveryStrategy):
        self.delivery_strategy = strategy

    def calculate_delivery_cost(self, order_amount: float) -> float:
        # Использование текущей стратегии для расчета стоимости
        return self.delivery_strategy.calculate_cost(order_amount)

def main():
    # Создание объектов стратегий
    pickup_strategy = PickupStrategy()
    external_delivery_strategy = ExternalDeliveryStrategy()
    own_delivery_strategy = OwnDeliveryStrategy()

    # Создание контекста доставки с начальной стратегией (например, самовывоз)
    delivery_context = DeliveryContext(pickup_strategy)

    # Расчет стоимости для разных способов доставки
    order_amount = 50.0
    pickup_cost = delivery_context.calculate_delivery_cost(order_amount)

    # Изменение стратегии (например, на внешнюю доставку)
    delivery_context.set_delivery_strategy(external_delivery_strategy)
    external_delivery_cost = delivery_context.calculate_delivery_cost(order_amount)

    # Изменение стратегии (например, на собственную доставку)
    delivery_context.set_delivery_strategy(own_delivery_strategy)
    own_delivery_cost = delivery_context.calculate_delivery_cost(order_amount)

if __name__ == "__main__":
    main()
