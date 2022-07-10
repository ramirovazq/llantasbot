from utils.constants import ALL_BRANDS, ALL_ECONOMICO
from utils.constants import ALL_MEASURES
from utils.constants import ALL_OWNERS
from utils.constants import ALL_STATUS
from utils.constants import ALL_ECONOMICO

ALL_BRANDS_REGEX =  '^(' + "|".join(ALL_BRANDS.keys()) + ')$'
ALL_MEASURES_REGEX =  '^(' + "|".join(ALL_MEASURES) + ')$'
DOTS_REGEX = '^#\d{4}(,#\d{4})*$'
ALL_OWNERS_REGEX =  '^(' + "|".join(ALL_OWNERS) + ')$'
ALL_STATUS_REGEX =  '^(' + "|".join(ALL_STATUS) + ')$'
ALL_ECONOMICO_REGEX =  '^(' + "|".join(ALL_ECONOMICO) + ')$'
