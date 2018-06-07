from datapackage import Package

p = Package()

p.infer('*.csv')

p.descriptor['title'] = 'Openmod-Example'
p.descriptor['spatial'] = 'Random'
p.descriptor['sources'] = 'Created by hand'

p.commit()

p.save('datapackage.json')
