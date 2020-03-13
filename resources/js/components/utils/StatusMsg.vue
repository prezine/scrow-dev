<template>
    <div class="fixed-top alert-container">
        <div class="alert alert-dismissible fade show" role="alert" v-if="statusMsg.msg"
             :class="[{'alert-danger': statusMsg.type === 'error'}, {'alert-warning': statusMsg.type === 'warning'}, {'alert-success': statusMsg.type === 'success'}, {'alert-info': statusMsg.type === 'info'}]">
            <button aria-label="Close" class="close" data-dismiss="alert" type="button"><span aria-hidden="true"> &times;</span></button>
            {{statusMsg.msg}}
        </div>
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
    .alert-container {
        width: 380px;
        max-width: 97%;
        top: 80px;
        right: 10px;
        left: initial;
    }
</style>
