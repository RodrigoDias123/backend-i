from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create admin, editor, and viewer groups with meeting permissions"

    def handle(self, *args, **options):
        admin_group, _ = Group.objects.get_or_create(name="admin")
        editor_group, _ = Group.objects.get_or_create(name="editor")
        viewer_group, _ = Group.objects.get_or_create(name="viewer")

        change_perm = Permission.objects.get(codename="change_meeting")
        view_perm = Permission.objects.get(codename="view_meeting")
        delete_perm = Permission.objects.get(codename="delete_meeting")

        admin_group.permissions.clear()
        editor_group.permissions.clear()
        viewer_group.permissions.clear()

        admin_group.permissions.add(change_perm, view_perm, delete_perm)
        editor_group.permissions.add(change_perm, view_perm)
        viewer_group.permissions.add(view_perm)

        self.stdout.write(self.style.SUCCESS("Groups and permissions configured"))
