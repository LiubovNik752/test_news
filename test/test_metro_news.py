from datetime import datetime, timezone
from conftest import db_connect

class Test_metro_news:

    def test_check_title(self, db_connect):
        """Проверка, что полученные из БД значения заголовка не пустые и не равны 'смотреть еще больше →'"""

        all_values = db_connect.get_dict_of_values()
        for value in all_values:
            article_title = all_values[value][0]
            assert article_title is not None and not article_title.startswith('смотреть\xa0еще\xa0больше')

    def test_check_img_url(self, db_connect):
        """Проверка, что полученные из БД значения заголовка не пустые и начинаются с 'http://mosday.ru/news/preview'"""

        all_values = db_connect.get_dict_of_values()
        for value in all_values:
            img_url = all_values[value][1]
            assert img_url is not None and img_url.startswith('http://mosday.ru/news/preview')

    def test_check_published_date(self, db_connect):
        """Проверка, что дата публикации меньше или равна текущей даты"""

        all_values = db_connect.get_dict_of_values()
        for value in all_values:
            published_date = all_values[value][2]
            assert published_date <= datetime.now(timezone.utc)

    def test_check_pursed_date(self, db_connect):
        """Проверка, что спаршенная дата равна текущей дате"""

        all_values = db_connect.get_dict_of_values()
        for value in all_values:
            parsed_date = all_values[value][3]
            parsed_formatted_date = parsed_date.strftime('%Y-%m-%d')
            assert parsed_formatted_date == datetime.today().strftime('%Y-%m-%d')

