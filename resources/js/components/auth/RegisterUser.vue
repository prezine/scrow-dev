<template>
    <form @submit.prevent="createUser">
        <div class="form-group">
            <label for="">Your Name</label>
            <input type="text" v-model.trim="$v.formData.name.$model" class="form-control" placeholder="Name">
            <div class="pre-icon os-icon os-icon-user-male-circle"></div>
            <div class="invalid-feedback" v-if="!$v.formData.name.required">Enter your name</div>
        </div>
        <div class="form-group">
            <input type="email" v-model.trim="$v.formData.email.$model" class="form-control" placeholder="Email">
            <div class="pre-icon os-icon os-icon-email-2-at"></div>
            <div class="invalid-feedback" v-if="!$v.formData.email.required">Enter your email address</div>
            <div class="invalid-feedback" v-if="!$v.formData.email.email">Enter a valid email address</div>
        </div>
        <div class="row">
            <div class="col-sm-4">
                <div class="form-group">
                    <label for="">Phone</label>
                    <input class="form-control" placeholder="Code" type="text">
                    <div class="pre-icon os-icon os-icon-phone"></div>
                </div>
            </div>
            <div class="col-sm-8">
                <div class="form-group">
                    <label for="">&nbsp;</label>
                    <input type="tel" v-model.trim="$v.formData.phone.$model" class="form-control"
                           placeholder="Phone">
                    <div class="invalid-feedback" v-if="!$v.formData.phone.required">Enter phone number</div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-sm-6">
                <div class="form-group">
                    <input type="password" v-model.trim="$v.formData.password.$model" class="form-control"
                           placeholder="Password">
                    <div class="pre-icon os-icon os-icon-fingerprint"></div>
                    <div class="invalid-feedback" v-if="!$v.formData.password.required">Enter password</div>
                    <div class="invalid-feedback" v-if="!$v.formData.password.minLength">Password must be at least 6
                        characters
                    </div>
                </div>
            </div>
            <div class="col-sm-6">
                <div class="form-group">
                    <input type="password" v-model.trim="$v.formData.retype_password.$model" class="form-control"
                           placeholder="Retype Password">
                    <div class="invalid-feedback"
                         v-if="!$v.formData.retype_password.sameAsPassword">
                        Password and retyped password does not match.
                    </div>
                </div>
            </div>
        </div>
        <div class="form-group">
            <label for="">Gender</label>
            <select v-model.trim="$v.formData.gender.$model" class="form-control">
                <option value="" disabled selected>-- Choose gender --</option>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
            </select>
            <div class="pre-icon os-icon os-icon-user-male-circle"></div>
            <div class="invalid-feedback" v-if="!$v.formData.gender.required">Select your gender</div>
        </div>
        <div class="form-group">
            <label for="">Your Location</label>
            <input class="form-control" v-model.trim="$v.formData.location.$model" id="location"
                   placeholder="Enter your location" type="text">
            <div class="pre-icon os-icon os-icon-ui-74"></div>
            <div class="invalid-feedback" v-if="!$v.formData.location.required">Select your country</div>
        </div>
        <div id="map"></div>
        <div class="form-group">
            <label for=""> Date of birth </label>
            <datetime type="date" v-model.trim="$v.formData.date_of_birth.$model"></datetime>
            <div class="pre-icon os-icon os-icon-basic-2-259-calendar"></div>
            <div class="invalid-feedback" v-if="!$v.formData.date_of_birth.required">Enter your date of birth</div>
        </div>

        <div class="buttons-w">
            <button class="btn btn-primary" type="submit">Create my account</button>
        </div>
    </form>
</template>

<script>
    import {required, minLength, email, sameAs} from 'vuelidate/lib/validators';
    import {formErrorHandler} from "../../utils";

    export default {
        name: "RegisterUser",
        props: {
            'noReload': {
                type: Boolean,
                required: false
            },
        },
        data() {
            return {
                isLoading: false,
                formErrors: [],
                formData: {
                    name: '',
                    email: '',
                    password: '',
                    retype_password: '',
                    phone: '',
                    calling_code: '',
                    gender: '',
                    address: '',
                    location: '',
                    date_of_birth: ''
                }
            }
        },
        validations: {
            formData: {
                name: {
                    required
                },
                email: {
                    required,
                    email
                },
                calling_code: {
                    required
                },
                phone: {
                    required
                },
                password: {
                    required,
                    minLength: minLength(6)
                },
                retype_password: {
                    sameAsPassword: sameAs('password')
                },
                gender: {
                    required
                },
                location: {
                    required
                },
                address: {
                    required
                },
                date_of_birth: {
                    required
                }
            }
        },
        methods: {
            non400ErrorMsg() {
                this.$store.commit('setstatusMsg', {
                    type: 'warning',
                    msg: 'Request could not be completed. Please reload and try again.'
                });
            },
            createUser: function () {
                this.$v.$touch();
                if (!this.$v.$invalid) {
                    axios.post('/api/users/create-user', this.formData).then(resp => {
                        if (this.noReload) {
                            this.$store.commit('createUser', {
                                registered: true,
                                userId: resp.data.id
                            });
                        } else {
                            window.location = '/dashboard';
                        }
                    }).catch(err => {
                        if (err.response.statusCode === 400) {
                            formErrorHandler(err.response.data, this.$store, this.formErrors);
                        } else {
                            this.non400ErrorMsg();
                        }
                    });
                }
            }
        }
    }
</script>

<style scoped>

</style>
