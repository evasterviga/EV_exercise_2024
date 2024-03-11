import pandas as pd
from mails import end_mail

# TODO: find file each time is generated 
# TODO: add input path to config, look for files there
samples = pd.read_csv(r'data/samples.txt')

origins = set(''.join([x[1:2] for x in samples['sample']]))

results = [(i, len(samples[(samples.qc_pass == False) & (samples['sample'].str[1:2] == i)]), len(samples[samples['sample'].str[1:2] == i])) for i in origins]
results = pd.DataFrame(results) # Convert to data frame
results = results.rename(columns={0:'origin', 1:'num_failed_qc', 2:'TOTAL_SAMPLES'})
results['pct_fail'] = results.num_failed_qc / results.TOTAL_SAMPLES * 100


# Check if there are more than 10 % failed samples from any origin
results['pct_fail_pass'] = results.pct_fail > 10

if len(results.pct_fail_pass[results.pct_fail_pass == True]) > 0:
    mail_subject = "WARNING: Quality cut-off check results"
    mail_text = "Script to check quality cutoff found > 10 % fails. See results below:"
elif len(results.pct_fail_pass[results.pct_fail_pass == True]) == 0:
    mail_subject = "Quality cut-off check results"
    mail_text = "Script to check quality cutoff found < 10 % fails. See results below:"


print(mail_subject)
print(mail_text)

end_mail(mail_subject, mail_text)
