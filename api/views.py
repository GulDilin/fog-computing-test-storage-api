from rest_framework.viewsets import ModelViewSet
from .serializers import (
    TestInstanceSerializer,
    TestBuildSerializer,
    TestSuiteSerializer,
    TestCaseSerializer
)
from .models import (
    TestInstance,
    TestBuild,
    TestSuite,
    TestCase
)


class TestInstanceViewSet(ModelViewSet):
    queryset = TestInstance.objects.all()
    serializer_class = TestInstanceSerializer


class TestBuildViewSet(ModelViewSet):
    def get_queryset(self):
        return TestBuild.objects.filter(test_instance=self.kwargs.get('test_instance_pk'))

    serializer_class = TestBuildSerializer


class TestSuiteViewSet(ModelViewSet):
    def get_queryset(self):
        return TestSuite.objects.filter(test_build=self.kwargs.get('test_build_pk'))

    serializer_class = TestSuiteSerializer


class TestCaseViewSet(ModelViewSet):
    def get_queryset(self):
        return TestCase.objects.filter(test_suite=self.kwargs.get('test_suite_pk'))

    serializer_class = TestCaseSerializer
