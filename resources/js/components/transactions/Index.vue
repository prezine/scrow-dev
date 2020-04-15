<template>
    <div>
        <div class="os-tabs-w">
            <div class="os-tabs-controls os-tabs-complex">
                <ul class="nav nav-tabs">
                    <li class="nav-item">
                        <a aria-expanded="false" class="nav-link active" data-toggle="tab" href="#tab_overview"
                           data-title="Transactions Overview" @click="selectedTabView='tab-overview'">
                            <span class="tab-label">Overview</span>
                            <span class="badge badge-success">
                                                <i class="os-icon os-icon-award"></i>
                                                <span></span>
                                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a aria-expanded="false" class="nav-link" data-toggle="tab" href="#tab_create_transaction"
                           data-title="New Transaction" @click="selectedTabView='tab-new-transaction'">
                            <span class="tab-label">New Transaction</span>
                        </a>
                    </li>
                    <li class="nav-item d-none d-xl-block">
                        <a aria-expanded="false" class="nav-link" data-toggle="tab" href="#tab_history"
                           data-title="Transaction History" @click="selectedTabView='tab-history'">
                            <span class="tab-label">History</span>
                        </a>
                    </li>
                </ul>
            </div>
        </div>
        <component :is="selectedTabView"></component>
    </div>
</template>

<script>
    import NewTransaction from "./tabs/NewTransaction";
    import History from "./tabs/History";
    import Overview from "./tabs/Overview";

    export default {
        name: "Index",
        data() {
            return {
                selectedTabView: 'tab-overview'
            }
        },
        components: {
            TabHistory: History,
            TabNewTransaction: NewTransaction,
            TabOverview: Overview
        }
    }
</script>

<style scoped>

</style>
