from rest_framework import serializers


class FilterCommentListSerializer(serializers.ListSerializer):
    """ Filter comments only for parents """
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """ Output recursively cheldren """
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data      