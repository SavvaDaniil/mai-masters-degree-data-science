import requests
from requests import Response


class ParserService:

    def get_html_content_from_url(self, url: str) -> str:
        """Получение контента HTML-контента страницы по URL"""
        response: Response = requests.get(url=url)
        html_answer: str = response.content
        response.close()
        return html_answer