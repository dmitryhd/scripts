#!/usr/bin/env python3
from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import cmdrsp, context
from pysnmp.carrier.asynsock.dgram import udp

# Create SNMP engine
snmpEngine = engine.SnmpEngine()
config.addSocketTransport(
    snmpEngine,
    udp.domainName,
    udp.UdpTransport().openServerMode(('127.0.0.1', 1611))
)
# user: usr-sha-none, auth: SHA, priv NONE
config.addV3User(
    snmpEngine, 'usr-sha-none',
    config.usmHMACSHAAuthProtocol, 'authkey1'
)
config.addVacmUser(snmpEngine, 3, 'usr-sha-none', 'authNoPriv',
                   (1,3,6,1,2,1), (1,3,6,1,2,1))
# Get default SNMP context this SNMP engine serves
snmpContext = context.SnmpContext(snmpEngine)
# Register SNMP Applications at the SNMP engine for particular SNMP context
cmdrsp.GetCommandResponder(snmpEngine, snmpContext)
# OUT: <pysnmp.entity.rfc3413.cmdrsp.GetCommandResponder object at 0x7f7ca0ef7940>
cmdrsp.SetCommandResponder(snmpEngine, snmpContext)
# OUT: <pysnmp.entity.rfc3413.cmdrsp.SetCommandResponder object at 0x7f7ca0ef7cf8>
cmdrsp.NextCommandResponder(snmpEngine, snmpContext)
# OUT: <pysnmp.entity.rfc3413.cmdrsp.NextCommandResponder object at 0x7f7ca0f06908>
cmdrsp.BulkCommandResponder(snmpEngine, snmpContext)
# OUT: <pysnmp.entity.rfc3413.cmdrsp.BulkCommandResponder object at 0x7f7ca1970f28>
# Register an imaginary never-ending job to keep I/O dispatcher running forever
snmpEngine.transportDispatcher.jobStarted(1)
# Run I/O dispatcher which would receive queries and send responses
try:
    snmpEngine.transportDispatcher.runDispatcher()
except:
    snmpEngine.transportDispatcher.closeDispatcher()
    raise
