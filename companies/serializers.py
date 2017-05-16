from rest_framework import serializers
from .models import Stock
#converting a data into other form like to save in flash-drive or other transferable forms


class StockSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Stock
        #or users etc anything

        #now what you want to return
        # fields = ('ticker', 'volume')
        fields = '__all__' #you might not want to send all things
