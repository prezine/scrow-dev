<template>
    <div class="element-box hide" id="tab_team">
        <h6 class="form-header text-center" style="font-weight: 600">Team members</h6>
        <div class="col-sm-12">
            <div class="element-wrapper">
                <div class="element-box-tp">
                    <div class="table-responsive">
                        <table class="table table-padded">
                            <thead>
                            <tr>
                                <th>Name</th>
                                <th>Email</th>
                                <th>Role</th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr v-for="member in members">
                                <td>
                                    <div class="user-with-avatar">
                                        <img alt="" :src="member.role.user.photo"><span
                                            class="text-capitalize">{{member.role.user.name}}</span>
                                    </div>
                                </td>
                                <td>
                                    <div class="smaller lighter">{{member.role.user.email}}</div>
                                </td>
                                <td>
                                    <div class="semi-bold">{{member.role.role}}</div>
                                </td>
                            </tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="form-group">
                        <button class="mr-2 mb-2 btn btn-sm btn-rounded btn-primary btn-outline-success"
                                type="button" data-target="#addTeamMembersDialog" data-toggle="modal"> Add team member
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <add-members></add-members>
    </div>
</template>

<script>
    import AddMembers from "./AddMembers";

    export default {
        name: "TeamMembers",
        components: {
            AddMembers
        },
        data() {
            return {
                members: []
            }
        },
        created() {
            this.getTeamMembers();
        },
        methods: {
            getTeamMembers() {
                axios.get('/business/team').then(resp => {
                    this.members = resp.data
                }).catch(err => {
                    this.$store.commit('setstatusMsg', {msg: err.response.data.detail, type: 'error'});
                });
            }
        }
    }
</script>

<style scoped>

</style>
