import logging
import messagebird
import requests
import urllib3
import chardet
import sys
import os
import certifi
import dns.ipv4
import dns.resolver
import dns.inet
import idna
import __future__


def filter_input(topic_message):
    message = topic_message
    try:
        if 'ns=2;s=plc.plc_device.input1' in message.values() or 'ns=2;s=plc.plc_device.input2' in message.values():
            toggle(message)
        elif 'ns=2;s=plc.plc_device.greenbutton' in message.values() or 'ns=2;s=plc.plc_device.redbutton' in message.values():
            button(message)
    except Exception as e:
        logging.error(e)

def toggle(toggle_input):
    message = toggle_input
    try:
        if 'ns=2;s=plc.plc_device.input1' in message.values():
            sms_content = "Someone clicked Input1!"
            send_sms(sms_content)
        elif 'ns=2;s=plc.plc_device.input2' in message.values():
            sms_content = "Someone clicked Input2!"
            send_sms(sms_content)
    except Exception as e:
        logging.error(e)

def button(button_input):
    message = button_input
    try:
        if 'ns=2;s=plc.plc_device.greenbutton' in message.values():
            for key, values in message.iteritems():
                if isinstance(values, dict):
                    if 1 in values.values():
                        sms_content = "Someone clicked in the green button!"
                        send_sms(sms_content)
        elif 'ns=2;s=plc.plc_device.redbutton' in message.values():
            for key, values in message.iteritems():
                if isinstance(values, dict):
                    if 0 in values.values():
                        sms_content = "Someone clicked in the red button!"
                        send_sms(sms_content)
    except Exception as e:
        logging.error(e)

def send_sms(sms_content):
    access_key = 'AccessKey'
    client = messagebird.Client(access_key)
    sms_originator = 'phonenumber'
    sms_recipients = 'phonenumber'
    try:
        client.message_create(sms_originator,sms_recipients,sms_content)
    except Exception as e:
        logging.error(e)

def function_handler(event, context):
    try:
        filter_input(event)
    except Exception as e:
        logging.error(e)
    return
