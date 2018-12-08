import re

# try:
#     value = "1|None,RX30,ComputerRx"
#     values = re.split('[,|]', value)
#     integration = values[int(values[0])+1]
#     print(integration)
# except Exception as e:
#     print(e)


try:
    value = "1None,RX30,ComputerRx"
    refillIntegrationIndex, refillIntegrationValues = value.split("|")
    integration = refillIntegrationValues.split(",")[int(refillIntegrationIndex)]
    print(integration)
except Exception as e:
    print(e)