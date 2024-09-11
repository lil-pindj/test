import s_taper
from s_taper.consts import *

scheme = {
    'nickname': TEXT,
    'id': INT + KEY,
    'items': TEXT
}
clients = s_taper.Taper('clients', 'data.db').create_table(scheme)

