from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.utils import timezone
from rest_framework.mixins import (
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
)
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


class ApiModelViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    GenericViewSet
):
    pass


class StartStopModelMixin(GenericViewSet):
    @action(detail=True, methods=['post'])
    def start(self, request, *args, **kwargs):
        item = self.get_object()
        if item.started:
            return Response({'started': 'Already set'}, status=status.HTTP_400_BAD_REQUEST)
        item.started = timezone.now()
        item.save()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def finish(self, request, *args, **kwargs):
        item = self.get_object()
        if item.finished:
            return Response({'finished': 'Already set'}, status=status.HTTP_400_BAD_REQUEST)
        item.finished = timezone.now()
        item.save()
        serializer = self.get_serializer(item)
        return Response(serializer.data)


class TestInstanceViewSet(ApiModelViewSet):
    queryset = TestInstance.objects.all()
    serializer_class = TestInstanceSerializer


class TestBuildViewSet(ApiModelViewSet, StartStopModelMixin):
    serializer_class = TestBuildSerializer

    def get_queryset(self):
        return TestBuild.objects.filter(test_instance=self.kwargs.get('test_instance_pk'))

    def perform_create(self, serializer):
        serializer.save(test_instance=TestInstance.objects.get(pk=self.kwargs.get('test_instance_pk')))


class TestSuiteViewSet(ApiModelViewSet, StartStopModelMixin):
    serializer_class = TestSuiteSerializer

    def get_queryset(self):
        return TestSuite.objects.filter(test_build=self.kwargs.get('test_build_pk'))

    def perform_create(self, serializer):
        serializer.save(test_build=TestBuild.objects.get(pk=self.kwargs.get('test_build_pk')))


class TestCaseViewSet(ApiModelViewSet, StartStopModelMixin):
    serializer_class = TestCaseSerializer

    def get_queryset(self):
        return TestCase.objects.filter(test_suite=self.kwargs.get('test_suite_pk'))

    def perform_create(self, serializer):
        serializer.save(test_suite=TestSuite.objects.get(pk=self.kwargs.get('test_suite_pk')))

