<template>
    <div class="element-box" id="tab_profile">
        <form @submit.prevent="updateProfile">
            <h6 class="form-header text-center" style="font-weight: 600">Your Profile</h6>
            <div class="form-group">
                <label for="name"> Your Name</label>
                <input class="form-control" id="name" placeholder="Your Name"
                       required="required" :value="formData.name" type="text" readonly>
                <div>

                </div>
            </div>
            <div class="row">
                <div class="col-sm-6">
                    <div class="form-group">
                        <label for="email"> Email address</label>
                        <input class="form-control"
                               :class="{'is-invalid': formErrors.email || $v.formData.email.$error}" id="email"
                               placeholder="Your Email Address" v-model.trim="$v.formData.email.$model"
                               required="required"
                               type="email">
                        <div class="invalid-feedback" v-if="!$v.formData.email.required">Please provide your email
                            address
                        </div>
                        <div class="invalid-feedback" v-if="!$v.formData.email.email">Enter a valid email address</div>
                        <div class="invalid-feedback" v-if="formErrors.email">{{formErrors.email[0]}}</div>
                    </div>
                </div>
                <div class="col-sm-6">
                    <div class="form-group">
                        <label for="gender"> Gender </label>
                        <select class="form-control"
                                :class="{'is-invalid': formErrors.gender || $v.formData.gender.$error}"
                                v-model.trim="$v.formData.gender.$model" id="gender">
                            <option>Select gender</option>
                            <option value="Male">Male</option>
                            <option value="Female">Female</option>
                        </select>
                        <div class="invalid-feedback" v-if="!$v.formData.gender.required">Please select gender</div>
                        <div class="invalid-feedback" v-if="formErrors.gender">{{formErrors.gender[0]}}</div>
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
                    <input class="form-control" :class="{'is-invalid': formErrors.phone || $v.formData.phone.$error}"
                           v-model.trim="$v.formData.phone.$model" id="phone"
                           placeholder="817 123 4567" type="text">
                </div>
                <div class="invalid-feedback" v-if="!$v.formData.phone.required">Enter your phone number</div>
                <div class="invalid-feedback" v-if="formErrors.phone">{{formErrors.phone[0]}}</div>
            </div>
            <div class="row">
                <div class="col-sm-12">
                    <div class="form-group">
                        <label for="">Location</label>
                        <vue-google-autocomplete
                                id="map"
                                v-model="$v.formData.location.$model"
                                :classname="locationStyleClass"
                                placeholder="Enter your location"
                                v-on:placechanged="getAddressData"
                        >
                        </vue-google-autocomplete>
                        <div class="invalid-feedback" v-if="!$v.formData.location.required">Enter location</div>
                        <div class="invalid-feedback" v-if="formErrors.location">{{formErrors.location[0]}}</div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-12">
                    <div class="form-group">
                        <label for="date_of_birth"> Date of Birth</label>
                        <datetime
                                :input-class="{'form-control': true, 'is-invalid': formErrors.date_of_birth || $v.formData.date_of_birth.$error}"
                                id="date_of_birth" type="date"
                                v-model.trim="$v.formData.date_of_birth.$model"></datetime>
                        <div class="invalid-feedback" v-if="!$v.formData.date_of_birth.required">Enter your date of
                            birth
                        </div>
                        <div class="invalid-feedback" v-if="formErrors.date_of_birth">{{formErrors.date_of_birth[0]}}
                        </div>
                    </div>
                </div>
            </div>
            <div class="form-buttons-w" align="center">
                <button class="mr-2 mb-2 btn btn-outline-success" type="submit" :disabled="isLoading"> Save Changes</button>
            </div>
        </form>
    </div>
</template>

<script>
    import {required, email} from 'vuelidate/lib/validators';
    import VueGoogleAutocomplete from 'vue-google-autocomplete';
    import {formErrorHandler, non400ErrorMsg} from "../../utils/utils";

    export default {
        name: "Profile",
        components: {
            VueGoogleAutocomplete
        },
        data() {
            return {
                isLoading: false,
                formErrors: [],
                formData: {
                    name: '',
                    email: '',
                    gender: '',
                    phone: '',
                    location: '',
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
                location: {
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
        computed: {
            locationStyleClass() {
                let className = 'form-control';

                if (this.formErrors.location || this.$v.formData.location.$error) {
                    className += ' is-invalid';
                }

                return className;
            }
        },
        methods: {
            getAddressData: function (addressData, placeResultData, id) {
                this.formData.location = placeResultData.formatted_address;
            },
            getProfileDetails() {
                axios.get('/api/users/profile-details').then(resp => {
                    const {name, email, phone, gender, location, date_of_birth} = resp.data;
                    this.formData = {
                        name,
                        email,
                        gender,
                        phone,
                        location,
                        date_of_birth
                    };
                }).catch(err => {
                    this.$store.commit('setstatusMsg', {type: 'error', msg: 'Request could not be validated.'});
                });
            },
            updateProfile() {
                this.$v.$touch();
                if (!this.$v.$invalid) {
                    this.isLoading = true;
                    axios.put('/api/users/profile-details', this.formData).then(resp => {
                        this.$store.commit('setstatusMsg', {type: 'success', msg: 'Profile details updated.'});
                    }).catch(err => {
                        this.isLoading = false;
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
