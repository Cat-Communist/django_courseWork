<script setup>
import { computed, ref } from 'vue'

const a = ref(67);
const b = ref(33);
let c = computed(() => {
    return a.value + b.value;
})

const list = ref([1, 2, 3, 4, 5])
const agent_list = ref([
    {"name": "James Bond", "code": "007"},
    {"name": "Daril Williams", "code": "008"},
    {"name": "John Wick", "code": "009"},
]);

const dict = ref({
    "007": {"title": "super"},
    "008": {"title": "middle"},
    "009": {"title": "junior"},
})
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
        <template v-for="item in agent_list">
            <div>{{ item.name }} {{ item.code }}</div>
        </template>
        <hr>
        <template v-for="item in agent_list">
            <div>{{ item.name }} {{ dict[item.code].title }}</div>
        </template>
    </div>
</template>

<style scoped></style>
