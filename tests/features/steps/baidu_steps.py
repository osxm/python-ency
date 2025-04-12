from behave import given, when, then
from selenium import webdriver
from time import sleep

@given('关键词 {keyword}')    # 对应步骤  Given 关键词 behave， 参数放在{}中
def step_impl(context, keyword):   # context是上下文对象，有参数的话，加上对应参数
    context.keyword = keyword  # 将参数绑定上下文对象，以便其他步骤使用

@when('打开百度页面')
def step_impl(context):
    context.driver = driver = webdriver.Chrome()  # 同样绑定上下文对象
    driver.implicitly_wait(10)
    driver.get('https://www.baidu.com')


@when('输入关键词')
def step_impl(context):
    context.driver.find_element('id', 'kw').send_keys(context.keyword)


@when('点击百度一下按钮')
def step_impl(context):
    context.driver.find_element('id', 'su').click()
    sleep(0.5)


@then('页面标题中应包含关键词')
def step_impl(context):
    assert context.keyword in context.driver.title
