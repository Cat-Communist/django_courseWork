<script setup>
import { computed, ref, onBeforeMount } from 'vue'
import axios from 'axios'
import Cookies from 'js-cookie'

const a = ref(67);
const b = ref(33);
let c = computed(() => {
    return a.value + b.value;
})

const list = ref([1, 2, 3, 4, 5])
const agentList = ref([
    { "name": "James Bond", "code": "007" },
    { "name": "Daril Williams", "code": "008" },
    { "name": "John Wick", "code": "009" },
]);

const dict = ref({
    "007": { "title": "super" },
    "008": { "title": "middle" },
    "009": { "title": "junior" },
})

const movieList = ref([]);
const categoryList = ref([])
async function fetchMovies() {
    const r = await axios.get("/api/movies/");
    console.log(r.data);
    movieList.value = r.data;
}

async function fetchCategories() {
    const r = await axios.get("/api/categories/");
    console.log(r.data);
    categoryList.value = r.data;
}

async function downloadOnClick() {
    await fetchMovies();
}

onBeforeMount(async () => {
    await fetchMovies();
    await fetchCategories();
    axios.defaults.headers.common['X-CSRFToken'] = Cookies.get('csrftoken');
})

const movieToAdd = ref({});
async function onMovieToAdd() {
    await axios.post("/api/movies/", {
        ...movieToAdd.value,
    });
    await fetchMovies(); // переподтягиваю
}

async function onRemoveClick(movie) {
    await axios.delete(`/api/movies/${movie.id}/`);
    await fetchMovies(); // переподтягиваю
}

const movieToEdit = ref({});
async function onMovieEditClick(movie) {
    movieToEdit.value = { ...movie };
}

async function onUpdateMovie() {
    await axios.put(`/api/movies/${movieToEdit.value.id}/`, {
        ...movieToEdit.value
    });
    await fetchMovies();
}
</script>

<template>
    <div>
        <h3>Калькулятор сложения</h3>
        <input type="number" v-model="a"></input> <br>
        <input type="number" v-model="b"></input> <br>
        <!-- <button>Считать</button> -->
        {{ a }} + {{ b }} = {{ c }}
        <hr>

        <h3>Работа со списками</h3>
        <template v-for="item in list">
            <div>{{ item }}</div>
        </template>
        <hr>
        <h3>Работа со словарями</h3>
        <template v-for="item in agentList">
            <div>{{ item.name }} {{ item.code }}</div>
        </template>
        <hr>

        <template v-for="item in agentList">
            <div>{{ item.name }} {{ dict[item.code].title }}</div>
        </template>
        <hr>

        <h3>Работа с бэкендом</h3>
        <b>Список фильмов:</b> <br>
        <button @click="downloadOnClick">Загрузить с сервера</button>
        <div v-for="item in movieList" class="movie-item">
            <div>{{ item.title }}
                <!-- <div>{{ groupsById[item.group]?.name }}</div> -->
                <button class="btn btn-success" @click="onMovieEditClick(item)" data-bs-toggle="modal"
                    data-bs-target="#editMovieModal">
                    <i class="bi bi-pen-fill"></i>
                </button>
                <button class="btn btn-danger" @click="onRemoveClick(item)">
                    <i class="bi bi-x"></i>
                </button>
            </div>
        </div>
        <b>Добавление фильма</b> <br>
        <!-- ТУТ ПОДКЛЮЧИЛ обработчик отправки формы -->
        <form @submit.prevent.stop="onMovieToAdd">
            <div class="row">
                <div class="col">
                    <div class="form-floating">
                        <!-- ТУТ ПОДКЛЮЧИЛ movieToAdd.name -->
                        <input type="text" class="form-control" v-model="movieToAdd.title" required />
                        <label for="floatingInput">Название</label>
                    </div>
                </div>
                <div class="col-auto">
                    <!-- А ТУТ ПОДКЛЮЧИЛ К select -->
                    <div class="form-floating">
                        <select class="form-select" v-model="movieToAdd.category" required>
                            <option :value="c.id" v-for="c in categoryList">{{ c.title }}</option>
                        </select>
                        <label for="floatingInput">Категория</label>
                    </div>
                </div>
                <div class="col-auto">
                    <button class="btn btn-primary">
                        Добавить
                    </button>
                </div>
            </div>
        </form>

        <div class="modal fade" id="editMovieModal" tabindex="-1">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">
                            Редактировать
                        </h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="row">
                            <div class="col">
                                <div class="form-floating">
                                    <input type="text" class="form-control" v-model="movieToEdit.title" />
                                    <label for="floatingInput">Название</label>
                                </div>
                            </div>
                            <div class="col">
                                <div class="form-floating">
                                    <input type="text" class="form-control" v-model="movieToEdit.description" />
                                    <label for="floatingInput">Описание</label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                            Закрыть
                        </button>
                        <button data-bs-dismiss="modal" type="button" class="btn btn-primary" @click="onUpdateMovie">
                            Сохранить
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped></style>
