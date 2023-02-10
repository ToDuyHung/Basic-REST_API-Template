import os
import logging

from config.config import Config
from data_models.singleton import BaseSingleton


class BaseService:
    def __init__(self, config: Config = None):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.config = config if config is not None else Config()
        self.session = None
        self.logger.info(f"CREATE {self.__class__.__name__}")
        

class BaseServiceSingleton(BaseService, BaseSingleton):
    pass