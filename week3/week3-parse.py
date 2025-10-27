import urllib.request as request
import bs4
import csv


def get_data(url):

    with request.urlopen(url) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")

    article_data = root.find_all("div", class_="r-ent")
    articles = []

    for article in article_data:
        title = article.find("div", class_="title")
        if title.a != None:
            title_str = title.a.string
            articleURL = "https://www.ptt.cc" + title.a.attrs["href"]
            date_str = get_date(articleURL)
        else:  # excluding deleted articles
            continue
        like_count = article.find("div", class_="nrec")
        if like_count.span != None:
            like_str = like_count.span.string
        else:
            like_str = "0"

        valid_article = Article(title_str, like_str, date_str)
        articles.append(valid_article)

    print
    nextURL = ""
    btns = root.find_all("a", class_="btn wide")

    for btn in btns:
        if btn.string == "‹ 上頁":
            nextURL = btn.attrs["href"]
            return ("https://www.ptt.cc" + nextURL), articles
    return None, articles


def get_date(articleURL):
    with request.urlopen(articleURL) as response:
        data = response.read().decode("utf-8")
        root = bs4.BeautifulSoup(data, "html.parser")
        meta = root.find_all("div", class_="article-metaline")
        for m in meta:
            tag = m.find("span", class_="article-meta-tag")
            if tag.string == "時間":
                value = m.find("span", class_="article-meta-value")
                if value.string is not None:
                    return value.string
                else:
                    return ""  # If there is no publish time data, fill it with an empty string.
    return ""


class Article:
    def __init__(self, title, likes, publish_time):
        self.title = title
        self.likes = likes
        self.publish_time = publish_time


start_page_url = "https://www.ptt.cc/bbs/Steam/index.html"


def get_all_articles_till_page(start_url, total_pages):

    current_page_url = start_url
    count = 0
    all_articles = []
    while count <= total_pages:
        newURL, articles = get_data(current_page_url)
        current_page_url = newURL
        all_articles.extend(articles)
        if current_page_url is None:
            break

        count += 1

    return all_articles


def write_articles_to_csv(articles):
    with open("articles.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        for article in articles:
            writer.writerow([article.title, article.likes, article.publish_time])


all_articles = get_all_articles_till_page(start_page_url, 2)
write_articles_to_csv(all_articles)
