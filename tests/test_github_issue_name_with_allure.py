import allure
from selene import have
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


@allure.tag("without allure")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", " Ilya Shebanov")
@allure.feature("Имя задачи в репозитории")
@allure.story("Имя задачи в репозитории без шагов")
@allure.link("https://github.com", name="Testing")
def test_github_issue_name_without_allure():
    browser.open('https://github.com')

    s('.header-search-button').click()
    s('#query-builder-test').send_keys('eroshenkoam/allure-example')
    s('#query-builder-test').submit()

    s(by.link_text('eroshenkoam/allure-example')).click()

    s('#issues-tab').click()

    s(by.text('Тестируем тест')).click()

    s('[data-testid=issue-title]').should(have.exact_text('Тестируем тест'))


@allure.tag("with allure")
@allure.severity(Severity.NORMAL)
@allure.label("owner", " Ilya Shebanov")
@allure.feature("Имя задачи в репозитории")
@allure.story("Имя задачи в репозитории с лямбда шагами")
@allure.link("https://github.com", name="Testing")
def test_github_issue_name_dynamic_steps():
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий'):
        s('.header-search-button').click()
        s('#query-builder-test').send_keys('eroshenkoam/allure-example')
        s('#query-builder-test').submit()

    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем таб Issues'):
        s('#issues-tab').click()

    with allure.step('Открываем Issue с именем "Тестируем тест"'):
        s(by.text('Тестируем тест')).click()

    with allure.step('Проверяем, что имя Issue - "Тестируем тест"'):
        s('[data-testid=issue-title]').should(have.exact_text('Тестируем тест'))


@allure.tag("with allure")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", " Ilya Shebanov")
@allure.feature("Имя задачи в репозитории")
@allure.story("Имя задачи в репозитории с шагами с декоратором")
@allure.link("https://github.com", name="Testing")
def test_github_issue_name_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    open_issue_with_name('Тестируем тест')
    should_see_name('Тестируем тест')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com')


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    s('.header-search-button').click()
    s('#query-builder-test').send_keys(repo)
    s('#query-builder-test').submit()


@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открываем таб Issues')
def open_issue_tab():
    s('#issues-tab').click()


@allure.step('Открываем Issue с именем "{name}"')
def open_issue_with_name(name):
    s(by.text(name)).click()


@allure.step('Проверяем, что имя Issue - "{name}"')
def should_see_name(name):
    s('[data-testid=issue-title]').should(have.exact_text(name))
