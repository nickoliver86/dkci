from selenium import webdriver

def before_feature(context, feature):
    if 'browser' in feature.tags:
        context.browser = webdriver.Firefox()
        context.browser.implicitly_wait(15)

def after_feature(context, feature):
    if 'browser' in feature.tags:
        context.browser.quit()
