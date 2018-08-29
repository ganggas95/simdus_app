''' settings.py '''
import os


class BaseConfig(object):

    DIR_PATH = os.path.dirname(
        os.path.realpath(__file__))
    PER_PAGE = '15'


class UploadPathConfig(object):

    ROOT_DATA_DIR = os.path.join(
        BaseConfig.DIR_PATH,
        'uploads'
    )
    DIR_FOTO = os.path.join(
        ROOT_DATA_DIR,
        'foto'
    )
    DIR_KK = os.path.join(
        ROOT_DATA_DIR,
        'kk'
    )
    DIR_KTP = os.path.join(
        ROOT_DATA_DIR,
        'ktp'
    )
