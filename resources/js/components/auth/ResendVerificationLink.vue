<template>
    <div>
        <div v-if="!isLinkSent">
            <button type="button" @click="resendLink">Resend Verification Link</button>
        </div>
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
