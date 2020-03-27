<template>
    <div class="modal-content">
        <div class="modal-header">
            <h5 class="modal-title" id="profileLabel">Personal Information</h5>
            <button aria-label="Close" class="close" data-dismiss="modal" type="button">
                <span aria-hidden="true"> &times;</span></button>
        </div>
        <form @submit.prevent="updateProfile">
            <div class="modal-body text-left">
                <div class="row">
                    <div class="col-sm-6">
                        <div class="form-group">
                            <label for=""> First name</label>
                            <input class="form-control" v-model.trim="$v.formData.firstName.$model"
                                   placeholder="First name" type="text"
                                   :class="{'is-invalid': formErrors.name || $v.formData.lastName.$error}">
                            <div class="invalid-feedback" v-if="!$v.formData.firstName.required">Enter your first name
                            </div>
                            <div class="invalid-feedback" v-if="formErrors.name">{{formErrors.name[0]}}</div>
                        </div>
                    </div>
                    <div class="col-sm-6">
                        <div class="form-group">
                            <label for="">Last name</label>
                            <input class="form-control" v-model.trim="$v.formData.lastName.$model"
                                   placeholder="Last name" type="text"
                                   :class="{'is-invalid': $v.formData.lastName.$error}">
                            <div class="invalid-feedback" v-if="!$v.formData.lastName.required">Enter your last name
                            </div>
                        </div>
                    </div>
                </div>
                <div class="form-group">
                    <label for=""> Phone number </label>
                    <input class="form-control" placeholder="Enter phone number" v-model.trim="$v.formData.phone.$model"
                           type="tel" :class="{'is-invalid': formErrors.phone || $v.formData.phone.$error}">
                    <div class="invalid-feedback" v-if="!$v.formData.phone.required">Enter your first name
                    </div>
                    <div class="invalid-feedback" v-if="formErrors.phone">{{formErrors.phone[0]}}</div>
                </div>

            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" data-dismiss="modal" type="button">
                    Close
                </button>
                <button class="btn btn-primary" type="submit" :disabled="isLoading"> Save changes</button>
            </div>
        </form>
    </div>
</template>

<script>
    import {required} from 'vuelidate/lib/validators';
    import {formErrorHandler, non400ErrorMsg} from "../../../utils/utils";

    export default {
        name: "PersonalInformation",
        props: ['username', 'phone'],
        data() {
            return {
                name: this.username,
                formErrors: [],
                isLoading: false,
                formData: {
                    firstName: '',
                    lastName: '',
                    phone: this.phone
                }
            }
        },
        validations: {
            formData: {
                firstName: {
                    required,
                },
                lastName: {
                    required,
                },
                phone: {
                    required
                }
            }
        },
        created() {
            this.insertName();
        },
        methods: {
            insertName() {
                let splitterUsername = this.name.split(' ');

                if (splitterUsername.length > 0) {
                    this.formData.firstName = splitterUsername.splice(0, 1);

                    for (name of splitterUsername) {
                        this.formData.lastName += splitterUsername.splice(0, 1);
                    }
                } else {
                    this.formData.firstName = this.name;
                }
            },
            combineName() {
                this.formData.name = this.formData.firstName + ' ' + this.formData.lastName;
                this.name = this.formData.name;
            },
            updateProfile() {
                this.$v.$touch();
                if (!this.$v.$invalid) {
                    this.isLoading = true;
                    this.combineName();
                    delete this.formData.firstName;
                    delete this.formData.lastName;
                    axios.put('/api/users/half-profile-details', this.formData).then(resp => {
                        this.$store.commit('setstatusMsg', {type: 'success', msg: 'Profile details updated.'});
                        setTimeout(() => {
                            location.reload();
                        }, 3000);
                    }).catch(err => {
                        this.isLoading = false;
                        this.insertName();
                        if (err.response.status === 400) {
                            formErrorHandler(err.response.data, this);
                        } else {
                            non400ErrorMsg(this);
                        }
                    })
                }
            }
        }
    }
</script>

<style scoped>

</style>
