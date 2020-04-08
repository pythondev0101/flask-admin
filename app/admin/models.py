""" ADMIN MODELS"""


class Admin(object):
    @property
    def admin_index_fields(self):
        raise NotImplementedError('Must implement ADMIN_INDEX_FIELDS')
