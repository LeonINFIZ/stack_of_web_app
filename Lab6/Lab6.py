from abc import ABC, abstractmethod

# Интерфейс для загрузки файлов
class Downloader(ABC):
    @abstractmethod
    def download(self, url: str):
        pass

# Реализация интерфейса Downloader
class SimpleDownloader(Downloader):
    def download(self, url: str):
        # Реализация загрузки файлов
        print(f"Загрузка файла из: {url}")

# Класс ProxyDownloader, который выступает в роли заместителя и добавляет кэширование
class ProxyDownloader(Downloader):
    def __init__(self, downloader: SimpleDownloader):
        self.simple_downloader = downloader
        self.cache = {}

    def download(self, url: str):
        # Проверка кэша
        if url in self.cache:
            print(f"Получение файла из кэша: {url}")
        else:
            # Если нет в кэше, используем реальный объект SimpleDownloader
            self.simple_downloader.download(url)
            self.cache[url] = "Содержимое кэша"  # Сохраняем в кэше

def main():
    # Создание реального объекта SimpleDownloader
    real_downloader = SimpleDownloader()

    # Создание заместителя ProxyDownloader
    proxy_downloader = ProxyDownloader(real_downloader)

    # Клиентский код использует ProxyDownloader, но не должен знать о кэшировании
    proxy_downloader.download("https://example.com/file1.txt")
    proxy_downloader.download("https://example.com/file2.txt")
    proxy_downloader.download("https://example.com/file1.txt")  # Использует кэш

if __name__ == "__main__":
    main()
