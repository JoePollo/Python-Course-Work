from bs4 import BeautifulSoup
from requests import get as reqGet

httpResponseCodes = BeautifulSoup(
    reqGet(
        "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status",
        headers = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        }
    ).text, "html.parser"
)
cleanedHTTPResponseCodes = [
    element for element in [
        elements.text.strip() for elements in httpResponseCodes.find_all("code")
    ] if any(char.isdigit() for char in element)
]

httpDictionary = {
    int(element[0:3]): element[4:] for element in cleanedHTTPResponseCodes
}
