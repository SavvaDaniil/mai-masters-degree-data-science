from bs4 import BeautifulSoup

from internal.service.ParserService import ParserService

class ParserFacade:

    def __init__(self):
        self.parserService: ParserService = ParserService()

    def parse_page_by_url(self, url: str) -> None:
        """Парсинг HTML-контента страницы по url"""
        html_content: str = self.parserService.get_html_content_from_url(url=url)
        soup = BeautifulSoup(html_content, 'html.parser')
        print(soup.prettify())

