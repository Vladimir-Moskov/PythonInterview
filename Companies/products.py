"""
 technical / code interview for EclecticIQ
 Date: 2019-12-01
 Refactored:
 Created by: Volodymyr Moskov

 Summary: Hi Volodymyr,
    Thanks again for your application, and for submitting the assignment.
    Unfortunately, we have decided not to move forward with you in the hiring process as we believe we have other
     candidates more fit for the role in our pipeline right now.

    We wish you the best in your next career steps.

    Best regards,
    EclecticIQ
"""

"""
Hi Volodymyr,

Thank you for your application. In order to make an assessment of your Python knowledge and eye for detail,
we'd like to ask you to complete a short assignment.

I've attached a piece of code that I'd like you to review as if it was a regular code review -
 imagine you're a senior member of a team and a junior asks for your approval. Point out whatever flaws you find,
 explain them if necessary, and maybe even point out some suggestions on how to do things better.

We would prefer to see your review as a set of in-line comments in the Python module,
but you're free to choose another way if it works better for you.

Please submit the assignment by 2019-12-03. Thank you!

Best regards,
EclecticIQ

"""


"""
This module contains code that:

1. fetches a product record, containing product manual details,
   from some SQL database,
2. uses ImageMagic via shell to covert PDF product manual into
   a JPEG byte stream.

Your task is to uncover as many issues as you can.
"""

# General conclusions: original code does not have any comments and pydocs documentation with it which is not really
# good practice.
# Variable/Class/Function names are mostly self described, code follow PEP 8 - so it deserves  some credits for this.

# imports looks good so far
import json
import os
import pathlib

# 1 - Absolute import preferable over Relative
# 99% of cases Use absolute import instead relative, unless you know what you are doing,
# generally speaking Relative import is bad practice in this particular example.
# Relative imports are also not as readable as absolute ones, and it’s not easy to tell the location of the imported
# resources and can make cause problems when project files/folders will be moving around.
from . import db, config

# 2
# sponsored_id_list should not be created on the module level,
# if it is going to be used only by ProductFinder as static
# variable then should be  moved  on class level. Also the point to create another references we can use
# config.get_sponsored() directly
# The right usage of sponsored_id_list really depends on implementation of - config.get_sponsored()
# A case - config.get_sponsored() is just wrapper of config file and/or just static data holder -
# just use config.get_sponsored()
# B case - config.get_sponsored() do some heavy calculations or/and dp/server/.. calls - and it make sense to create
# variable to keep it - so just move it inside ProductFinder
sponsored_id_list = config.get_sponsored()


class ProductFinder:
    # 3
    # if the function should be "static" - use @staticmethod then,
    # else if function should be called on instance level, then the first argument 'self' is missed
    # For default value of ids - the value [] should not be used (on first function call  with dafault argument
    # reference to the empty array will be created and will be reused for all next call for default parameter) -
    # it is better do do like this ids=None and if not ids: ids = []
    def get_product_details(ids=[]):
        ids.extend(sponsored_id_list)
        cursor = db.cursor()
        cursor.execute('''
            SELECT product_id, product_manual_data
            FROM product
            WHERE product_id IN {}
        '''.format(tuple(ids)))
        return cursor.fetchall()

# 4
# the folder name '/var/lib/app' as static string - should be moved to config.py we have imported early
# code below can be replaced with one line
#   plist = pathlib.Path(config.VAR_LIB_APP).glob('*.' + config.MANUAL_EXTENSION),
# also it is better to use path.join if it consists from many parts
# where config.VAR_LIB_APP = '/var/lib/app'
# config.MANUAL_EXTENSION = 'pdf'
# also this code should be moved inside render_product_manual method, there is no reason to keep it on module
# level, it looks more logical to call this at the same time we want to do file processing
# Anyway those 6 line of code are redundant - see reason below
tmp = pathlib.Path('/var/lib/app').glob('*')
plist = []
for p in tmp:
    if p.name.endswith('pdf'):
        plist.insert(0, p)
del tmp

# 5
# the variable name 'data' is too short and too common. it is better to be more specific
# for instance - product_manual_db_data
def render_product_manual(data):
    # again something like product_manual will be more appropriate name for the variable 'd'
    d = json.loads(data)
    if not d['manual_filename']:
        raise ValueError('Product details have no manual')

    # 6
    # logic in this  section below could be replaced with two lines bellow
    # if not pathlib.Path(config.VAR_LIB_APP).joinpath(d['manual_filename']).is_file():
    #     raise ValueError('Product PDF is not found')
    # and all logic around plist will become redundant
    found_pdf = False
    for p in plist:
        if d['manual_filename'] == p:
            found_pdf = True
    if not found_pdf:
        raise ValueError('Product PDF is not found')

    # 7
    # It will be a good idea to have some validators for case
    # when d.manual_render_params is not empty - to validate does ImageMagic can handle it
    # temp folder  "/tmp" should also be taken from config and
    # file image name 'tmp_image.jpg' should be unique to avoid processing collisions
    # like 'tmp_' + d['manual_filename'] + random_str '.jpg'
    # where random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    os.system('convert {} {} /tmp/tmp_image.jpg'.format(
        d.get('manual_render_params', ''), d['manual_filename']))

    # 8
    # I am not sure is silence catch of exception is a good practice,
    # actually I am 100% sure it is not best way to deal with file system
    try:
        return open('/tmp/tmp_image.jpg', 'rb')
    except:
        pass

# The End
