from django.core.management.base import BaseCommand

from assessments.models import Question
from compliance.models import Control
from threats.models import Threat


QUESTIONS = [
    (1, "Is the Purdue Level 0-1 (Process/Field devices) network segmented from Level 2 (Supervisory) systems?", 9),
    (2, "Is remote access to ICS/OT systems strictly controlled and monitored?", 9),
    (3, "Are firewalls and conduits implemented between Purdue zones according to IEC 62443?", 9),
    (4, "Do you have a patch management program for OT/ICS systems?", 9),
    (5, "Is there strict access control (least privilege) for engineers and contractors?", 9),
    (6, "Are USB and removable media policies enforced on OT systems?", 9),
    (7, "Is network monitoring and anomaly detection in place for Purdue Level 0-2?", 9),
    (8, "Have staff received recent training on ICS cybersecurity awareness?", 9),
]

THREATS = [
    ("Ransomware", "Malicious software that encrypts critical OT systems and demands payment.", "0-1, 2", "high"),
    ("Stuxnet-style Worm", "Targeted malware that damages physical industrial equipment (PLCs).", "0-1", "critical"),
    ("Insider Threat", "Authorised personnel misusing access to alter control logic.", "2, 3", "medium"),
    ("Phishing & Social Engineering", "Deceptive emails leading to credential theft or malware delivery.", "3, 4-5", "high"),
    ("DDoS Attack on SCADA", "Overwhelming supervisory systems causing loss of visibility.", "2", "high"),
    ("USB Malware Propagation", "Infected removable media bypassing air-gapped systems.", "0-1", "critical"),
]

CONTROLS = [
    (1, "Network segmentation between Purdue levels"),
    (2, "Controlled remote access to OT systems"),
    (3, "Firewalls and conduits between zones (IEC 62443)"),
    (4, "Patch management programme for ICS/OT"),
    (5, "Least-privilege access for engineers and contractors"),
    (6, "USB and removable media policy on OT systems"),
    (7, "Monitoring and anomaly detection on Level 0-2"),
    (8, "ICS cybersecurity awareness training for staff"),
]


class Command(BaseCommand):
    help = "Load starter questions, threats and controls."

    def handle(self, *args, **options):
        for order, text, points in QUESTIONS:
            Question.objects.get_or_create(
                order=order,
                defaults={"text": text, "points": points},
            )
        for name, description, purdue_level, impact in THREATS:
            Threat.objects.get_or_create(
                name=name,
                defaults={
                    "description": description,
                    "purdue_level": purdue_level,
                    "impact": impact,
                },
            )
        for order, title in CONTROLS:
            Control.objects.get_or_create(
                order=order,
                defaults={"title": title},
            )
        self.stdout.write(self.style.SUCCESS("Seed data loaded."))
