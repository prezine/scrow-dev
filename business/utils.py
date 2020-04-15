from business.models import BusinessVerification
from transactions.models import ProductBacklog


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


class ProductBacklogAction:
    ModelClass = ProductBacklog

    def _save_backlog(self, **kwargs):
        return self.ModelClass.objects.create(**kwargs)

    def add_product(self, user, product):
        action_msg = 'Added product %s' % product.name
        self._save_backlog(user=user, product=product, action=action_msg)

    def update_product(self, user, product):
        action_msg = 'Updated product %s' % product.name
        self._save_backlog(user=user, product=product, action=action_msg)

    def delete_product(self, user, product):
        action_msg = 'Deleted %s' % product.name
        self._save_backlog(user=user, product=product, action=action_msg)

    def update_stock(self, user, product):
        action_msg = '%s products in stock was updated to %s' % (product.name, product.quantity)
        self._save_backlog(user=user, product=product, action=action_msg)
