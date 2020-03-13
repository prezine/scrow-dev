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
