from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting database population...')

        try:
            with transaction.atomic():
                # Clear existing data
                self.stdout.write('Clearing existing data...')
                User.objects.all().delete()
                Team.objects.all().delete()
                Activity.objects.all().delete()
                Leaderboard.objects.all().delete()
                Workout.objects.all().delete()

                # Create users
                self.stdout.write('Creating users...')
                users = [
                    User(username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
                    User(username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
                    User(username='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword'),
                    User(username='crashoverride', email='crashoverride@hmhigh.edu', password='crashoverridepassword'),
                    User(username='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword'),
                ]
                User.objects.bulk_create(users)

                # Create teams
                self.stdout.write('Creating teams...')
                team = Team(name='Blue Team')
                team.save()
                team.members.set(User.objects.all())

                # Create activities
                self.stdout.write('Creating activities...')
                activities = [
                    Activity(user=users[0], activity_type='Cycling', duration=timedelta(hours=1)),
                    Activity(user=users[1], activity_type='Crossfit', duration=timedelta(hours=2)),
                    Activity(user=users[2], activity_type='Running', duration=timedelta(hours=1, minutes=30)),
                    Activity(user=users[3], activity_type='Strength', duration=timedelta(minutes=30)),
                    Activity(user=users[4], activity_type='Swimming', duration=timedelta(hours=1, minutes=15)),
                ]
                Activity.objects.bulk_create(activities)

                # Create leaderboard entries
                self.stdout.write('Creating leaderboard entries...')
                leaderboard_entries = [
                    Leaderboard(user=users[0], score=100),
                    Leaderboard(user=users[1], score=90),
                    Leaderboard(user=users[2], score=95),
                    Leaderboard(user=users[3], score=85),
                    Leaderboard(user=users[4], score=80),
                ]
                Leaderboard.objects.bulk_create(leaderboard_entries)

                # Create workouts
                self.stdout.write('Creating workouts...')
                workouts = [
                    Workout(name='Cycling Training', description='Training for a road cycling event'),
                    Workout(name='Crossfit', description='Training for a crossfit competition'),
                    Workout(name='Running Training', description='Training for a marathon'),
                    Workout(name='Strength Training', description='Training for strength'),
                    Workout(name='Swimming Training', description='Training for a swimming competition'),
                ]
                Workout.objects.bulk_create(workouts)

            self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error populating database: {e}'))