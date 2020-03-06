<template>
    <div>
        <div>
            <div class="fileinput-exists">Upload CAC</div>
            <input type="file" @change="cacFileChange" accept="image/*">
        </div>
        <div>
            <div class="fileinput-exists">Upload TAX Document</div>
            <input type="file" @change="taxFileChange" accept="image/*">
        </div>
        <div>
            <div class="fileinput-exists">Personal ID(National ID, International Passport ...)</div>
            <input type="file" @change="personalIdFileChange" accept="image/*">
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
                errorResponse: ''
            }
        },
        methods: {
            async cacFileChange(e) {
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
                    return this.errorResponse = err;
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

                let extensions = ['image/png', 'image/gif', 'image/jpeg', 'image/jpg'];
                try {
                    await fileHandler(file, extensions);
                } catch (err) {
                    this.isLoading = false;
                    return this.errorResponse = err;
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

                let extensions = ['image/png', 'image/gif', 'image/jpeg', 'image/jpg'];
                try {
                    await fileHandler(file, extensions);
                } catch (err) {
                    this.isLoading = false;
                    return this.errorResponse = err;
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
                        this.errorResponse = resp.data.response;
                    })
                    .catch((err) => {
                        this.isLoading = false;
                        this.errorResponse = err.response.data.response;
                    });
            }
        }
    }
</script>

<style scoped>

</style>
