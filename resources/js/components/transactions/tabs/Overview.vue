<template>
    <!-- Overview -->
    <div class="element-box" id="tab_overview">
        <div class="row">
            <div class="col-sm-12 col-lg-8 col-xxl-6">
                <div class="element-balances justify-content-between mobile-full-width">
                    <div class="balance balance-v2">
                        <div class="balance-title">Total Revenue</div>
                        <div class="balance-value"><span class="d-xxl-none">₦0</span>
                            <span class="d-none d-xxl-inline-block">₦0</span>
                        </div>
                    </div>
                    <div class="balance-table pl-sm-2">
                        <table class="table table-lightborder table-bordered table-v-compact mb-0">
                            <tr>
                                <td><strong>2</strong>
                                    <div class="balance-label smaller lighter text-nowrap">Fraud Block</div>
                                </td>
                                <td><strong>0</strong>
                                    <div class="balance-label smaller lighter text-nowrap">Bank Error</div>
                                </td>
                                <td><strong>0</strong>
                                    <div class="balance-label smaller lighter text-nowrap">Customer Error</div>
                                </td>
                            </tr>
                            <tr>
                                <td><strong>0</strong>
                                    <div class="balance-label smaller lighter text-nowrap">Processing Errors</div>
                                </td>
                                <td class="text-success"><strong>80%</strong>
                                    <div class="balance-label smaller lighter text-nowrap">Success rate</div>
                                </td>
                                <td class="text-danger"><strong>20%</strong>
                                    <div class="balance-label smaller lighter text-nowrap">Failed rate</div>
                                </td>
                            </tr>
                        </table>
                    </div>
                </div>
                <div class="element-wrapper compact">
                    <div class="element-box-tp">
                        <div class="element-actions d-none d-sm-block">
                            <form class="form-inline justify-content-sm-end">
                                <label class="smaller" for="">Show Period:</label>
                                <select class="form-control form-control-sm form-control-faded">
                                    <option selected="true">Last 30 days</option>
                                    <option>This Week</option>
                                    <option>This Month</option>
                                    <option>Today</option>
                                </select>
                            </form>
                        </div>
                        <h6 class="element-box-header">Balance History</h6>
                        <div class="el-chart-w">
                            <canvas data-chart-data="13,28,19,24,43,49,40,35,42,46,38,32,45" height="50"
                                    id="liteLineChartV3" width="300"></canvas>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-sm-2 d-none d-xxl-block">
                <div class="element-box less-padding">
                    <h6 class="element-box-header text-center">Portfolio Distribution</h6>
                    <div class="el-chart-w">
                        <canvas height="120" id="donutChart1" width="120"></canvas>
                        <div class="inside-donut-chart-label"><strong>263</strong><span>Coins</span></div>
                    </div>
                    <div class="el-legend condensed">
                        <div class="row">
                            <div class="col-auto col-xxxxl-6 ml-sm-auto mr-sm-auto">
                                <div class="legend-value-w">
                                    <div class="legend-pin legend-pin-squared"
                                         style="background-color: #6896f9;"></div>
                                    <div class="legend-value"><span>Bitcoins</span>
                                        <div class="legend-sub-value">17%, 12 Coins</div>
                                    </div>
                                </div>
                                <div class="legend-value-w">
                                    <div class="legend-pin legend-pin-squared"
                                         style="background-color: #85c751;"></div>
                                    <div class="legend-value"><span>Litecoin</span>
                                        <div class="legend-sub-value">22%, 0.3 Coins</div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-sm-6 d-none d-xxxxl-block">
                                <div class="legend-value-w">
                                    <div class="legend-pin legend-pin-squared"
                                         style="background-color: #806ef9;"></div>
                                    <div class="legend-value"><span>Etherium</span>
                                        <div class="legend-sub-value">3%, 7 Coins</div>
                                    </div>
                                </div>
                                <div class="legend-value-w">
                                    <div class="legend-pin legend-pin-squared"
                                         style="background-color: #d97b70;"></div>
                                    <div class="legend-value"><span>Ripple</span>
                                        <div class="legend-sub-value">15%, 4 Coins</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-sm-4 d-none d-lg-block">
                <img src="/dist/img/master_drib.jpg" style="width: 310px">
            </div>
        </div>
        <div class="row pt-2">
            <div class="col-6 col-sm-3 col-xxl-2">
                <a class="element-box el-tablo centered trend-in-corner smaller" href="./transactions#">
                    <div class="label">Fraud Block</div>
                    <div class="value">1</div>
                    <div class="trending trending-up"><span>12%</span><i class="os-icon os-icon-arrow-up6"></i>
                    </div>
                </a>
            </div>
            <div class="col-6 col-sm-3 col-xxl-2">
                <a class="element-box el-tablo centered trend-in-corner smaller" href="./transactions#">
                    <div class="label">Bank Error</div>
                    <div class="value text-danger">1</div>
                    <div class="trending trending-down"><span>12%</span><i class="os-icon os-icon-arrow-down6"></i>
                    </div>
                </a>
            </div>
            <div class="col-6 col-sm-3 col-xxl-2">
                <a class="element-box el-tablo centered trend-in-corner smaller" href="./transactions#">
                    <div class="label">Customer Error</div>
                    <div class="value">1</div>
                    <div class="trending trending-up"><span>12%</span><i class="os-icon os-icon-arrow-up6"></i>
                    </div>
                </a>
            </div>
            <div class="col-6 col-sm-3 col-xxl-2">
                <a class="element-box el-tablo centered trend-in-corner smaller" href="./transactions#">
                    <div class="label">Processing Errors</div>
                    <div class="value">0</div>
                    <div class="trending trending-up"><span>12%</span><i class="os-icon os-icon-arrow-up6"></i>
                    </div>
                </a>
            </div>
            <div class="col-6 col-xxl-2 d-sm-none d-xxl-block">
                <a class="element-box el-tablo centered trend-in-corner smaller" href="./transactions#">
                    <div class="label">Litecoin Price</div>
                    <div class="value">-$3,473</div>
                    <div class="trending trending-down"><span>5%</span><i class="os-icon os-icon-arrow-down6"></i>
                    </div>
                </a>
            </div>
            <div class="col-6 col-xxl-2 d-sm-none d-xxl-block">
                <a class="element-box el-tablo centered trend-in-corner smaller" href="./transactions#">
                    <div class="label">Last Month</div>
                    <div class="value">-$3,248</div>
                    <div class="trending trending-down"><span>12%</span><i class="os-icon os-icon-arrow-down6"></i>
                    </div>
                </a>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Overview"
    }
</script>

<style scoped>

</style>
