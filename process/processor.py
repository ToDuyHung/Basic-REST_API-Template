from data_models.base_service import BaseServiceSingleton
from config.config import Config

class Model(BaseServiceSingleton):
    def __init__(self, config: Config):
        super(Model, self).__init__(config=config)


class Processor(BaseServiceSingleton):
    def __init__(self, config: Config):
        super(Processor, self).__init__(config=config)
        # Init processor
        self.config = config
        model = Model(config=config)
    
    async def process(self, input_data):
        pass
        # input: input_data
        # return output
        