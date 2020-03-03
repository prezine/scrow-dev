from django.db import models
from django.utils import timezone


class SoftDeleteQuerySet(models.QuerySet):
    def pop(self, query_obj=None, **kwargs):
        update = self.update
        if any(kwargs.values()):
            update = self.filter(**kwargs).update
        try:
            query = query_obj.update if query_obj else update
        except AttributeError:
            raise AttributeError('Invalid object passed.')
        return query(deleted_at=timezone.now())


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        query = SoftDeleteQuerySet(self.model, using=self._db)
        query = query.filter(deleted_at__isnull=True)

        return query

    def pop(self, **kwargs):
        queryset = self.get_queryset()
        query = queryset.filter(deleted_at__isnull=True, **kwargs)

        if not query:
            try:
                query = queryset.get(deleted_at__isnull=True, **kwargs)
            except self.model.DoesNotExist:
                raise self.model.DoesNotExist(
                    "%s matching query does not exist." %
                    self.model._meta.object_name
                )

        return queryset.pop(query)
