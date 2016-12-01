from __future__ import absolute_import, division
from mongoengine import (EmbeddedDocument, EmbeddedDocumentField, StringField,
                         ListField, IntField, BooleanField)

from .transcript import Transcript
from scout.constants import (CONSEQUENCE, FEATURE_TYPES, SO_TERMS)

from scout.models import PhenotypeTerm


class Gene(EmbeddedDocument):
    # The hgnc gene symbol
    hgnc_id = IntField(required=True)
    # A list of Transcript objects
    transcripts = ListField(EmbeddedDocumentField(Transcript))
    # This is the worst functional impact of all transcripts
    functional_annotation = StringField(choices=SO_TERMS.keys())
    # This is the region of the most severe functional impact
    region_annotation = StringField(choices=FEATURE_TYPES)
    # This is most severe sift prediction of all transcripts
    sift_prediction = StringField(choices=CONSEQUENCE)
    # This is most severe polyphen prediction of all transcripts
    polyphen_prediction = StringField(choices=CONSEQUENCE)

    @property
    def omim_link(self):
        return "http://omim.org/entry/{}".format(self.omim_gene_entry)
