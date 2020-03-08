<template>
    <div class="modal fade" id="addTeamMembersDialog" tabindex="-1" role="dialog"
         aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title" id="exampleModalLongTitle">Invite Team Member</h4>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <form @submit.prevent="sendInvite">
                    <div class="modal-body">
                        <div class="form-group">
                            <label>Member Name</label>
                            <input type="text" v-model.trim="$v.formData.name.$model" class="form-control">
                            <div class="error" v-if="!$v.formData.name.required">Enter invitee name</div>
                        </div>
                        <div class="form-group">
                            <label>Email address</label>
                            <input type="email" v-model.trim="$v.formData.email.$model" class="form-control">
                            <div class="error" v-if="!$v.formData.email.required">Enter your email address</div>
                        </div>
                        <div class="form-group">
                            <label>Roles</label>
                            <select v-model.trim="$v.formData.role.$model" class="form-control">
                                <option value="" selected default>
                                    Select role
                                </option>
                                <option value="Developer">Developer</option>
                                <option value="Moderator">Moderator</option>
                            </select>
                            <div class="error" v-if="!$v.formData.role.required">Select role</div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="submit" class="btn btn-primary">Send Invite</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import {required, email} from 'vuelidate/lib/validators';

    export default {
        name: "AddMembers",
        data() {
            return {
                isLoading: false,
                formErrors: [],
                errorResponse: '',
                successResponse: '',
                formData: {
                    name: '',
                    email: '',
                    role: ''
                }
            }
        },
        validations: {
            formData: {
                name: {
                    required
                },
                role: {
                    required
                },
                email: {
                    required,
                    email
                }
            }
        },
        methods: {
            sendInvite() {
                this.$v.$touch();
                if (!this.$v.$invalid) {
                    axios.post('/business/team', this.formData).then(resp => {
                        console.log(resp.data);
                        this.$store.commit('setstatusMsg', {msg: resp.data, type: 'success'});
                    }).catch(err => {
                        console.log(err.response);
                        if (err.response.data) {
                            console.log(err.response.data);
                        }
                    });
                }
            }
        }
    }
</script>

<style scoped>

</style>
