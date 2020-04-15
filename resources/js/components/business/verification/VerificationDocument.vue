<template>
    <div class="modal-content">
        <form @submit.prevent="saveVerificationDocument">
            <div class="modal-header">
                <h5 class="modal-title" id="profileLabel">Verification Documents</h5>
                <button aria-label="Close" class="close" data-dismiss="modal" type="button">
                    <span aria-hidden="true"> &times;</span></button>
            </div>
            <div class="modal-body text-left">

                <div class="form-group">
                    <label for=""> BVN </label>
                    <span class="hint">Please enter your Nigerian Bank Verification Number (BVN). If you don’t have a BVN, please contact your bank on how to proceed.</span>
                    <input class="form-control" placeholder="000000000000" type="tel"
                           v-model.trim="$v.formData.bvn.$model"
                           :class="{'is-invalid': formErrors.bvn || $v.formData.bvn.$error}">
                    <div class="invalid-feedback" v-if="!$v.formData.bvn.required">
                        Please provide your BVN
                    </div>
                    <div class="invalid-feedback" v-if="formErrors.bvn">
                        {{formErrors.bvn[0]}}
                    </div>
                </div>
                <div class="form-group">
                    <label for="">What registration document do you have?</label>
                    <select class="form-control" v-model.trim="$v.formData.document_type.$model"
                            @change="onSelectDocument"
                            :class="{'is-invalid': formErrors.document_type || $v.formData.document_type.$error}">
                        <option value="" selected disabled> -- Choose --</option>
                        <option value="RC Document">RC Document</option>
                        <option value="BN Document">BN Document</option>
                        <option value="NEPZA Document">NEPZA Document</option>
                        <option value="CAC IT Document">CAC IT Document</option>
                    </select>
                    <div class="invalid-feedback" v-if="!$v.formData.document_type.required">
                        Please provide your BVN
                    </div>
                    <div class="invalid-feedback" v-if="formErrors.document_type">
                        {{formErrors.document_type[0]}}
                    </div>
                </div>
                <div class="form-group pb-2" v-if="formData.document_type">
                    <label for=""> {{document_label}} </label>
                    <span class="hint" style="display: block">Attach the document in (*PDF, *DOCX, *DOC)</span>
                    <input class="form-control" placeholder type="file" @change="documentFileChange"
                           :accept="file_types"/>
                </div>
                <div class="form-group">
                    <div class="form-group">
                        <label for=""> Date Company Started </label>
                        <div class="date-input">
                            <datetime
                                    :input-class="{'form-control': true, 'is-invalid': formErrors.date_company_started || $v.formData.date_company_started.$error}"
                                    type="date"
                                    v-model.trim="$v.formData.date_company_started.$model"></datetime>
                        </div>
                        <span class="hint">This date should match the Date of Birth associated with your BVN.</span>
                        <div class="invalid-feedback" v-if="!$v.formData.date_company_started.required">
                            Please provide your BVN
                        </div>
                        <div class="invalid-feedback" v-if="formErrors.bvn">
                            {{formErrors.date_company_startedbvn[0]}}
                        </div>
                    </div>
                </div>

            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" data-dismiss="modal" type="button">
                    Close
                </button>
                <button class="btn btn-primary" type="submit" :disabled="!noEmptyFields || isLoading"> Save changes
                </button>
            </div>
        </form>
    </div>
</template>

<script>
    import {required, email} from "vuelidate/lib/validators";
    import {fileHandler, formErrorHandler, non400ErrorMsg} from "../../../utils/utils";

    export default {
        name: "VerificationDocument",
        props: ['business_id'],
        data() {
            return {
                file_types: 'application/pdf,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.wordprocessingml.document, application/msword',
                document_label: '',
                formErrors: [],
                isLoading: false,
                extensions: [
                    'application/pdf',
                    'application/vnd.ms-excel',
                    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                    'application/msword'
                ],
                formData: {
                    bvn: '',
                    document_type: '',
                    date_company_started: ''
                }
            }
        },
        validations: {
            formData: {
                bvn: {
                    required
                },
                document_type: {
                    required
                },
                date_company_started: {
                    required
                }
            }
        },
        computed: {
            noEmptyFields() {
                return !!(this.formData.bvn && this.formData.document_type && this.formData.date_company_started && this.formData.document);
            }
        },
        methods: {
            saveVerificationDocument() {
                this.$v.$touch();
                if (!this.$v.$invalid) {
                    this.isLoading = true;
                    let businessId = parseInt(this.business_id);
                    let formData = new FormData();
                    let formDataKeys = Object.keys(this.formData);
                    let formDataValues = Object.values(this.formData);

                    formDataKeys.map((key, index) => {
                        formData.append(key, formDataValues[index]);
                    });
                    formData.append('business', businessId);

                    axios.post('/business/documents-upload', formData)
                        .then((resp) => {
                            this.isLoading = false;
                            this.$store.commit('setstatusMsg', {type: 'success', msg: 'Upload successful'});
                            setTimeout(() => {
                                location.reload();
                            }, 3000);
                        })
                        .catch((err) => {
                            this.isLoading = false;
                            if (err.response.status === 400) {
                                formErrorHandler(err.response.data, this);
                            } else {
                                non400ErrorMsg(this);
                            }
                        });
                }
            },
            onSelectDocument() {
                if (this.formData.document_type) {
                    this.document_label = this.formData.document_type;
                }
            },
            async documentFileChange(e) {
                let files = e.target.files || e.dataTransfer.files;
                if (!files.length) {
                    return;
                }

                let file = files[0];

                try {
                    await fileHandler(file, this.extensions);
                } catch (err) {
                    this.$store.commit('setstatusMsg', {type: 'error', msg: err});
                    return;
                }

                this.formData.document = file;
            }
        }
    }
</script>

<style scoped>

</style>
