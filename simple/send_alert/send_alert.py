"""
Send a Single message to ECM as alert.
"""
from cp_lib.app_base import CradlepointAppBase


# this name "run_router_app" is not important, reserved, or demanded
# - but must match below in __main__ and also in __init__.py
def run_router_app(app_base):
    """

    :param CradlepointAppBase app_base: resources: logger, settings, etc
    """

    app_base.logger.info("Send ALERT to ECM via CSClient")

    # user may have passed in another path
    alert = "Default Message - All is well!"
    if "send_alert" in app_base.settings:
        if "alert" in app_base.settings["send_alert"]:
            alert = app_base.settings["send_alert"]["alert"]

    # here we send to Syslog using our OWN facility/channel
    app_base.logger.info('LOG: Sending alert to ECM=[{}].'.format(alert))

    # this line will be sent via Router's Syslog facility/channel
    app_base.cs_client.log(
        'RouterSDKDemo', 'CS: Sending alert to ECM=[{}].'.format(alert))
    app_base.cs_client.alert('RouterSDKDemo', alert)

    return 0


if __name__ == "__main__":
    import sys

    my_app = CradlepointAppBase("simple/send_alert")

    _result = run_router_app(my_app)
    my_app.logger.info("Exiting, status code is {}".format(_result))
    sys.exit(_result)
