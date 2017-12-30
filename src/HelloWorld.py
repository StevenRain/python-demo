import json

sample = '{"transactionId":"dab15f80-ed30-11e7-b190-ed7253c916ba","transactionProcessedTime":"2017-12-30T15:12:54.136+08:00"}'
if sample.__contains__('transactionId'):
  print("done %s" % json.loads(sample)['transactionId'])

