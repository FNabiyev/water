from rest_framework import routers
from .viewsets import *

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'brand', BrandViewSet)
router.register(r'products', ProductsViewSet)
router.register(r'shop', ShopViewSet)
router.register(r'shopitems', ShopItemsViewSet)