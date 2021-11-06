from playwright.sync_api import sync_playwright

def get_urls():
  text_file = open('links.txt', 'a')
  with sync_playwright() as p:
    browser = p.chromium.launch(headless = True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://www.zaginieni.pl/jak-pomagamy/poszukiwanie-zaginionych/zagineli/wyniki-wyszukiwania/?firstname=&lastname=&type=missing&height_from=&height_to=&eyes=&age_from=&age_to=&age=now&city=&district=")

    current_page = 1
    last_page = page.query_selector('//p[@class="search_result_pagination"]/a[last()]').text_content()

    profiles = page.query_selector_all('//a[contains(@href, "profil-osoby")]')

    for profile in profiles:
      text_file.write(profile.get_attribute('href')+'\n')

    while current_page < int(last_page): #int(last_page)
      print(current_page)
      page.click('//p[@class="search_result_pagination"]/a[contains(@href,'+ str(current_page + 1) + ')]')
      page.wait_for_load_state()
      profiles = page.query_selector_all('//a[contains(@href, "profil-osoby")]')
      for profile in profiles:
        text_file.write(profile.get_attribute('href')+'\n')
      current_page += 1

    browser.close()
  text_file.close()

get_urls()
