<template>
    <div>
        <h1>Models</h1>
        <ul>
            <li v-for="model in models" :key="model.id">
                {{ model.name }}
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    data() {
        return {
            models: []
        }
    },
    mounted() {
        this.$axios.get('/models/').then(response => {
            this.models = response.data
        })
    }
}
</script>