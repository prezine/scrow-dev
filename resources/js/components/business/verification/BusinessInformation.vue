<template>
    <form @submit.prevent="updateSettings">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="profileLabel">Business Information</h5>
                <button aria-label="Close" class="close" data-dismiss="modal" type="button">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body text-left">
                <div class="row">
                    <div class="col-sm-12 col-md-7">
                        <div class="form-group">
                            <label>What does @businessname do?</label>
                            <textarea
                                    class="form-control"
                                    rows="3"
                                    v-model.trim="$v.formData.description.$model"
                                    :class="{'is-invalid': formErrors.description || $v.formData.description.$error}"
                            ></textarea>
                            <span
                                    class="hint"
                            >Please enter a detailed description of the goods and services your business provides.</span>
                            <div
                                    class="invalid-feedback"
                                    v-if="!$v.formData.description.required"
                            >Please tell us about your business
                            </div>
                            <div class="invalid-feedback" v-if="formErrors.description">{{formErrors.description[0]}}
                            </div>
                        </div>
                        <div class="form-group">
                            <label for>Business Email</label>
                            <input
                                    class="form-control"
                                    placeholder="Enter business email"
                                    type="email"
                                    :class="{'is-invalid': formErrors.email || $v.formData.email.$error}"
                                    v-model.trim="$v.formData.email.$model"
                            />
                            <span
                                    class="hint"
                            >This is the primary contact email for your business. Transaction notifications go to this email.</span>
                            <div
                                    class="invalid-feedback"
                                    v-if="!$v.formData.email.required"
                            >Please enter your email address
                            </div>
                            <div class="invalid-feedback" v-if="formErrors.email">{{formErrors.email[0]}}</div>
                        </div>
                        <div class="form-group">
                            <label for>Business Phone</label>
                            <input
                                    class="form-control"
                                    placeholder="Enter business phone number"
                                    type="tel"
                                    :class="{'is-invalid': formErrors.phone || $v.formData.phone.$error}"
                                    v-model.trim="$v.formData.phone.$model"
                            />
                            <div
                                    class="invalid-feedback"
                                    v-if="!$v.formData.phone.required"
                            >Please provide your business phone number
                            </div>
                            <div class="invalid-feedback" v-if="formErrors.phone">{{formErrors.phone[0]}}</div>
                        </div>
                        <div class="form-group">
                            <label for>Physical Address of the Business</label>
                            <vue-google-autocomplete
                                    id="map"
                                    v-model="formData.address"
                                    :classname="locationStyleClass"
                                    placeholder="Enter your location"
                                    v-on:placechanged="getAddressData"
                            ></vue-google-autocomplete>
                            <div
                                    class="invalid-feedback"
                                    v-if="!$v.formData.address.required"
                            >Please enter address
                            </div>
                            <div class="invalid-feedback" v-if="formErrors.address">{{formErrors.address[0]}}</div>
                        </div>
                    </div>
                    <div class="col-sm-12 col-md-5">
                        <div class="form-group">
                            <label for>Business Logo</label>
                            <div class="form-group pb-2">
                                <input
                                        class="form-control"
                                        placeholder
                                        type="file"
                                        @change="photoFileChange"
                                        accept="image/*"
                                />
                            </div>
                        </div>
                        <div class="form-group">
                            <label for>Business Website link</label>
                            <div class="form-group pb-2">
                                <input
                                        class="form-control"
                                        placeholder="https://circlepanda.io/"
                                        type="text"
                                        v-model="formData.website"
                                />
                            </div>
                        </div>
                        <div class="form-group">
                            <label for>Business Social Media</label>
                            <span class="hint">Where can we find your business on the internet</span>
                            <div class="input-group pb-2">
                                <div class="input-group-prepend">
                                    <div class="input-group-text socialtag">Facebook</div>
                                </div>
                                <input
                                        class="form-control"
                                        placeholder="https://web.facebook.com/teamcirclepanda/"
                                        type="text"
                                        v-model="formData.facebook_username"
                                />
                            </div>
                            <div class="input-group pb-2">
                                <div class="input-group-prepend">
                                    <div class="input-group-text socialtag">Twitter</div>
                                </div>
                                <input
                                        class="form-control"
                                        placeholder="https://twitter.com/Circlepandaa"
                                        type="text"
                                        v-model="formData.twitter_username"
                                />
                            </div>
                            <div class="input-group pb-2">
                                <div class="input-group-prepend">
                                    <div class="input-group-text socialtag">Instagram</div>
                                </div>
                                <input
                                        class="form-control"
                                        placeholder="https://www.instagram.com/circlepandaa/"
                                        type="text"
                                        v-model="formData.instagram_username"
                                />
                            </div>
                            <div class="input-group pb-2">
                                <div class="input-group-prepend">
                                    <div class="input-group-text socialtag">Linkedin</div>
                                </div>
                                <input
                                        class="form-control"
                                        placeholder="https://www.linkedin.com/company/circlepanda/"
                                        type="text"
                                        v-model="formData.linkedin_username"
                                />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" data-dismiss="modal" type="button">Close</button>
                <button class="btn btn-primary" type="submit" :disabled="isLoading">Save changes</button>
            </div>
        </div>
    </form>
</template>
<script>
    import {required, email} from "vuelidate/lib/validators";
    import VueGoogleAutocomplete from "vue-google-autocomplete";
    import {fileHandler, formErrorHandler, non400ErrorMsg} from "../../../utils/utils";

    export default {
        components: {
            VueGoogleAutocomplete
        },
        data() {
            return {
                isLoading: false,
                formErrors: [],
                formData: {
                    email: "",
                    phone: "",
                    description: "",
                    address: "",
                    website: "",
                    instagram_username: "",
                    linkedin_username: "",
                    facebook_username: "",
                    twitter_username: ""
                }
            };
        },
        validations: {
            formData: {
                email: {
                    required,
                    email
                },
                phone: {
                    required
                },
                description: {
                    required
                },
                address: {
                    required
                }
            }
        },
        created() {
            this.getSettings();
        },
        computed: {
            locationStyleClass() {
                let className = "form-control";

                if (this.formErrors.address || this.$v.formData.address.$error) {
                    className += " is-invalid";
                }

                return className;
            }
        },
        methods: {
            getAddressData: function (addressData, placeResultData, id) {
                this.formData.address = placeResultData.formatted_address;
            },
            getSettings() {
                axios
                    .get("/business/details")
                    .then(resp => {
                        const {
                            phone,
                            description,
                            email,
                            address,
                            website,
                            twitter_username,
                            facebook_username,
                            linkedin_username,
                            instagram_username
                        } = resp.data;

                        this.formData = {
                            phone,
                            description,
                            email,
                            address,
                            website: website === 'null' ? '' : website,
                            twitter_username: twitter_username === 'null' ? '' : twitter_username,
                            facebook_username: facebook_username === 'null' ? '' : facebook_username,
                            linkedin_username: linkedin_username === 'null' ? '' : linkedin_username,
                            instagram_username: instagram_username === 'null' ? '' : instagram_username
                        };
                    })
                    .catch(err => {
                        this.$store.commit("setstatusMsg", {
                            type: "error",
                            msg: "Request could not be validated."
                        });
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

                    axios
                        .put("/business/details", formData)
                        .then(resp => {
                            this.$store.commit("setstatusMsg", {
                                type: "success",
                                msg: "Profile details updated."
                            });
                            setTimeout(() => {
                                location.reload();
                            }, 4000);
                        })
                        .catch(err => {
                            this.isLoading = false;
                            if (err.response.status === 400) {
                                formErrorHandler(err.response.data, this);
                            } else {
                                non400ErrorMsg(this);
                            }
                        });
                }
            },
            async photoFileChange(e) {
                let files = e.target.files || e.dataTransfer.files;
                if (!files.length) {
                    return;
                }

                let file = files[0];
                this.isLoading = true;

                let extensions = ["image/png", "image/gif", "image/jpeg", "image/jpg"];
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
    };
</script>
<style scoped>
</style>
