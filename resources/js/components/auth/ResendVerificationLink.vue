<template>
    <div>
        <template @click="resendLink" v-if="!isLinkSent">
            <slot></slot>
        </template>
    </div>
</template>

<script>
    import {mapGetters, mapActions} from 'vuex';

    export default {
        name: "ResendVerificationLink",
        computed: {
            ...mapGetters({
                isLinkSent: 'isVerificationLinkSent'
            })
        },
        methods: {
            ...mapActions({
                resendLink: 'resendVerificationLink'
            })
        }
    }
</script>

<style scoped>
</style>
