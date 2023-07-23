from tech_news.database import search_news


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
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
