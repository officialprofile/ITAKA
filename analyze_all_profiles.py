from playwright.sync_api import sync_playwright

def analyze_profile(profile_url):
  profile_data = []
  with sync_playwright() as p:
    browser = p.chromium.launch(headless = True)
    page = browser.new_page()
    page.goto(profile_url)
    name = page.query_selector('//div[contains(@class, "content")]/h1')
    if (name == None):
      return('')
    profile_data.append(name.text_content())
    attributes = page.query_selector_all('//div[contains(@class, "right")]')
    [profile_data.append(attribute.text_content()) for attribute in attributes]
    browser.close()
  return(';'.join(profile_data)+'\n')

def analyze_all_profiles(text_file_name):
  raw_data = open('raw_data.txt', 'a')
  
  with open(text_file_name, 'r') as links:
    for i, link in enumerate(links):
      raw_data.write(analyze_profile(link))
      print(i+1)
    links.close()
  raw_data.close()

analyze_all_profiles('links.txt')
