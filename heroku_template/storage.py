# -*- coding: utf-8 -*-
from storages.backends.s3boto import S3BotoStorage
from pipeline.storage import PipelineMixin

class S3PipelineStorage(PipelineMixin, S3BotoStorage):
    pass
