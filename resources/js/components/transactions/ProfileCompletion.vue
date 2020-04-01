<template>
    <div class="element-box-tp">
        <div class="fancy-progress-with-label">
            <div class="fpl-label">{{completionRecord.percentage}}%</div>
            <div class="fpl-progress-w">
                <div class="fpl-progress-i" :style="'width: '+completionRecord.percentage+'%;'"></div>
            </div>
        </div>
        <div class="todo-list">
            <a class="todo-item" :class="{'complete': completionRecord.personal_details}"
               :href="completionRecord.personal_details ? 'javascript:void(0)' : '/business/activate'">
                <div class="ti-info">
                    <div class="ti-header">Personal detail</div>
                    <div class="ti-sub-header">About yourself</div>
                </div>
                <div class="ti-icon">
                    <i class="os-icon"
                       :class="[{'os-icon-check': completionRecord.personal_details}, {'os-icon-arrow-right7': !completionRecord.personal_details}]"></i>
                </div>
            </a>
            <a class="todo-item" :class="{'complete': completionRecord.business_details}"
               :href="completionRecord.business_details ? 'javascript:void(0)' : '/business/activate'">
                <div class="ti-info">
                    <div class="ti-header">Business Information</div>
                    <div class="ti-sub-header">About your business</div>
                </div>
                <div class="ti-icon">
                    <i class="os-icon"
                       :class="[{'os-icon-check': completionRecord.business_details}, {'os-icon-arrow-right7': !completionRecord.business_details}]"></i>
                </div>
            </a>
            <a class="todo-item" :class="{'complete': completionRecord.verification_documents}"
               :href="completionRecord.verification_documents ? 'javascript:void(0)' : '/business/activate'">
                <div class="ti-info">
                    <div class="ti-header">Verification Documents</div>
                    <div class="ti-sub-header">Verify your BVN and Business Registration Doc</div>
                </div>
                <div class="ti-icon">
                    <i class="os-icon"
                       :class="[{'os-icon-check': completionRecord.verification_documents}, {'os-icon-arrow-right7': !completionRecord.verification_documents}]"></i>
                </div>
            </a>
            <a class="todo-item" :class="{'complete': completionRecord.settlement_account}"
               :href="completionRecord.settlement_account ? 'javascript:void(0)' : '/business/activate'">
                <div class="ti-info">
                    <div class="ti-header">Settlement Account</div>
                    <div class="ti-sub-header">Connect account through which you'll receive payment</div>
                </div>
                <div class="ti-icon">
                    <i class="os-icon"
                       :class="[{'os-icon-check': completionRecord.settlement_account}, {'os-icon-arrow-right7': !completionRecord.settlement_account}]"></i>
                </div>
            </a>
        </div>
    </div>
</template>

<script>
    export default {
        name: "ProfileCompletion",
        data() {
            return {
                completionRecord: {}
            }
        },
        created() {
            this.getProfileDetails();
        },
        methods: {
            getProfileDetails() {
                axios.get('/business/completed-details').then(resp => {
                    this.completionRecord = resp.data;
                }).catch(err => {
                    this.$store.commit('setStatusMsg', {type: 'warning', msg: 'An error may have occurred.'})
                })
            }
        }
    }
</script>

<style scoped>

</style>
