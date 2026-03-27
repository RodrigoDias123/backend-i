# Session 17 | Authentication and Permissions - Exercise

## Exercise
Configure `editor` group without meeting delete permission.

## Requirements
1. Create user groups: admin, editor, viewer
2. Assign permissions to each group
3. Admin: all permissions
4. Editor: can view and change meetings (NO delete)
5. Viewer: can only view meetings
6. Test with Django shell

## Expected Behavior
```bash
# Django shell setup
python manage.py shell
>>> from django.contrib.auth.models import Group, Permission
>>> from django.contrib.auth.models import User
>>> 
>>> # Create groups
>>> admin_group, _ = Group.objects.get_or_create(name="admin")
>>> editor_group, _ = Group.objects.get_or_create(name="editor")
>>> viewer_group, _ = Group.objects.get_or_create(name="viewer")
>>> 
>>> # Get permissions
>>> change_perm = Permission.objects.get(codename="change_meeting")
>>> view_perm = Permission.objects.get(codename="view_meeting")
>>> delete_perm = Permission.objects.get(codename="delete_meeting")
>>> 
>>> # Assign permissions
>>> editor_group.permissions.add(change_perm, view_perm)
>>> viewer_group.permissions.add(view_perm)
>>> admin_group.permissions.add(change_perm, view_perm, delete_perm)
```

## Permission Testing
```python
>>> user = User.objects.create_user("jorge", password="pass123")
>>> user.groups.add(editor_group)
>>> 
>>> # Check permissions
>>> user.has_perm("meetings.change_meeting")  # True
>>> user.has_perm("meetings.view_meeting")   # True
>>> user.has_perm("meetings.delete_meeting") # False (editor has NO delete)
```

## Files to Create/Modify
- `management/commands/create_groups.py` - Optional: Create management command
- Django shell for setup

## Success Criteria
- Three groups created: admin, editor, viewer
- Editor group has change and view permissions (NO delete)
- Viewer group has only view permission
- Admin group has all permissions
- Permission checks work in Django shell
- Users can be assigned to groups
