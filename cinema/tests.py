from decimal import Decimal

from django.test import TestCase
from rest_framework.test import APIClient
from django.utils.dateparse import parse_duration

from model_bakery import baker
from cinema.models import Category, Movie, Subscription

# Create your tests here.
class BaseViewsetTestCase(TestCase):
    server_url = "http://testserver" 
    media_url = server_url+"media"
    model: str = ""
    def setUp(self):
        self.client = APIClient()

    # @staticmethod
    def instantiate(self, _quantity = None, **kwargs):
        return baker.make(self.model, _quantity, **kwargs)

class MovieViewsetTestCase(BaseViewsetTestCase):
    model = "cinema.Movie"
    
    def test_get_list(self):
        movie = self.instantiate(poster=baker.mock_file_jpeg)
        
        r = self.client.get('/api/movies/')
        data = r.json()

        assert movie.id == data[0]['id'], "id фильма не совпало"
        assert movie.title == data[0]['title'], "название не совпало"
        assert movie.duration == data[0]['duration'], "длительность не совпала"
        assert movie.description == data[0]['description'], "описание не совпало"
        assert self.server_url+movie.poster.url == data[0]['poster'], "постер не совпал"
        assert len(data) == 1

    def test_create(self):        
        r = self.client.post("/api/movies/", {
            "title": "Комар на улице сасов",
            "duration": parse_duration("01:23:00"),
            "description": "Описание"
        })
    
        data = r.json()

        new_movie = Movie.objects.all().filter(id=data['id']).first()

        assert new_movie.id == data['id'], "id не совпал"
        assert new_movie.title == data['title'], "название не совпало"
        assert new_movie.duration == parse_duration(data['duration']), "длительность не совпала"
        assert new_movie.description == data['description'], "описание не совпало"

    def test_delete(self):
        quantity = 5

        movies = baker.make("cinema.Movie", _quantity=quantity)
        r = self.client.get("/api/movies/")
        data = r.json()

        assert len(data) == quantity

        movie_id_to_delete = movies[3].id

        self.client.delete(f"/api/movies/{movie_id_to_delete}/")

        r = self.client.get("/api/movies/")
        data = r.json()
        assert len(data) == quantity - 1, f"Неправильное количество элементов: {len(data)}"

        assert movie_id_to_delete not in [i['id'] for i in data]

    def test_update_movie(self):
        quantity = 5

        movies = self.instantiate(_quantity=quantity)
        movie = movies[3]

        r = self.client.get(f"/api/movies/{movie.id}/")
        data = r.json()
        assert data['title'] == movie.title

        new_title = "Кошмар на улице вязов"
        r = self.client.put(f'/api/movies/{movie.id}/', {
            "title": new_title
        })
        assert r.status_code == 200

        r = self.client.get(f"/api/movies/{movie.id}/")
        data = r.json()
        assert data['title'] == new_title

        movie.refresh_from_db()
        assert data['title'] == movie.title

class CategoryViewsetTestCase(BaseViewsetTestCase):
    model = "cinema.Category"

    def test_get_list(self):
        category = self.instantiate()
        
        r = self.client.get("/api/categories/")
        data = r.json()

        assert len(data) == 1
        assert category.id == data[0]['id'], "не совпали id категорий"
        assert category.title == data[0]['title'], "не совпал title категорий"

    def test_create(self):
        r = self.client.post("/api/categories/", {
            "title": "Яндекс.Плюс"
        })
        data = r.json()

        new_category = Category.objects.all().filter(id=data['id']).first()

        assert new_category.id == data['id'], "Не совпали id объектов"
        assert new_category.title == data['title'], "Не совпал title категорий"

    def test_delete(self):
        quantity = 5
        categories = self.instantiate(_quantity=quantity)
        
        r = self.client.get("/api/categories/")
        data = r.json()
        assert len(data) == quantity, f"Неправильное количество объектов: q: {quantity} vs d: {len(data)}"

        category_to_delete_id = categories[0].id
        self.client.delete(f"/api/categories/{category_to_delete_id}/")

        r = self.client.get("/api/categories/")
        data = r.json()

        assert len(data) == quantity - 1
        assert category_to_delete_id not in [i['id'] for i in data]

    def test_update(self):
        quantity = 5

        categories = self.instantiate(_quantity=quantity)
        category = categories[3]

        r = self.client.get(f"/api/categories/{category.id}/")
        data = r.json()
        assert data['title'] == category.title

        new_title = "Яндекс.Плюс"
        r = self.client.put(f"/api/categories/{category.id}/", {
            "title": new_title
        })
        assert r.status_code == 200
        
        data = r.json()
        assert data['title'] == new_title

        category.refresh_from_db()
        assert data['title'] == category.title

class SubscriptionViewSetTestCase(BaseViewsetTestCase):
    model = "cinema.Subscription"

    def test_get_list(self):
        subscription = self.instantiate()

        r = self.client.get("/api/subscriptions/")
        data = r.json()

        assert len(data) == 1, ""
        assert subscription.title == data[0]['title']
        assert subscription.price == data[0]['price']
        assert subscription.duration == data[0]['duration']

    def test_create(self):
        r = self.client.post("/api/subscriptions/", {
            "title": "Эконом",
            "price": 1200.00,
            "duration": 30
        })
        data = r.json()

        new_subscription = Subscription.objects.all().filter(id=data['id']).first()

        assert new_subscription.id == data['id']
        assert new_subscription.title == data['title']
        assert new_subscription.price == Decimal(data['price'])
        assert new_subscription.duration == data['duration']

    def test_delete(self):
        quantity = 5
        subscriptions = self.instantiate(_quantity=quantity)
        subscription = subscriptions[3]

        r = self.client.get("/api/subscriptions/")
        data = r.json()
        assert len(data) == quantity

        self.client.delete(f"/api/subscriptions/{subscription.id}/")

        r = self.client.get("/api/subscriptions/")
        data = r.json()
        assert len(data) == quantity - 1

        assert subscription.id not in [i['id'] for i in data]

    def test_update(self):
        quantity = 5
        subscriptions = self.instantiate(_quantity=quantity)
        subscription = subscriptions[3]

        r = self.client.get(f"/api/subscriptions/{subscription.id}/")
        data = r.json()
        assert data['title'] == subscription.title

        new_title = "Премиум"
        r = self.client.put(f"/api/subscriptions/{subscription.id}/", {
            "title": new_title
        })
        assert r.status_code == 200

        data = r.json()
        assert data['title'] == new_title

        subscription.refresh_from_db()
        assert data['title'] == subscription.title