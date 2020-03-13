import authomatic
from authomatic.providers import oauth2, oauth1

CONFIG = {
             'twitter': {  # Your internal provider name

                 # Provider class
                 'class_': oauth1.Twitter,

                 # Twitter is an AuthorizationProvider so we need to set several other properties too:
                 'consumer_key': '########################',
                 'consumer_secret': '########################',
             },

             'facebook': {

                 'class_': oauth2.Facebook,

                 # Facebook is an AuthorizationProvider too.
                 'consumer_key': '########################',
                 'consumer_secret': '########################',

                 # But it is also an OAuth 2.0 provider and it needs scope.
                 'scope': ['user_about_me', 'email', 'publish_stream'],
             },

             'amazon': {
                 'class_': oauth2.Amazon,
                 'consumer_key': 'amzn1.application-oa2-client.4d5c2aaa5bfe423e91df6eb26c17bdc7',
                 'consumer_secret': '384ac41e740ef47bfb5e951e728f7da678437151df9e4b9296ffd3ae8debeef7',
                 'id': authomatic.provider_id(),
                 'scope': oauth2.Amazon.user_info_scope,
             },

             'google': {
                 'class_': oauth2.Google,

                 'consumer_key': '612544506151-rodqid01sbtns93ddi7fqfucnelmunjf.apps.googleusercontent.com',
                 'consumer_secret': 'RwYl6SNLCM8L07sVkldwwsAs',
                 'id': authomatic.provider_id(),
                 'scope': oauth2.Google.user_info_scope + [
                     'https://www.googleapis.com/auth/userinfo.profile',
                     'https://www.googleapis.com/auth/userinfo.email']
             },

        }

