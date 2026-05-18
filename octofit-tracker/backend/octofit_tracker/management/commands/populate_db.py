from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team_id=str(marvel.id))
        captain = User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password', team_id=str(marvel.id))
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team_id=str(dc.id))
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team_id=str(dc.id))

        # Activities
        Activity.objects.create(user_id=str(ironman.id), type='run', duration=30, distance=5)
        Activity.objects.create(user_id=str(batman.id), type='cycle', duration=60, distance=20)
        Activity.objects.create(user_id=str(superman.id), type='swim', duration=45, distance=2)
        Activity.objects.create(user_id=str(captain.id), type='walk', duration=90, distance=8)

        # Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        Workout.objects.create(name='Strength Training', description='Strength for all heroes', duration=60)

        # Leaderboard
        Leaderboard.objects.create(user_id=str(ironman.id), points=100)
        Leaderboard.objects.create(user_id=str(batman.id), points=90)
        Leaderboard.objects.create(user_id=str(superman.id), points=80)
        Leaderboard.objects.create(user_id=str(captain.id), points=70)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
