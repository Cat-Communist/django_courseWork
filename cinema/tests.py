from django.test import TestCase
from rest_framework.test import APIClient
from django.utils.dateparse import parse_duration

from model_bakery import baker
from cinema.models import Movie

# Create your tests here.
class BaseViewsetTestCase(TestCase):
    server_url = "http://testserver" 
    media_url = server_url+"media"
    def setUp(self):
        self.client = APIClient()

class MovieViewsetTestCase(BaseViewsetTestCase):
    def setUp(self):
        super().setUp()
    
    def test_get_list(self):
        movie = baker.make(
            "cinema.Movie",
            poster=baker.mock_file_jpeg
        )
        
        r = self.client.get('/api/movies/')
        data = r.json()

        assert movie.id == data[0]['id'], "id фильма не совпало"
        assert movie.title == data[0]['title'], "название не совпало"
        assert movie.duration == data[0]['duration'], "длительность не совпала"
        assert movie.description == data[0]['description'], "описание не совпало"
        assert self.server_url+movie.poster.url == data[0]['poster'], "постер не совпал"
        assert len(data) == 1

    def test_create_movie(self):
        movie = baker.make(
            "cinema.Movie",
            title="Комар на улице сасов",
            duration=parse_duration("01:23:00"),
            description="Описание",
        )
        
        r = self.client.post("/api/movies/", {
            "title": movie.title,
            "duration": movie.duration,
            "description": movie.description
        })
    
        data = r.json()

        new_movie = Movie.objects.all().filter(id=data['id']).first()

        assert new_movie.id == data['id'], "id не совпал"
        assert new_movie.title == data['title'], "название не совпало"
        assert new_movie.duration == parse_duration(data['duration']), "длительность не совпала"
        assert new_movie.description == data['description'], "описание не совпало"

    def test_delete_movie(self):
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

        movies = baker.make("cinema.Movie", _quantity=quantity)
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


class SubscriptionViewsetTestCase(BaseViewsetTestCase):
    def setUp(self):
        super().setup()

    def test_case(self):
        pass