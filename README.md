# Timesheet-Filler
Ease the pain of logging your time in JIRA Timesheets

# Installation 

Run following command to install `timeSHIT` module:

`pip install timeSHIT`

# How to run?
Create a `config.txt` file with following content: 

<pre>{
    "jira_url": "http://0.0.0.0",
    "username": "[your_username]",
    "password": "[your_password]",
    "timesheet_jira_id": "ABCD-1",
    "hours_to_fill": "8",
    "minutes_to_fill": "0",
    "comment": "[your_comment]"
}</pre>

Now run following command in the directory where above `config.txt` is saved.

For Linux: `nohup python -m timeSHIT &`
