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
                                <tr>
                                    <td>
                                        <div class="user-with-avatar"><img alt=""
                                                                           src="/dist/img/avatar1.jpg"><span>Precious Tom</span>
                                        </div>
                                    </td>
                                    <td><span> Nike Shoe </span></td>
                                    <td class="bolder"><span class="text-success">1,250 USD</span></td>
                                    <td class="nowrap">
                                        <span class="status-pill smaller yellow"></span>
                                        <span>In progress</span>
                                    </td>
                                    <td><span class="lighter">2 Days ago</span></td>
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
    export default {
        name: "History"
    }
</script>

<style scoped>

</style>
