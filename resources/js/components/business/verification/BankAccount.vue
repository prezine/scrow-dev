<template>
    <div class="modal-content">
        <form @submit.prevent="saveBankDetails">
            <div class="modal-header">
                <h5 class="modal-title" id="profileLabel">Settlement Account</h5>
                <button aria-label="Close" class="close" data-dismiss="modal" type="button">
                    <span aria-hidden="true"> &times;</span></button>
            </div>
            <div class="modal-body text-left">
                <div class="alert alert-warning">
                    Please use a <strong>Corporate Bank Account</strong> that matches
                    the verification documents you’ve provided.
                </div>
                <div class="form-group">
                    <label for="">Bank Account</label>
                    <select class="form-control bank"
                            :class="{'is-invalid': formErrors.bank_name || $v.formData.bank_name.$error}"
                            v-model.trim="$v.formData.bank_name.$model">
                        <option value="" selected disabled>-- Choose --</option>
                        <option v-for="bank in banks" :value="bank">{{bank}}</option>
                    </select>
                    <div class="invalid-feedback" v-if="!$v.formData.bank_name.required">
                        Please enter your email address
                    </div>
                    <div class="invalid-feedback" v-if="formErrors.bank_name">{{formErrors.bank_name[0]}}</div>
                </div>
                <div class="form-group">
                    <label for=""> Corporate Bank Account Number </label>
                    <input class="form-control" placeholder="Account number" type="text"
                           :class="{'is-invalid': formErrors.account_number || $v.formData.account_number.$error}"
                           v-model.trim="$v.formData.account_number.$model">
                    <span class="hint">Enter your 10-digits bank account number</span>
                    <div class="invalid-feedback" v-if="!$v.formData.account_number.required">
                        Please enter your email address
                    </div>
                    <div class="invalid-feedback" v-if="formErrors.account_number">{{formErrors.account_number[0]}}
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" data-dismiss="modal" type="button">
                    Close
                </button>
                <button class="btn btn-primary" type="submit"> Save changes</button>
            </div>
        </form>
    </div>
</template>

<script>
    import {banks} from '../../../utils/bank';
    import {required, email} from "vuelidate/lib/validators";
    import {formErrorHandler, non400ErrorMsg} from "../../../utils/utils";

    export default {
        name: "BankAccount",
        data() {
            return {
                banks: banks(),
                isLoading: false,
                formErrors: [],
                formData: {
                    account_number: "",
                    bank_name: ""
                }
            }
        },
        validations: {
            formData: {
                account_number: {
                    required
                },
                bank_name: {
                    required
                }
            }
        },
        methods: {
            saveBankDetails() {
                this.$v.$touch();
                if (!this.$v.$invalid) {
                    this.isLoading = true;

                    axios.post("/finance/", this.formData)
                        .then(resp => {
                            this.$store.commit("setstatusMsg", {
                                type: "success",
                                msg: "Bank details updated."
                            });
                            setTimeout(() => {
                                location.reload();
                            }, 3000);
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
