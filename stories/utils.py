from github import Github
import sys

def calc_correlation(search_string, max_repo_count = 10):

    g = Github("YOUR_KEY_HERE")

    language_usages = dict()
    repo_count = 1

    try:
        for repo in g.search_repositories(search_string):
            print("{:1.2f}%".format(repo_count/max_repo_count), end="\r")
            for lang in repo.get_languages():
                language_usages[lang] = language_usages.get(lang, 0) + 1
            repo_count += 1
            if repo_count >= max_repo_count:
                break

    except Exception as e:
        print("Repositories collected: ", repo_count, e)

    for key in language_usages:
        language_usages[key] /= repo_count

    return language_usages
