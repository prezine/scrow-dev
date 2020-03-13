<template>
    <div>
        <h3>Business Registration</h3>
        <form @submit.prevent="createBusiness">
            <div v-if="errorResponse">{{errorResponse}}</div>
            <div v-if="successResponse">{{successResponse}}</div>
            <div class="form-group">
                <input type="text" v-model.trim="$v.formData.name.$model" class="form-control"
                       placeholder="Business Name">
                <div class="error" v-if="!$v.formData.name.required">Enter business name</div>
            </div>
            <div class="form-group">
                <input type="email" v-model.trim="$v.formData.email.$model" class="form-control" placeholder="Email">
                <div class="error" v-if="!$v.formData.email.required">Enter email address</div>
                <div class="error" v-if="!$v.formData.email.email">Enter a valid email address</div>
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
                <input type="text" v-model.trim="$v.formData.category.$model" class="form-control"
                       placeholder="Category">
                <div class="error" v-if="!$v.formData.category.required">Category is required</div>
            </div>
            <div class="form-group">
                <input type="text" v-model.trim="$v.formData.sub_category.$model" class="form-control"
                       placeholder="Sub Category">
                <div class="error" v-if="!$v.formData.sub_category.required">Sub Category is required</div>
            </div>
            <div class="form-group">
                <input type="text" v-model="formData.website" class="form-control"
                       placeholder="Website Link">
            </div>
            <div class="form-group">
                <select v-model.trim="$v.formData.business_type.$model" class="form-control">
                    <option value="" disabled selected>Select Business Type</option>
                    <option value="Startup">Startup</option>
                    <option value="Running">Running</option>
                </select>
                <div class="error" v-if="!$v.formData.business_type.required">Enter your business type</div>
            </div>

            <div class="form-group">
                <button class="btn btn-primary" type="submit">Create Business</button>
            </div>
        </form>
    </div>
</template>

<script>
    import {required, email} from 'vuelidate/lib/validators';
    import { mapGetters } from 'vuex';
    export default {
        name: "BusinessRegistrationForm",
        data() {
            return {
                isLoading: false,
                formErrors: [],
                errorResponse: '',
                successResponse: '',
                formData: {
                    userId: '',
                    name: '',
                    email: '',
                    address: '',
                    city: '',
                    state: '',
                    country: '',
                    business_type: '',
                    category: '',
                    sub_category: ''
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
                country: {
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
                business_type: {
                    required
                },
                category: {
                    required
                },
                sub_category: {
                    required
                }
            }
        },
        computed: {
            ...mapGetters(['userCreated'])
        },
        mounted() {
            this.formData.userId = this.userCreated.userId;
        },
        methods: {
            createBusiness: function () {
                this.$v.$touch();
                if (!this.$v.$invalid) {
                    axios.post('/business/create', this.formData).then(resp => {
                        window.location = '/business/setup';
                    }).catch(err => {
                        console.log(err.response);
                        if (err.response.statusCode === 400) {
                            if (err.response.data) {
                                console.log(err.response.data)
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
