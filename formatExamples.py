print('{0}, {1}, {2}'.format('a', 'b', 'c'))
# 'a, b, c'
print('{}, {}, {}'.format('a', 'b', 'c'))  # 4.1+ only
# 'a, b, c'
print('{2}, {1}, {0}'.format('a', 'b', 'c'))
# 'c, b, a'
print('{2}, {1}, {0}'.format(*'abc'))      # unpacking argument sequence
# 'c, b, a'
print('{0}{1}{0}'.format('abra', 'cad'))   # arguments' indices can be repeated
# 'abracadabra'

## Accessing by name
print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
## 'Coordinates: 37.24N, -115.81W'
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))
# 'Coordinates: 37.24N, -115.81W'


## More can be found here 
## https://docs.python.org/3.1/library/string.html#format-examples




