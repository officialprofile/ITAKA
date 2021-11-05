from playwright.sync_api import sync_playwright

initial_url = "http://www.zaginieni.pl/jak-pomagamy/poszukiwanie-zaginionych/zagineli/wyniki-wyszukiwania/?firstname=&lastname=&type=missing&height_from=&height_to=&eyes=&age_from=&age_to=&age=now&city=&district="
profiles = []
links = []

def get_urls():
  with sync_playwright() as p:
    browser = p.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(initial_url)

    current_page = 1
    last_page = page.query_selector('//p[@class="search_result_pagination"]/a[last()]').text_content()

    profiles = page.query_selector_all('//a[contains(@href, "profil-osoby")]')
    [links.append(profile.get_attribute('href')) for profile in profiles]
    
    while (current_page < 4): # current_page < last_page
      current_links = []
      with context.expect_page() as tab:
        current_page += 1
        page.click('//p[@class="search_result_pagination"]/a[contains(@href,'+ str(current_page) + ')]')
        profiles = page.query_selector_all('//a[contains(@href, "profil-osoby")]')
        links += [current_links.append(profile.get_attribute('href')) for profile in profiles]
      tab.close()
      
    browser.close()
  return(links)  

get_urls()
