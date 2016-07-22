from django.shortcuts import redirect
from social.pipeline.partial import partial

def user_details(strategy, details, response, is_new=False, user=None, *args, **kwargs):
    """Update user details using data from provider."""
    if user and is_new:
        changed = False # flag to track changes
        protected = strategy.setting('PROTECTED_USER_FIELDS', [])
        keep = ('username', 'id', 'pk') + tuple(protected)
        
        for name, value in details.items():
            if name not in keep and hasattr(user, name):
                if value and value != getattr(user, name, None):
                    try:
                        setattr(user, name, value)
                        changed = True
                    except AttributeError:
                        pass
        
        if changed:
            strategy.storage.user.changed(user)

"""@partial
def get_email(backend, strategy, request, details, response, user=None, is_new=False, *args, **kwargs):
    if user and user.email:
        return
    elif is_new:
        if strategy.session_get('saved_email'):
            details['email'] = strategy.session_pop('saved_email')
        else:
            return redirect('/add_email/')"""

def get_email(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        profile = user.get_profile()
        if profile is None:
            profile = Profile(user_id=user.id)
        profile.email = response.get('email')
        profile.save()

"""def user_details(strategy, details, user=None, *args, **kwargs):
    if user:
        changed = False  # flag to track changes
        protected = ('username', 'id', 'pk', 'email') + \
            tuple(strategy.setting('PROTECTED_USER_FIELDS', []))

        # Update user model attributes with the new data sent by the current
        # provider. Update on some attributes is disabled by default, for
        # example username and id fields. It's also possible to disable update
        # on fields defined in SOCIAL_AUTH_PROTECTED_FIELDS.
        for name, value in details.items():
            if value and hasattr(user, name):
                # Check https://github.com/omab/python-social-auth/issues/671
                current_value = getattr(user, name, None)
                if not current_value or name not in protected:
                    changed |= current_value != value
                    setattr(user, name, value)

        if changed:
            strategy.storage.user.changed(user)"""