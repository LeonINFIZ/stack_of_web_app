from abc import ABC, abstractmethod

# Базовый класс для представления страниц
class Renderer(ABC):
    @abstractmethod
    def render_page(self, title: str, content: str):
        pass

    @abstractmethod
    def render_product(self, product_name: str, description: str, image: str, product_id: int):
        pass

# Конкретный класс HTMLRenderer, который реализует представление в формате HTML
class HTMLRenderer(Renderer):
    def render_page(self, title: str, content: str):
        # Рендеринг HTML страницы
        pass

    def render_product(self, product_name: str, description: str, image: str, product_id: int):
        # Рендеринг HTML товара
        pass

# Конкретный класс JsonRenderer, который реализует представление в формате JSON
class JsonRenderer(Renderer):
    def render_page(self, title: str, content: str):
        # Рендеринг JSON страницы
        pass

    def render_product(self, product_name: str, description: str, image: str, product_id: int):
        # Рендеринг JSON товара
        pass

# Конкретный класс XmlRenderer, который реализует представление в формате XML
class XmlRenderer(Renderer):
    def render_page(self, title: str, content: str):
        # Рендеринг XML страницы
        pass

    def render_product(self, product_name: str, description: str, image: str, product_id: int):
        # Рендеринг XML товара
        pass

# Базовый класс для страниц
class Page(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def render(self):
        pass

# Конкретный класс SimplePage, который реализует простую страницу
class SimplePage(Page):
    def __init__(self, renderer: Renderer, title: str, content: str):
        super().__init__(renderer)
        self.title = title
        self.content = content

    def render(self):
        self.renderer.render_page(self.title, self.content)

# Конкретный класс ProductPage, который реализует страницу товара
class Product:
    def __init__(self, product_name: str, description: str, image: str, product_id: int):
        self.product_name = product_name
        self.description = description
        self.image = image
        self.product_id = product_id

class ProductPage(Page):
    def __init__(self, renderer: Renderer, product: Product):
        super().__init__(renderer)
        self.product = product

    def render(self):
        self.renderer.render_product(self.product.product_name, self.product.description, self.product.image, self.product.product_id)

def main():
    html_renderer = HTMLRenderer()
    json_renderer = JsonRenderer()
    xml_renderer = XmlRenderer()

    # Рендеринг простой страницы в разных форматах
    simple_page = SimplePage(html_renderer, "Простая HTML страница", "Привет, это простая HTML страница.")
    simple_page.render()

    simple_page_json = SimplePage(json_renderer, "Простая JSON страница", "Привет, это простая JSON страница.")
    simple_page_json.render()

    simple_page_xml = SimplePage(xml_renderer, "Простая XML страница", "Привет, это простая XML страница.")
    simple_page_xml.render()

    # Рендеринг страницы товара в разных форматах
    product = Product("Ноутбук", "Мощный ноутбук с высоким разрешением экрана", "laptop.jpg", 12345)
    product_page = ProductPage(html_renderer, product)
    product_page.render()

    product_page_json = ProductPage(json_renderer, product)
    product_page_json.render()

    product_page_xml = ProductPage(xml_renderer, product)
    product_page_xml.render()

if __name__ == "__main__":
    main()
