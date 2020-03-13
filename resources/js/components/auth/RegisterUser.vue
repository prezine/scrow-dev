<template>
    <div>
        <h3>User Registration</h3>
        <div v-if="errorResponse">{{errorResponse}}</div>
        <div v-if="successResponse">{{successResponse}}</div>
        <form @submit.prevent="createUser">
            <div class="form-group">
                <input type="text" v-model.trim="$v.formData.name.$model" class="form-control" placeholder="Name">
                <div class="error" v-if="!$v.formData.name.required">Enter your name</div>
            </div>
            <div class="form-group">
                <input type="email" v-model.trim="$v.formData.email.$model" class="form-control" placeholder="Email">
                <div class="error" v-if="!$v.formData.email.required">Enter your email address</div>
                <div class="error" v-if="!$v.formData.email.email">Enter a valid email address</div>
            </div>
            <div class="form-group">
                <input type="tel" v-model.trim="$v.formData.calling_code.$model" class="form-control"
                       placeholder="Calling code">
                <div class="error" v-if="!$v.formData.calling_code.required">Select calling code</div>
            </div>
            <div class="form-group">
                <input type="tel" v-model.trim="$v.formData.phone.$model" class="form-control"
                       placeholder="Phone">
                <div class="error" v-if="!$v.formData.phone.required">Enter phone number</div>
            </div>
            <div class="form-group">
                <input type="password" v-model.trim="$v.formData.password.$model" class="form-control"
                       placeholder="Password">
                <div class="error" v-if="!$v.formData.password.required">Enter password</div>
                <div class="error" v-if="!$v.formData.password.minLength">Password must be at least 6 characters</div>
            </div>
            <div class="form-group">
                <input type="password" v-model.trim="$v.formData.retype_password.$model" class="form-control"
                       placeholder="Retype Password">
                <div class="error"
                     v-if="!$v.formData.retype_password.sameAsPassword">
                    Password and retyped password does not match.
                </div>
            </div>
            <div class="form-group">
                <select v-model.trim="$v.formData.gender.$model" class="form-control">
                    <option value="" disabled selected>Select Gender</option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                </select>
                <div class="error" v-if="!$v.formData.gender.required">Select your gender</div>
            </div>
            <div class="form-group">
                <select v-model.trim="$v.formData.country.$model" class="form-control">
                    <option value="" disabled selected>Select Country</option>
                    <option value="Nigeria">Nigeria</option>
                    <option value="Spain">Spain</option>
                </select>
                <div class="error" v-if="!$v.formData.country.required">Select your country</div>
            </div>
            <div class="form-group">
                <input type="text" v-model.trim="$v.formData.state.$model" class="form-control"
                       placeholder="State">
                <div class="error" v-if="!$v.formData.state.required">Enter state/province</div>
            </div>
            <div class="form-group">
                <input type="text" v-model.trim="$v.formData.city.$model" class="form-control"
                       placeholder="City">
                <div class="error" v-if="!$v.formData.city.required">Enter city</div>
            </div>
            <div class="form-group">
                <input type="text" v-model.trim="$v.formData.address.$model" class="form-control"
                       placeholder="Address">
                <div class="error" v-if="!$v.formData.address.required">Enter your address</div>
            </div>
            <div class="form-group">
                <label>Date of birth</label>
                <datetime type="date" v-model.trim="$v.formData.date_of_birth.$model"></datetime>
                <div class="error" v-if="!$v.formData.date_of_birth.required">Enter your date of birth</div>
            </div>

            <div class="form-group">
                <button class="btn btn-primary" type="submit">Create Account</button>
            </div>
        </form>
    </div>
</template>

<script>
    import {required, minLength, email, sameAs} from 'vuelidate/lib/validators';

    export default {
        name: "RegisterUser",
        props: {
            'noReload': {
                type: Boolean,
                required: false
            },
            'invite_id': {
                type: String,
                required: false
            }
        },
        data() {
            return {
                isLoading: false,
                formErrors: [],
                errorResponse: '',
                successResponse: '',
                formData: {
                    name: '',
                    email: '',
                    password: '',
                    retype_password: '',
                    phone: '',
                    calling_code: '',
                    gender: '',
                    address: '',
                    city: '',
                    state: '',
                    country: '',
                    date_of_birth: '',
                    invite_id: this.invite_id
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
                country: {
                    required
                },
                gender: {
                    required
                },
                state: {
                    required
                },
                city: {
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
                        console.log(err.response);
                        if (err.response.statusCode === 400) {
                            if (err.response.data) {
                                console.log(err.response.data);
                            }
                        }
                    });
                }
            }
        }
    }
</script>

<style scoped>

</style>
