from django.db import models


class Task(models.Model):
    """
    A model for task class.
    """
    task_text = models.TextField()
    comment = models.TextField()
    create_date = models.DateTimeField()
    is_done = models.BooleanField()

    class Meta:
        ordering = ["-create_date"]

    def __str__(self):
        """
        String for representing the Task object.
        """
        return self.task_text
