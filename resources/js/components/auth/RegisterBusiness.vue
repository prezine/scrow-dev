<template>
    <div>
        <component :is="currentComponent" :noReload="true"></component>
    </div>
</template>

<script>
    import BusinessRegistrationForm from "./BusinessRegistrationForm";
    import {mapGetters} from 'vuex';

    export default {
        name: "RegisterBusiness",
        props: ['user_id'],
        created() {
            let user_id = parseInt(this.user_id);
            if (this.user_id && !isNaN(user_id)) {
                this.$store.commit('createUser', {
                    registered: true,
                    userId: this.user_id
                });
            }
        },
        computed: {
            ...mapGetters(['userCreated']),
            currentComponent() {
                return this.userCreated.registered ? 'business-registration-form' : 'register-user';
            }
        },
        components: {
            BusinessRegistrationForm
        }
    }
</script>

<style scoped>

</style>
