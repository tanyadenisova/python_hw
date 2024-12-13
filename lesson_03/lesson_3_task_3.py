from address import Address
from mailing import Mailing

to_address = Address(603123, "Нижний Новогород", "Южное шоссе", 16, 41)
from_address = Address(400006, "Волгоград", "Волгоградская", 112, 89)
mailing = Mailing(to_address, from_address, 90, 33377723)

print(mailing)