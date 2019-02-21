from haystack import indexes

from .models import FavoriteWord

class FavoriteWordIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(model_attr='word', document=True)
    user = indexes.CharField(model_attr='user__username')

    def get_model(self):
        return FavoriteWord
