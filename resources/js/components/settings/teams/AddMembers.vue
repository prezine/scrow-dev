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
                            <label>Email address</label>
                            <input type="email" v-model.trim="$v.formData.email.$model"
                                   :class="{'is-invalid': formErrors.email || $v.formData.email.$error}"
                                   @input="findUser"
                                   placeholder="Add by email" class="form-control">
                            <div class="invalid-feedback" v-if="!$v.formData.email.email">Enter a valid email address
                            </div>
                            <div class="invalid-feedback" v-if="!$v.formData.email.required">Enter an email address
                            </div>
                            <div class="invalid-feedback" v-if="formErrors.email">{{formErrors.email[0]}}</div>
                            <div class="position-relative" v-if="users">
                                <div class="team-members-area">
                                    <div class="team-member" @click="selectUser(user)" v-for="user in users">
                                        {{user.name}}
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="form-group">
                            <label>Roles</label>
                            <select v-model.trim="$v.formData.role.$model" class="form-control"
                                    :class="{'is-invalid': formErrors.role || $v.formData.role.$error}">
                                <option value="" selected disabled>
                                    Select role
                                </option>
                                <option value="Developer">Developer</option>
                                <option value="Moderator">Moderator</option>
                            </select>

                            <div class="invalid-feedback" v-if="!$v.formData.role.required">Select role
                            </div>
                            <div class="invalid-feedback" v-if="formErrors.role">
                                {{formErrors.role[0]}}
                            </div>
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
    import {formErrorHandler, non400ErrorMsg} from "../../../utils/utils";

    export default {
        name: "AddMembers",
        data() {
            return {
                users: [],
                isLoading: false,
                formErrors: [],
                formData: {
                    email: '',
                    role: ''
                }
            }
        },
        validations: {
            formData: {
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
                    this.isLoading = true;
                    axios.post('/business/team', this.formData).then(resp => {
                        this.$store.commit('setstatusMsg', {msg: resp.data, type: 'success'});
                        setTimeout(() => {
                            location.reload();
                        }, 3000);
                    }).catch(err => {
                        this.isLoading = false;
                        if (err.response.status === 400) {
                            formErrorHandler(err.response.data, this);
                        } else {
                            non400ErrorMsg(this);
                        }
                    });
                }
            },
            findUser() {
                axios.get(`business/team/find?email=${this.formData.email}`).then(resp => {
                    this.users = resp.data;
                }).catch(err => {
                    console.log(err);
                });
            },
            selectUser(user) {
                this.formData.email = user.email;
                this.users = [];
            }
        }
    }
</script>

<style scoped>
    .team-members-area {
        position: absolute;
        left: 0;
        width: 100%;
        background: #fff;
        padding: 7px 12px;
        max-height: 90px;
        overflow-y: auto;
    }

    .team-member {
        display: block;
        padding: 8px 12px;
        color: #5e6063;
        cursor: pointer;
    }

    .team-member:hover, .team-member:focus {
        background-color: #fafafa;
    }

    .team-member + .team-member {
        border-top: solid 1px #eee;
    }
</style>
