
from internal.facade.ParserFacade import ParserFacade

if __name__ == '__main__':
    parserFacade: ParserFacade = ParserFacade()
    parserFacade.parse_page_by_url(url="https://yandex.ru")