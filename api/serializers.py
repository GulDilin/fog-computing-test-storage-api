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
        fields = '__all__'
        read_only_fields = ['id']


class TestBuildSerializer(ModelSerializer):
    class Meta:
        model = TestBuild
        fields = '__all__'
        read_only_fields = ['id', 'started', 'finished', 'test_instance']


class TestSuiteSerializer(ModelSerializer):
    class Meta:
        model = TestSuite
        fields = '__all__'
        read_only_fields = ['id', 'started', 'finished', 'test_build']


class TestCaseSerializer(ModelSerializer):
    class Meta:
        model = TestCase
        fields = '__all__'
        read_only_fields = ['id', 'started', 'finished', 'test_suite']
