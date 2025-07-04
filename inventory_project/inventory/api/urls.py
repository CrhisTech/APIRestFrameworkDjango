from rest_framework.routers import DefaultRouter
from inventory.api.views import CategoryViewSet, SubCategoryViewSet, ProductViewSet



router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('subcategories', SubCategoryViewSet, basename='subcategory')
router.register('products', ProductViewSet, basename='product')
urlpatterns = router.urls
