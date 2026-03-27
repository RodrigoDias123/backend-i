# Session 16 | Django Admin - Exercise

## Exercise
Add `list_display` and `search_fields` for `Meeting`.

## Requirements
1. Register Meeting model with Django admin
2. Customize admin to show: id, title, date, owner
3. Add search functionality on title and owner
4. Add filtering by date and owner
5. Test in admin interface

## Expected Behavior
```bash
# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Access admin at http://127.0.0.1:8000/admin
# - Login with superuser credentials
# - See meetings listed with title, date, owner
# - Search by title or owner
# - Filter by date or owner
```

## Admin Configuration
```python
@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "date", "owner")
    list_filter = ("date", "owner")
    search_fields = ("title", "owner")
    ordering = ("-date",)
    readonly_fields = ("created_at",)
```

## Features to Implement
1. List display shows: ID, Title, Date, Owner
2. Search works on title and owner fields
3. Filter sidebar shows date and owner options
4. Default ordering is by date (newest first)
5. Can create/edit/delete meetings

## Files to Create/Modify
- `meetings/admin.py` - Register model with custom admin
- `meetings/models.py` - Add `__str__` method if not present

## Success Criteria
- Admin page displays meetings correctly
- Search functionality works
- Filters work properly
- Can create new meetings
- Can edit existing meetings
- Can delete meetings
- UI is user-friendly
