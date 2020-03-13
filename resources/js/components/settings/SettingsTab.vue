<template>
    <div>
        <div class="os-tabs-w mx-5">
            <div class="os-tabs-controls">
                <ul class="nav nav-tabs" style="font-weight: 600">
                    <li class="nav-item">
                        <a aria-expanded="false" @click="selectedTabView='tab-profile'" class="nav-link active"
                           data-toggle="tab"
                           href="#tab_profile" data-title="Profile Settings"> Profile </a>
                    </li>
                    <li class="nav-item" v-if="business_id && user_role === 'Owner'">
                        <a aria-expanded="false"
                           @click="selectedTabView='tab-business'"
                           class="nav-link" data-toggle="tab" href="#tab_business"
                           data-title="Business Settings">
                            Business </a>
                    </li>
                    <li class="nav-item">
                        <a aria-expanded="false" class="nav-link" data-toggle="tab"
                           href="#tab_accounts"
                           data-title="Account Settings"> Settlement Accounts </a>
                    </li>
                    <li class="nav-item" v-if="business_id && user_role === 'Owner'">
                        <a aria-expanded="false" class="nav-link" data-toggle="tab" href="#tab_team"
                           data-title="Team Settings" @click="selectedTabView='tab-team'">
                            Team </a>
                    </li>
                    <li class="nav-item">
                        <a aria-expanded="false" class="nav-link" data-toggle="tab" href="#tab_preferences"
                           data-title="Preference Settings"> Preferences </a>
                    </li>
                    <li class="nav-item">
                        <a aria-expanded="false" class="nav-link" data-toggle="tab" href="#tab_api"
                           data-title="API Settings"> API Keys & Webhooks </a>
                    </li>
                </ul>
            </div>
        </div>

        <div class="row">
            <div class="col-md-3"></div>
            <div class="col-md-6 col-sm-12">
                <div class="element-wrapper">
                    <component :is="selectedTabView"></component>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Profile from "./Profile";
    import Business from "./Business";
    import Team from './teams/TeamMembers'

    export default {
        name: "SettingsTab",
        props: ['user_role', 'business_id'],
        data() {
            return {
                selectedTabView: 'tab-profile'
            }
        },
        components: {
            TabProfile: Profile,
            TabBusiness: Business,
            TabTeam: Team
        },
        created() {

        },
        methods: {}
    }
</script>

<style scoped>

</style>
