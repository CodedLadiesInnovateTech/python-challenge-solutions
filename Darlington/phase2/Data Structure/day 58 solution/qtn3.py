#program to display all the member name of an enum class ordered by their values.
import enum
class Country(enum.IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
print('Country Name ordered by Country Code:')
print('\n'.join('  ' + c.name for c in sorted(Country)))