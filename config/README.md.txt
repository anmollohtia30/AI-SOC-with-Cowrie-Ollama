# Configuration Files

This folder contains the configuration files used during the implementation of the AI-Powered Security Operations Center (SOC).

## Files

### cowrie.cfg.example

Configuration file for the Cowrie Honeypot.

Used for:
- SSH Honeypot configuration
- Logging configuration
- Network settings
- Authentication settings

### ossec.conf.example

Configuration file for Wazuh.

Used for:
- Log monitoring
- Cowrie JSON log collection
- Security event processing

### local_rules.xml

Contains custom Wazuh detection rules created for this project.

The rules are responsible for:
- Detecting Cowrie events
- Generating security alerts
- Classifying suspicious activities

## Important

These configuration files are provided as examples.

Before using them:
- Update file paths according to your environment.
- Verify network addresses.
- Modify settings if your installation differs from this project.

##Notes
- Check these lines in last of ossec.conf file

<localfile>
  <location>/home/cowrie/cowrie/var/log/cowrie/cowrie.json</location>
  <log_format>json</log_format>
</localfile>

- Change the path acc to your system
- also check all files conf