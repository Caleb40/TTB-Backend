from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework.permissions import AllowAny


# Customise the default UserCreate serializer from Djoser to include email
class UserCreateSerializer(BaseUserCreateSerializer):
    permission_classes = [AllowAny]

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'phone',
                  'city', 'address', 'country', 'company_name', 'corporate_phone',
                  'corporate_reg_no', 'company_vat_no', 'profile_image',
                  'total_investment_plans', 'active_investment_plans', 'total_deposit',
                  'total_withdrawal', 'total_ref_bonus', 'account_balance']
        ref_name = "user_creator"


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'email', 'first_name', 'last_name', 'phone',
                  'city', 'address', 'country', 'company_name', 'corporate_phone',
                  'corporate_reg_no', 'company_vat_no', 'profile_image',
                  'total_investment_plans', 'active_investment_plans',
                  'total_deposit', 'total_withdrawal', 'total_ref_bonus', 'account_balance'
                  ]
        ref_name = "user_lister"
