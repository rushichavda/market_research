# from django.db import models

# class Survey(models.Model):
#     AGE_CHOICES = [
#         ('under_18', 'Under 18'),
#         ('18_25', '18-25'),
#         ('26_35', '26-35'),
#         ('36_50', '36-50'),
#         ('50_plus', '50+'),
#     ]
   
#     age_group = models.CharField(max_length=20, choices=AGE_CHOICES, blank=True)
#     discovery_source = models.CharField(max_length=100, blank=True)
#     discovery_other = models.CharField(max_length=255, blank=True)
#     location = models.CharField(max_length=100, blank=True)
#     location_other = models.CharField(max_length=255, blank=True)
#     app_usage = models.BooleanField(default=False)
#     apps_used = models.JSONField(default=list, blank=True)
#     app_other = models.CharField(max_length=255, blank=True)
#     feature_preferences = models.JSONField(default=dict, blank=True)
#     motivation = models.IntegerField()
#     willingness = models.TextField(blank=True)
#     barriers = models.TextField(blank=True)
#     barrier_other = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Survey #{self.id} - Age Group: {self.age_group}"

from django.db import models

class Survey(models.Model):
    AGE_GROUP_CHOICES = [
        ('<18', 'Under 18'),
        ('18-24', '18 to 24'),
        ('24-34', '24 to 34'),
        ('35-44', '35 to 44'),
        ('45-54', '45 to 54'),
        ('55+', '55 and above'),
    ]

    age_group = models.CharField(max_length=10, choices=AGE_GROUP_CHOICES, blank=True)
    discovery_source = models.CharField(max_length=100, blank=True)
    discovery_other = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=100, blank=True)
    location_other = models.CharField(max_length=255, blank=True)
    app_usage = models.BooleanField(default=False)
    apps_used = models.JSONField(default=list, blank=True)
    app_other = models.CharField(max_length=255, blank=True)
    feature_preferences = models.JSONField(default=dict, blank=True)
    motivation = models.IntegerField(default=2)  # 0-4 mapped from emoji slider
    willingness = models.CharField(max_length=50, blank=True)  # e.g., "100-300"
    barriers = models.CharField(max_length=100, blank=True)
    barrier_other = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=255, blank=True)
   
    def __str__(self):
        return f"Survey #{self.id} - Age: {self.age_group}"


