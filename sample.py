#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gettext
gettext.bindtextdomain('sample', 'lang/')
gettext.textdomain('sample')
_ = gettext.gettext

print _('This is a translatable string.')
n = 1
print gettext.ngettext('%(useful_favorable)s of %(useful_total)s people found this review helpful, including you', '%(useful_favorable)s of %(useful_total)s people found this review helpful, including you', n ) % { 'useful_favorable': 10, 'useful_total': n }

n = 12
print gettext.ngettext('%(useful_favorable)s of %(useful_total)s people found this review helpful, including you', '%(useful_favorable)s of %(useful_total)s people found this review helpful, including you', n ) % { 'useful_favorable': 10, 'useful_total': n }
