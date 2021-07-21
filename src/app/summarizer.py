from newspaper import Article


def generate_summary(url: str) -> str:
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    return article.summary
