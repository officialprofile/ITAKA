from playwright.sync_api import sync_playwright

def get_urls():
  initial_url = "http://www.zaginieni.pl/jak-pomagamy/poszukiwanie-zaginionych/zagineli/wyniki-wyszukiwania/?firstname=&lastname=&type=missing&height_from=&height_to=&eyes=&age_from=&age_to=&age=now&city=&district="
  links = []

  with sync_playwright() as p:
    browser = p.chromium.launch(headless = True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(initial_url)

    current_page = 1
    last_page = page.query_selector('//p[@class="search_result_pagination"]/a[last()]').text_content()

    profiles = page.query_selector_all('//a[contains(@href, "profil-osoby")]')
    [links.append(profile.get_attribute('href')) for profile in profiles]
 
    # if it is possible to go to the next page
    while current_page < 4: # currecnt_page < int(last_page)
      current_page += 1
      page.click('//p[@class="search_result_pagination"]/a[contains(@href,'+ str(current_page) + ')]')
      page.wait_for_load_state()
      profiles = page.query_selector_all('//a[contains(@href, "profil-osoby")]')
      [links.append(profile.get_attribute('href')) for profile in profiles]

    browser.close()

  return(links)

print(*get_urls())
