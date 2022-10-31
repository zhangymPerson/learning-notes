$log = 'script-run.log'
Start-Transcript 
java -version > $log
Stop-Transcript