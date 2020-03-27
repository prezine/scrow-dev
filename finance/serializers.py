from rest_framework import serializers

from finance.models import Bank


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Bank
