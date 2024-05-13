from utils import get_movie_info

def get_movie_info(url):
    # 웹 페이지 로딩 및 파싱 로직
    # 예시:
    title = soup.find("title").get_text().replace(" : 네이버 통합검색", "")
    return title, image, desc

