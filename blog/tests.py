from unicodedata import name
from .models import Good
from bs4 import BeautifulSoup
from django.test import TestCase, Client

# Create your tests here.
class TestView(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_shopping_list(self):
        response = self.client.get('/shopping/')
        # 페이지 로드 
        self.assertEqual(response.status_code, 200) 

        # 페이지의 타이틀이 sonnic shopping인지 확인
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'sonnic shopping')

        # 네비게이션 바에 Home, Shop 있는지 확인
        navbar = soup.nav
        self.assertIn('Home', navbar.text)
        self.assertIn('Shop', navbar.text)

        # 게시물 개수 확인
        self.assertEqual(Good.objects.count(), 0)

        #게시물이 없다면 '아직 쇼핑 품목이 없습니다.'출력하기
        # main_area = soup.find('div', id='main-area')
        # self.assertIn('아직 쇼핑 품목이 없습니다.', main_area.text)

        # 게시물 만들고 다시 확인
        post_001 = Good.objects.create(
            name = '킹 사이즈 침대',
            price = 450000,
        )
        post_002 = Good.objects.create(
            name = '퀸 사이즈 침대',
            price = 400000,
        )
        self.assertEqual(Good.objects.count(), 2) # 게시물 개수 2개 확인

        # 포스트 목록 새로고침 했을 경우
        response = self.client.get('/shopping/')
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(response.status_code, 200)

        # main-area에 게시물 2개의 제목이 존재하는지 확인
        main_area = soup.find('div', id='main-area')
        # self.assertEqual(post_001.name, main_area.text)
        # self.assertEqual(post_002.name, main_area.text)

        # '아직 쇼핑 상품이 없습니다.'문구 안 나타나는 것 확인
        self.assertNotEqual('아직 쇼핑 품목이 없습니다.', main_area.text)
