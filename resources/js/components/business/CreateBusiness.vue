<template>
    <div class="element-box">
        <form @submit.prevent="createBusiness">
            <h5 class="form-header">My Business</h5>
            <div class="form-group">
                <label for=""> Business Name </label>
                <input class="form-control" placeholder="Enter business name" type="text"
                       v-model.trim="$v.formData.name.$model"
                       :class="{'is-invalid': formErrors.name || $v.formData.name.$error}">
                <div class="invalid-feedback" v-if="!$v.formData.name.required">Enter business name</div>
                <div class="invalid-feedback" v-if="formErrors.name">{{formErrors.name[0]}}</div>
            </div>
            <div class="form-group">
                <label for=""> Business Email</label>
                <input class="form-control" placeholder="Enter business email" type="email"
                       v-model.trim="$v.formData.email.$model"
                       :class="{'is-invalid': formErrors.email || $v.formData.email.$error}">
                <div class="invalid-feedback" v-if="!$v.formData.email.required">Enter business email address</div>
                <div class="invalid-feedback" v-if="formErrors.email">{{formErrors.email[0]}}</div>
            </div>
            <div class="row">
                <div class="col-sm-4">
                    <div class="form-group">
                        <label for=""> Business Phone </label>
                        <input class="form-control" maxlength="5" placeholder="Phone Code" type="text"
                               v-model.trim="$v.formData.calling_code.$model"
                               :class="{'is-invalid': formErrors.calling_code || $v.formData.calling_code.$error}">
                        <div class="invalid-feedback" v-if="!$v.formData.calling_code.required">Enter your calling
                            code
                        </div>
                        <div class="invalid-feedback" v-if="formErrors.calling_code">{{formErrors.calling_code[0]}}
                        </div>
                    </div>
                </div>
                <div class="col-sm-8">
                    <div class="form-group">
                        <label for="">&nbsp;</label>
                        <input class="form-control" placeholder="Phone Number" type="tel"
                               v-model.trim="$v.formData.phone.$model"
                               :class="{'is-invalid': formErrors.phone || $v.formData.phone.$error}">
                        <div class="invalid-feedback" v-if="!$v.formData.phone.required">Enter business phone number
                        </div>
                        <div class="invalid-feedback" v-if="formErrors.phone">{{formErrors.phone[0]}}</div>
                    </div>
                </div>
            </div>
            <div class="form-group">
                <label for=""> Business Address</label>
                <vue-google-autocomplete
                        id="map"
                        :classname="addressStyleClass"
                        placeholder="Enter your address"
                        v-on:placechanged="getAddressData">
                </vue-google-autocomplete>
                <div class="invalid-feedback" v-if="!$v.formData.address.required">Enter business address</div>
                <div class="invalid-feedback" v-if="formErrors.address">{{formErrors.address[0]}}</div>
                <div id="map"></div>
            </div>
            <div class="form-group">
                <label> About Business </label>
                <textarea class="form-control" rows="3" maxlength="150" v-model.trim="$v.formData.about.$model"
                          :class="{'is-invalid': formErrors.about || $v.formData.about.$error}"></textarea>
                <div class="invalid-feedback" v-if="!$v.formData.about.required">Tell us about your business</div>
                <div class="invalid-feedback" v-if="formErrors.about">{{formErrors.about[0]}}</div>
            </div>
            <div class="form-group">
                <select class="form-control" v-model.trim="$v.formData.business_type.$model"
                        :class="{'is-invalid': formErrors.business_type || $v.formData.business_type.$error}">
                    <option value="" disabled selected>Select Business Type</option>
                    <option value="Startup">Startup</option>
                    <option value="Running">Running</option>
                </select>
                <div class="invalid-feedback" v-if="!$v.formData.business_type.required">Select your business type</div>
                <div class="invalid-feedback" v-if="formErrors.business_type">{{formErrors.business_type[0]}}</div>
            </div>
            <fieldset class="form-group">
                <legend><span>Business Social Handles</span></legend>
                <div class="row">
                    <div class="col-sm-6">
                        <div class="form-group">
                            <label for="">Instagram URL</label>
                            <div class="input-group">
                                <div class="input-group-prepend">
                                    <div class="input-group-text">@</div>
                                </div>
                                <input class="form-control" placeholder="https://www.instagram.com/xyz/" type="text">
                            </div>
                            <div class="invalid-feedback" v-if="formErrors.instagram_username">
                                {{formErrors.instagram_username[0]}}
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-6">
                        <div class="form-group">
                            <label for="">Twitter URL</label>
                            <div class="input-group">
                                <div class="input-group-prepend">
                                    <div class="input-group-text">@</div>
                                </div>
                                <input class="form-control" placeholder="https://twitter.com/xyz" type="text">
                            </div>
                            <div class="invalid-feedback" v-if="formErrors.twitter_username">
                                {{formErrors.twitter_username[0]}}
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-sm-6">
                        <div class="form-group">
                            <label for="">Linkedin URL</label>
                            <div class="input-group">
                                <div class="input-group-prepend">
                                    <div class="input-group-text">@</div>
                                </div>
                                <input class="form-control" placeholder="https://linkedin.com/in/xyz" type="text">
                            </div>
                            <div class="invalid-feedback" v-if="formErrors.linkedin_username">
                                {{formErrors.linkedin_username[0]}}
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-6">
                        <div class="form-group">
                            <label for="">Website (optional)</label>
                            <div class="input-group">
                                <div class="input-group-prepend">
                                    <div class="input-group-text">@</div>
                                </div>
                                <input class="form-control" placeholder="https://xyz.com/" type="text">
                            </div>
                            <div class="invalid-feedback" v-if="formErrors.website_username">
                                {{formErrors.website_username[0]}}
                            </div>
                        </div>
                    </div>
                </div>
            </fieldset>
            <div>
                On submitting you've agreed to our <a href="#">terms and conditions</a>
            </div>
            <div class="form-buttons-w">
                <button class="btn btn-primary" type="submit" :disabled="isLoading"> Create a business</button>
                <a href="./" class="btn btn-grey"> Skip </a>
            </div>
        </form>
    </div>
</template>

<script>
    import {required, email} from 'vuelidate/lib/validators';
    import VueGoogleAutocomplete from 'vue-google-autocomplete';
    import {formErrorHandler, non400ErrorMsg} from "../../utils/utils";

    export default {
        name: "RegisterBusiness",
        props: ['user_id'],
        components: {
            VueGoogleAutocomplete
        },
        data() {
            return {
                isLoading: false,
                formErrors: [],
                formData: {
                    userId: '',
                    name: '',
                    email: '',
                    calling_code: '',
                    phone: '',
                    about: '',
                    address: '',
                    business_type: '',
                    website: '',
                    instagram_username: '',
                    linkedin_username: '',
                    twitter_username: ''
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
                about: {
                    required
                },
                address: {
                    required
                },
                business_type: {
                    required
                }
            }
        },
        created() {
            let user_id = parseInt(this.user_id);
            if (this.user_id && !isNaN(user_id)) {
                this.formData.userId = user_id;
            }
        },
        computed: {
            addressStyleClass() {
                let className = 'form-control';

                if (this.formErrors.address || this.$v.formData.address.$error) {
                    className += ' is-invalid';
                }

                return className;
            }
        },
        methods: {
            getAddressData: function (addressData, placeResultData, id) {
                this.formData.address = placeResultData.formatted_address;
            },
            createBusiness: function () {
                this.$v.$touch();
                if (!this.$v.$invalid) {
                    this.isLoading = true;
                    axios.post('/business/create', this.formData).then(resp => {
                        window.location = '/dashboard';
                    }).catch(err => {
                        this.isLoading = false;
                        if (err.response.status === 400) {
                            formErrorHandler(err.response.data, this);
                        } else {
                            non400ErrorMsg(this);
                        }
                    });
                }
            }
        }
    }
</script>

<style scoped>

</style>
