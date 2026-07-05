<template>
    <div>
        <h1>Datasets</h1>
        <ul>
            <li v-for="dataset in datasets" :key="dataset.id">
                {{ dataset.name }}
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    data() {
        return {
            datasets: []
        }
    },
    mounted() {
        this.$axios.get('/datasets/').then(response => {
            this.datasets = response.data
        })
    }
}
</script>