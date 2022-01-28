from django.urls import include, path
from rest_framework_nested.routers import (NestedSimpleRouter, DefaultRouter)

from .views import (TestInstanceViewSet, TestBuildViewSet, TestSuiteViewSet, TestCaseViewSet)

router = DefaultRouter()
router.register(r'test_instance', TestInstanceViewSet, basename='test_instance')

test_instance_router = NestedSimpleRouter(router, 'test_instance', lookup='test_instance')
test_instance_router.register(r'test_build', TestBuildViewSet, basename='test_build')

test_build_router = NestedSimpleRouter(test_instance_router, 'test_build', lookup='test_build')
test_build_router.register(r'test_suite', TestSuiteViewSet, basename='test_suite')

test_suite_router = NestedSimpleRouter(test_build_router, 'test_suite', lookup='test_suite')
test_suite_router.register(r'test_case', TestCaseViewSet, basename="test_case")

urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'api/', include(test_instance_router.urls)),
    path(r'api/', include(test_build_router.urls)),
    path(r'api/', include(test_suite_router.urls)),
]
