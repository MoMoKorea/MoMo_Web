from user.models import CustomUser
from user.serializers import UserSerializers


class UserRecords:
      """
      Kyle 2019-07-20

      @API: 회원정보 Query
      """
      @staticmethod
      def update(userId, data):
            user = UserRecords.getUser(userId)
            serializer = UserSerializers(user, data=data, partial=True)
            if serializer.is_valid():
                  serializer.save()
                  return serializer.data
            else:
                  return None

      @staticmethod
      def getUser(userId):
            return CustomUser.objects.get(id=userId)


