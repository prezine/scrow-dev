<template>
    <div class="element-box-tp">
        <div class="fancy-progress-with-label">
            <div class="fpl-label">65%</div>
            <div class="fpl-progress-w">
                <div class="fpl-progress-i" style="width: 65%;"></div>
            </div>
        </div>
        <div class="todo-list">
            <a class="todo-item complete" href="./#">
                <div class="ti-info">
                    <div class="ti-header">Verify Account</div>
                    <div class="ti-sub-header">Verify email address</div>
                </div>
                <div class="ti-icon"><i class="os-icon os-icon-check"></i></div>
            </a>
            <a class="todo-item complete" href="./#">
                <div class="ti-info">
                    <div class="ti-header">Connect Bank Account</div>
                    <div class="ti-sub-header">You have connected 2 accounts</div>
                </div>
                <div class="ti-icon"><i class="os-icon os-icon-check"></i></div>
            </a>
            <a class="todo-item complete" href="./#">
                <div class="ti-info">
                    <div class="ti-header">Upload Tax Documents</div>
                    <div class="ti-sub-header">You uploaded W-2 and 1099</div>
                </div>
                <div class="ti-icon"><i class="os-icon os-icon-check"></i></div>
            </a>
            <a class="todo-item" href="./#">
                <div class="ti-info">
                    <div class="ti-header">Deposit Money</div>
                    <div class="ti-sub-header">You can deposit from your bank</div>
                </div>
                <div class="ti-icon"><i class="os-icon os-icon-arrow-right7"></i></div>
            </a>
        </div>
    </div>
</template>

<script>
    export default {
        name: "ProfileCompletion",
        data(){
            return {
                profileDetails: {}
            }
        },
        created() {
            this.getProfileDetails();
        },
        methods: {
            getProfileDetails(){
                axios.get('/api/users/profile-details').then(resp => {
                    this.profileDetails = resp.data;
                }).catch(err => {
                    this.$store.commit('setStatusMsg', {type: 'warning', msg: 'An error may have occurred.'})
                })
            }
        }
    }
</script>

<style scoped>

</style>
