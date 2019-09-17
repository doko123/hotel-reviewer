from afinn import Afinn
from decimal import Decimal

from workflows.providers.comments import booking
from workflows.dry_provider.mixed_comments import factory_tweets


def sa_afinn(test):
    afinn_en = Afinn(language="en")
    result = Decimal(afinn_en.score(test))
    len(test.split())
    print("* Result of full text analyzis: " + f"{result:.2f}" + " *")
    n_gram = test.split(" ")
    result_n_gram = []
    i = 0
    while len(n_gram) > 1:
        result_n_gram.append(" ".join((n_gram[i], n_gram[i + 1])))
        n_gram.pop(i)
    if n_gram:
        result_n_gram.append(n_gram.pop(i))
    print([afinn_en.score(gram) for gram in result_n_gram])
    print([afinn_en.score(gram) for gram in result_n_gram])
    summarized = sum([afinn_en.score(gram) for gram in result_n_gram])
    result_n_gram = Decimal(summarized / 2 * len(result_n_gram) * 10)
    print("* Result of 2-gram analyzis:    " + f"{result_n_gram:.2f}" + " *")


if __name__ == "__main__":
    scrapper = booking.BookingScrapper("Światowit", "Lodz")

    scrapper.scrape(days_range=365, random=True, random_count=10)
    tweets = scrapper.reviews or factory_tweets

    for i, tweet in enumerate(tweets):
        print(20 * "*" + str(i) + 20 * "*")
        sa_afinn(tweet)
