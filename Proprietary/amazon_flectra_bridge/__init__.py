# -*- coding: utf-8 -*-
#################################################################################
#
#    Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE URL <https://store.webkul.com/license.html/> for full copyright and licensing details.
#################################################################################
from . import tools
from . import models
from . import wizard
def pre_init_check(cr):
	from flectra.service import common
	from flectra.exceptions import Warning
	version_info = common.exp_version()
	server_serie =version_info.get('server_serie')
	if server_serie!='11.0':raise Warning('Module support Perpul series 11.0 found {}.'.format(server_serie))
	return True
