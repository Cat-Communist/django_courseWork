from django.test import TestCase
from rest_framework.test import APIClient
from django.utils.dateparse import parse_duration
# from tempfile import NamedTemporaryFile
# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.core.files import File
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
        movie = Movie.objects.create(
            title="Комар на улице сасов",
            duration=parse_duration("1:23:00"),
            description="Хых о сасах",
            poster="img_poster.jpg"
        )
        r = self.client.get('/api/movies/')
        data = r.json()
        print(data)
        assert movie.id == data[0]['id'], "id фильма не совпало"
        assert movie.title == data[0]['title'], "название не совпало"
        assert movie.duration == parse_duration(data[0]['duration']), "длительность не совпала"
        assert movie.description == data[0]['description'], "описание не совпало"
        assert self.server_url+movie.poster.url == data[0]['poster'], "постер не совпал"
        assert len(data) == 1

    def test_create_movie(self):
        r = self.client.post('/api/movies/', {
            "title": "Комар на улице сасов",
            "duration": parse_duration("1:23:00"),
            "description": "Хых о сасах",
            # "poster": SimpleUploadedFile(name='test_image', content=open(image_path, 'rb').read(), content_type='image/jpg')
            # как по уму мокнуть постер? не хочется зависеть от картинки
        })

        data = r.json()

        new_movie_id = data['id']
        new_movie = Movie.objects.all().filter(id=new_movie_id).first()
        
        assert new_movie.title == data['title'], "название не совпало"
        assert new_movie.duration == parse_duration(data['duration']), "длительность не совпала"
        assert new_movie.description == data['description'], "описание не совпало"
        # assert self.server_url+new_movie.poster.url == data['poster'], "постер не совпал"
