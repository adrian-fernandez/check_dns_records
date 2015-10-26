import os
from subprocess import Popen, PIPE

DOMAINS = [{
		"name": "google.es",
		"data":[{
			"name": "Registro TXT",
			"query": "host -t txt google.es",			
			"should_be": "descriptive text \"v=spf1 -all\""
                     }]
	},
	{
		"name": "microsoft.com",
		"data":[{
				"name": "Registro TXT",
				"query": "host -t txt microsoft.com",
				"should_be": "registry_not_found"
			}
		       ]
		}
	 ]



def check(command, should_be):
	process = Popen(command.split(" "), stdout=PIPE)
	(output, err) = process.communicate()
	exit_code = process.wait()

	if should_be in output:
		print "[OK]\t" + should_be
	else:
		print "[FAIL]\t" + should_be

for domain in DOMAINS:
	print "\n" + domain['name'] + "\n========="

	for data in domain['data']:
		print "\n" + data["name"] + ": "
		check(data['query'], data['should_be'])


	print "\n"
