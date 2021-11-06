from playwright.sync_api import sync_playwright

# The function returns 9 elements:
#     1. Zaginiony(a): imie drugie imie nazwisko
#     2. aktualny wiek
#     3. data zaginiecia
#     4. wiek w dniu zaginiecia, 
#     5. wzrost
#     6. kolor oczu
#     7. znaki szczegolne
#     8. ostatnie miejsce pobytu
#     9. kraj

def analyze_profile(profile_url):
  labels = ['Imie', 'Aktualny wiek', 'Data zaginiecia', 'Wiek w dniu zaginiecia', 'Wzrost', 'Kolor oczu', 'Znaki szczegolne', 'Ostatnie miejsce pobytu', 'Kraj']
  profile_data = []
  with sync_playwright() as p:
    browser = p.chromium.launch(headless = True)
    page = browser.new_page()
    page.goto(profile_url)

    name = page.query_selector('//div[contains(@class, "content")]/h1')
    profile_data.append(name.text_content())
    attributes = page.query_selector_all('//div[contains(@class, "right")]')
    [profile_data.append(attribute.text_content()) for attribute in attributes]
    browser.close()
  return(dict(zip(labels, profile_data)))

link = 'http://www.zaginieni.pl/jak-pomagamy/poszukiwanie-zaginionych/zagineli/profil-osoby/?o=22386'
print(analyze_profile(link))
