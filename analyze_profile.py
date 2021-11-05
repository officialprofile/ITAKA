from playwright.sync_api import sync_playwright

# This function returns 8 elements in the following order: 
#     1. aktualny wiek
#     2. data zaginiecia
#     3. wiek w dniu zaginiecia, 
#     4. wzrost
#     5. kolor oczu
#     6. znaki szczegolne
#     7. ostatnie miejsce pobytu
#     8. kraj

def analyze_profile(url):
  profile_data = []
  with sync_playwright() as p:
    browser = p.chromium.launch(headless = True)
    page = browser.new_page()
    page.goto(url)
    attributes = page.query_selector_all('//div[contains(@class, "right")]')
    [profile_data.append(attribute.text_content()) for attribute in attributes]
    browser.close()
  return(profile_data)

example_url = 'http://www.zaginieni.pl/jak-pomagamy/poszukiwanie-zaginionych/zagineli/profil-osoby/?o=22386'
print(analyze_profile(example_url))
