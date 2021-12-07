__version__ = '0.7.1'


from .als import als
from .als import als2


from .anova import ANOVA


from .cross import cross


from .maxvol import maxvol
from .maxvol import rect_maxvol


from .tensor import add
from .tensor import erank
from .tensor import full
from .tensor import get
from .tensor import getter
from .tensor import mean
from .tensor import mul
from .tensor import norm
from .tensor import rand
from .tensor import show
from .tensor import sum
from .tensor import truncate


from .utils import confidence
from .utils import get_cdf
from .utils import ind2poi
from .utils import ind2str
from .utils import lhs
from .utils import str2ind
from .utils import tt_sample
from .utils import tt_svd
from .utils import tt_svd_incomplete
