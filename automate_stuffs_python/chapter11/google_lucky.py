import requests, sys, bs4

_args = sys.argv

if len(_args) < 2:
    print("Error: You must provide a term to search")
    sys.exit(-1)

_term = _args[1]
_headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
request_expression = f"https://www.google.com/search?q={_term}"

response = requests.get(request_expression, headers=_headers)

if not response.ok:
    print(f"Error: Something went wrong trying to search the term '{_term}'. Please try again in few minutes.")
    sys.exit(-1)

scrapper = bs4.BeautifulSoup(response.text, features="html.parser")

link_elements = scrapper.select(".r > a:nth-of-type(1)")

print(f"Google Search: {len(link_elements)} result(s)")

for element in link_elements:
    title_select = element.select("h3 .ellip")
    title_value = title_select[0].string

    link_url = element.get("href")

    print(f"* {title_value}\n{link_url}")
