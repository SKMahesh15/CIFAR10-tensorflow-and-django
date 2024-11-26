from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        """
        Returns a filename that's free on the target storage system, and
        available for new content to be written to.

        This file storage solves the overwrite-on-upload problem.
        """
        # If the filename already exists, remove it from the file system
        if self.exists(name):
            file_path = os.path.join(settings.MEDIA_ROOT, name)
            os.remove(file_path)
        # Call the parent class's method to handle the `max_length` argument correctly
        return super().get_available_name(name, max_length=max_length)
