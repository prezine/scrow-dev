<template>
    <!-- New Transaction -->
    <div class="element-box hide" id="tab_create_transaction">
        <div class="row">
            <div class="col-lg-2">&nbsp;</div>
            <div class="col-lg-8">
                <div class="element-wrapper">
                    <h6 class="element-header">Create New Transaction</h6>
                    <form @submit.prevent="createTransaction">
                        <div class="form-group">
                            <label for=""> Customer Name </label>
                            <input class="form-control" v-model.trim="$v.formData.customer.name.$model"
                                   placeholder="Enter customer name" type="text"
                                   :class="{'is-invalid': $v.formData.customer.name.$error}">
                            <div class="invalid-feedback" v-if="!$v.formData.customer.name.required">enter customer
                                name
                            </div>
                        </div>
                        <div class="form-group">
                            <label for=""> Customer Email address</label>
                            <input class="form-control" placeholder="Enter customer email" type="email"
                                   v-model.trim="$v.formData.customer.email.$model"
                                   :class="{'is-invalid': $v.formData.customer.email.$error}">
                            <div class="invalid-feedback" v-if="!$v.formData.customer.email.required">enter customer
                                email address
                            </div>
                        </div>
                        <div class="form-group">
                            <label for=""> Customer Home address</label>
                            <input class="form-control" placeholder="Enter customer home address" type="text"
                                   v-model.trim="$v.formData.customer.address.$model"
                                   :class="{'is-invalid': $v.formData.customer.address.$error}">
                            <div class="invalid-feedback" v-if="!$v.formData.customer.address.required">provide customer
                                address
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-sm-6">
                                <div class="form-group">
                                    <label for=""> Customer Phone </label>
                                    <input class="form-control" placeholder="Enter customer phone" type="tel"
                                           v-model.trim="$v.formData.customer.phone.$model"
                                           :class="{'is-invalid': $v.formData.customer.phone.$error}">
                                    <div class="invalid-feedback" v-if="!$v.formData.customer.phone.required">enter
                                        customer phone number
                                    </div>
                                </div>
                            </div>
                            <div class="col-sm-6">
                                <div class="form-group">
                                    <label for="">Customer Gender</label>
                                    <select class="form-control" v-model.trim="$v.formData.customer.gender.$model"
                                            :class="{'is-invalid': $v.formData.customer.gender.$error}">
                                        <option value="" disabled selected>Select gender</option>
                                        <option value="Male">Male</option>
                                        <option value="Female">Female</option>
                                        <option value="Not sure">Not sure</option>
                                    </select>
                                    <div class="invalid-feedback" v-if="!$v.formData.customer.gender.required">provide
                                        customer gender
                                    </div>
                                </div>
                            </div>
                        </div>
                        <fieldset class="form-group">
                            <legend><span>Transaction Data</span></legend>
                            <div class="row">
                                <div class="col-sm-6">
                                    <div class="form-group">
                                        <label for=""> Name of Item</label>
                                        <input class="form-control" placeholder="Enter item name" type="text"
                                               v-model.trim="$v.formData.transaction.product_name.$model"
                                               :class="{'is-invalid': $v.formData.transaction.product_name.$error}">
                                        <div class="invalid-feedback"
                                             v-if="!$v.formData.transaction.product_name.required">name of item is
                                            required
                                        </div>
                                    </div>
                                </div>
                                <div class="col-sm-6">
                                    <div class="form-group">
                                        <label for="">Item Quantity</label>
                                        <input class="form-control" placeholder="Item Quantity" type="number"
                                               v-model.trim="$v.formData.transaction.product_quantity.$model"
                                               :class="{'is-invalid': $v.formData.transaction.product_quantity.$error}">
                                        <div class="invalid-feedback"
                                             v-if="!$v.formData.transaction.product_quantity.required">provide quantity
                                            of item
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-sm-6">
                                    <div class="form-group">
                                        <label for=""> Expected Delivery Date</label>
                                        <datetime type="date"
                                                  v-model.trim="$v.formData.transaction.delivery_date.$model"
                                                  :input-class="{'form-control': true, 'is-invalid': $v.formData.transaction.delivery_date.$error}"></datetime>
                                        <div class="invalid-feedback"
                                             v-if="!$v.formData.transaction.delivery_date.required">provide deliver
                                            date
                                        </div>
                                    </div>
                                </div>
                                <div class="col-sm-6">
                                    <div class="form-group">
                                        <label for="">Currency</label>
                                        <select class="form-control"
                                                v-model.trim="$v.formData.transaction.currency.$model"
                                                :class="{'is-invalid': $v.formData.transaction.currency.$error}">
                                            <option>Select currency</option>
                                            <option>Nigerian Naira (NGN)</option>
                                            <option>U.S. Dollar (USD)</option>
                                            <option>European Euro (EUR)</option>
                                            <option>Japanese Yen (JPY)</option>
                                            <option>British Pound (GBP)</option>
                                            <option>Swiss Franc (CHF)</option>
                                            <option>Canadian Dollar (CAD)</option>
                                            <option>Australian/New Zealand Dollar</option>
                                            <option>South African Rand (ZAR)</option>
                                        </select>
                                        <div class="invalid-feedback"
                                             v-if="!$v.formData.transaction.currency.required">select currency to
                                            receive with
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for=""> Amount </label>
                                <money v-model.trim="$v.formData.transaction.amount.$model" v-bind="money"
                                       class="form-control" placeholder="Enter amount per item"
                                       :class="{'is-invalid': $v.formData.transaction.amount.$error}"></money>
                                <div class="invalid-feedback"
                                     v-if="!$v.formData.transaction.amount.required">enter amount
                                </div>
                            </div>
                            <div class="form-group">
                                <label> Terms of service </label>
                                <textarea class="form-control" rows="3"
                                          placeholder="We agreed that we'll send x item in gold color and x Ton by y day"
                                          v-model.trim="$v.formData.transaction.terms.$model"
                                          :class="{'is-invalid': $v.formData.transaction.terms.$error}"></textarea>
                                <div class="invalid-feedback"
                                     v-if="!$v.formData.transaction.terms.required">enter terms and condition
                                </div>
                            </div>
                        </fieldset>
                        <div class="form-buttons-w">
                            <button class="btn btn-primary" type="submit" :disabled="isLoading"> Create New
                                Transaction
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {required, email} from 'vuelidate/lib/validators';
    import {Money} from 'v-money';
    import {non400ErrorMsg} from "../../../utils/utils";

    export default {
        name: "NewTransaction",
        props: ['business_id'],
        components: {Money},
        data() {
            return {
                isLoading: false,
                money: {
                    decimal: '.',
                    thousands: ',',
                    prefix: '',
                    suffix: '',
                    precision: 2,
                    masked: false
                },
                formData: {
                    customer: {
                        name: '',
                        email: '',
                        address: '',
                        phone: '',
                        gender: ''
                    },
                    transaction: {
                        product_name: '',
                        product_quantity: '',
                        delivery_date: '',
                        currency: '',
                        amount: 0,
                        terms: ''
                    }
                }
            }
        },
        validations: {
            formData: {
                customer: {
                    name: {
                        required
                    },
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
                    gender: {
                        required
                    }
                },
                transaction: {
                    product_name: {
                        required
                    },
                    product_quantity: {
                        required
                    },
                    delivery_date: {
                        required
                    },
                    currency: {
                        required
                    },
                    amount: {
                        required
                    },
                    terms: {
                        required
                    }
                }
            }
        },
        methods: {
            createTransaction() {
                this.$v.$touch();
                if (!this.$v.$invalid) {
                    this.isLoading = true;
                    axios.post('/transactions/new', this.formData).then(resp => {
                        location.reload();
                    }).catch(err => {
                        this.isLoading = false;
                        if (err.response.status === 400) {
                            if (err.response.data.non_field_errors) {
                                this.$store.commit('setstatusMsg', {
                                    type: 'warning',
                                    msg: err.response.data.non_field_errors[0]
                                });
                            } else {
                                this.$store.commit('setstatusMsg', {
                                    type: 'warning',
                                    msg: 'Please fill in all fields.'
                                });
                            }
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
