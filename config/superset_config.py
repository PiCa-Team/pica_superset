import os
from dotenv import load_dotenv

load_dotenv()

FEATURE_FLAGS = {
    'CLIENT_CACHE': True,
    'ENABLE_EXPLORE_JSON_CSRF_PROTECTION': True,
    'PRESTO_EXPAND_DATA': False,
    'SSH_TUNNELING': True,
    }

SSH_TUNNEL_MANAGER_CLASS = "superset.extensions.ssh.SSHManager"
SSH_TUNNEL_LOCAL_BIND_ADDRESS = "127.0.0.1"

SECRET_KEY = os.environ.get('SECRET_KEY')
# Generate a secure SECRET_KEY usng "openssl rand -base64 42"
