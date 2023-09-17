from django.db import models


class EfoTerm(models.Model):
    term_id = models.CharField(max_length=200, unique=True)
    label = models.CharField(max_length=300)

    def __str__(self):
        return self.term_id


class EfoTermSynonym(models.Model):
    efo_term = models.ForeignKey(EfoTerm, on_delete=models.CASCADE)
    synonym = models.CharField(max_length=300)

    class Meta:
        unique_together = ('efo_term', 'synonym')

    def __str__(self):
        return self.synonym


class EfoTermOntology(models.Model):
    parent_efo_term = models.ForeignKey(EfoTerm, related_name='child_relationships', on_delete=models.CASCADE)
    child_efo_term = models.ForeignKey(EfoTerm, related_name='parent_relationships', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('parent_efo_term', 'child_efo_term')
