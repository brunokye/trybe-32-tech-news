from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    data = search_news({"title": {"$regex": title, "$options": "i"}})
    news_list = []

    for news in data:
        form = (news["title"], news["url"])
        news_list.append(form)

    return news_list


# Requisito 8
def search_by_date(date):
    try:
        new_form = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        data = search_news({"timestamp": new_form})
        news_list = []

        for news in data:
            form = (news["title"], news["url"])
            news_list.append(form)

        return news_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
