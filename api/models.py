from django.db import models


class TestInstance(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=500, unique=True)


class TestBuild(models.Model):
    number = models.IntegerField()
    started = models.DateTimeField(null=True)
    finished = models.DateTimeField(null=True)
    test_instance = models.ForeignKey(TestInstance, related_name='test_instance', on_delete=models.CASCADE,
                                      blank=False, null=False)


class TestSuite(models.Model):
    name = models.CharField(max_length=32, unique=True)
    started = models.DateTimeField(null=True)
    finished = models.DateTimeField(null=True)
    test_build = models.ForeignKey(TestBuild, related_name='test_build', on_delete=models.CASCADE,
                                   blank=False, null=False)


class TestCase(models.Model):
    TestCaseStatus = (
        ('SUCCESS', 'SUCCESS'),
        ('ERROR', 'ERROR'),
        ('FAILED', 'FAILED'),
        ('NOT_SET', 'NOT_SET'),
    )

    name = models.CharField(max_length=32, unique=True)
    started = models.DateTimeField(null=True)
    finished = models.DateTimeField(null=True)
    result_status = models.CharField(
        max_length=8,
        choices=TestCaseStatus,
        default='NOT_SET',
    )
    test_suite = models.ForeignKey(TestSuite, related_name='test_suite', on_delete=models.CASCADE,
                                   blank=False, null=False)
