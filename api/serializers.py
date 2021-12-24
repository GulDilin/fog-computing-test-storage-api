from rest_framework.serializers import ModelSerializer

from .models import (
    TestInstance,
    TestBuild,
    TestSuite,
    TestCase,
)


class TestInstanceSerializer(ModelSerializer):
    class Meta:
        model = TestInstance
        fields = ['pk', 'name', 'description']


class TestBuildSerializer(ModelSerializer):
    class Meta:
        model = TestBuild
        fields = ['pk', 'number', 'started', 'finished']


class TestSuiteSerializer(ModelSerializer):
    class Meta:
        model = TestSuite
        fields = ['pk', 'name', 'started', 'finished']


class TestCaseSerializer(ModelSerializer):
    class Meta:
        model = TestCase
        fields = ['pk', 'name', 'started', 'finished', 'result_status']
