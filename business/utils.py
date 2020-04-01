from business.models import BusinessVerification


class BusinessVerificationCheck:
    def __init__(self, user):
        self.completed_records_count = 0
        self.completion_records = {
            'percentage': 0,
            'personal_details': False,
            'business_details': False,
            'verification_documents': False,
            'settlement_account': False
        }
        self.user = user
        self.business = user.active_business

    @staticmethod
    def is_user_details_verified(user):
        if user.name and user.phone:
            return True
        return False

    @staticmethod
    def is_business_details_verified(business):
        if business.email and business.phone and business.description and business.address:
            return True
        return False

    def verify_user_details(self):
        if self.is_user_details_verified(self.user):
            self.completed_records_count += 1
            self.completion_records['personal_details'] = True

    def verify_business_details(self):
        if self.is_business_details_verified(self.business):
            self.completed_records_count += 1
            self.completion_records['business_details'] = True

    def verify_documents(self):
        if BusinessVerification.objects.filter(business=self.business.pk).exists():
            self.completed_records_count += 1
            self.completion_records['verification_documents'] = True

    def verify_settlement_account(self):
        if self.business.bank:
            self.completed_records_count += 1
            self.completion_records['settlement_account'] = True

    def details_verification(self):
        self.verify_user_details()
        self.verify_business_details()
        self.verify_documents()
        self.verify_settlement_account()

    def completion_percentage(self):
        percent = (self.completed_records_count * 100) / 4
        self.completion_records['percentage'] = percent

    def verify_and_get_details(self):
        self.details_verification()
        self.completion_percentage()

        return self.completion_records
