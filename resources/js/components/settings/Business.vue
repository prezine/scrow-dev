<template>
    <div class="element-box hide" id="tab_business">
        <form @submit.prevent="updateSettings">
            <h6 class="form-header text-center" style="font-weight: 600">Your Business</h6>
            <div class="row">
                <div class="col-sm-3">
                    <div class="form-group">
                        <label for="currency"> Default Currency</label>
                        <select class="form-control"
                                :class="{'is-invalid': formErrors.currency || $v.formData.currency.$error}"
                                id="currency" v-model.trim="$v.formData.currency.$model">
                            <option value="NGN" :selected="formData.currency === 'NGN'">NG</option>
                            <option value="USD" :selected="formData.currency === 'USD'">USD</option>
                        </select>
                        <div class="invalid-feedback" v-if="!$v.formData.currency.required">Please select currency</div>
                        <div class="invalid-feedback" v-if="formErrors.currency">{{formErrors.currency[0]}}
                        </div>
                    </div>
                </div>
                <div class="col-sm-9">
                    <div class="form-group">
                        <label for="email"> Business Contact Email</label>
                        <input id="email" class="form-control"
                               :class="{'is-invalid': formErrors.email || $v.formData.email.$error}"
                               v-model.trim="$v.formData.email.$model"
                               placeholder="Your Business Email Address" type="email">
                        <div class="invalid-feedback" v-if="!$v.formData.email.required">Please provide contact email
                            address
                        </div>
                        <div class="invalid-feedback" v-if="!$v.formData.email.email">Please provide a valid contact
                            email
                            address
                        </div>
                        <div class="invalid-feedback" v-if="formErrors.email">{{formErrors.email[0]}}
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-6">
                    <div class="form-group">
                        <label for="support_email"> Business Support Email</label>
                        <input id="support_email" class="form-control"
                               :class="{'is-invalid': formErrors.support_email || $v.formData.support_email.$error}"
                               v-model.trim="$v.formData.support_email.$model"
                               placeholder="Your Support Email Address" type="email">
                        <div class="invalid-feedback" v-if="!$v.formData.support_email.required">enter support email
                        </div>
                        <div class="invalid-feedback" v-if="!$v.formData.support_email.email">enter a valid support
                            email
                        </div>
                        <div class="invalid-feedback" v-if="formErrors.support_email">{{formErrors.support_email[0]}}
                        </div>
                    </div>
                </div>
                <div class="col-sm-6">
                    <div class="form-group">
                        <label for="chargeback_email"> Business Chargeback Email</label>
                        <input id="chargeback_email" class="form-control"
                               :class="{'is-invalid': formErrors.chargeback_email || $v.formData.chargeback_email.$error}"
                               v-model.trim="$v.formData.chargeback_email.$model"
                               placeholder="Your Chargeback Email Address" type="email">
                        <div class="invalid-feedback" v-if="!$v.formData.chargeback_email.required">enter chargeback
                            email
                        </div>
                        <div class="invalid-feedback" v-if="!$v.formData.chargeback_email.email">enter a valid
                            chargeback email
                        </div>
                        <div class="invalid-feedback" v-if="formErrors.chargeback_email">
                            {{formErrors.chargeback_email[0]}}
                        </div>
                    </div>
                </div>
            </div>
            <div class="form-group">
                <label for="name"> Business Name</label>
                <input id="name" class="form-control"
                       placeholder="Your Business Name"
                       readonly="readonly" :value="formData.name" type="text">
            </div>
            <div class="form-group">
                <label for="phone">Business Phone Number</label>
                <div class="input-group">
                    <div class="input-group-prepend">
                        <div class="input-group-text" style="padding: 0 25px;font-weight: 600">
                            +234
                        </div>
                    </div>
                    <input id="phone" v-model.trim="$v.formData.phone.$model" class="form-control"
                           :class="{'is-invalid': formErrors.phone || $v.formData.phone.$error}"
                           placeholder="817 123 4567" type="tel">
                </div>
                <div class="invalid-feedback" v-if="!$v.formData.phone.required">Please enter phone number</div>
                <div class="invalid-feedback" v-if="formErrors.phone">{{formErrors.phone[0]}}
                </div>
            </div>
            <div class="row">
                <div class="col-sm-6">
                    <div class="form-group">
                        <label> Business Address</label>
                        <vue-google-autocomplete
                                id="map"
                                v-model="formData.address"
                                :classname="locationStyleClass"
                                placeholder="Enter your location"
                                v-on:placechanged="getAddressData"
                        >
                        </vue-google-autocomplete>
                        <div class="invalid-feedback" v-if="!$v.formData.address.required">Please enter address</div>
                        <div class="invalid-feedback" v-if="formErrors.address">{{formErrors.address[0]}}
                        </div>
                    </div>
                </div>
                <div class="col-sm-6">
                    <div class="form-group">
                        <label for="website">Business Website</label>
                        <input id="website" class="form-control" v-model="formData.website"
                               placeholder="Your Business Website" type="text">
                    </div>
                </div>
            </div>
            <div class="form-group">
                <label for="photo">Business Logo</label>
                <input id="photo" class="form-control" @change="photoFileChange"
                       placeholder="Your Business Website" type="file" accept="image/*">
            </div>
            <fieldset class="form-group">
                <legend><span>Social Media</span></legend>
                <div class="row">
                    <div class="col-sm-6">
                        <div class="form-group">
                            <label for="instagram_username">Instagram Username</label>
                            <div class="input-group">
                                <div class="input-group-prepend">
                                    <div class="input-group-text">@</div>
                                </div>
                                <input id="instagram_username" v-model="formData.instagram_username"
                                       class="form-control"
                                       placeholder="Instagram username"
                                       type="text">
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-6">
                        <div class="form-group">
                            <label for="twitter_username">Twitter Username</label>
                            <div class="input-group">
                                <div class="input-group-prepend">
                                    <div class="input-group-text">@</div>
                                </div>
                                <input id="twitter_username" v-model="formData.twitter_username" class="form-control"
                                       placeholder="Twitter username"
                                       type="text">
                            </div>
                        </div>
                    </div>
                </div>
            </fieldset>
            <div class="form-buttons-w" align="center">
                <button class="mr-2 mb-2 btn btn-outline-success" type="submit" :disabled="isLoading"> Save Changes
                </button>
            </div>
        </form>
    </div>
</template>

<script>
    import {required, email} from 'vuelidate/lib/validators';
    import VueGoogleAutocomplete from 'vue-google-autocomplete';
    import {fileHandler, formErrorHandler, non400ErrorMsg} from "../../utils/utils";

    export default {
        name: "Business",
        components: {
            VueGoogleAutocomplete
        },
        data() {
            return {
                formErrors: [],
                isLoading: false,
                formData: {
                    calling_code: '',
                    name: '',
                    phone: '',
                    email: '',
                    address: '',
                    currency: '',
                    website: '',
                    support_email: '',
                    chargeback_email: '',
                    twitter_username: '',
                    instagram_username: ''
                }
            }
        },
        validations: {
            formData: {
                email: {
                    required,
                    email
                },
                address: {
                    required
                },
                phone: {
                    required
                },
                currency: {
                    required
                },
                support_email: {
                    required,
                    email
                },
                chargeback_email: {
                    required,
                    email
                }
            }
        },
        created() {
            this.getSettings();
        },
        computed: {
            locationStyleClass() {
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
            getSettings() {
                axios.get('/business/details').then(resp => {
                    const {
                        name,
                        calling_code,
                        phone,
                        email,
                        address,
                        currency,
                        website,
                        support_email,
                        chargeback_email,
                        twitter_username,
                        instagram_username
                    } = resp.data;
                    this.formData = {
                        name,
                        calling_code,
                        phone,
                        email,
                        address,
                        currency,
                        support_email,
                        chargeback_email,
                        website: website === 'null' ? '' : website,
                        twitter_username: twitter_username === 'null' ? '' : twitter_username,
                        instagram_username: instagram_username === 'null' ? '' : instagram_username
                    };
                }).catch(err => {
                    this.$store.commit('setstatusMsg', {type: 'error', msg: 'Request could not be validated.'});
                });
            },
            updateSettings() {
                this.$v.$touch();
                if (!this.$v.$invalid) {
                    this.isLoading = true;
                    let formData = new FormData();
                    let formDataKeys = Object.keys(this.formData);
                    let formDataValues = Object.values(this.formData);

                    formDataKeys.map((key, index) => {
                        formData.append(key, formDataValues[index]);
                    });

                    axios.put('/business/details', formData).then(resp => {
                        this.$store.commit('setstatusMsg', {type: 'success', msg: 'Profile details updated.'});
                        setTimeout(() => {
                            location.reload();
                        }, 4000)
                    }).catch(err => {
                        this.isLoading = false;
                        if (err.response.status === 400) {
                            formErrorHandler(err.response.data, this);
                        } else {
                            non400ErrorMsg(this);
                        }
                    })
                }

            },
            async photoFileChange(e) {
                let files = e.target.files || e.dataTransfer.files;
                if (!files.length) {
                    return;
                }

                let file = files[0];
                this.isLoading = true;

                let extensions = ['image/png', 'image/gif', 'image/jpeg', 'image/jpg'];
                try {
                    await fileHandler(file, extensions);
                } catch (err) {
                    this.isLoading = false;
                    this.$store.commit('setstatusMsg', {type: 'error', msg: err});
                    return;
                }

                this.formData.photo = file;
            }
        }
    }
</script>

<style scoped>

</style>
