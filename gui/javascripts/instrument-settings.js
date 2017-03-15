class InstrumentSettings {
	constructor() {
		if (config.has('address')) {
			this.address = config.get('address');
		}
	}

	get connectionType() {
		return 'tcpip';
	}

	get address() {
		var addr = $('#address').val();
		config.set('address', addr)
		return addr;
	}
	set address(addr) {
		config.set('address', addr);
		$('#address').val(addr);
	}

	toJSON() {
		return {
			"connection type": this.connectionType,
			"address":         this.address
		};
	}
}

module.exports = InstrumentSettings;
