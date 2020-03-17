<template>
    <div>
        <div class="form-group" v-if="!verificationDetails.cac_verified">
            <label for="cac"> Upload CAC</label>
            <div>
                <a :href="verificationDetails.cac_cert" v-show="verificationDetails.cac_cert" class="btn btn-link">{{verificationDetails.cac_cert}}</a>
            </div>
            <input type="file" class="form-control" @change="cacFileChange" id="cac"
                   accept="application/pdf,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.wordprocessingml.document, application/msword">
        </div>
        <div class="form-group" v-if="!verificationDetails.tax_doc_verified">
            <label for="tax"> Upload TAX Document</label>
            <div>
                <a :href="verificationDetails.tax_doc" v-show="verificationDetails.tax_doc" class="btn btn-link">{{verificationDetails.tax_doc}}</a>
            </div>
            <input type="file" class="form-control" @change="taxFileChange" id="tax"
                   accept="application/pdf,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.wordprocessingml.document, application/msword">
        </div>
        <div class="form-group" v-if="!verificationDetails.personal_id_verified">
            <label for="personal_id"> Personal ID(National ID, International Passport ...)</label>
            <div>
                <a :href="verificationDetails.personal_id" v-show="verificationDetails.personal_id" class="btn btn-link">{{verificationDetails.personal_id}}</a>
            </div>
            <input type="file" class="form-control" @change="personalIdFileChange" id="personal_id"
                   accept="application/pdf,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.wordprocessingml.document, application/msword">
        </div>
    </div>
</template>

<script>
    import {fileHandler} from '../../utils';

    export default {
        props: {
            business_id: {
                type: String,
                required: true
            }
        },
        name: "VerifyDetails",
        data() {
            return {
                isLoading: false,
                extensions: [
                    'application/pdf',
                    'application/vnd.ms-excel',
                    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                    'application/msword'
                ],
                verificationDetails: {}
            }
        },
        created() {
            this.getVerificationDetails();
        },
        methods: {
            async cacFileChange(e) {
                let files = e.target.files || e.dataTransfer.files;
                if (!files.length) {
                    return;
                }

                let file = files[0];
                this.isLoading = true;

                try {
                    await fileHandler(file, this.extensions);
                } catch (err) {
                    this.isLoading = false;
                    return this.$store.commit('setstatusMsg', {type: 'warning', msg: err});
                }

                let formData = new FormData();
                let businessId = parseInt(this.business_id);

                formData.append('cac_cert', file);
                formData.append('business', businessId);
                this.uploadFile(formData);
            },
            async taxFileChange(e) {
                let files = e.target.files || e.dataTransfer.files;
                if (!files.length) {
                    return;
                }

                let file = files[0];
                this.isLoading = true;

                try {
                    await fileHandler(file, this.extensions);
                } catch (err) {
                    this.isLoading = false;
                    return this.$store.commit('setstatusMsg', {type: 'warning', msg: err});
                }

                let formData = new FormData();
                let businessId = parseInt(this.business_id);

                formData.append('tax_doc', file);
                formData.append('business', businessId);
                this.uploadFile(formData);
            },
            async personalIdFileChange(e) {
                let files = e.target.files || e.dataTransfer.files;
                if (!files.length) {
                    return;
                }

                let file = files[0];
                this.isLoading = true;

                try {
                    await fileHandler(file, this.extensions);
                } catch (err) {
                    this.isLoading = false;
                    return this.$store.commit('setstatusMsg', {type: 'warning', msg: err});
                }

                let formData = new FormData();
                let businessId = parseInt(this.business_id);

                formData.append('personal_id', file);
                formData.append('business', businessId);
                this.uploadFile(formData);
            },
            uploadFile(formData) {
                axios.post('/business/documents-upload', formData)
                    .then((resp) => {
                        this.isLoading = false;
                        this.$store.commit('setstatusMsg', {type: 'success', msg: 'Upload successful'});
                        setTimeout(() => {
                            location.reload();
                        }, 3000)
                    })
                    .catch((err) => {
                        this.isLoading = false;
                        this.$store.commit('setstatusMsg', {type: 'warning', msg: 'Request could not be completed'});
                    });
            },
            getVerificationDetails() {
                axios.get('/business/verification_details').then(resp => {
                    this.verificationDetails = resp.data;
                }).catch(err => {
                    this.$store.commit('setstatusMsg', {type: 'warning', msg: 'Request could not be completed'});
                });
            }
        }
    }
</script>

<style scoped>

</style>
