#! /usr/bin/python

def sendDMXframe(signal):

	import array
	from ola.ClientWrapper import ClientWrapper

	def DmxSent(state):
		wrapper.Stop()
	i = 0
	data = array.array('B')
	while i < 6:
		data.append(signal[i])
		i += 1
	wrapper = ClientWrapper()
	client = wrapper.Client()
	client.SendDmx(1, data, DmxSent)
	wrapper.Run()


