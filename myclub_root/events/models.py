from django.db import models

class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.CharField(max_length=120)
    # venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.CharField(max_length=60)
    # attendees = models.ManyToManyField(MyClubUser, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
