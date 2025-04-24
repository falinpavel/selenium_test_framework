from urllib.parse import urljoin


class Links:
    HOST = "https://phptravels.net/"
    HOME_PAGE = HOST
    LOGIN_PAGE = urljoin(HOST, "login")
    LOGOUT_PAGE = urljoin(HOST, "logout")
