from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from decouple import config
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

class Command(BaseCommand):
    help = "Send motivational emails on Sundays"

    def handle(self, *args, **kwargs):
        email = config('EMAIL_USER')
        password = config('EMAIL_PASSWORD')
        quotes = [
            ("When you arise in the morning think of what a privilege it is to be alive, to think, to enjoy, to love...", "Marcus Aurelius"),
            ("Either you run the day or the day runs you.", "Jim Rohn"),
            ("Mondays are the start of the work week which offer new beginnings 52 times a year!", "David Dweck"),
            ("You've got to get up every morning with determination if you're going to go to bed with satisfaction.", "George Lorimer"),
            ("Be miserable. Or motivate yourself. Whatever has to be done, it's always your choice.", "Wayne Dyer"),
            ("Your Monday morning thoughts set the tone for your whole week. See yourself getting stronger, and living a fulfilling, happier & healthier life.", "Germany Kent"),
            ("You don't have to be great to start, but you have to start to be great.", "Zig Ziglar"),
            ("Each morning when I open my eyes I say to myself: I, not events, have the power to make me happy or unhappy today. I can choose which it shall be. Yesterday is dead, tomorrow hasn't arrived yet. I have just one day, today, and I'm going to be happy in it.", "Groucho Marx"),
            ("Life is full of beauty. Notice it. Notice the bumble bee, the small child, and the smiling faces. Smell the rain, and feel the wind. Live your life to the fullest potential, and fight for your dreams.", "Ashley Smith"),
            ("When you start to do the things that you truly love, it wouldn't matter whether it is Monday or Friday; you would be so excited to wake up each morning to work on your passions.", "Edmond Mbiaka"),
            ("A ship is always safe at shore but that is not what it's built for.", "Albert Einstein"),
            ("Stress is caused by being 'here' but wanting to be 'there.'", "Eckhart Tolle"),
            ("People rarely succeed unless they have fun in what they are doing.", "Dale Carnegie"),
            ("Your attitude, not your aptitude, will determine your altitude.", "Zig Ziglar"),
            ("You may have to fight a battle more than once to win it.", "Margaret Thatcher"),
            ("If you don't design your own life plan, chances are you'll fall into someone else's plan. And guess what they have planned for you? Not much.", "Jim Rohn"),
            ("Try not to become a person of success, but rather try to become a person of value.", "Albert Einstein"),
            ("Morning is an important time of day, because how you spend your morning can often tell you what kind of day you are going to have.", "Lemony Snicket"),
            ("Just one small positive thought in the morning can change your whole day.", "Dalai Lama"),
            ("Think of many things; do one.", "Portuguese proverb"),
            ("One of the best pieces of advice I ever got was from a horse master. He told me to go slow to go fast. I think that applies to everything in life. We live as though there aren't enough hours in the day but if we do each thing calmly and carefully we will get it done quicker and with much less stress.", "Viggo Mortensen"),
            ("Don't let what you cannot do interfere with what you can do.", "John R. Wooden"),
            ("Success means doing the best we can with what we have. Success is the doing, not the getting; in the trying, not the triumph. Success is a personal standard, reaching for the highest that is in us, becoming all that we can be.", "Zig Ziglar"),
            ("The starting point of all achievement is desire.", "Napoleon Hill"),
            ("I was thinking one day and I realized that if I just had somebody behind me all the way to motivate me I could make a big difference. Nobody came along like that so I just became that person for myself.", "Unknown"),
            ("If you don't pay appropriate attention to what has your attention, it will take more of your attention than it deserves.", "David Allen"),
            ("Spend eighty percent of your time focusing on the opportunities of tomorrow rather than the problems of yesterday.", "Brian Tracy"),
            ("Keep on going, and the chances are that you will stumble on something, perhaps when you are least expecting it. I never heard of anyone ever stumbling on something sitting down.", "Charles F. Kettering"),
            ("Shoot for the moon. Even if you miss, you'll land among the stars.", "Brian Littrell"),
            ("Whether you think you can or think you can't, you're right.", "Henry Ford")
        ]
        i = 0

        if datetime.now().weekday() == 6:
            users = User.objects.all()
            try:
                con = smtplib.SMTP("smtp.gmail.com", 587)
                con.starttls()
                con.login(email, password)

                for user in users:
                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = user.email
                    msg['Subject'] = "Sunday Motivation"
                    msg.attach(MIMEText(f"{quotes[i][0]}\n-{quotes[i][1]}", 'plain'))
                    con.sendmail(email, user.email, msg.as_string())
                    print(f"Sending email to {user.email}")
                    time.sleep(2)

                con.close()
                i = (i + 1) % len(quotes)

                self.stdout.write(self.style.SUCCESS('Emails sent successfully!'))

            except Exception as e:
                self.stderr.write(self.style.ERROR(f"Error occurred: {e}"))
