<template>
    <!-- History -->
    <div class="element-box unstyle_elementbox hide" id="tab_history">
        <div class="row pt-1">
            <div class="col-sm-12">
                <!--START - Recent Ticket Comments-->
                <div class="element-wrapper">
                    <h6 class="element-header">Transaction History</h6>
                    <div class="element-box-tp">
                        <div class="table-responsive">
                            <table class="table table-padded">
                                <thead>
                                <tr>
                                    <th>Customer</th>
                                    <th>Item</th>
                                    <th>Amount</th>
                                    <th>Status</th>
                                    <th>Date</th>
                                    <th>Actions</th>
                                </tr>
                                </thead>
                                <tbody>
                                <tr v-for="customer in transactions">
                                    <td>
                                        <div class="user-with-avatar"><span>{{customer.name}}</span>
                                        </div>
                                    </td>
                                    <td><span> {{customer.product.name}} </span></td>
                                    <td class="bolder"><span class="text-success">{{customer.product.amount}} {{customer.product.currency}}</span>
                                    </td>
                                    <td class="nowrap">
                                        <span class="status-pill smaller yellow"></span>
                                        <span>{{customer.product.status}}</span>
                                    </td>
                                    <td><span class="lighter">{{formatTime(customer.created_at)}}</span></td>
                                    <td class="row-actions">
                                        <a href="#"><i class="os-icon os-icon-grid-10"></i></a>
                                        <a href="#"><i class="os-icon os-icon-ui-44"></i></a>
                                        <a class="danger" href="#"><i class="os-icon os-icon-ui-15"></i></a>
                                    </td>
                                </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
                <!--END - Recent Ticket Comments-->
            </div>
        </div>
    </div>
</template>

<script>
    import {DateTime} from "luxon";
    import {non400ErrorMsg} from "../../../utils/utils";

    export default {
        name: "History",
        data() {
            return {
                transactions: [],
                isLoading: true
            }
        },
        methods: {
            formatTime(time) {
                return DateTime.fromISO(time).setZone("Africa/Lagos").toRelative();
            },
            getTransactions() {
                axios.get('/transactions/customers').then(resp => {
                    this.transactions = resp.data;
                }).catch(err => {
                    if (err.response.status === 400) {
                        this.$store.commit('setstatusMsg', {
                            type: 'warning',
                            msg: err.response.data.response
                        });
                    } else {
                        non400ErrorMsg(this);
                    }
                });
            }
        },
        created() {
            this.getTransactions();
        }
    }
</script>

<style scoped>

</style>
