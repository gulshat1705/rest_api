from rest_framework import permissions, mixins, viewsets

class MixedPermission:
    """ Mixin permissions for action """
    def get_permissions(self):
        try:
            return [permissions() for permission in self.get_permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.get_permission_classes]


class MixedPermissionViewSet(MixedPermission, viewsets.ViewSet): #объединение MixedPermission с ViewSet
    pass            


class MixedPermissionGenericViewSet(MixedPermission, viewsets.GenericViewSet):
    pass



class CreateUpdateDestroy(mixins.CreateModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.DestroyModelMixin,
                                    MixedPermission, 
                                    viewsets.GenericViewSet
                                    ):
    """
    """
    pass                                


class CreateRetrieveUpdateDestroy(mixins.CreateModelMixin,
                                    mixins.RetrieveModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.DestroyModelMixin,
                                    MixedPermission, 
                                    viewsets.GenericViewSet
                                    ):
    """
    """
    pass                                