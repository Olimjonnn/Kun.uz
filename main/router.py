from rest_framework import routers 
from main.views import *


router = routers.DefaultRouter()

router.register("category", CategoryView)
router.register("categorycity", CategoryCityView)
router.register("news", NewsView)
router.register("videocategory", ViderCategoryView)