After finishing my PoC of AWS Greengrass with PLC i was curious if i could send SMS's from the PLC.

![ABB PLC](PLC.jpg)

*My PoC with AWS Greengrass and a PLC: https://www.hackster.io/mariopoeta/allen-bradley-plc-aws-iot-poc-7ef061*

Created another AWS Lambda (this lambda) and another subscription in AWS IoT.

![sms_messagebird](sms_messagebird.jpg)

By the way, if you are curious about the mongodb lambda check my other repo: https://github.com/mariopoeta/aws-lambda-awsgreengrass-mongodb

End result:

![sms](SMS.jpeg)

