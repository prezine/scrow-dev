<template>
    <div>
        {{statusMsg.msg}}
    </div>
</template>

<script>
    import {mapGetters} from 'vuex';
    export default {
        name: "status-msg",
        computed: {
            ...mapGetters(['statusMsg'])
        }
    }
</script>

<style scoped>

</style>
