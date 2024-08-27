from src.textSummary.config.configuration import ConfigurationManager
from src.textSummary.components.data_transformation import DataTransformation
from src.textSummary.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        # Initialize any required attributes or configurations here
        pass

    def main(self):
        try:
            # Load configuration
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            logger.info("Configuration loaded successfully.")

            # Initialize DataTransformation
            data_transformation = DataTransformation(config=data_transformation_config)
            logger.info("DataTransformation instance created.")

            # Perform data transformation
            data_transformation.convert()
            logger.info("Data transformation completed successfully.")

        except Exception as e:
            logger.error(f"An error occurred during data transformation: {e}")
            raise
