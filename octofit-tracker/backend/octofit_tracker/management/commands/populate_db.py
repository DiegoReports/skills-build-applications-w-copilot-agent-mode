from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = "Populate the octofit_db database with test data"

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Test data
        users = [
            {"username": "john_doe", "email": "john@example.com", "password": "password123"},
            {"username": "jane_smith", "email": "jane@example.com", "password": "password123"},
        ]
        teams = [
            {"name": "Team Alpha", "description": "The first team"},
            {"name": "Team Beta", "description": "The second team"},
        ]
        activities = [
            {"name": "Running", "calories_burned_per_minute": 10},
            {"name": "Cycling", "calories_burned_per_minute": 8},
        ]
        leaderboard = [
            {"user_id": 1, "team_id": 1, "points": 100},
            {"user_id": 2, "team_id": 2, "points": 80},
        ]
        workouts = [
            {"user_id": 1, "activity_id": 1, "duration_minutes": 30},
            {"user_id": 2, "activity_id": 2, "duration_minutes": 45},
        ]

        # Populate database
        for user in users:
            User.objects.create(**user)
        for team in teams:
            Team.objects.create(**team)
        for activity in activities:
            Activity.objects.create(**activity)
        for entry in leaderboard:
            Leaderboard.objects.create(**entry)
        for workout in workouts:
            Workout.objects.create(**workout)

        self.stdout.write(self.style.SUCCESS("Database populated with test data."))
