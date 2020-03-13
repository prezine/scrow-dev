<template>
    <div class="element-box" id="tab_profile">
        <form @submit.prevent="updateProfile">
            <h6 class="form-header text-center" style="font-weight: 600">Your Profile</h6>
            <div class="form-group">
                <label for="name"> Your Name</label>
                <input class="form-control" id="name" placeholder="Your Name"
                       required="required" v-model="formData.name" type="text" readonly>
                <div>

                </div>
            </div>
            <div class="row">
                <div class="col-sm-6">
                    <div class="form-group">
                        <label for="email"> Email address</label>
                        <input class="form-control" id="email"
                               placeholder="Your Email Address" v-model.trim="$v.formData.email.$model"
                               required="required"
                               type="email">
                        <div class="help-block form-text with-errors form-control-feedback"></div>
                        <div class="error" v-if="!$v.formData.email.required">Please provide your email address</div>
                    </div>
                </div>
                <div class="col-sm-6">
                    <div class="form-group">
                        <label for="gender"> Gender </label>
                        <select class="form-control" v-model.trim="$v.formData.gender.$model" id="gender">
                            <option>Select gender</option>
                            <option value="Male">Male
                            </option>
                            <option value="Female">Female
                            </option>
                        </select>
                        <div class="error" v-if="!$v.formData.gender.required">Please select gender</div>
                    </div>
                </div>
            </div>
            <div class="form-group">
                <button class="mr-2 mb-2 btn btn-sm btn-rounded btn-primary btn-outline-primary"
                        type="button"> Change Password
                </button>
            </div>
            <div class="form-group">
                <label for="phone">Phone Number</label>
                <div class="input-group">
                    <div class="input-group-prepend">
                        <div class="input-group-text" style="padding: 0 25px;font-weight: 600">
                            +234
                        </div>
                    </div>
                    <input class="form-control" v-model.trim="$v.formData.phone.$model" id="phone"
                           placeholder="817 123 4567" type="text">
                </div>
                <div class="error" v-if="!$v.formData.phone.required">Enter your phone number</div>
            </div>
            <div class="row">
                <div class="col-sm-6">
                    <div class="form-group">
                        <label for="country">Country</label>
                        <select class="form-control" v-model.trim="$v.formData.country.$model" id="country"
                                required></select>
                        <div class="help-block form-text with-errors form-control-feedback"></div>
                        <div class="error" v-if="!$v.formData.country.required">Please select country</div>
                    </div>
                </div>
                <div class="col-sm-6">
                    <div class="form-group">
                        <label for="state">State</label>
                        <select class="form-control" v-model.trim="$v.formData.state.$model" id="state"
                                required></select>
                        <div class="error" v-if="!$v.formData.state.required">Please select state</div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-12">
                    <div class="form-group">
                        <label for="city">City</label>
                        <input type="text" class="form-control" v-model.trim="$v.formData.city.$model" id="city"
                               required>
                        <div class="error" v-if="!$v.formData.city.required">Enter city</div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-12">
                    <div class="form-group">
                        <label for="date_of_birth"> Date of Birth</label>
                        <datetime class="form-control" id="date_of_birth" type="date"
                                  v-model.trim="$v.formData.date_of_birth.$model"></datetime>
                        <div class="error" v-if="!$v.formData.date_of_birth.required">Enter your date of birth</div>
                    </div>
                </div>
            </div>
            <div class="form-buttons-w" align="center">
                <button class="mr-2 mb-2 btn btn-outline-success" type="submit"> Save Changes</button>
            </div>
        </form>
    </div>
</template>

<script>
    import {required, email} from 'vuelidate/lib/validators';

    export default {
        name: "Profile",
        data() {
            return {
                formData: {
                    name: '',
                    email: '',
                    gender: '',
                    phone: '',
                    country: '',
                    state: '',
                    city: '',
                    date_of_birth: ''
                }
            }
        },
        validations: {
            formData: {
                email: {
                    required,
                    email
                },
                gender: {
                    required
                },
                phone: {
                    required
                },
                country: {
                    required
                },
                state: {
                    required
                },
                city: {
                    required
                },
                date_of_birth: {
                    required
                }
            }
        },
        mounted() {
            this.getProfileDetails();
        },
        methods: {
            getProfileDetails() {
                axios.get('/api/users/profile-details').then(resp => {
                    const {name, email, phone, gender, country, state, city, date_of_birth} = resp.data;
                    this.formData = {
                        name,
                        email,
                        gender,
                        phone,
                        country,
                        state,
                        city,
                        date_of_birth
                    };
                }).catch(err => {
                    this.$store.commit('setstatusMsg', {type: 'error', msg: 'Request could not be validated.'});
                });
            },
            updateProfile() {
                this.$v.$touch();
                if (!this.$v.$invalid) {
                    axios.put('/api/users/profile-details', this.formData).then(resp => {
                        this.$store.commit('setstatusMsg', {type: 'success', msg: 'Profile details updated.'});
                        console.log('Form Success: ', resp.data);
                    }).catch(err => {
                        if (err.response) {
                            if (err.response.data.non_field_errors) {
                                this.$store.commit('setstatusMsg', {
                                    type: 'error',
                                    msg: err.response.data.non_field_errors[0]
                                });
                            }
                        }
                    })
                }
            }
        }
    }
</script>

<style scoped>

</style>
