'''
Packages
 Package is a container for multiple modules.
 A package is a directory or a folder.
 All the related modules are stored in a package
 While making a new directory add a special file names __init__.py which
 will denote that directory as a package.
'''

'''
For practical implementation a new directory named ecommerce is used
Below are the ways to import 
import package_name.module_name
package_name.module_name.function1()

from package_name.module_name import function1,function2,function3
function1()

from package_name import module_name
module_name.function1()
'''

import ecommerce.shipping

ecommerce.shipping.shipping_cost()

