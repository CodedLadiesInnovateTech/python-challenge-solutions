#program to get the unique enumeration values.
import enum
class Countries(enum.Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    India = 355
    USA = 213
for result in Countries:
    print('{:15} = {}'.format(result.name, result.value))