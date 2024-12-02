from .models import Content
from haystack import indexes


class VideoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(document=True, use_template=True)
    uploader = indexes.CharField(model_attr='owner__username')
    keywords = indexes.CharField(model_attr='keywords')

    def get_model(self):
        return Content

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
