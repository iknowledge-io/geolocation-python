"""this ensures that the ApiClientException instance is properly initialized, including any 
necessary initialization done in the parent Exception class, and provides context about
the exception by passing the message to the parent class."""


class ApiClientException(Exception):
    """Exception for Api Client."""
    
    def __init__(self, original_exception):
        # Extract the message from the original exception
        self.message = str(original_exception)
        # Call the __init__ method of the parent class (Exception) and pass the message
        super().__init__(self.message)
