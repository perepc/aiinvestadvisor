""" Custom tools definition """
from typing import List, Dict
from io import BytesIO
from langchain.tools import tool
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
from pypdf import PdfReader
import requests
from call_function_with_timeout import SetTimeout


class SearchTools():
    @tool("Web search")
    @staticmethod
    def web_search(keywords: str) -> List[Dict[str, str]]:
        """ Search the web using keywords in one string input variable and obtain a list of URLs """
        ddgs = DDGS()

        results = ddgs.text(keywords=keywords, max_results=1)
        return results


class ReadTools():
    @tool("Read PDF")
    @staticmethod
    def read_pdf(pdf: str) -> str:
        """ Reads a PDF from an URL as parameter and returns the text from the PDF file.
            Only works for URLs containing a pdf. If the URL does not contain a pdf,
            it will return an empty string  """
        if not ".pdf" in pdf.lower():
            return "This is not a PDF"

        response = requests.get(pdf, timeout=30)

        if response.status_code == 200:
            print("Response 200 reading PDF file")
            # Leer el contenido del PDF
            pdf_file = BytesIO(response.content)
            pdf_reader = PdfReader(pdf_file)
            # Extraer el texto de todas las páginas
            print("Extracting text from pdf")
            text = ""
            for page in pdf_reader.pages:
                func_with_timeout = SetTimeout(
                    page.extract_text(), timeout=10)
                is_done, is_timeout, error_message, results = func_with_timeout()
                if is_timeout:
                    text = ""
                    break
                text += results
                # text += pagina.extract_text()
            return text
        else:
            return "Unable to download PDF"

    @ tool("Read URL")
    @ staticmethod
    def read_url(url: str) -> str:
        """ Reads web site content using its URL as parameter  """
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            paragraphs = soup.find_all('p')
            result = [p.get_text() for p in paragraphs]
        else:
            result = "Web page not available"

        return result
