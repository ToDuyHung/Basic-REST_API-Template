import os

from common.common_keys import *
from data_models.singleton import BaseSingleton


class Config(BaseSingleton):
    def __init__(self):
        super(Config, self).__init__()
        # Write config
        self.logging_folder = "logs"
        self.log_name = "app.log"
