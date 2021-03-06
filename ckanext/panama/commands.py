# -*- coding: utf-8 -*-

from ckan.common import OrderedDict
from pylons import config
from ckan.plugins import toolkit
import ckanapi


groups = OrderedDict([
    ('local-governments', ('Local Governments', 'Municipios')),
    ('health', ('Health', 'Salud')),
    ('business', ('Business', 'Comercio e Industrias')),
    ('transportation', ('Transportation', 'Transporte y Logística')),
    ('education', ('Education', 'Educación')),
    ('justice', ('Justice', 'Justicia')),
    ('social-development', ('Social Development', 'Desarrollo Social')),
    ('finance', ('Finance', 'Finanzas Publicas')),
    ('labour', ('Labour', 'Empleo')),
    ('environment', ('Environment', 'Ambiente')),
])


class CreateFeaturedGroups(toolkit.CkanCommand):
    '''Create featured groups

    Usage:
      create_featured_groups             - create featured groups
    '''

    summary = __doc__.split('\n')[0]
    usage = __doc__
    max_args = 0
    min_args = 0

    def command(self):
        self._load_config()

        url = config['ckan.site_url']
        local_ckan = ckanapi.LocalCKAN()

        print groups.items

        for name, title in groups.items():
            try:
                result = local_ckan.action.group_create(
                    name=name,
                    image_url='{url}/images/{image}.png'.format(url=url,
                                                                image=name)
                )
                print result
            except ckanapi.ValidationError, e:
                print e
